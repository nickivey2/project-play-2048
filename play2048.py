# Nicholas Ivey Play 2048 3/23/2016

#TODO: Import the module that will allow you to use Selenium
from selenium import webdriver
#TODO: Import the module that will allow you to use the up, down, left, and right keys on your keyboard
from selenium.webdriver.common.keys import Keys

def play2048( times ):
    #TODO: write code in this function that:
    # 1. opens a game of 2048 from the URL: https://gabrielecirulli.github.io/2048/
    browser = webdriver.Firefox()
    browser.get('https://gabrielecirulli.github.io/2048/')
    # 2. uses the parameter 'times' to determine how many times your code will try to play the game
    htmlElem = browser.find_element_by_tag_name('html')
    scoreElem = browser.find_element_by_class_name('score-container')
    # 3. for each 'time', press these keys in this order: UP, RIGHT, DOWN, LEFT
    i = 0
    for i in range(times):
        htmlElem.send_keys(Keys.UP)
        htmlElem.send_keys(Keys.LEFT)
        htmlElem.send_keys(Keys.DOWN)
        htmlElem.send_keys(Keys.RIGHT)
        i += 1
    # 4. print the final score after all tries to the screen 
    print('Total Score: ' +scoreElem.text)
