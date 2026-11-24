"""Claude Code status line: model, effort, context, session tokens, 5h and week limits.

Reads the status line JSON from stdin and prints one line. Field reference:
https://code.claude.com/docs/en/statusline
"""

import json
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

BERLIN = ZoneInfo("Europe/Berlin")
# Hardcoded instead of strftime("%b %p"): the system locale is German, which
# would give "Dez" for December and an empty string for am/pm.
MONTHS = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]


def format_tokens(n):
    if n < 1000:
        return str(n)
    if n < 1_000_000:
        return f"{round(n / 1000)}k"
    return f"{n / 1_000_000:.2f}M"


def format_reset(resets_at, now, always_date=False):
    t = datetime.fromtimestamp(resets_at, BERLIN)
    hour = t.hour % 12 or 12
    clock = f"{hour}:{t.minute:02d}{'am' if t.hour < 12 else 'pm'}"
    if always_date or t.date() != now.astimezone(BERLIN).date():
        return f"{MONTHS[t.month - 1]} {t.day}, {clock}"
    return clock


def session_tokens(transcript_path):
    """Return (new, cached) tokens for the session.

    new = input + cache writes + output; cached = cache reads. The status line
    JSON has no cumulative count, so this sums the transcript.
    """
    usage_by_message = {}
    try:
        with open(transcript_path) as f:
            for line in f:
                record = json.loads(line)
                message = record.get("message")
                if isinstance(message, dict) and message.get("usage"):
                    # One API response appears on several lines with the same id;
                    # keying by id counts it once.
                    usage_by_message[message.get("id")] = message["usage"]
    except (OSError, TypeError):
        return 0, 0

    new = cached = 0
    for usage in usage_by_message.values():
        new += (
            usage.get("input_tokens", 0)
            + usage.get("cache_creation_input_tokens", 0)
            + usage.get("output_tokens", 0)
        )
        cached += usage.get("cache_read_input_tokens", 0)
    return new, cached


def limit_segment(label, window, now, always_date=False):
    if not window:
        return f"{label} –"
    reset = format_reset(window["resets_at"], now, always_date)
    return f"{label} {round(window['used_percentage'])}% (resets {reset})"


def build_line(data, now):
    parts = [data["model"]["display_name"]]

    effort = (data.get("effort") or {}).get("level")
    if effort:
        parts.append(f"{effort}")

    context = (data.get("context_window") or {}).get("used_percentage") or 0
    parts.append(f"ctx {round(context)}%")

    new, cached = session_tokens(data.get("transcript_path"))
    cost = (data.get("cost") or {}).get("total_cost_usd") or 0
    parts.append(
        f"token {format_tokens(new)} + {format_tokens(cached)} cached ({cost:.2f}$)"
    )

    limits = data.get("rate_limits") or {}
    parts.append(limit_segment("5h limit", limits.get("five_hour"), now))
    parts.append(
        limit_segment("week limit", limits.get("seven_day"), now, always_date=True)
    )

    return " · ".join(parts)


if __name__ == "__main__":
    print(build_line(json.load(sys.stdin), datetime.now(BERLIN)))
