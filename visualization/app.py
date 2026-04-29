from flask import Flask, send_from_directory
import json

app = Flask(__name__)

@app.route("/")
def home():
    try:
        with open("/app/reports/data_quality.json") as f:
            quality = json.load(f)
    except:
        quality = {}

    try:
        with open("/app/reports/data_research.json") as f:
            research = json.load(f)
    except:
        research = {}

    html = f"""
    <h1>Open Data AI Analytics</h1>

    <h2>Data Quality</h2>
    <pre>{quality}</pre>

    <h2>Data Research</h2>
    <pre>{research}</pre>

    <h2>Plots</h2>
    <img src="/plots/hist.png" width="400">
    <img src="/plots/scatter.png" width="400">
    """
    return html

@app.route("/plots/<path:filename>")
def serve_plot(filename):
    return send_from_directory("/app/plots", filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)