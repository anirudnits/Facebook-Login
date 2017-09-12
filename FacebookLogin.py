import sys
from selenium import webdriver

email = sys.argv[1]
password = sys.argv[2]

browser = webdriver.Firefox()
browser.get('https://www.facebook.com/')

email_field = browser.find_element_by_id('email')
pass_field = browser.find_element_by_id('pass')

email_field.send_keys(email)
pass_field.send_keys(password)

sub = browser.find_element_by_id('u_0_2')
sub.submit()