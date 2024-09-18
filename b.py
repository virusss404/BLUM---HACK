import pyautogui
import time
import keyboard
import sys  # For exiting the program




name = '''
╔═╗╦╔═╗╔╦╗
╚═╗║╠═╣║║║
╚═╝╩╩ ╩╩ ╩

'''
print("@virussss404, " + name + "!")



# Flag to indicate the current image to search for
searching_for_a = True

# Time interval for finding each image
search_interval = 1  # 1 second for each image

# Time tracker for switching images
last_switch_time = time.time()

# Function to find and click the button 5 times
def find_and_click_button():
    global searching_for_a, last_switch_time
    
    current_time = time.time()
    
    # Switch image to search based on interval
    if current_time - last_switch_time >= search_interval:
        # Update last switch time
        last_switch_time = current_time
        
        # Determine which image to search for
        image_to_search = 'Crypto mining/ETH.png' if searching_for_a else 'Crypto mining/BTC.png'
        print(f"FIND BITCOIN '{image_to_search}'...")
        

        name = """
                                                                                                
  ____  _    _   _ __  __           _   _    _    ____ _  __
 | __ )| |  | | | |  \/  |         | | | |  / \  / ___| |/ /
 |  _ \| |  | | | | |\/| |  _____  | |_| | / _ \| |   | ' / 
 | |_) | |__| |_| | |  | | |_____| |  _  |/ ___ | |___| . \ 
 |____/|_____\___/|_|  |_|         |_| |_/_/   \_\____|_|\_\
                                                                                                                                                                                            
"""
        print("Hello, " + name + "!")


        try:
            # Locate the button image
            button_location = pyautogui.locateOnScreen(image_to_search, confidence=0.9)
            
            if button_location:
                print(f"Button '{image_to_search}' found at {button_location}")
                # Click on the button 5 times
                for _ in range(5):
                    pyautogui.click(button_location)
                print("Clicked 5 times!")
                
            else:
                print(f"'{image_to_search}' not found on the screen")
        
        except pyautogui.ImageNotFoundException:
            print(f"'{image_to_search}' image not found on the screen")
        except Exception as e:
            print(f"An error occurred: {e}")
        
        # Toggle the flag to search for the other image next time
        searching_for_a = not searching_for_a

# Flag to toggle between pause and resume
paused = False

# Function to toggle pause/resume
def toggle_pause():
    global paused
    paused = not paused
    if paused:
        print("Paused")
    else:
        print("Resumed")

# Function to quit the program
def quit_program():
    print("Exiting the program...")
    sys.exit()

# Bind the 'p' key to toggle pause/resume
keyboard.add_hotkey('p', toggle_pause)

# Bind the 'a' key to quit the program
keyboard.add_hotkey('a', quit_program)

# Main loop
while True:
    if not paused:
        find_and_click_button()
    time.sleep(0.1)  # Sleep for a short time to keep the loop responsive
