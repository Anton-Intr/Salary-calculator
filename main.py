from fastapi import FastAPI, Depends, Query
import calculator
app = FastAPI()

class Params:
    def __init__(
        self,
        account_key: str = Query(description='Jira key, you can get it by visiting your Jira profile and copy-pasting key from URL, like 5a4ce9e3ebeb8229f4b2d45a'),
        tempo_token:str = Query(description='API token for Tempo integration. See docs for getting it: https://apidocs.tempo.io/#section/Authentication#using-the-rest-api-as-an-individual-user'),
        users_rate:float = Query(description='Hourly rate'),
        date_start: str = Query(description='Start date for salary calculation. Format: YYYY-MM-DD.'),
        date_end: str = Query('now',description='End date for salary calculation. Leave now - to calculate till today (including). Format: YYYY-MM-DD.'),
        rate_multiplier: float = Query(1.5, description='User\'s rate multiplier. Normal is 1. Default is 1.5 now cause of paid by hour.'),
        education_rate_multiplier: float = Query(1, description='User\'s education rate multiplier. Normal is 1.'),
        education_task_id: int = Query(71358, description='Jira task ID of task-logger for education time spendings. Unlikely to be changed'),
        tempo_endpoint: str = Query('https://api.tempo.io/4/worklogs/user/', description='API endpoint used to get user\'s hours. Unlikely to be changed'),
    ):
        self.account_key = account_key
        self.tempo_token = tempo_token
        self.users_rate = users_rate
        self.date_start = date_start
        self.date_end = date_end
        self.rate_multiplier = rate_multiplier
        self.education_rate_multiplier = education_rate_multiplier
        self.education_task_id = education_task_id
        self.tempo_endpoint = tempo_endpoint

    


@app.get("/calculate_salary/")
async def calculate_salary(params: Params = Depends()):
    return (calculator.calculate(params.tempo_token,params.account_key,params.users_rate,params.rate_multiplier,params.education_rate_multiplier,params.education_task_id,params.tempo_endpoint,params.date_start,params.date_end))
    # calculator.calculate(params)