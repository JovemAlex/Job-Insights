from typing import Union, List, Dict
import src.insights.jobs as JOBS_FILE


def get_max_salary(path: str) -> int:
    salariesList = set()
    jobs = JOBS_FILE.read(path)
    for job in jobs:
        if job["max_salary"].isnumeric():
            salariesList.add(int(job["max_salary"]))
    maxSalary = max(salariesList)

    return maxSalary


def get_min_salary(path: str) -> int:
    salariesList = set()
    jobs = JOBS_FILE.read(path)
    for job in jobs:
        if job["min_salary"].isnumeric():
            salariesList.add(int(job["min_salary"]))
    minSalary = min(salariesList)

    return minSalary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        salary = int(salary)

        if min_salary > max_salary:
            raise ValueError
        elif min_salary <= int(salary) <= max_salary:
            return True
        else:
            return False

    except (Exception):
        raise ValueError("Algumas das chaves não têm valores numéricos")


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    jobsSelected = []

    for job in jobs:

        try:
            jobSalaries = dict(
                max_salary=int(job["max_salary"]),
                min_salary=int(job["min_salary"]),
            )

            if matches_salary_range(jobSalaries, salary):
                jobsSelected.append(job)

        except (ValueError):
            pass

    return jobsSelected
