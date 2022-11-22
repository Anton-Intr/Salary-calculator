# Import dependencies
import requests
from datetime import date

def calculate (tempo_token, account_key, users_rate, rate_multiplier, education_rate_multiplier, education_task_id, tempo_endpoint, date_start, date_end):
    if date_end == 'now':
        date_end = date.today()


    # Get hours from Jira
    logs = 0
    logs_education = 0
    url = f'{tempo_endpoint}/{account_key}?from={date_start}&to={date_end}&limit=1000'
    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {tempo_token}'
    }
    response = requests.request('GET', url, headers=headers, data=payload)
    response_body = response.json()
    response_status = response.status_code
    if response_status != 200:
        raise Exception(
            f'Accountant service response status must be 200, got {response_status}.')
    logs_details = response_body['results']
    for i in logs_details:
        issue_id = i['issue']['id']
        if issue_id != education_task_id:
            log = i['timeSpentSeconds']
            logs += log
        else:
            log = i['timeSpentSeconds']
            logs_education += log
    logs = round(logs/3600, 2)
    logs_education = round(logs_education/3600, 2)


    # Calculator
    salary = round(rate_multiplier*logs*users_rate + education_rate_multiplier*logs_education*users_rate)
    return{f'Salary for timespan from {date_start} to {date_end}: {rate_multiplier*users_rate}*{logs} + {education_rate_multiplier*users_rate}*{logs_education} = {salary}'}
