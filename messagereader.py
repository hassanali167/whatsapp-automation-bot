import pyautogui
import cv2
import pytesseract
import time

# Set Tesseract OCR Path (Windows only)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def capture_chat_area():
    """ Capture a screenshot of the chat messages. """
    x, y, width, height = 200, 300, 400, 500  # Adjust as needed
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot.save("chat.png")

def extract_text():
    """ Extract text from the chat screenshot using OCR. """
    image = cv2.imread("chat.png")
    text = pytesseract.image_to_string(image)
    return text.strip()

def read_latest_messages():
    """ Read latest messages from WhatsApp Desktop. """
    capture_chat_area()
    messages = extract_text()
    print("Latest Messages:\n", messages)

# Example Usage
read_latest_messages()
