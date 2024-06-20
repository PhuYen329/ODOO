import json

def initialize_default_data(
    status="error", data=None, error="Unexpected error occurred"
):
    if data is None:
        data = []
    return json.dumps({"status": status, "data": data, "error": error})
