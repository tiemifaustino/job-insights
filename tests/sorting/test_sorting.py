from src.sorting import sort_by
import pytest


@pytest.fixture()
def jobs_list():
    return [
        {
            "date_posted": "2020-10-02",
            "max_salary": 30000,
            "min_salary": 2000,
        },
        {
            "date_posted": "2020-05-02",
            "max_salary": 50000,
            "min_salary": 1000,
        },
        {
            "date_posted": "2020-07-02",
            "max_salary": 40000,
            "min_salary": 3000,
        },
    ]


def test_sort_by_criteria(jobs_list):
    sort_by(jobs_list, "max_salary")
    assert jobs_list[0]["max_salary"] == 50000
    assert jobs_list[1]["max_salary"] == 40000
    assert jobs_list[2]["max_salary"] == 30000

    sort_by(jobs_list, "min_salary")
    assert jobs_list[0]["min_salary"] == 1000
    assert jobs_list[1]["min_salary"] == 2000
    assert jobs_list[2]["min_salary"] == 3000

    sort_by(jobs_list, "date_posted")
    assert jobs_list[0]["date_posted"] == "2020-10-02"
    assert jobs_list[1]["date_posted"] == "2020-07-02"
    assert jobs_list[2]["date_posted"] == "2020-05-02"
