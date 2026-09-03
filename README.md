# SkillRadar

AI/ML job market intelligence for Ireland. Extracts structured skills from job
postings, tracks how demand changes, and identifies gaps against your own profile.

## Why

Job requirements are written as unstructured prose, scattered across thousands of
postings, with no two worded the same way. There's no way to query them, so people
read ads one at a time and guess at the patterns.

## Status

Early. Currently: matching rules and tests. Data ingestion is next.

## Setup

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    pytest