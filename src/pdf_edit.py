
import os

import glob
from pypdf import PdfWriter, PdfReader

def concatenate_pdfs_in_directory(directory_path, output_filename="merged_output.pdf"):
    """
    Finds all PDF files in the specified directory, sorts them by name,
    and concatenates them into a single PDF.

    Args:
        directory_path (str): The path to the directory containing PDF files.
        output_filename (str): The name of the output PDF file (will be saved in the same directory).
    """
    if not os.path.isdir(directory_path):
        print(f"Error: Directory not found: {directory_path}")
        return

    pdf_files = sorted(
        list(set(
            glob.glob(os.path.join(directory_path, "*.pdf")) +
            glob.glob(os.path.join(directory_path, "*.PDF"))
        ))
    )

    if not pdf_files:
        print(f"No PDF files found in directory: {directory_path}")
        return

    merger = PdfWriter()
    print("\nConcatenating the following PDF files in order:")
    files_to_merge_count = 0
    for pdf_path in pdf_files:
        if os.path.basename(pdf_path) == output_filename:
            print(f"Skipping potential output file: {os.path.basename(pdf_path)}")
            continue
        
        print(f" - Adding: {os.path.basename(pdf_path)}")
        try:
            reader = PdfReader(pdf_path)
            if not reader.pages:
                print(f"   Warning: {os.path.basename(pdf_path)} has no pages or is invalid. Skipping.")
                continue
            for page in reader.pages:
                merger.add_page(page)
            files_to_merge_count +=1
        except Exception as e:
            print(f"  Error processing {os.path.basename(pdf_path)}: {e}. Skipping this file.")

    if len(merger.pages) > 0:
        output_path = os.path.join(directory_path, output_filename)
        try:
            with open(output_path, "wb") as f_out:
                merger.write(f_out)
            print(f"\nSuccessfully concatenated {files_to_merge_count} PDF(s) into: {output_path}")
        except Exception as e:
            print(f"Error writing output file {output_path}: {e}")
    else:
        print("No pages were added. Output file not created (possibly no valid PDFs found or all were empty).")

    merger.close()