# Program     :  GOODLE FORM AUTO FILLER
# Author      :  ONG CHANG LE
# Email       :  websitecl03@gmail.com
# Start Date  :  02/05/2022 (One day project)
# Finish Date :  02/05/2022
# Update Date :  Any Day You Use It



# Disclaimer :
# 1. Don't spam others without permission, this program is just for fun and google form auto filler
# 2. Manage and control the number of form filler easily, but all the choice is randomize
# 3. The data sent will cause your investigation less accurate, so think twice before you use
# 4. Set the google form to no need to sign in with gmail to fill the form
# 5. You should know how to update the script according to your google form, to grab the web element and place in the template
# 6. If you want to involve in this project or any feedback, kindly hit the mail box mention above
# 7. Developer/Author will not take any responsibility on your account banning and troubles you cause



# Tutorial how to update this script:
# https://www.youtube.com/watch?v=HlYLIv0IPIk&t=1030s


# Demo Video
# https://youtu.be/Hkuh5pFczi4



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random


# requirements :
# 1. selenium module (pip install selenium)
# 2. chrome driver (https://chromedriver.chromium.org/downloads) --> Setup tutorial :https://www.youtube.com/watch?v=Xjv1sY630Uc




PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
# Insert your google form link below
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeNe5755EkIYbsXLb3peyFT0hmnxLVtyjJmb8IqnbK9DB4gcQ/viewform?usp=sf_link")
time.sleep(2)


# Set the number of forms you want to fill using for loops (now is 10)
for i in range(10):

    # Set random name with lst
    random_name = random.choice(["Joh", "kalj", "wkpl", "lak", "owk", "halo", "auto", "filler"])


    name = driver.find_element(by=By.XPATH,value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    name.click()
    name.send_keys(random_name)

    email = driver.find_element(by=By.XPATH,value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    email.click()
    email.send_keys(" ")

    button = random.choice(["i15","i18","i21","i24"])

    choose = driver.find_element(by=By.ID,value=button)
    choose.click()

    button2 = random.choice(["i32","i35","i38","i41","i44"])

    select = driver.find_element(by=By.ID,value=button2)
    select.click()


    driver.find_element(by=By.XPATH,value="//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div").click()
    # Refresh and fill again
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeNe5755EkIYbsXLb3peyFT0hmnxLVtyjJmb8IqnbK9DB4gcQ/viewform?usp=sf_link")

