from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
from selenium.webdriver.common.action_chains import ActionChains

def open_chrome(site):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.maximize_window()
    driver.get(site)
    return driver


def login(driver, user, pwd):
    load = ''
    while load != 'completed':
        try:
            user_field = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
            user_field.send_keys(user)
            pwd_field = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
            pwd_field.send_keys(pwd)
            load = 'completed'
        except:
            time.sleep(2)

    enter_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div')
    enter_button.click()
    time.sleep(3)
          
    #handle popup 
    load = ''
    counter = 0
    while True:
        #If after 15 seconds the popup does not apear then the loging falied
        try:
            notification_popup = driver.find_element_by_xpath('//*[name()="button" and @class="aOOlW   HoLwm "]')
            notification_popup.click()
            return 'succsses', ''
        except:
            try:
                #handle popup that asks if we want the browser to keep our info
                notification_popup = driver.find_element_by_xpath('//*[name()="button" and @class="sqdOP yWX7d    y3zKF     "]')  
                notification_popup.click()
                counter = 0
            except:
                pass
                
        #Loging falied handler
        
            try:
                Warning_message = driver.find_element_by_xpath('//*[@id="slfErrorAlert"]')
                Warning_message = Warning_message.text
                driver.quit()
                message = "Não foi possivel fazer o Login na sua conta.\n " + Warning_message
                return 'fail', message
            except:
                if counter == 15:
                    driver.quit()
                    message = "Não foi possivel conectar no seu Instagram."
                    return 'fail', message
        time.sleep(1)
        counter += 1


def like_posts(driver, qty):
    posts_liked = 0
    while posts_liked <= qty:
        #Find loaded Hearts in the chrome and add them in a list
        hearts = driver.find_elements_by_xpath('//*[name()="svg" and @fill="#262626" and @aria-label="Like"]')
        #hearts = driver.find_elements_by_xpath('//*[name()="svg" and @fill="#ed4956" and @aria-label="Descurtir"]')
        if len(hearts) == 0:
            hearts = driver.find_elements_by_xpath('//*[name()="svg" and @fill="#262626" and @aria-label="Curtir"]')

        hearts_qty = len(hearts)

        #chek if there more white hearts to click, if not, close the program
        if hearts_qty == 0:
            posts_liked = str(posts_liked)
            return posts_liked + " posts foram curtidos dessa vez!"
        else:
            #Like the posts
            try:
                actions = ActionChains(driver)
                actions.move_to_element(hearts[0]).perform()
                time.sleep(1)
                hearts[0].click()
                driver.find_element_by_css_selector('body').send_keys(Keys.DOWN)
                time.sleep(1)
            except:
                pass
            posts_liked += 1
            print (posts_liked)

    return "Limite máximo de " + str(posts_liked) + " posts curtidos atingido!"