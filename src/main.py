from graph_builder import build_graph
from rca_engine import parse_alerts, parse_changes, find_root_cause
from llm_summary import summarize
import os

graph = build_graph("data/cmdb.json")
alerts = parse_alerts("data/alerts.json")
changes = parse_changes("data/changes.json")

results = find_root_cause(alerts, changes, graph)

for result in results:
    print("ALERT:", result["alert"]["message"])
    print("Possible root cause:", result["cause"]["change"])
    try:
        print("AI Explanation:", summarize(result["alert"], result["cause"]))
    except Exception as e:
        print("LLM not configured or error:", e)
    print("-" * 40)
