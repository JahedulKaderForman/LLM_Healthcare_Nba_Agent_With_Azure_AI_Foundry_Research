import azure.functions as func
from Nba import generate_nba

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        summary = generate_nba()
        return func.HttpResponse(summary, status_code=200)
    except Exception as e:
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
