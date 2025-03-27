import pyautogui
import time
import pyperclip

# Constants
WHATSAPP_OPEN_DELAY = 5
SEARCH_DELAY = 2
MESSAGE_BOX_POS = (500, 900)  # Adjust based on screen resolution

def open_whatsapp():
    """ Opens WhatsApp Desktop (Ensure it is installed). """
    try:
        pyautogui.hotkey('win', 's')  # Open Windows search
        time.sleep(1)
        pyautogui.write('WhatsApp')
        pyautogui.press('enter')
        time.sleep(WHATSAPP_OPEN_DELAY)  # Wait for WhatsApp to open
    except Exception as e:
        print(f"❌ Error opening WhatsApp: {e}")

def search_contact(contact_name):
    """ Searches for a contact in WhatsApp Desktop. """
    try:
        pyautogui.hotkey('ctrl', 'f')  # Open search
        time.sleep(1)

        pyperclip.copy(contact_name)  # Copy contact name to clipboard
        pyautogui.hotkey("ctrl", "v")  # Paste the contact name
        time.sleep(SEARCH_DELAY)
        pyautogui.press('enter')  # Open the chat
        time.sleep(SEARCH_DELAY)
    except Exception as e:
        print(f"❌ Error searching for contact: {e}")

def send_whatsapp_message(contact_name, message):
    """ Sends a WhatsApp message using the Desktop app. """
    try:
        open_whatsapp()
        search_contact(contact_name)

        # Ensure message box is active
        pyautogui.click(*MESSAGE_BOX_POS)
        time.sleep(1)

        # Type and send message
        pyperclip.copy(message)
        pyautogui.hotkey("ctrl", "v")  # Paste message
        time.sleep(1)
        pyautogui.press('enter')  # Send the message

        print(f"✅ Message sent to {contact_name} successfully!")

    except Exception as e:
        print(f"❌ Error sending message: {e}")

# Example Usage
if __name__ == "__main__":
    contact_name = input("Enter the contact name: ")
    message = input("Enter your message: ")
    send_whatsapp_message(contact_name, message)
