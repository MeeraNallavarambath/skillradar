import json

MIN_SALARY = 45000
REQUIRED_SKILL = "python"


def meets_salary(salary_min: int) -> bool:
    """Returns True if the salary is at least MIN_SALARY"""
    return salary_min >= MIN_SALARY


def mentions_skill(description: str, skill: str) -> bool:
    """Return True if the skill appears anywhere in the description."""
    return skill.lower() in description.lower()


def is_relevant(job: dict) -> bool:
    """Return True if the posting meets salary AND mentions the required skill."""
    return meets_salary(job["salary_min"]) and mentions_skill(
        job["description"], REQUIRED_SKILL
    )


def load_jobs(path: str) -> list:
    """Read job postings from a JSON file."""
    with open(path) as f:
        return json.load(f)


if __name__ == "__main__":
    jobs = load_jobs("jobs.json")
    relevant_count = 0

    for job in jobs:
        if is_relevant(job):
            relevant_count += 1
            print(f"{job['title']} at {job['company']} - RELEVANT")
        else:
            print(f"{job['title']} at {job['company']} - SKIP")

    print(f"{relevant_count} of {len(jobs)} postings relevant")
