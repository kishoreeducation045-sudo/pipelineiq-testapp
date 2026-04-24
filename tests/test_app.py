"""Unit tests for app.py.

These tests will pass in the baseline state and fail when we intentionally
break the `add` or `multiply` functions for our failure scenarios.
"""
import os
import sys

# Ensure the app module is importable when pytest runs from the repo root
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, add, multiply


def test_home():
    """The root endpoint returns the expected greeting."""
    client = app.test_client()
    r = client.get("/")
    assert r.status_code == 200
    body = r.get_json()
    assert body["message"] == "PipelineIQ test app"


def test_health():
    """The health endpoint returns status ok."""
    client = app.test_client()
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json() == {"status": "ok"}


def test_add_positive():
    """add(2, 3) must equal 5."""
    assert add(2, 3) == 5


def test_add_negatives():
    """add handles negative numbers correctly."""
    assert add(-1, 1) == 0
    assert add(-5, -3) == -8


def test_multiply_basic():
    """multiply(4, 5) must equal 20."""
    assert multiply(4, 5) == 20


def test_multiply_zero():
    """multiply by zero returns zero."""
    assert multiply(0, 100) == 0
    assert multiply(100, 0) == 0
