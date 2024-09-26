# zoe - 2024
# cookie sprinter
import time

import cv2
import numpy as np
import pyautogui

battle_button = "battleButton.png"
victory_image = "victory.png"
victory_image2 = "victory2.png"

def locate_and_click(image_path, threshold=0.7):
    # take a screenshot
    screenshot = pyautogui.screenshot()
    
    # convert and check screenshot ---------------------
    screen_np = np.array(screenshot)
    target_image = cv2.imread(image_path)
    screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)
    target_gray = cv2.cvtColor(target_image, cv2.COLOR_BGR2GRAY)
    screen_gray = cv2.GaussianBlur(screen_gray, (5, 5), 0)
    target_gray = cv2.GaussianBlur(target_gray, (5, 5), 0)
    result = cv2.matchTemplate(screen_gray, target_gray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(f"Checking for {image_path}: Max Val: {max_val}")
    #----------------------------------------------------

    # return if match was found
    if max_val >= threshold:
        return max_loc
    else:
        return None


while True:

    battle_location = locate_and_click(battle_button)
    if battle_location:
        click_x, click_y = battle_location
        pyautogui.click(click_x, click_y + 10)
        print(f"Clicked Battle Button at {click_x}, {click_y}")
    else:

        victory_location = locate_and_click(victory_image)
        victory2_location = locate_and_click(victory_image2)


        if victory2_location:
            click_x, click_y = victory2_location
            pyautogui.click(click_x + 600, click_y + 95)
            print(f"Clicked Victory2 at {click_x}, {click_y}")
        elif victory_location:
            # only click Victory if Victory2 is not found
            click_x, click_y = victory_location
            pyautogui.click(click_x, click_y)
            print(f"Clicked Victory at {click_x}, {click_y}")
    time.sleep(1) 
