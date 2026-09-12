import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")

print("APP ID loaded", APP_ID is not None)
print("APP KEY loaded", APP_KEY is not None)

url = "https://api.adzuna.com/v1/api/jobs/gb/search/1"

params = {
    "app_id": APP_ID,
    "app_key": APP_KEY,
    "what": "Machine Learning",
    "results_per_page": 50,
}

response = requests.get(url, params=params)
print("Status code = ", response.status_code)

data = response.json()

print(type(data))
print(data.keys())

print("Total matching jobs:", data["count"])
print("Mean salary:", data["mean"])
print("Results returned:", len(data["results"]))


print(json.dumps(data["results"][0], indent=2))


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


for raw in data["results"]:
    print(to_job_posting(raw))

missing_salary = sum(1 for r in data["results"] if "salary_min" not in r)
predicted_salary = sum(
    1 for r in data["results"] if r.get("salary_is_predicted") == "1"
)

print(f"Missing salary: {missing_salary} of {len(data['results'])}")
print(f"Predicted salary: {predicted_salary} of {len(data['results'])}")

if __name__ == "__main__":
    jobs = [to_job_posting(raw) for raw in data["results"]]

    with open("jobs.json", "w") as f:
        json.dump(jobs, f, indent=2)

    print(f"Saved {len(jobs)} jobs to jobs.json")
