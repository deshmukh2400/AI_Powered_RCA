import os

try:
    import openai
    from dotenv import load_dotenv
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    USE_LLM = openai.api_key is not None
except ImportError:
    USE_LLM = False

def summarize(alert, change):
    if not USE_LLM:
        return "(LLM summary disabled — no OpenAI key found)"
    
    prompt = f"""
Given the following IT alert and a recent change, explain in plain English how the change could have caused the alert.

Alert:
- CI: {alert['ci']}
- Time: {alert['timestamp']}
- Message: {alert['message']}

Change:
- CI: {change['ci']}
- Time: {change['timestamp']}
- Change Detail: {change['change']}

Explain the cause-effect relationship briefly:
"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6,
            max_tokens=150,
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"(LLM summary error: {e})"
