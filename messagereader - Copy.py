import pyautogui
import cv2
import pytesseract

# Constants for screenshot region (Adjust as needed)
SCREENSHOT_REGION = (200, 300, 400, 500)
IMAGE_PATH = "chat.png"
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Set Tesseract OCR Path (Windows only)
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def capture_chat_area(image_path=IMAGE_PATH):
    """ Capture a screenshot of the chat messages. """
    try:
        screenshot = pyautogui.screenshot(region=SCREENSHOT_REGION)
        screenshot.save(image_path)
        return image_path
    except Exception as e:
        print(f"Error capturing screenshot: {e}")
        return None

def extract_text(image_path=IMAGE_PATH):
    """ Extract text from the chat screenshot using OCR. """
    try:
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError("Failed to load image.")
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        print(f"Error extracting text: {e}")
        return ""

def read_latest_messages():
    """ Read latest messages from WhatsApp Desktop. """
    image_path = capture_chat_area()
    if not image_path:
        return
    
    messages = extract_text(image_path)
    if messages:
        print("Latest Messages:\n", messages)
    else:
        print("No text extracted.")

# Example Usage
if __name__ == "__main__":
    read_latest_messages()
