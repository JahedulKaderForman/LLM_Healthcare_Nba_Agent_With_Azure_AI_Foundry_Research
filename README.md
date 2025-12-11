# 🏀 NBA AI Agent - Next Best Action Engine (Azure AI Foundry)

A **NBA AI Agent** recommends personalized, contextual next-best actions for healthcare members using Azure SQL as a data source and Azure OpenAI for intelligent decisioning. This project demonstrates how LLMs can support care gap closure, improve satisfaction, and reduce avoidable risk. This project is intended solely for R&D / experimentation. All member data shown in examples is entirely fictional and not based on real individuals.

## Architecture Overview
<img width="975" height="568" alt="image" src="https://github.com/user-attachments/assets/d5316c2f-da55-43f3-aefe-73806f3c75de" />


## Architecture Flow:
1. Member ID or JSON sent to Azure Function
2. Function retrieves data from Azure SQL DB
3. Function injects data into a few-shot prompt
4. GPT generates next best actions
5. UI / Copilot displays results

## Example Inputs
```json
{
  "member_id": "M123456",
  "hedis_gaps": ["Colorectal Cancer Screening", "HbA1c Test"],
  "cahps_scores": {
    "access_to_care": "low",
    "care_coordination": "medium",
    "communication": "low"
  },
  "sdoh_flags": ["transportation", "low_income"],
  "risk_score": 0.81,
  "last_visit": "2025-05-10",
  "recent_claims": [
    {
      "type": "ER",
      "date": "2025-06-01",
      "reason": "Asthma exacerbation"
    },
    {
      "type": "PCP",
      "date": "2025-05-10",
      "reason": "Annual wellness visit"
    }
  ]
}
```
## Example Output:
```json
{
  "action": "Mobile screening outreach",
  "reason": "High diabetes risk + transportation issue + care gap"
}
```


## Few-shot Example Prompt

You are a healthcare engagement assistant. Given a member's data, identify the top 1-2 next best actions to close care gaps, improve satisfaction, or reduce risk.
Always explain the reasoning. Focus on personalized, actionable suggestions based on risk and gaps.

Member Profile:
- HEDIS Gaps: Colorectal screening, HbA1c
- CAHPS issues: Low access to care, poor communication
- Risk: 0.81 (high)
- SDOH: Transportation, Low Income
- Recent Claims: ER visit for asthma on 6/1, PCP visit on 5/10

What is the next best action?

## LLM Output:
```json

{
  "next_best_actions": [
    {
      "action": "Schedule mobile screening for colorectal cancer",
      "reason": "Member is overdue for colorectal screening and has transportation issues. A mobile solution addresses both care gap and SDOH barrier."
    },
    {
      "action": "Engage member with a nurse educator about asthma management",
      "reason": "Recent ER visit for asthma signals poor control. Education could reduce future utilization and improve satisfaction."
    }
  ]
}

```

## Azure Function

- Accepts member ID or JSON
- Retrieves member data from Azure SQL DB
- Builds few-shot prompt
- Sends request to GPT
- Returns structured NBA recommendations



## Integrate into Copilot Studio or UI

Workflow:
1. User selects “Suggest Next Best Action”
2. UI collects or fetches member data
3. UI sends data to Azure Function API
4. API returns NBA recommendations
5. UI displays them


