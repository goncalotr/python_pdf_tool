
# --- Libraries ---
import os
from pypdf import PdfWriter, PdfReader

# --- Functions ---

def concatenate_pdfs(pdf_list, output_filename="concatenated_output.pdf"):
	"""
	Concatenates a list of PDF files into a single PDF.

	Args:
		pdf_list (list): A list of paths to PDF files to concatenate.
		output_filename (str): The name of the output PDF file.
	"""

	merger = PdfWriter()

	for pdf_path in pdf_list:
		if not os.path.exists(pdf_path):
			print(f"Warning: File not found and will be skipped: {pdf_path}")
			continue
		try:
			reader = PdfReader(pdf_path)
			for page in reader.pages:
				merger.add_page(page)
			print(f"Added: {pdf_path}")
		except Exception as e:
			print(f"Error processing {pdf_path}: {e}")
			

	if len(merger.pages) > 0:
		try:
			with open(output_filename, "wb") as f_out:
				merger.write(f_out)
			print(f"Successfully concatenated PDFs into: {output_filename}")
		except Exception as e:
			print(f"Error writing output file {output_filename}: {e}")
	else:
		print("No pages were added. Output file not created.")

	merger.close()

# --- Main ---

if __name__ == "__main__":

	try:
		writer1 = PdfWriter()
		writer1.add_blank_page(width=200, height=200)
		with open("dummy1.pdf", "wb") as f: writer1.write(f)
		writer1.close()

		writer2 = PdfWriter()
		writer2.add_blank_page(width=300, height=300) # Different size for demo
		with open("dummy2.pdf", "wb") as f: writer2.write(f)
		writer2.close()

		print("Dummy PDFs created for demonstration.")

	except Exception as e:
		print(f"Could not create dummy PDFs (pypdf might need to be installed): {e}")
		print("Please ensure you have pypdf installed: pip install pypdf")
		print("And provide your own PDF files for testing.")

	pdfs_to_join = ["dummy1.pdf", "non_existent_file.pdf", "dummy2.pdf"]
	output_pdf_name = "my_merged_document.pdf"
	concatenate_pdfs(pdfs_to_join, output_pdf_name)

	if os.path.exists("dummy1.pdf"): os.remove("dummy1.pdf")
	if os.path.exists("dummy2.pdf"): os.remove("dummy2.pdf")
