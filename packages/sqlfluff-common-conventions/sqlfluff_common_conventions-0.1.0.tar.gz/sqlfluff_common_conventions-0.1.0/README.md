# sqlfluff-common-conventions

A plugin for rules that enforce common SQL conventions not available in SQLFluff, compatible with BigQuery SQL.

## Rules

As of 25 April 2024, all rules are compatible with snake, dromedary, and pascal case.

- CC01: Start boolean columns with `is` or `has`.
- CC02: End datetime, time, and timestamp columns with `at`.
- CC03: End date columns with `date`.
- CC04: Only allows a list of configurable words to be used in identifiers.