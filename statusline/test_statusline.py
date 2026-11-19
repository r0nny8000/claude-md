import json
from datetime import datetime
from zoneinfo import ZoneInfo

from statusline import build_line, format_reset, format_tokens, session_tokens

BERLIN = ZoneInfo("Europe/Berlin")
NOW = datetime(2026, 11, 19, 1, 0, tzinfo=BERLIN)


def epoch(*args):
    return int(datetime(*args, tzinfo=BERLIN).timestamp())


def write_transcript(path, records):
    path.write_text("\n".join(json.dumps(r) for r in records) + "\n")


def assistant(msg_id, input=0, cache_write=0, cache_read=0, output=0):
    return {
        "type": "assistant",
        "message": {
            "id": msg_id,
            "usage": {
                "input_tokens": input,
                "cache_creation_input_tokens": cache_write,
                "cache_read_input_tokens": cache_read,
                "output_tokens": output,
            },
        },
    }


def full_input(transcript_path):
    return {
        "model": {"id": "claude-opus-5-5", "display_name": "Opus 5.5"},
        "effort": {"level": "high"},
        "context_window": {"used_percentage": 8.4},
        "cost": {"total_cost_usd": 4.1234},
        "transcript_path": str(transcript_path),
        "rate_limits": {
            "five_hour": {"used_percentage": 12.3, "resets_at": epoch(2026, 11, 19, 3, 59)},
            "seven_day": {"used_percentage": 3.1, "resets_at": epoch(2026, 11, 25, 5, 59)},
        },
    }


def test_format_tokens():
    assert format_tokens(0) == "0"
    assert format_tokens(950) == "950"
    assert format_tokens(85_350) == "85k"
    assert format_tokens(1_189_278) == "1.19M"


def test_format_reset_today_shows_time_only():
    assert format_reset(epoch(2026, 11, 19, 3, 59), NOW) == "3:59am"


def test_format_reset_other_day_adds_date():
    assert format_reset(epoch(2026, 11, 20, 15, 5), NOW) == "Nov 20, 3:05pm"


def test_format_reset_always_date():
    assert format_reset(epoch(2026, 11, 19, 3, 59), NOW, always_date=True) == "Nov 19, 3:59am"


def test_format_reset_midnight_and_noon():
    assert format_reset(epoch(2026, 11, 19, 0, 30), NOW) == "12:30am"
    assert format_reset(epoch(2026, 11, 19, 12, 0), NOW) == "12:00pm"


def test_format_reset_uses_berlin_regardless_of_input_tz():
    # 02:59 UTC is 03:59 in Berlin (CET, UTC+1)
    utc_epoch = int(datetime(2026, 11, 19, 2, 59, tzinfo=ZoneInfo("UTC")).timestamp())
    assert format_reset(utc_epoch, NOW) == "3:59am"


def test_session_tokens_counts_each_message_once(tmp_path):
    transcript = tmp_path / "t.jsonl"
    # Claude Code writes one API response as several lines with the same message id
    write_transcript(transcript, [
        {"type": "user", "message": {"role": "user", "content": "hi"}},
        assistant("msg_1", input=10, cache_write=1000, cache_read=5000, output=200),
        assistant("msg_1", input=10, cache_write=1000, cache_read=5000, output=200),
        assistant("msg_2", input=5, cache_write=0, cache_read=7000, output=100),
    ])
    assert session_tokens(str(transcript)) == (10 + 1000 + 200 + 5 + 100, 12000)


def test_session_tokens_missing_file():
    assert session_tokens("/nonexistent/t.jsonl") == (0, 0)


def test_build_line_normal(tmp_path):
    transcript = tmp_path / "t.jsonl"
    write_transcript(transcript, [
        assistant("msg_1", input=54, cache_write=69_326, cache_read=1_189_278, output=15_970),
    ])
    assert build_line(full_input(transcript), NOW) == (
        "Opus 5.5 · effort high · context 8% · token 85k + 1.19M cached (4.12$)"
        " · 5h limit 12% (resets 3:59am) · week limit 3% (resets Nov 25, 5:59am)"
    )


def test_build_line_before_first_response(tmp_path):
    data = {
        "model": {"id": "claude-opus-5-5", "display_name": "Opus 5.5"},
        "effort": {"level": "high"},
        "context_window": {"used_percentage": None},
        "cost": {"total_cost_usd": 0},
        "transcript_path": str(tmp_path / "missing.jsonl"),
    }
    assert build_line(data, NOW) == (
        "Opus 5.5 · effort high · context 0% · token 0 + 0 cached (0.00$)"
        " · 5h limit – · week limit –"
    )


def test_build_line_without_effort(tmp_path):
    data = full_input(tmp_path / "missing.jsonl")
    data["model"]["display_name"] = "Haiku 5.5"
    del data["effort"]
    assert build_line(data, NOW).startswith("Haiku 5.5 · context 8% · token ")


def test_build_line_one_limit_window_missing(tmp_path):
    data = full_input(tmp_path / "missing.jsonl")
    del data["rate_limits"]["five_hour"]
    assert build_line(data, NOW).endswith(
        "· 5h limit – · week limit 3% (resets Nov 25, 5:59am)"
    )
