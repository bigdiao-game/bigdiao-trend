#!/usr/bin/env python3
"""Redact configured credentials and private identifiers from streamed logs."""

from __future__ import annotations

import os
import sys


SENSITIVE_ENV_VARS = (
    "FEISHU_WEBHOOK_URL",
    "TELEGRAM_BOT_TOKEN",
    "TELEGRAM_CHAT_ID",
    "DINGTALK_WEBHOOK_URL",
    "WEWORK_WEBHOOK_URL",
    "EMAIL_FROM",
    "EMAIL_PASSWORD",
    "EMAIL_TO",
    "NTFY_TOPIC",
    "NTFY_TOKEN",
    "BARK_URL",
    "SLACK_WEBHOOK_URL",
    "GENERIC_WEBHOOK_URL",
    "AI_API_KEY",
    "S3_BUCKET_NAME",
    "S3_ACCESS_KEY_ID",
    "S3_SECRET_ACCESS_KEY",
)


def main() -> None:
    sensitive_values = sorted(
        {
            value
            for name in SENSITIVE_ENV_VARS
            if len(value := os.environ.get(name, "")) >= 4
        },
        key=len,
        reverse=True,
    )

    for line in sys.stdin:
        for value in sensitive_values:
            line = line.replace(value, "***")
        sys.stdout.write(line)
        sys.stdout.flush()


if __name__ == "__main__":
    main()
