# Salary-calculator
You can find the working demo of the application at https://om1eea.deta.dev/docs#/default/calculate_salary_calculate_salary__get. Click 'Try it out' and pay attention to inputs and their descriptions. Short instructions are provided there.

## Local installation
Run uvicorn main:app --reload in the directory to run the application. You need FastAPI (see https://fastapi.tiangolo.com/tutorial/#install-fastapi) for this. Then go to http://127.0.0.1:8000/docs#/default/calculate_salary_calculate_salary__get and click 'Try it out'.

## Yet to do:
- Replace Jira task id with Jira task key in the request to simplify UX (will need to fetch information from Jira for this)