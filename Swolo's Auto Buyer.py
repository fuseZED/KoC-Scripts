from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter
from tkinter import *


from bs4 import BeautifulSoup
import time
import random



  
#unpacking user input from actuallyGrabbing()then running AutoBank()
def grabInfo():
    
    userr,passw,minTime,maxTime,repeat=actuallyGrabbing()
    minTime=int(minTime)
    maxTime=int(maxTime)
    repeat=int(repeat)
    autoBank(minTime=minTime,maxTime=maxTime,repeated=repeat,usernameStr=userr,passwordStr=passw)

#grabbing data from user
def actuallyGrabbing():
    minTime=minBox.get()
    maxTime=maxBox.get()
    repeat=timeBox.get()
    userr=userEnt.get()
    passw=passEnt.get()
    return userr,passw,minTime,maxTime,repeat
    

def autoBank(minTime, maxTime,repeated,usernameStr,passwordStr):

        for i in range(repeated):

            #login Process
            browser = webdriver.Chrome()
            browser.get(('http://Kingsofchaos.com'))
            time.sleep(15)
            username = browser.find_element_by_name('usrname')
            browser.find_element_by_name('usrname').click();
            username.send_keys(usernameStr)
            
            password = browser.find_element_by_name('peeword')
            
            password.send_keys(passwordStr)
            loginButton = browser.find_elements_by_class_name('login_input')
            loginButton[2].click()

            #Sleep to make sure selenium doesnt fuck up
            time.sleep(15)





            #Navigating to armory

            browser.get(('http://Kingsofchaos.com/armory.php'))
            time.sleep(15)
            content = browser.page_source

            #Scraping html for gold table
            soup = BeautifulSoup(content, "lxml")
            table = soup.find("td", attrs={"class":"menu_cell_repeater_vert"})
            #Parsing table and manipulating string to get amount of gold
            tableRow = table.find("tr")
            goldString = (tableRow.get_text())
            goldString=(goldString[31:])
            goldString=goldString[:-19]
            goldString = goldString.replace(',', '')
            amount2buy = (int(goldString)//50000)

            #navigating armory and purchasing weapons
            purchaseField = browser.find_element_by_name('buy_weapon[23]')
            purchaseField.clear()
            purchaseField.send_keys(amount2buy)
            PurchaseButton = browser.find_element_by_name('buybut')
            PurchaseButton.click()
            time.sleep(15)
            
            browser.close()
           
            i=i+1
            #Random time range to perform banking
            time.sleep(random.randrange(minTime,maxTime))


master=Tk()
master.title("Swolo's Auto Buyer")
master.geometry("400x200")
Label(master, text="UserName:").grid(row=0)
Label(master, text="Password:").grid(row=1)
userEnt = Entry(master)
passEnt = Entry(master)
userEnt.grid(row=0, column=1)
passEnt.grid(row=1, column=1)



Label(master, text="Minimum Time to wait between spending:").grid(row=3)
Label(master, text="Maximum Time to wait between spending").grid(row=4)
Label(master, text="Number of times to bank:").grid(row=5)

minBox = Entry(master)
minBox.grid(row =3, column = 1)
maxBox = Entry(master)
maxBox.grid(row=4,column=1) 
timeBox=Entry(master)
timeBox.grid(row=5, column=1)
startButton = Button(master, text="Start", width=15, height=2, command=grabInfo).place(x= 120, y = 130)


