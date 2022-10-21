from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    brazilian_jobs = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    for job in brazilian_jobs:
        assert "title" in job
        assert "salary" in job
        assert "type" in job
