MIN_SALARY = 45000
REQUIRED_SKILL = "python"


def meets_salary(salary_min: int) -> bool:
    """Returns True if the salary is atleast equal to MIN_SALARY"""
    return salary_min >= MIN_SALARY


def mentions_skill(description: str, skill: str) -> bool:
    """Return True if the skill appears anywhere in the description."""
    return skill.lower() in description.lower()


def is_relevant(job: dict) -> bool:
    """Return True if the posting meets salary AND mentions the required skill."""
    return meets_salary(job["salary_min"]) and mentions_skill(
        job["description"], REQUIRED_SKILL
    )


jobs = [
    {
        "title": "ML Engineer",
        "company": "Fenergo",
        "salary_min": 55000,
        "description": "Strong Python and PyTorch experience required.",
    },
    {
        "title": "Data Analyst",
        "company": "Aon",
        "salary_min": 38000,
        "description": "Excel, SQL and Power BI.",
    },
    {
        "title": "AI Engineer",
        "company": "Stripe",
        "salary_min": 70000,
        "description": "Python, LLMs, RAG systems, AWS.",
    },
    {
        "title": "Junior Developer",
        "company": "Version 1",
        "salary_min": 48000,
        "description": "Java and Spring Boot.",
    },
]

relevant_count = 0

for job in jobs:
    if is_relevant(job):
        relevant_count += 1
        print(f"{job['title']} at {job['company']} - RELEVANT")
    else:
        print(f"{job['title']} at {job['company']} - SKIP")

print(f"{relevant_count} of {len(jobs)} postings relevant")
