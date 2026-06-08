from vertexai.preview.generative_models import GenerativeModel
import json, functions_framework

model = GenerativeModel("gemini-1.5-pro")

@functions_framework.http
def rwa_agent(request):
    # Demo PLC data - simulate BRALIRWA methane tank
    plc_data = {"tank_level": 87, "methane_ppm": 125, "pressure_bar": 3.4}

    prompt = f"""You are RWA Industrial Safety Agent for Rwanda factories.
PLC Data: {plc_data}
RULES: If methane_ppm > 100 → Return JSON {{"status":"EMERGENCY","action":"CLOSE_VALVE","drone":"LAUNCH","alert":"BRALIRWA_LEAK"}}
Else → Return JSON {{"status":"SAFE","action":"MONITOR"}}"""

    response = model.generate_content(prompt)
    try:
        return json.loads(response.text)
    except:
        return {"status": "SAFE", "action": "MONITOR"}
