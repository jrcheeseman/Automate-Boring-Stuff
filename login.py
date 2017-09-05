# -*- coding: utf-8 -*-
"""
Automate the Boring Stuff - Chapter 11 – Web Scraping

Filling out and submitting forms: Logging into YahooMail

"""

from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://mail.yahoo.com')
try:
    emailElem = browser.find_element_by_id('login-username')
    emailElem.send_keys('[email address]')
    
    nextElem = browser.find_element_by_id('login-signin')
    type(nextElem)
    nextElem.click()
    
    passwordElem = browser.find_element_by_id('login-passwd')
    passwordElem.send_keys('[password]')

    signinElem = browser.find_element_by_id('login-signin')
    type(signinElem)
    signinElem.click()
except:
    print('Failed.')
    
    
    