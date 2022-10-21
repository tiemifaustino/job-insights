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
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
