# Made by  BOSS Jason-_- 
from sys import stdout
from os import system
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time
from time import sleep
import random
import tkinter
import os
import termcolor
from termcolor import colored

now = datetime.now()
current_time = now.strftime("[%H:%M:%S]")
clear = lambda: os.system('cls')
system('title [Mass Account Creator]')





adlogo = """

  ___      _  ___  ___                           _     _ 
 / _ \    | | |  \/  |                          | |   | |
/ /_\ \ __| | | .  . | ___  _ __ ___   ___ _ __ | |_  | |
|  _  |/ _` | | |\/| |/ _ \| '_ ` _ \ / _ \ '_ \| __| | |
| | | | (_| | | |  | | (_) | | | | | |  __/ | | | |_  |_|
\_| |_/\__,_| \_|  |_/\___/|_| |_| |_|\___|_| |_|\__| (_)
                                                         
                                                         

"""
print(colored(adlogo , 'magenta'))
print(colored("JOIN MY DISCORD SERVER :) : https://discord.gg/wA5G4KH", 'magenta'))
print(colored("Go take a look at my shoppy.gg :) : https://shoppy.gg/@Lepetithacker", 'magenta'))
print(colored("Future ad is coming !", 'magenta'))
sleep(10)
clear()


logo = """
  __  __                                                 _    _____                _             
 |  \/  |                 /\                            | |  / ____|              | |            
 | \  / | __ _ ___ ___   /  \   ___ ___ ___  _   _ _ __ | |_| |     _ __ ___  __ _| |_ ___  _ __ 
 | |\/| |/ _` / __/ __| / /\ \ / __/ __/ _ \| | | | '_ \| __| |    | '__/ _ \/ _` | __/ _ \| '__|
 | |  | | (_| \__ \__ \/ ____ \ (_| (_| (_) | |_| | | | | |_| |____| | |  __/ (_| | || (_) | |   
 |_|  |_|\__,_|___/___/_/    \_\___\___\___/ \__,_|_| |_|\__|\_____|_|  \___|\__,_|\__\___/|_|   by Jason-_-#7076
                                                                                                 
                                                                                                 
                                                                                                            
                                                                                                            
"""





print(colored(logo, 'magenta'))
print(colored('Mass Account Creator ! Beta v0.2', 'magenta'))
print('')
print('')


fichier = open("log.txt", "a")
fichier.close
accNo = int(input(colored(current_time + " " + "How many accounts ? : ", 'magenta')))

print(colored(current_time + " " + "[-]Requesting Proxies:", 'blue'))
req_proxy = RequestProxy()
req_proxy.set_logger_level(50)
proxies = req_proxy.get_proxy_list()
maxNum = len(proxies)
print(colored(current_time + " " + "[+]Proxies Requested !", 'green'))
print(colored(current_time + " " +" [+] Max Proxies:" + str(maxNum) + "\n \n", 'green'))


i = 0


while accNo > i:
    k =random.randint(0, maxNum-1)
    l =random.randint(0, maxNum-1)
    PROXY = proxies[k].get_address()
    PROXY_PLACE = proxies[k].country
    first_name = (random.choice(open("Fnames.txt").read().split()))
    last_name =  (random.choice(open("Lnames.txt").read().split()))
    full_name = (first_name + ' ' + last_name)
    username = (first_name + last_name + '.' + str(random.randint(1, 100)) + str(random.randint(1, 1000)))
    password = (open("password.txt").readline())
    email = (username + '@' + 'gmail.com')
    print(colored(current_time + " " + "[-]Connecting to Proxy: " + PROXY + "\n", 'blue'))
    print(colored(current_time + " " + "[+]Connected !", 'green'))
    print(colored(current_time + " " + "[+]IP is from: " + str(PROXY_PLACE) + "\n \n", 'green'))

    webdriver.DesiredCapabilities.CHROME['proxy']={
        "httpProxy":PROXY,
        "ftpProxy":PROXY,
        "sslProxy":PROXY,

        "proxyType":"MANUAL",
    }
    
    #browser.get('https://www.expressvpn.com/what-is-my-ip')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-logging")
    chrome_options.add_argument("--disable-login-animations")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-default-apps")
    chrome_options.add_argument("--log-level=3")
    browser = webdriver.Chrome(ChromeDriverManager().install())
    try:
        browser.set_page_load_timeout(30) # wait 30 second
        browser.get('https://www.instagram.com/accounts/emailsignup/')
    except TimeoutException as ex:
        print(colored(current_time + " " + "[!]Could not load website ...", 'red'))
        print(colored(current_time + " " + "[-]Trying again !", 'blue'))
        browser.close()
        continue
        
    print(colored(current_time + " " + "[+]Instagram Webpage Opened ! \n \n", 'green'))
    sleep(3)
    
    try:
        email_in = browser.find_element_by_name("emailOrPhone")
    except NoSuchElementException:
        continue
    
    email_in.send_keys(email)
    sleep(4)

    print(colored(current_time + " " + "[+] Your randomize Email:" + email + "\n \n", 'green'))

    full_name_in = browser.find_element_by_name("fullName")
    full_name_in.send_keys(full_name)
    sleep(5)
    print(colored(current_time + " " + "[+]Your randomize Full Name is: " + full_name + "\n \n", 'green'))
    username_in = browser.find_element_by_name("username")
    username_in.send_keys(username)
    print(colored(current_time + " " + "[+]Your randomize Username is: " + username + "\n \n", 'green'))
    sleep(4)

    password_in = browser.find_element_by_name("password")
    password_in.send_keys(password)
    print("\n \n Password Entred \n \n")
    sleep(3)

    sign_up = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[7]/div/button')
    sign_up.click()
    sleep(5)

    year_index = (random.randint(20, 46))
    month_index = (random.randint(1, 12))
    day_index = (random.randint(1, 27))

    year_in =  Select(browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[1]/select'))
    month_in =  Select(browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[2]/select'))
    day_in =  Select(browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select'))
    year_in.select_by_index(year_index)
    print("\n Years Entred \n")
    sleep(1)
    month_in.select_by_index(month_index)
    print("\n Month Entred \n")
    sleep(1)
    day_in.select_by_index(day_index)
    print("\n Date Entred \n")
    sleep(5)
    try:
        next1 = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[7]/div/button')
        next1.click()
    except NoSuchElementException:
        next1 = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[5]/div[2]/button') 
        next1.click()
    sleep(10)
    with open('username.txt', 'w') as f_output:
            f_output.write(username)
    browser.close()

    i = i+1
