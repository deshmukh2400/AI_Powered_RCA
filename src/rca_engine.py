import json
from datetime import datetime

def parse_alerts(alert_path):
    with open(alert_path) as f:
        return json.load(f)

def parse_changes(change_path):
    with open(change_path) as f:
        return json.load(f)

def find_root_cause(alerts, changes, graph):
    root_causes = []
    for alert in alerts:
        alert_ci = alert["ci"]
        alert_time = datetime.fromisoformat(alert["timestamp"].replace("Z", "+00:00"))
        for change in changes:
            if graph.has_node(change["ci"]) and graph.has_node(alert_ci) and change["ci"] in graph and alert_ci in graph:
                if nx.has_path(graph, change["ci"], alert_ci):
                    change_time = datetime.fromisoformat(change["timestamp"].replace("Z", "+00:00"))
                    if abs((alert_time - change_time).total_seconds()) < 3600:
                        root_causes.append({
                            "alert": alert,
                            "cause": change
                        })
    return root_causes
