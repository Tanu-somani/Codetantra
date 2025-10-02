import time
import pyautogui

def main():
    # Countdown before starting the auto-typer
    print("Autotyper will start in:")
    for i in range(10, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    
    print("Starting the auto-typer!")

    # Open the file that contains the text to be typed
    with open("code.txt", "r") as file:
        data = file.readlines()

    # Loop through each line in the file and type it out
    for line in data:
        pyautogui.typewrite(line.strip())  # Remove any leading/trailing whitespaces
        pyautogui.press("enter")  # Press 'Enter' after each line
        time.sleep(0)  # Short delay before typing the next line (adjust as needed)

if __name__ == "__main__":
    main()