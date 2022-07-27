# 7/25/22 - 7/27/22
# Nathaniel Masson
# ------
# This will run without you installing selenium or pyautogui. But I'm assuming you have time and os installed.
# ------
# Last note; make sure you have the same Chrome version as the Chrome driver installed, or else
# chromedriver.exe won't run, and an error will occur.
# ------
from selenium import webdriver
import pyautogui
import time
import os

# ----------------------------------------------------------------------------------------------------------------------

# second octate
x = input("What location? (enter 'x' in 10.x.21.2-254): ")

a = input("User/Pass default? (y/n) ")
if a == "y":
    username = "admin"
    password = "admin"
if a == "n":
    username = input("Enter current username: ")
    password = input("Enter current password: ")

newPassword = input("Enter new password: ")
sleeptime = input("How long does it generally take for a website to load on your computer? (in seconds; no decimals.): ")

# ----------------------------------------------------------------------------------------------------------------------

for i in range(2, 255):
    ip_sig = ["10." + str(x) + ".21." + str(i)]
    for ip in ip_sig:
        response = os.popen(f"ping {ip} -n 1 -w 1000").read()
        print(response)
        if "Destination host unreachable." in response:
            continue
        if "Received = 1, Lost = 0" in response:
            path = '.\\passwordChangeMod\\chromedriver.exe'
            browser = webdriver.Chrome(path)

            # opening the browser windows
            browser.get("http://192." + str(x) + ".255." + str(i) + "/servlet?m=mod_data&p=security&q=load")

# ----------------------------------------------------------------------------------------------------------------------

            # logging in / ensuring if the website accessed is correct
            try:
                time.sleep(3)
                browser.find_element("id", "idUsername").send_keys(username)
            except:
                print("\n10." + str(x) + ".21." + str(i) + " is a valid url, but isn't what you're looking for! Continuing to next ip..\n")
                browser.close()
                continue

            browser.find_element("id", "idPassword").send_keys(password)
            browser.find_element("id", "idConfirm").click()

            # fullscreen
            pyautogui.press('f11')

            # moving mouse to click 'Security'
            time.sleep(int(sleeptime))
            pyautogui.moveTo(1385, 116)
            pyautogui.click()

            # editing the password
            browser.find_element("name", "editOldPassword").send_keys(password)
            browser.find_element("name", "editNewPassword").send_keys(newPassword)
            browser.find_element("name", "editConfirmPassword").send_keys(newPassword)

            # clicking the button to change the password
            browser.find_element("id", "btn_confirm1").click()

            # obviously, closing the browser once done with this ip instance
            browser.close()