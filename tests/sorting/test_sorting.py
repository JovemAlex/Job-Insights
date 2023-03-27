from src.pre_built.sorting import sort_by
import pytest
from datetime import date, timedelta


def test_sort_by_criteria():

    today = date.today()
    yesterday = today - timedelta(days=1)

    jobs = [
        {
            "title": "Job 1",
            "min_salary": 2000,
            "max_salary": 4000,
            "date_posted": today,
        },
        {
            "title": "Job 2",
            "min_salary": 4000,
            "max_salary": 8000,
            "date_posted": yesterday,
        },
    ]

    sort_by(jobs, 'min_salary')
    assert jobs[0]['title'] == 'Job 1'
    assert jobs[1]['title'] == 'Job 2'

    sort_by(jobs, 'max_salary')
    assert jobs[0]['title'] == 'Job 2'
    assert jobs[1]['title'] == 'Job 1'

    sort_by(jobs, 'date_posted')
    assert jobs[0]['title'] == 'Job 2'
    assert jobs[1]['title'] == 'Job 1'

    with pytest.raises(ValueError):
        sort_by(jobs, "invalid_criteria")
