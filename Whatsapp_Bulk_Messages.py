import pyautogui
import time

def send_bulk_messages(message, count, delay=0.2):
    """
    Sends bulk messages to an open WhatsApp chat.
    
    :param message: The message to send.
    :param count: Number of times to send the message.
    :param delay: Delay between messages to avoid spamming.
    """
    try:
        input("🔔 Switch to the WhatsApp chat window and press Enter to continue...")

        for i in range(count):
            pyautogui.typewrite(message)  # Type the message
            pyautogui.press('enter')  # Send message
            time.sleep(delay)  # Avoid overwhelming the app

        print(f"✅ {count} messages sent successfully!")

    except Exception as e:
        print(f"❌ Error: {e}")

# Example Usage
if __name__ == "__main__":
    message = input("Enter the message to send: ")
    count = int(input("Enter the number of times to send the message: "))
    send_bulk_messages(message, count)
