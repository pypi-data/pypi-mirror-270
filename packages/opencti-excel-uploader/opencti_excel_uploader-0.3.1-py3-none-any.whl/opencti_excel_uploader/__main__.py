import os
from dotenv import load_dotenv

load_dotenv()  # Load the environment variables from .env file

from .xlsx_utils import folder_to_json
import sys


def main():
    setup_opencti_config()


def setup_opencti_config():
    # Load existing environment variables from .env if it exists
    load_dotenv(".env")

    # Check if environment variables are set
    url = os.getenv("OPENCTI_URL")
    token = os.getenv("OPENCTI_TOKEN")

    if url and token:
        print("Existing configuration found. Proceeding with process...")
        process_folder()
    else:
        print("Setup for OPENCTI API Access")
        url = input("Enter OPENCTI_URL: ")
        token = input("Enter OPENCTI_TOKEN: ")

        # Write the new environment variables to .env file
        with open(".env", "w") as f:
            f.write(f"OPENCTI_URL={url}\n")
            f.write(f"OPENCTI_TOKEN={token}\n")

        print("Configuration saved. Please ensure to keep your .env file secure!")

        # Set environment variables for current session
        os.environ["OPENCTI_URL"] = url
        os.environ["OPENCTI_TOKEN"] = token

        process_folder()


def process_folder():
    try:

        print("Starting to convert.", flush=True)
        # Assuming 'folder_to_json' needs these credentials, pass them as needed
        folder_path = sys.argv[1] if len(sys.argv) > 1 else "."
        if folder_path:
            print(f"Folder path: {folder_path}", flush=True)
        else:
            print("No folder path provided. Using current directory.", flush=True)
            folder_path = "."
        folder_to_json(folder_path)
        # Modify this line as per actual function signature
    except Exception as e:
        print(f"Error: {e}", flush=True)


if __name__ == "__main__":
    print("Starting...", flush=True)
    setup_opencti_config()
