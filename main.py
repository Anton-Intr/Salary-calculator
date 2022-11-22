from fastapi import FastAPI
import calculator
app = FastAPI()

@app.get("/calculate_salary/")
async def read_item(account_key:str, tempo_token:str, users_rate:float, date_start: str, date_end: str = 'now', rate_multiplier: float = 1.5, education_rate_multiplier: float = 1, education_task_id: int = 71358, tempo_endpoint: str = 'https://api.tempo.io/4/worklogs/user/'):
    return calculator.calculate(tempo_token, account_key, users_rate, rate_multiplier, education_rate_multiplier, education_task_id, tempo_endpoint, date_start, date_end)