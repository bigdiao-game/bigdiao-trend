# Execution logs

The `Get Hot News` GitHub Actions workflow appends every TrendRadar crawler run
to `logs/YYYY-MM-DD.log`. Dates and timestamps use the `Asia/Shanghai` timezone.

Each entry contains the workflow run URL, crawler output, exit code, and finish
time. The workflow commits only the daily log file after each crawler run.
