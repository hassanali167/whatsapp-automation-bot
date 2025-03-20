import pyautogui
import time
import cv2
import pytesseract
from reportlab.pdfgen import canvas

# Set Tesseract OCR Path (For Windows users)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def open_whatsapp():
    """ Open WhatsApp Desktop using Windows search. """
    pyautogui.hotkey("win", "s")  # Open Windows search
    time.sleep(1)
    pyautogui.write("WhatsApp")  # Type 'WhatsApp' in search
    time.sleep(1)
    pyautogui.press("enter")  # Press Enter to open
    time.sleep(5)  # Wait for WhatsApp to open

def open_chat(contact_name):
    """ Open the chat by searching for the contact name. """
    pyautogui.click(200, 150)  # Adjust this based on screen resolution
    time.sleep(1)
    
    pyautogui.write(contact_name)
    time.sleep(1)
    pyautogui.press("enter")  # Open the chat
    time.sleep(3)

def scroll_up(times=10):
    """ Scroll up multiple times to load older messages. """
    chat_area = (500, 500)  # Adjust coordinates for the chat area
    for _ in range(times):
        pyautogui.moveTo(chat_area)
        pyautogui.scroll(500)  # Scroll up
        time.sleep(1)

def capture_chat():
    """ Capture a screenshot of the chat area. """
    x, y, width, height = 200, 200, 500, 600  # Adjust for your screen
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot.save("whatsapp_chat.png")

def extract_text():
    """ Extract text from the captured chat image. """
    image = cv2.imread("whatsapp_chat.png")
    text = pytesseract.image_to_string(image)
    return text.strip()

def save_to_pdf(text, filename="whatsapp_chat.pdf"):
    """ Save extracted text to a PDF file. """
    c = canvas.Canvas(filename)
    c.drawString(100, 800, "WhatsApp Chat History")  # Title
    y = 780
    for line in text.split("\n"):
        c.drawString(100, y, line)
        y -= 20
    c.save()
    print(f"Chat saved to {filename}")

def download_chat(contact_name):
    """ Automate the entire process: open WhatsApp, extract messages, and save to PDF. """
    open_whatsapp()
    time.sleep(5)
    open_chat(contact_name)
    time.sleep(3)
    scroll_up(15)  # Scroll to load more messages
    time.sleep(3)
    capture_chat()
    extracted_text = extract_text()
    save_to_pdf(extracted_text)

# Example Usage
download_chat("Friend Name")  # Replace with contact or group name
