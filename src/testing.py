
import os

from pypdf import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm

def create_dummy_pdf_with_pages(filename="dummy_test.pdf", num_pages=3):
    """
    Creates a dummy PDF with a specified number of pages,
    each page having "Page X of Y" written on it.
    """

    c = canvas.Canvas(filename, pagesize=A4)
    width_points, height_points = A4

    for i in range(1, num_pages + 1):
        c.setFont("Helvetica", 12)
        text = f"Page {i} of {num_pages}"

        text_width_points = c.stringWidth(text, "Helvetica", 12)
        x_position_points = (width_points - text_width_points) / 2
        y_position_points = 15 * mm

        c.drawString(x_position_points, y_position_points, text)
        c.showPage()

    try:
        c.save()
    except Exception as e:
        print(f"Error saving dummy PDF {filename}: {e}")

def create_multiple_dummy_pdfs(base_name="dummy_test_pdf", num_files=2, pages_per_file=2, output_dir="."):
    """Creates multiple dummy PDF files for testing concatenation."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
        print(f"Created directory: {output_dir}")

    print(f"\nCreating {num_files} dummy PDF files in '{os.path.abspath(output_dir)}':")
    for i in range(1, num_files + 1):
        filename = os.path.join(output_dir, f"{base_name}_{i}.pdf")
        create_dummy_pdf_with_pages(filename, pages_per_file)
