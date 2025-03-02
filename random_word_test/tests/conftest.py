import pytest
import requests
from unittest.mock import patch

from playwright.sync_api import sync_playwright

from random_word_test.random_word_app import app
import subprocess
import time
import requests
import pytest

@pytest.fixture(scope="session", autouse=True)
def start_server():
    """Ensure Flask is running before tests start."""
    try:
        # Check if Flask is already running
        requests.get("http://127.0.0.1:5000")
        print("✅ Flask is already running!")
    except requests.ConnectionError:
        print("🔄 Starting Flask server...")
        flask_process = subprocess.Popen(["python", "..//random_word_app.py"])
        time.sleep(3)
        try:
            requests.get("http://127.0.0.1:5000")
            print("✅ Flask started successfully!")
        except requests.ConnectionError:
            flask_process.kill()
            pytest.exit("Failed to start Flask. Exiting tests.")

        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            flask_process.kill()
            pytest.exit("Failed to start Flask. Exiting tests.")

    yield
    flask_process.terminate()

@pytest.fixture(scope="session")
def browser_session():
    """Start a Playwright browser session."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://127.0.0.1:5000")  # Load the Flask app
        yield page
        browser.close()




@pytest.fixture(scope="function")
def client():
    """Flask test client fixture for making requests in tests."""
    with app.test_client() as client:
        yield client

@pytest.fixture
def mock_get_random_phrase():
    """Mock the external API call for get_random_phrase()."""
    with patch("app.requests.get") as mock_request:
        mock_request.return_value.status_code = 200
        mock_request.return_value.json.return_value = ["mock", "word", "test"]
        yield mock_request

@pytest.fixture
def mock_single_word():
    """Mock a single-word response from the external API."""
    with patch("app.requests.get") as mock_request:
        mock_request.return_value.status_code = 200
        mock_request.return_value.json.return_value = ["mockedword"]
        yield mock_request
