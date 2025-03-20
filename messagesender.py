import pyautogui
import time
import pyperclip

def open_whatsapp():
    """ Open WhatsApp Desktop (Ensure it's pinned to Taskbar in Windows). """
    pyautogui.hotkey("win", "s")  # Open Windows search
    time.sleep(1)
    pyautogui.write("WhatsApp")  # Search for WhatsApp
    time.sleep(1)
    pyautogui.press("enter")  # Open WhatsApp
    time.sleep(5)  # Wait for WhatsApp to open

def send_message(contact_name, message):
    """ Send a WhatsApp message using the Desktop App. """
    
    # Click on the search bar (Position may vary, adjust as needed)
    pyautogui.click(200, 150)  # Adjust this based on screen resolution
    time.sleep(1)
    
    pyperclip.copy(contact_name)
    pyautogui.hotkey("ctrl", "v")  # Paste the contact name
    time.sleep(1)
    pyautogui.press("enter")  # Open the chat
    
    time.sleep(2)  # Wait for chat to load
    
    pyperclip.copy(message)
    pyautogui.hotkey("ctrl", "v")  # Paste message
    time.sleep(1)
    pyautogui.press("enter")  # Send message
    
    print(f"Message sent to {contact_name}")

# Example Usage
open_whatsapp()
time.sleep(5)  # Ensure WhatsApp is open before sending
send_message("Friend Name", "Hello! This is an automated message.")
