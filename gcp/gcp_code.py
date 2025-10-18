import json
import functions_framework

@functions_framework.http
def hello_http(request):
    """HTTP Cloud Function.
    Expects JSON with 'total_bilirubin' and 'direct_bilirubin' (or query params as fallback).
    Returns a simple JSON classification.
    """
    # Prefer JSON body; fall back to query parameters for convenience
    data = request.get_json(silent=True) or {}
    args = request.args or {}

    total = data.get("total_bilirubin", args.get("total_bilirubin"))
    direct = data.get("direct_bilirubin", args.get("direct_bilirubin"))

    # Presence check
    if total is None or direct is None:
        return (
            json.dumps({"error": "Both 'total_bilirubin' and 'direct_bilirubin' are required (mg/dL)."}),
            400,
            {"Content-Type": "application/json"},
        )

    # Type/convert check
    try:
        total_val = float(total)
        direct_val = float(direct)
    except (TypeError, ValueError):
        return (
            json.dumps({"error": "'total_bilirubin' and 'direct_bilirubin' must be numbers."}),
            400,
            {"Content-Type": "application/json"},
        )

    # Simple interpretation using Mount Sinai reference ranges:
    # total normal: 0.1 - 1.2 mg/dL
    # direct normal: < 0.3 mg/dL
    total_normal = 0.1 <= total_val <= 1.2
    direct_normal = direct_val < 0.3

    if total_normal and direct_normal:
        status = "normal"
        category = "Normal (total 0.1–1.2 mg/dL; direct <0.3 mg/dL)"
    else:
        status = "abnormal"
        if not direct_normal:
            category = "Elevated direct bilirubin (direct ≥ 0.3 mg/dL)"
        else:
            category = "Elevated total bilirubin (total outside 0.1–1.2 mg/dL)"

    payload = {
        "total_bilirubin_mg_per_dL": total_val,
        "direct_bilirubin_mg_per_dL": direct_val,
        "status": status,
        "category": category,
    }

    return json.dumps(payload), 200, {"Content-Type": "application/json"}
