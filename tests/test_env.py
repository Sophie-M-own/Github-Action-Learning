import os
def test_app_env_exists():
    env = os.environ.get("APP_ENV","")
    assert env != "","APP_ENV should be set by CI"
