import os
import json
from langchain_openai import AzureChatOpenAI
from langchain.schema import HumanMessage

def generate_nba():
    endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
    deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    api_key = os.environ["AZURE_OPENAI_API_KEY"]
    api_version = os.environ["AZURE_OPENAI_API_VERSION"]

    client = AzureChatOpenAI(
        api_version=api_version,
        azure_deployment=deployment,
        azure_endpoint=endpoint,
        api_key=api_key,
    )

    member_data = {
        "member_id": "M123456",
        "hedis_gaps": ["Colorectal Screening", "HbA1c Test"],
        "cahps_scores": {"access_to_care": "low", "communication": "low"},
        "sdoh_flags": ["transportation", "low_income"],
        "risk_score": 0.81,
        "recent_claims": [
            {"type": "ER", "date": "2025-06-01", "reason": "Asthma"},
            {"type": "PCP", "date": "2025-05-10", "reason": "Wellness Visit"}
        ]
    }

    prompt = f"""
    You are a healthcare assistant.

    Member Profile:
    - HEDIS Gaps: {', '.join(member_data['hedis_gaps'])}
    - CAHPS Scores: {json.dumps(member_data['cahps_scores'])}
    - SDOH Flags: {', '.join(member_data['sdoh_flags'])}
    - Risk Score: {member_data['risk_score']}
    - Recent Claims: {json.dumps(member_data['recent_claims'], indent=2)}

    Based on this, return 1–2 personalized next best actions and explain why.
    """

    summary_prompt = f"""
    Summarize this into 2 short bullet points, no explanations:

    {prompt}
    """

    response = client([HumanMessage(content=summary_prompt)])
    return response.content
