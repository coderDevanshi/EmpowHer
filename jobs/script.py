from serpapi import GoogleSearch
import os, json


def extract_multiple_jobs(q):
    params = {
        # https://docs.python.org/3/library/os.html#os.getenv
        'api_key': "31be4f15c410807530c76a9f042334feda6bc7bd66b72bcdbca8af5483d6dfb8",        # your serpapi api
        'engine': 'google_jobs',                # SerpApi search engine 
        'gl': 'in',                             # country of the search
        'hl': 'en',                             # language of the search
        'q': q,                # search query
    }

    search = GoogleSearch(params)               # where data extraction happens on the SerpApi backend
    results = search.get_dict()                 # JSON -> Python dict

    return [job.get('job_id') for job in results['jobs_results']]


def scrape_google_jobs_listing(job_ids, q):
    data = []

    for job_id in job_ids:
        params = {
            # https://docs.python.org/3/library/os.html#os.getenv
            'api_key': "31be4f15c410807530c76a9f042334feda6bc7bd66b72bcdbca8af5483d6dfb8",    # your serpapi api
            'engine': 'google_jobs_listing',    # SerpApi search engine 
            'q': job_id,                        # search query (job_id)
        }

        search = GoogleSearch(params)           # where data extraction happens on the SerpApi backend
        results = search.get_dict()             # JSON -> Python dict

        data.append({
            'job_id': job_id,
            'apply_options': results.get('apply_options'),
            'salaries': results.get('salaries'),
            'ratings': results.get('ratings')
        })

    return data


def main(q):
    job_ids = extract_multiple_jobs(q)
    google_jobs_listing_results = scrape_google_jobs_listing(job_ids, q)

    print(json.dumps(google_jobs_listing_results, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    lis = ["full time", "internship", "part time", "remote", "freelance", "Bangalore", "Gurugram"]
    for q in lis:
        main(q)