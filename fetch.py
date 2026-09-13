import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")


def fetch_jobs(what: str, results_per_page: int = 50) -> list:
    """Fetch job postings from the Adzuna API."""
    url = "https://api.adzuna.com/v1/api/jobs/gb/search/1"

    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "what": what,
        "results_per_page": results_per_page,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json()["results"]


def to_job_posting(raw: dict) -> dict:
    """Convert an Adzuna result into our standard job posting shape."""
    return {
        "title": raw["title"],
        "company": raw["company"]["display_name"],
        "salary_min": raw.get("salary_min"),
        "salary_is_predicted": raw.get("salary_is_predicted") == "1",
        "description": raw["description"],
        "source": "adzuna",
        "source_id": raw["id"],
        "url": raw["redirect_url"],
        "created": raw["created"],
    }


def deduplicate(jobs: list) -> list:
    """Remove postings that repeat the same title and company."""
    seen = set()
    unique = []

    for job in jobs:
        key = (job["title"], job["company"])

        if key not in seen:
            seen.add(key)
            unique.append(job)
    return unique


if __name__ == "__main__":
    print("APP ID loaded", APP_ID is not None)
    print("APP KEY loaded", APP_KEY is not None)

    raw_jobs = fetch_jobs("machine learning python")
    jobs = [to_job_posting(raw) for raw in raw_jobs]
    jobs = deduplicate(jobs)

    print(f"After deduplication: {len(jobs)}")

    with open("jobs.json", "w") as f:
        json.dump(jobs, f, indent=2)

    print(f"Saved {len(jobs)} jobs to jobs.json")
