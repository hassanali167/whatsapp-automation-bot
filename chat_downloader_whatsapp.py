import pyautogui
import time
import cv2
import pytesseract
from reportlab.pdfgen import canvas

# Constants for positions and settings
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
SEARCH_BAR_POS = (200, 150)
CHAT_AREA = (500, 500)  # Adjust as needed
SCREENSHOT_REGION = (200, 200, 500, 600)  # Adjust for your screen
SCROLL_TIMES = 15
SCROLL_AMOUNT = 500

# Set Tesseract OCR Path (For Windows users)
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def open_whatsapp():
    """ Open WhatsApp Desktop using Windows search. """
    pyautogui.hotkey("win", "s")  # Open Windows search
    time.sleep(1)
    pyautogui.write("WhatsApp")  # Type 'WhatsApp' in search
    pyautogui.press("enter")  # Press Enter to open
    time.sleep(5)  # Wait for WhatsApp to open

def open_chat(contact_name):
    """ Open a specific chat in WhatsApp. """
    pyautogui.click(*SEARCH_BAR_POS)
    time.sleep(1)
    pyautogui.write(contact_name)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(3)

def scroll_up(times=SCROLL_TIMES):
    """ Scroll up in the chat window to load older messages. """
    pyautogui.moveTo(*CHAT_AREA)
    for _ in range(times):
        pyautogui.scroll(SCROLL_AMOUNT)
        time.sleep(0.5)  # Reduced delay for efficiency

def capture_chat(filename="whatsapp_chat.png"):
    """ Capture a screenshot of the chat area. """
    screenshot = pyautogui.screenshot(region=SCREENSHOT_REGION)
    screenshot.save(filename)
    return filename

def extract_text(image_path="whatsapp_chat.png"):
    """ Extract text from the chat screenshot using OCR. """
    try:
        image = cv2.imread(image_path)
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        print(f"Error extracting text: {e}")
        return ""

def save_to_pdf(text, filename="whatsapp_chat.pdf"):
    """ Save extracted chat text to a PDF file. """
    if not text:
        print("No text extracted, skipping PDF generation.")
        return
    
    c = canvas.Canvas(filename)
    c.drawString(100, 800, "WhatsApp Chat History")  # Title
    y = 780
    for line in text.split("\n"):
        c.drawString(100, y, line)
        y -= 20
    c.save()
    print(f"Chat saved to {filename}")

def download_chat(contact_name):
    """ Automate the process: open WhatsApp, extract messages, and save to PDF. """
    try:
        open_whatsapp()
        open_chat(contact_name)
        scroll_up()
        image_path = capture_chat()
        extracted_text = extract_text(image_path)
        save_to_pdf(extracted_text)
    except Exception as e:
        print(f"Error in chat download process: {e}")

# Example Usage
if __name__ == "__main__":
    download_chat("Friend Name")  # Replace with actual contact name
