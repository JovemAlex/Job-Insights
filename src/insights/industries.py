from typing import List, Dict
import src.insights.jobs as JOBS_FILE


def get_unique_industries(path: str) -> List[str]:
    industriesList = set()
    industries = JOBS_FILE.read(path)
    for industry in industries:
        if industry["industry"] != '':
            industriesList.add(industry["industry"])
    return industriesList


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    industriesSelected = list()
    for job in jobs:
        if job["industry"] == industry:
            industriesSelected.append(job)
    return industriesSelected
