from functools import lru_cache
from typing import List, Dict
import csv

filePath = "data/jobs.csv"


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path) as csvfile:
        content = list(csv.DictReader(csvfile))
        return content


def get_unique_job_types(path: str) -> List[str]:
    job_types = set()
    jobs = read(path)
    for job in jobs:
        if job["job_type"] != '':
            job_types.add(job["job_type"])
    return job_types


jobsDict = read(filePath)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    jobsSelected = list()
    for job in jobs:
        if job["job_type"] == job_type:
            jobsSelected.append(job)
    return jobsSelected
