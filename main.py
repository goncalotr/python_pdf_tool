
# --- Imports ---

# Libraries
import os
from pypdf import PdfWriter, PdfReader

# Other source files
from src.display import display_menu
from src.testing import *
from src.pdf_edit import *

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            directory = input("Enter the path to the directory containing PDF files: ").strip()

            if not directory:
                print("No directory entered. Returning to menu.")
                continue

            output_file_name = "concatenated_directory_output.pdf" 
            concatenate_pdfs_in_directory(directory, output_file_name)

        elif choice == '2':
            try:
                num_dummy_files = int(input("How many dummy PDF files to create? (e.g., 3): "))
                pages_in_each = int(input("How many pages in each dummy PDF? (e.g., 2): "))
                dummy_output_dir = input("Enter directory to save dummies (default: 'test_dummies' in current dir): ") or "test_dummies"

                if num_dummy_files <= 0 or pages_in_each <= 0:
                    print("Number of files and pages must be positive integers.")
                    continue

                create_multiple_dummy_pdfs(
                    base_name="sample_doc",
                    num_files=num_dummy_files,
                    pages_per_file=pages_in_each,
                    output_dir=dummy_output_dir
                )

            except ValueError:
                print("Invalid input. Please enter numbers.")
            except Exception as e:
                print(f"An error occurred: {e}")

        elif choice == '3':
            print("Exiting PDF tool. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    print("Welcome to the Simple PDF Tool!")
    main()
