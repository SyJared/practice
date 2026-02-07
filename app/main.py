"""Main application to print the mode based on APP_MODE environment variable."""
import os

"""Print whether the app is running in DEV or PROD mode based on APP_MODE."""
def main():
    mode = os.environ.get("APP_MODE", "prod")
    if mode == "dev":
        print("Running in DEV mode")
    else:
        print("Running in PROD mode")

if __name__ == "__main__":
    main()
