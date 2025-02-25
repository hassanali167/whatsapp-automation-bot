#This code will send bulk messages to a WhatsApp contact or group using Python and PyAutoGUI.

import pyautogui
import time

def send_whatsapp_messages(message, count):
    # Delay to switch to WhatsApp Desktop
    print("You have 5 seconds to open WhatsApp and select the chat...")
    time.sleep(5)

    for i in range(count):
        # Type the message
        pyautogui.typewrite(message)
        
        # Press "Enter" to send
        pyautogui.press('enter')
        
        # Small delay between messages to avoid overwhelming the app
        time.sleep(0.2)
        
    print(f"{count} messages sent successfully!")

# Example usage
send_whatsapp_messages("Hello! How are you???? 🚀", 5)
