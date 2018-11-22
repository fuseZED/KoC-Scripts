from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter
from tkinter import *
from bs4 import BeautifulSoup
import time
import random
"""
    To do list:
      Structure: Create: Login()
                         armoryPrefPurchase()
                         choicePurchase()
                         
      display: Amount of gold on login
               Amount of x tool purchased
               Time between banks
               Time until next bank.
      Fix current sleep with loop.
"""
"""gold/weapon purchase display:  in autoBank() loop create displayBox that outputs newString=oldString + [concatenation of amount2Buy, weapselect, goldString.]
                                   Once that string is created its displayed in displaybox. It gets saved as oldString, next iteration is oldString+newString"""
    
#unpacking user input from actuallyGrabbing()then running AutoBank()
def grabInfo2(weapNumber,weapPricee,frame):
    bankPref=CheckVar.get()
    userr,passw,minTime,maxTime,repeat=actuallyGrabbing()
    minTime=int(minTime)
    maxTime=int(maxTime)
    repeat=int(repeat) 
    autoBank(framed=frame,minTime=minTime,maxTime=maxTime,repeated=repeat,usernameStr=userr,passwordStr=passw,weapNum=weapNumber,weapPrice=weapPricee,bankPreference=bankPref)

#grabbing data from user
def actuallyGrabbing():
    minTime=minBox.get()
    maxTime=maxBox.get()
    repeat=timeBox.get()
    userr=userEnt.get()
    passw=passEnt.get()
    return userr,passw,minTime,maxTime,repeat
    
    
def autoBank(framed,minTime, maxTime,repeated,usernameStr,passwordStr,weapNum,weapPrice,bankPreference):
        oldText=''
        for i in range(repeated):
            #login Process
            browser = webdriver.Chrome()
            browser.get(('http://Kingsofchaos.com'))
            time.sleep(2)
            username = browser.find_element_by_name('usrname')
            browser.find_element_by_name('usrname').click();
            username.send_keys(usernameStr)
            
            password = browser.find_element_by_name('peeword')
            password.send_keys(passwordStr)
            loginButton = browser.find_elements_by_class_name('login_input')
            loginButton[2].click()

            #Sleep to make sure selenium doesnt break
            time.sleep(2)

            #Navigating to armory

            browser.get(('http://Kingsofchaos.com/armory.php'))
            
            if bankPreference==0:
                    #Clears pre selected in-game armory settings
                    attackField = browser.find_element_by_name('prefs[attack]')
                    attackField.clear()
                    attackField.send_keys('0')
                    defendField = browser.find_element_by_name('prefs[defend]')
                    defendField.clear()
                    defendField.send_keys('0')
                    spyField = browser.find_element_by_name('prefs[spy]')
                    spyField.clear()
                    spyField.send_keys('0')
                    sentryField = browser.find_element_by_name('prefs[sentry]')
                    sentryField.clear()
                    sentryField.send_keys('0')
                    updateButton = browser.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/p[3]/table/tbody/tr/td[1]/form/table/tbody/tr[6]/td/input')
                    updateButton.click()
                    #Could this be better handled in a for loop? repeat the find element, clear keys send keys. Just have elemement names in a nameList.
                    #then do blahblah.findelementbyname(namelist[i])
                    #also better handled by just calling bankUpdate() but you didnt think about anything ahead of time.

            
                    time.sleep(2)
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
                    amount2buy = (int(goldString)//weapPrice)
                    #navigating armory and purchasing weapons
                    purchaseField = browser.find_element_by_name('buy_weapon['+str(weapNum)+']')
                    purchaseField.clear()
                    purchaseField.send_keys(amount2buy)
                    newText="You Purchased: " + str(amount2buy) + ' weapons. With '+ goldString + ' gold. \n'
                    displayText= oldText+newText
                    Label(framed, fg='yellow', bg='black', text= displayText).place(x= 120, y = 175)
                    framed.update()
                    oldText=displayText
                    
            PurchaseButton = browser.find_element_by_name('buybut')
            PurchaseButton.click()
            #Change this value to something real high when trouble shooting to avoid multiple logins.
            time.sleep(2)
            
            browser.close()
           
            i=i+1
            #Random time range to perform banking
            waitTime=random.randrange(minTime,maxTime)
            print('sleepng')
            time.sleep(waitTime)


##################################################################################            
##################################################################################
#################                                              ###################
#################          Evertyhing below this is UI         ###################
#################                                              ###################
##################################################################################
##################################################################################

          
master=Tk()
master.title("Swolo's Auto Buyer")
master.geometry("450x200")
Label(master, text="UserName:").grid(row=0)
Label(master, text="Password:").grid(row=1)
userEnt = Entry(master)
passEnt = Entry(master)
userEnt.grid(row=0, column=1)
passEnt.grid(row=1, column=1)


#CREATE LABEL STATING IF NO SETTINGS ARE SAVED AINT SHIT GETTIN PURCHASED
Label(master, text="Minimum Time to wait between spending:").grid(row=3)
Label(master, text="Maximum Time to wait between spending").grid(row=4)
Label(master, text="Number of times to bank:").grid(row=5)
Label(master, text="Thats a drop down menu                -->").grid(row=7)

minBox = Entry(master)
minBox.grid(row =3, column = 1)
maxBox = Entry(master)
maxBox.grid(row=4,column=1) 
timeBox=Entry(master)
timeBox.grid(row=5, column=1)

mb = Menubutton(master, text='Select Weapon to bank')
mb.menu=Menu(mb)
mb["menu"]=mb.menu
mb.menu.add_command(label="Knife",command=lambda: grabInfo2(3,1000,master))
mb.menu.add_command(label="Chariot",command=lambda: grabInfo2(72,450000,master))
mb.menu.add_command(label="Black Powder Missile",command=lambda: grabInfo2(70,1000000,master))
mb.menu.add_command(label="DragonSkin",command=lambda: grabInfo2(51,200000,master))
mb.menu.add_command(label="Invisibility Shield",command=lambda: grabInfo2(71,1000000,master))
mb.menu.add_command(label="Nunchaku",command=lambda: grabInfo2(75,1000000,master))
mb.menu.add_command(label="Lookout Tower",command=lambda: grabInfo2(74,1000000,master))

mb.grid(row=7,column=1)

CheckVar = IntVar()

checkBox = Checkbutton(master, text = "Use Current Armory Settings", variable = CheckVar, onvalue = 1, offvalue = 0,)
checkBox.grid(row=6, column=1)
#startButton = Button(master, text="Start", width=15, height=2, command=grabInfo).place(x= 120, y = 130)

master.mainloop()
