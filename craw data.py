from selenium import webdriver
import random
from selenium.webdriver.common.keys import Keys
from time import sleep
from easygui import passwordbox



    #  1.2 Giả lập chrome
browser = webdriver.Chrome(executable_path="chromedriver.exe")
browser.get("https://shopee.vn/")
#Cào dữ liệu từ shoppe

mouse_shoppe = browser.find_elements_by_class_name("_1N6I4W")
print('Mouse Shoppe')
x = 1
for mouse in mouse_list:
    #mouns_l = mouns.find_element_by_xpath("_10Wbs- _5SSWfi UjjMrh")
    #sleep(random.randint(2,5))
    print(x,mouse.text)
    x = x+1
browser.close()
