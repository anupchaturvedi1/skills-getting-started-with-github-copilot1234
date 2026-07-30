from pathlib import Path


def test_signup_refreshes_activities_without_manual_reload():
    app_js_path = Path(__file__).resolve().parents[1] / "src" / "static" / "app.js"
    app_js = app_js_path.read_text()

    assert 'await fetchActivities()' in app_js
    assert 'signupForm.addEventListener("submit"' in app_js
