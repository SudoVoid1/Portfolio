#Imports Selenium and Chrome Driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()

#Alerts and Refresh Counter
goodalert = "Your item is Available! PROCEEDING TO CHECKOUT!!"
badalert = "Your Item is unavailabe after 5 refreshs"

def putincart(counter,fail):
    while True:        
        time.sleep(4)
        try:
            addtocartbutton = driver.find_element_by_xpath('/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[8]/div[1]/div/div/div/button')
            # Need to find a way to get the add to cart button for any page?
            addtocartbutton.click()
            time.sleep(4)
            gotocartbutton = driver.find_element_by_xpath('/html/body/div[7]/div/div[1]/div/div/div/div/div[1]/div[3]/a')
            gotocartbutton.click()
            time.sleep(2)
            False
            print(goodalert)
            checkoutbutton = driver.find_element_by_xpath('/html/body/div[1]/main/div/div[2]/div[1]/div/div[1]/div[1]/section[2]/div/div/div[3]/div/div[1]/button')
            checkoutbutton.click()
            time.sleep(2)
            break
        except:
            time.sleep(2)
            driver.refresh()
            True
            counter += 1
            fail += 1
            if (counter % 5) == 0:
                print(badalert)
            #Sets how many refreshs till the program will stop
            if fail > 25:
                print("Shutting down after"+ f'{fail}' + "refreshs")
                driver.quit()
                break

def logintoaccount(email,password):
    emailsend = driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/form/div[1]/div/input')
    emailsend.send_keys(email)
    passwordsend = driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/form/div[2]/div/div/input')
    passwordsend.send_keys(password)
    signin = driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/form/div[3]/button')
    signin.click()
    #must wait while it loads
    time.sleep(8)

    #takes you to payment info page
    contbutton = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/div/button')
    contbutton.click()
    time.sleep(3)

def paymentinfo(card,fname,lname,address,city,state,zipcode):
    creditcard = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[1]/div/section/div[1]/div/input')
    creditcard.send_keys(card)

    firstname = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/form/div/section/div[2]/label/div/input')
    firstname.send_keys(fname)

    lastname = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/form/div/section/div[3]/label/div/input')
    lastname.send_keys(lname)

    annoying_button = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/form/div/section/div[4]/label/div[2]/div/button')
    annoying_button.click()
    address_element = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/form/div/section/div[4]/label/div[2]/div/div/input')
    address_element.send_keys(address)
    

    city_element = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/form/div/section/div[6]/div/div[1]/label/div/input')
    city_element.send_keys(city)

    state_element = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/form/div/section/div[6]/div/div[2]/label/div/div/select')
    state_element.send_keys(state)

    zipcode_element = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/form/div/section/div[7]/div/div[1]/label/div/input')
    zipcode_element.send_keys(zipcode)

    #place order
    placeorder = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[4]/button')
    placeorder.click()
    print("Item Purchased Without Error\n Closing Program Tab in 100 seconds")
    time.sleep(100)
    driver.quit()
    


#User inputs URL
url = input("Paste your Best Buy Link:\n")
# = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442"


#Best Buy Account Info
email = input("Type your email to login to Best Buy: ")

password= input("Type your password: ")


#Shipping/Payment Info
print("\nNext Enter payment/shipping address\n")
card = input("Credit card number\n")
fname = input("First Name:\n")
lname = input("Last Name:\n")
address = input("Street Address:\n")
city = input("City:\n")
state = input("State Initials:\n")
zipcode = input("Zipcode:\n")

#brings up users page
driver.get(url)

#Excutes function with entered data
putincart(0,0)
logintoaccount(email,password)
paymentinfo(card,fname,lname,address,city,state,zipcode)
