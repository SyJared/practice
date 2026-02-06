import os

def get_mode():
    """Return the current app mode."""
    return os.getenv("APP_MODE", "prod")

def run_mode():
    """Return 'DEV' or 'PROD' based on mode."""
    mode = get_mode()
    if mode == "dev":
        return "DEV"
    return "PROD"


# ---------- Pytest Tests ----------

def test_get_mode_dev(monkeypatch):
    # Simulate APP_MODE=dev
    monkeypatch.setenv("APP_MODE", "dev")
    assert get_mode() == "dev"

def test_get_mode_default(monkeypatch):
    # Remove APP_MODE to test default
    monkeypatch.delenv("APP_MODE", raising=False)
    assert get_mode() == "prod"

def test_run_dev(monkeypatch):
    monkeypatch.setenv("APP_MODE", "dev")
    assert run_mode() == "DEV"

def test_run_prod(monkeypatch):
    monkeypatch.delenv("APP_MODE", raising=False)
    assert run_mode() == "PROD"


# Optional: standalone run
if __name__ == "__main__":
    print(run_mode())
