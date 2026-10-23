# Automotive Data Platform
![Tests](https://github.com/panellic/automotive-data-platform/actions/workflows/tests.yml/badge.svg)

End-to-end Data Engineering portfolio project built to simulate an automotive data platform.

## Project goals

- Ingest raw automotive data
- Validate and clean the data
- Build Bronze, Silver and Gold layers
- Create analytical data marts
- Orchestrate pipelines with Airflow
- Process larger datasets with PySpark
- Add tests and CI with GitHub Actions

## Tech stack

- Python
- SQL
- PostgreSQL
- PySpark
- Apache Airflow
- Docker
- Git / GitHub

## Run locally

Install dependencies:

```bash
python -m pip install -r requirements.txt

## Project structure

```text
automotive-data-platform/
├── .github/
│   └── workflows/
│       └── tests.yml
├── data/
│   └── vehicles.csv
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── read_vehicles.py
│   └── validation.py
├── tests/
│   └── test_validation.py
├── .gitignore
├── README.md
└── requirements.txt

