import os
import pytesseract
from PyPDF2 import PdfReader
from PIL import Image
from pathlib import Path
from tkinter import Tk, filedialog

# Set up pytesseract path if required (adjust for your installation)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Define the banner
BANNER = """
▒██   ██▒▄▄▄█████▓ ██▀███   ▄▄▄       ▄████▄  ▄▄▄█████▓
▒▒ █ █ ▒░▓  ██▒ ▓▒▓██ ▒ ██▒▒████▄    ▒██▀ ▀█  ▓  ██▒ ▓▒
░░  █   ░▒ ▓██░ ▒░▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▒ ▓██░ ▒░
 ░ █ █ ▒ ░ ▓██▓ ░ ▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒░ ▓██▓ ░ 
▒██▒ ▒██▒  ▒██▒ ░ ░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░  ▒██▒ ░ 
▒▒ ░ ░▓ ░  ▒ ░░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░  ▒ ░░   
░░   ░▒ ░    ░      ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒       ░    
 ░    ░    ░        ░░   ░   ░   ▒   ░          ░      
 ░    ░              ░           ░  ░░ ░               
                                     ░                    
"""

def extract_text_from_image(image_path):
    """Extract text from an image file."""
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        return f"Error extracting text from image: {e}"

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text.strip()
    except Exception as e:
        return f"Error extracting text from PDF: {e}"

def save_text_to_file(text, filename):
    """Save extracted text to a .txt file in the Downloads folder."""
    downloads_folder = Path.home() / "Downloads"
    downloads_folder.mkdir(exist_ok=True)  # Ensure Downloads folder exists
    file_path = downloads_folder / filename
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text)
        return file_path
    except Exception as e:
        return f"Error saving file: {e}"

def main():
    print(BANNER)
    print("\nWelcome to XTRACT - Extract text from images and PDFs!\n")
    
    while True:
        print("1. Extract text from an image")
        print("2. Extract text from a PDF")
        print("3. Exit")
        choice = input("\nEnter your choice (1/2/3): ").strip()

        if choice == "1":
            print("\nPlease select an image file.")
            Tk().withdraw()  # Hide the root tkinter window
            file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
            if file_path:
                text = extract_text_from_image(file_path)
                print("\nExtracted Text:\n")
                print(text)
                filename = input("\nEnter a name for the saved file (e.g., 'output.txt'): ").strip()
                save_path = save_text_to_file(text, filename)
                print(f"\nText saved to: {save_path}")
            else:
                print("No file selected. Please try again.")

        elif choice == "2":
            print("\nPlease select a PDF file.")
            Tk().withdraw()  # Hide the root tkinter window
            file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
            if file_path:
                text = extract_text_from_pdf(file_path)
                print("\nExtracted Text:\n")
                print(text)
                filename = input("\nEnter a name for the saved file (e.g., 'output.txt'): ").strip()
                save_path = save_text_to_file(text, filename)
                print(f"\nText saved to: {save_path}")
            else:
                print("No file selected. Please try again.")

        elif choice == "3":
            print("\nThank you for using XTRACT. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
