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
    author_firstname = os.getenv("AUTHOR_FIRSTNAME")
    author_secondname = os.getenv("AUTHOR_LASTNAME")
    author_email = os.getenv("AUTHOR_EMAIL")
    marking_definition = os.getenv("MARKING_DEFINITION")
    if (
        url
        and token
        and author_firstname
        and author_secondname
        and author_email
        and marking_definition
    ):
        print("Existing configuration found. Proceeding with process...")
        process_folder()
    else:
        print("Setup for OPENCTI API Access")
        url = input("Enter OPENCTI_URL: ")
        token = input("Enter OPENCTI_TOKEN: ")
        author_firstname = input("Enter AUTHOR FIRSTNAME: ")
        author_secondname = input("Enter AUTHOR_LASTNAME: ")
        author_email = input("Enter AUTHOR_EMAIL: ")
        marking_definition = input("Enter MARKING_DEFINITION: ")
        # Write the new environment variables to .env file
        with open(".env", "w") as f:
            f.write(f"OPENCTI_URL={url}\n")
            f.write(f"OPENCTI_TOKEN={token}\n")
            f.write(f"AUTHOR_FIRSTNAME={author_firstname}\n")
            f.write(f"AUTHOR_LASTNAME={author_secondname}\n")
            f.write(f"AUTHOR_EMAIL={author_email}\n")
            f.write(f"MARKING_DEFINITION={marking_definition}\n")

        print("Configuration saved. Please ensure to keep your .env file secure!")
        process_folder()


def process_folder():
    try:

        print("Starting to convert.", flush=True)
        folder_path = sys.argv[1] if len(sys.argv) > 1 else "."
        if folder_path:
            print(f"Folder path: {folder_path}", flush=True)
        else:
            print("No folder path provided. Using current directory.", flush=True)
            folder_path = "."
        folder_to_json(folder_path)
    except Exception as e:
        print(f"Error: {e}", flush=True)


if __name__ == "__main__":
    print("Starting...", flush=True)
    setup_opencti_config()
