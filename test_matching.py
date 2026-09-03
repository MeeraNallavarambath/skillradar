from matching import is_relevant, meets_salary, mentions_skill


def test_salary_above_floor_passes():
    assert meets_salary(50000) is True


def test_salary_at_floor_passes():
    assert meets_salary(45000) is True


def test_salary_below_floor_fails():
    assert meets_salary(25000) is False


def test_skill_match_is_case_insensitive_both_ways():
    assert mentions_skill("Strong PYTHON skills", "Python") is True


def test_absent_skill():
    assert (
        mentions_skill("Strong Python and PyTorch experience required.", "AWS") is False
    )


def test_meets_both_conditions():
    assert (
        is_relevant(
            {
                "title": "AI Engineer",
                "company": "Stripe",
                "salary_min": 70000,
                "description": "Python, LLMs, RAG systems, AWS.",
            }
        )
        is True
    )


def test_meets_salary_but_skill():
    assert (
        is_relevant(
            {
                "title": "AI Engineer",
                "company": "Stripe",
                "salary_min": 70000,
                "description": "LLMs, RAG systems, AWS.",
            }
        )
        is False
    )


def test_meets_skill_but_salary():
    assert (
        is_relevant(
            {
                "title": "AI Engineer",
                "company": "Stripe",
                "salary_min": 20000,
                "description": "Python, LLMs, RAG systems, AWS.",
            }
        )
        is False
    )
