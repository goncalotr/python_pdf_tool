# Simple PDF Tool

This is a basic command-line tool written in Python to perform simple PDF operations, primarily:
- Concatenating all PDF files within a specified directory (sorted by name).
- Creating dummy PDF files (A4 size) with page numbers for testing purposes.

## Prerequisites

- Python 3.6+
- pip (Python package installer, usually comes with Python)

## Setup and Installation

1. Download or clone repository

2. Open terminal and navigate to the root of the project folder

3. Recommended: Create a virtual environment

4. Install required libraries

```bash
pip install pypdf reportlab
```

## Running the Program

Run the main script from the project's root directory:

```bash
python main.py
```

## Usage

The program will present a menu in the console:

```bash
--- PDF Tool Menu ---
1. Concatenate PDFs in a directory
2. Create dummy test PDFs (A4, page numbers in mm from bottom)
3. Exit
Enter your choice (1-3):
```

Concatenate PDFs in a directory:
Select option 1.
	You will be prompted to enter the full path to the directory containing the PDF files you want to merge.
	Example path: C:\Users\YourName\Desktop\MyPDFs or /home/yourname/Documents/PDF_Collection
	The tool will find all .pdf files, sort them by name, and merge them into a new file named concatenated_directory_output.pdf within the same directory you specified.
	Create dummy test PDFs:

Select option 2.
	You'll be asked for:
	The number of dummy PDF files to create.
	The number of pages for each dummy PDF.
	The directory where these dummy PDFs should be saved (defaults to a test_dummies subfolder if you just press Enter).
	The created PDFs will be A4 size and have "Page X of Y" written 15mm from the bottom.

Exit:
	Select option 3 to close the program.
