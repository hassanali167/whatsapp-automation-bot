import pyautogui
import time
import pyperclip

# Constants
SEARCH_BAR_POS = (200, 150)  # Adjust based on screen resolution
WHATSAPP_SEARCH_DELAY = 1
CHAT_LOAD_DELAY = 2
MESSAGE_PASTE_DELAY = 1

def open_whatsapp():
    """ Open WhatsApp Desktop (Ensure it's pinned or available via search). """
    try:
        pyautogui.hotkey("win", "s")  # Open Windows search
        time.sleep(WHATSAPP_SEARCH_DELAY)
        pyautogui.write("WhatsApp")
        pyautogui.press("enter")
        time.sleep(5)  # Wait for WhatsApp to open
    except Exception as e:
        print(f"Error opening WhatsApp: {e}")

def search_contact(contact_name):
    """ Search and open a contact's chat in WhatsApp. """
    try:
        pyautogui.click(*SEARCH_BAR_POS)  # Click on the search bar
        time.sleep(WHATSAPP_SEARCH_DELAY)
        
        pyperclip.copy(contact_name)
        pyautogui.hotkey("ctrl", "v")  # Paste the contact name
        time.sleep(WHATSAPP_SEARCH_DELAY)
        pyautogui.press("enter")  # Open the chat
        time.sleep(CHAT_LOAD_DELAY)
    except Exception as e:
        print(f"Error searching for contact: {e}")

def send_message(contact_name, message):
    """ Send a WhatsApp message using the Desktop App. """
    try:
        search_contact(contact_name)

        pyperclip.copy(message)
        pyautogui.hotkey("ctrl", "v")  # Paste message
        time.sleep(MESSAGE_PASTE_DELAY)
        pyautogui.press("enter")  # Send message

        print(f"Message sent to {contact_name}")
    except Exception as e:
        print(f"Error sending message: {e}")

# Example Usage
if __name__ == "__main__":
    open_whatsapp()
    time.sleep(3)  # Ensure WhatsApp is fully open
    send_message("Friend Name", "Hello! This is an automated message.")
