from PIL import Image
import pytesseract
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit
import re

# Path to your image file
image_path = '/Users/aseempathak/Downloads/Python/Python-Coding-Practice/Learning/Day 14/Images/paknSav.jpeg'

# Extract text from image
extracted_text = pytesseract.image_to_string(Image.open(image_path))

# PDF file path to save the extracted text
pdf_output = '/Users/aseempathak/Downloads/Python/Python-Coding-Practice/Learning/Day 14/PDF files/File.pdf'

# Initialize PDF canvas
c = canvas.Canvas(pdf_output, pagesize=letter)

# Define starting position and maximum width for text
x, y = 100, 750
max_width = 400

# Split the extracted text into lines that fit within max_width using simpleSplit
lines = simpleSplit(extracted_text, "Helvetica", 12, max_width)

# Set font and size
c.setFont("Helvetica", 12)

# Regular expression to find lines with amounts
amount_pattern = r'\$\d+\.\d+'

# Determine right alignment position based on page width
page_width = letter[0]
amount_position = page_width - 100  # Adjust as needed for your layout

# Write lines to PDF
for line in lines:
    # Check if the line contains an amount
    if re.search(amount_pattern, line):
        # Split line into text and amount
        match = re.search(amount_pattern, line)
        text_part = line[:match.start()].strip()
        amount_part = line[match.start():].strip()

        # Draw text part
        c.drawString(x, y, text_part)

        # Right-align amount part
        c.drawRightString(amount_position, y, amount_part)
    else:
        # Draw regular line
        c.drawString(x, y, line)

    y -= 20  # Adjust line spacing as needed

# Save PDF
c.save()

print(f"Text extracted from image and saved to {pdf_output}")
