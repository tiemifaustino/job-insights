from functools import lru_cache
import csv


@lru_cache
def read(path):
    list_of_jobs = []
    with open(path) as file:
        file_read_jobs = csv.DictReader(file)
        for job in file_read_jobs:
            list_of_jobs.append(job)
    return list_of_jobs

    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
