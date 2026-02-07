"""
Docstring for app.main
"""
import os

"""main function"""
def main():
    mode = os.environ.get("APP_MODE", "prod")
    if mode == "dev":
        print("Running in DEV mode")
    else:
        print("Running in PROD mode")

if __name__ == "__main__":
    main()
