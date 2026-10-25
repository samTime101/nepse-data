# nepse-data

Historical and current daily OHLCV data for companies listed on the Nepal Stock Exchange (NEPSE), stored as one CSV per trading symbol.

> **Fork notice**
>
> This repository is a fork of [Aabishkar2/nepse-data](https://github.com/Aabishkar2/nepse-data), originally created by [Aabishkar2](https://github.com/Aabishkar2) and contributors.
>
> **Forked on:** Tue Oct 6 07:54:16 2026 +0545.
>
> The original project is MIT-licensed. This fork keeps the same license — see [Credits](#credits) and [License](#license).

## What is here

| Path | Contents |
| --- | --- |
| `data/company-wise/` | One CSV per symbol, sorted oldest to newest |
| `src/` | Scrapers and shared helpers |
| `src/constants/companyIdMap.py` | Generated symbol → sharesansar company ID map |
| `.github/workflows/` | Discovery, backfill, and daily update automation |
| `.github/actions/` | Composite actions shared by the workflows |

The dataset currently covers **399 symbols** and contains **over 520,000 daily rows**, with history going back to **1995-07-20**.

## Data

Each file in `data/company-wise/` contains the daily price history for one symbol. For example, [`NMB.csv`](data/company-wise/NMB.csv) contains NMB Bank Limited's data in ascending date order.

A few debenture symbols contain a slash (for example `GBILD84/85`). Since a slash cannot appear in a filename, the slash is stored as an underscore (`GBILD84_85.csv`). The original symbol is preserved in `companyIdMap.py` and in the scrapers.

Each CSV has these columns:

| Column | Description |
| --- | --- |
| `published_date` | Trading date (`YYYY-MM-DD`) |
| `open` | Opening price |
| `high` | Day's high |
| `low` | Day's low |
| `close` | Closing price |
| `per_change` | Percentage change from the previous close (`nan` for the first row of a series) |
| `traded_quantity` | Number of shares traded |
| `traded_amount` | Total turnover for the day |
| `status` | Derived: `1` if close > open, `-1` if open > close, `0` if equal |

Prices and turnover are in Nepalese rupees (NPR).

## Running the scrapers locally

The scrapers target Python 3.8, which is what the GitHub Actions workflows use.

```bash
# run everything from src/ — the scripts use paths relative to this directory
cd src

python3.8 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

# refresh the symbol -> company-id map from the live site
# (run this before a backfill so newly listed companies are picked up)
python discoverCompanies.py

# seed history for companies that do not have a CSV yet
# (on a fresh clone this can take a while; existing files are skipped)
python allDataScrapper.py

# append the latest session's prices to existing CSVs
python dailyDataScrapper.py
```

Notes:

- All three scripts must run from `src/`.
- `discoverCompanies.py` regenerates `src/constants/companyIdMap.py`. That file is generated — do not hand-edit it. It merges with the existing map, so delisted companies are never dropped.
- `allDataScrapper.py` skips any symbol that already has a CSV, so re-running it will not clobber or duplicate existing data.
- `dailyDataScrapper.py` only appends to CSVs that already exist and is idempotent — running it twice in a day will not add a duplicate row.
- Network requests use a 30-second timeout.
- The data comes from [sharesansar.com](https://www.sharesansar.com/)'s daily price and company history pages.

## Automation

All scheduled runs are **Monday to Friday**, in Nepal Time (UTC+05:45).

| Workflow | When | Purpose |
| --- | --- | --- |
| `discover-companies.yml` | 18:45 NPT | Refresh the symbol map and commit changes to `companyIdMap.py` |
| `backfill-companies.yml` | After discovery finishes, plus a 19:45 NPT retry | Fetch full history for newly discovered symbols |
| `update-daily-data.yml` | 19:15, 20:15, 21:15, 22:15, 23:15 NPT | Append the latest session's prices to existing CSVs |

`backfill-companies.yml` is connected to `discover-companies.yml` with a `workflow_run` trigger. All three workflows share the `nepse-data-write` concurrency group so they cannot push over each other, and each commits only when something actually changed.

Each workflow can also be started manually from the **Actions** tab (`workflow_dispatch`).

## Credits

- **Original project:** [Aabishkar2/nepse-data](https://github.com/Aabishkar2/nepse-data), created by [Aabishkar2](https://github.com/Aabishkar2) and contributors.
- **Fork maintained at:** [samTime101/nepse-data](https://github.com/samTime101/nepse-data).
- **Forked on:** Tue Oct 6 07:54:16 2026 +0545.
- **Data source:** [sharesansar.com](https://www.sharesansar.com/) for daily prices and company history; NEPSE for the underlying market data.

The original project is MIT-licensed, and this fork is distributed under the same license. Thank you to the original author and everyone who contributed to the upstream dataset.

## Contributing

Contributions are welcome. Please open an issue or pull request in this fork. If a change would also benefit the upstream project, consider opening a pull request against [Aabishkar2/nepse-data](https://github.com/Aabishkar2/nepse-data).

## License

This project is licensed under the MIT License, inherited from the original repository. See [LICENSE](LICENSE) for the full text.

Copyright (c) 2022 Aabishkar2 and contributors  
Copyright (c) 2026 samTime101 and contributors
