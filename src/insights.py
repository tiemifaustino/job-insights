from src.jobs import read


def get_unique_job_types(path):
    jobs_read = read(path)
    job_types = set()

    for job in jobs_read:
        job_types.add(job["job_type"])

    return job_types


def filter_by_job_type(jobs, job_type):
    job_list_by_job_type = [job for job in jobs if job_type == job["job_type"]]
    return job_list_by_job_type


def get_unique_industries(path):
    jobs_read = read(path)

    industry_list = [
        industry["industry"] for industry in jobs_read if industry["industry"]
    ]
    industries = set(industry_list)

    return industries


def filter_by_industry(jobs, industry):
    job_list_by_industry = [job for job in jobs if industry == job["industry"]]
    return job_list_by_industry


def get_max_salary(path):
    jobs_read = read(path)

    max_salary = [
        int(salary["max_salary"])
        for salary in jobs_read
        if salary["max_salary"].isdigit()
    ]
    return max(max_salary)


def get_min_salary(path):
    jobs_read = read(path)

    min_salary = [
        int(salary["min_salary"])
        for salary in jobs_read
        if salary["min_salary"].isdigit()
    ]
    return min(min_salary)


def matches_salary_range(job, salary):
    if (
        job.get("min_salary") is None  # ou "min_salary" not in job
        or job.get("max_salary") is None  # ou "max_salary" not in job
        or type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or type(salary) != int
        or job["min_salary"] > job["max_salary"]
    ):
        raise ValueError
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    jobs_list_by_salary = [
        job
        for job in jobs
        if type(salary) is int
        and job["min_salary"] <= salary <= job["max_salary"]
    ]

    return jobs_list_by_salary
