import fitz  # PyMuPDF library (fitz is an alias)


def extract_text_with_formatting(pdf_path, output_file="extracted_text.txt"):
    """Extracts text from a PDF file preserving spaces, tabs, and newlines.

    Args:
        pdf_path (str): The path to the PDF file.
        output_file (str, optional): The name of the output text file. Defaults to "extracted_text.txt".
    """

    doc = fitz.open(pdf_path)

    with open(output_file, "w", encoding="utf-8") as f:
        for page in doc:
            # Extract text with block level formatting (preserving spaces, tabs, newlines)
            page_text = page.get_text("blocks")

            for block in page_text:
                # The block[4] contains the actual text
                text = block[4]
                f.write(text)


# Main block to run the code
if __name__ == "__main__":
    pdf_path = "Application.pdf"  # Replace with your PDF file path
    extract_text_with_formatting(pdf_path)

    print(f"Text extracted from '{pdf_path}' and saved to 'extracted_text.txt'")