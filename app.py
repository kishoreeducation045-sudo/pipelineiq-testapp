"""PipelineIQ test application — a minimal Flask app with a few endpoints.

This app is intentionally simple. Its only purpose is to have a CI pipeline
that we can break in controlled ways for PipelineIQ's RCA engine to diagnose.
"""
from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route("/")
def home():
    """Root endpoint — returns a simple greeting."""
    return jsonify({"message": "PipelineIQ test app", "version": "1.0.0"})


@app.route("/health")
def health():
    """Health check endpoint — used by CI and uptime monitors."""
    return jsonify({"status": "ok"})


@app.route("/ping-external")
def ping_external():
    """Calls an external API — depends on the `requests` library.

    This endpoint makes the app sensitive to `requests` version changes,
    which is useful for triggering dependency-related failures.
    """
    try:
        r = requests.get("https://httpbin.org/status/200", timeout=2)
        return jsonify({"external_status": r.status_code})
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 502


def add(a, b):
    """Add two numbers. Used by tests."""
    return a + b


def multiply(a, b):
    """Multiply two numbers. Used by tests."""
    return a + b  # wrong operation — intentional break


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
