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
      Growth Tracker [requires getTFF() and parseTFF()]
      display:
               Time between banks
               Time until next bank.
      Fix current sleep with loop
"""
def autoAttack(frame):
    userr,passw,minG=autoAttackGrab()
    browser=login(usernameStr=userr,passwordStr=passw)
    run =1
    minG=int(minG)
    i=0
    OwnTFF=getOwnTFF(browser)
    print(OwnTFF)
    for i in range(3):
        count = 1
        while count < 36:
            pageNum=str(count)
            browser.get('https://www.kingsofchaos.com/battlefield.php?jump='+ pageNum)
            html_doc=browser.page_source
            soup = BeautifulSoup(html_doc, "lxml")
            table = soup.find('table', attrs={'class':'table_lines battlefield'})

            for row in table.find_all('tr')[2:22]:
                col=row.find_all("td")
                allianceString=(col[1].get_text())
                allianceString=allianceString[7:]
                goldString=(col[5].get_text())
                goldString=(goldString[:-5])
                goldString = goldString.replace(',', '')
                tffString=(col[3].get_text())
                tffString = tffString.replace(',', '')
                tffString=int(tffString)
                if goldString != "???":
                    goldString=int(goldString)
                    if goldString > minG:
                        if OwnTFF < tffString:
                            userID=col[2].find('a').get('href')
                            browser.get('https://www.kingsofchaos.com'+ userID)
                            attButton = browser.find_element_by_name('attackbut')
                            attButton.click()
                            time.sleep(1)
                            browser.get(('http://Kingsofchaos.com/armory.php'))
                            PurchaseButton = browser.find_element_by_name('buybut')
                            PurchaseButton.click()
                            goldString=str(goldString)
                            print('got one! for ' + goldString + ' gold')
            count=count+1
            i=i+1
        browser.quit()



    
    
def sellCatch(frame):
    userr,passw,minTime,maxTime,repeat=actuallyGrabbing()
    browser=login(usernameStr=userr,passwordStr=passw)
    run =1
    while run == 1:
        count = 1
        print("loop'd")
        while count < 42:
            pageNum=str(count)
            browser.get('https://www.kingsofchaos.com/battlefield.php?jump='+ pageNum)
            html_doc=browser.page_source
            soup = BeautifulSoup(html_doc, "lxml")
            table = soup.find('table', attrs={'class':'table_lines battlefield'})

            for row in table.find_all('tr')[2:22]:
                col=row.find_all("td")
                allianceString=(col[1].get_text())
                allianceString=allianceString[7:]
                goldString=(col[5].get_text())
                goldString=(goldString[:-5])
                goldString = goldString.replace(',', '')
                if goldString != "???":
                    goldString=int(goldString)
                    if goldString > 500000000:
                            if allianceString !="DEMK" and allianceString != "Sweet Revenge":
                                userID=col[2].find('a').get('href')
                                browser.get('https://www.kingsofchaos.com'+ userID)
                                #NOW DO THE ATTACKING
                                attButton = browser.find_element_by_name('attackbut')
                                attButton.click()
                                time.sleep(1)
                                browser.get(('http://Kingsofchaos.com/armory.php'))
                                PurchaseButton = browser.find_element_by_name('buybut')
                                PurchaseButton.click()
                                goldString=str(goldString)
                                print('got one! for ' + goldString + ' gold')
            count=count+1



    
    
def wizard(frame):
    i=0
    bankRound=0
    userr,passw,minTime,maxTime,repeat=actuallyGrabbing()
    browser=login(usernameStr=userr,passwordStr=passw)
    browser.get(('http://Kingsofchaos.com/conquest.php'))
    wizardButton = browser.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/p/table/tbody/tr[10]/td[3]/table/tbody/tr/td[2]/input')
    wizardButton.click()
    time.sleep(2)
    #xpath changes after first click due to HTML on page changing
    for i in range(99):
        wizardButton = browser.find_element_by_xpath('//html/body/table[2]/tbody/tr/td[2]/table[2]/tbody/tr[10]/td[3]/table/tbody/tr/td[2]/input')
        wizardButton.click()
        time.sleep(2)
        i=i+i
        bankRound=bankRound+1
        #banks your gold every 5th conquest. Currently uses armory settings.
        if bankRound % 5 == 0:
            browser.get(('http://Kingsofchaos.com/armory.php'))
            time.sleep(2)
            PurchaseButton = browser.find_element_by_name('buybut')
            PurchaseButton.click()
            browser.get(('http://Kingsofchaos.com/conquest.php'))
            time.sleep(1)
            #uses first xpath again, before returning to loop with second xpath
            wizardButton = browser.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/p/table/tbody/tr[10]/td[3]/table/tbody/tr/td[2]/input')
            wizardButton.click()
            time.sleep(2)
            bankRound=bankRound+1
                        
    
def main(weapNumber,weapPricee,frame):
    bankPref=CheckVar.get()
    userr,passw,minTime,maxTime,repeat=actuallyGrabbing()
    minTime=int(minTime)
    maxTime=int(maxTime)
    repeat=int(repeat)
    oldText=''
    for i in range(repeat):
        browser=login(usernameStr=userr,passwordStr=passw)
        browser.get(('http://Kingsofchaos.com/armory.php'))
        time.sleep(2)
        if bankPref==0:
                browser=armoryClear(webDriver=browser)
                time.sleep(4)
                amount2buy,goldString=getGold(webDriver=browser,weapPrice=weapPricee)
                browser=weapFill(webDriver=browser,weapNumber=weapNumber,goldString=goldString, amount2buy=amount2buy)
                newText="You Purchased: " + str(amount2buy) + ' weapons, with '+ goldString + ' gold. \n '
                displayText= oldText+newText
                #Label(frame, fg='yellow', bg='black', text= displayText).place(x= 120, y = 175)
                frame.update()
                oldText=displayText

        PurchaseButton = browser.find_element_by_name('buybut')
        PurchaseButton.click()
        #Change this value to something real high when trouble shooting to avoid multiple logins.
        time.sleep(4)

        browser.quit()


        i=i+1
        #Random time range to perform banking
        waitTime=random.randrange(minTime,maxTime)
        print('sleeping')
        time.sleep(waitTime)

def weapFill(webDriver,weapNumber,goldString, amount2buy):
    purchaseField = webDriver.find_element_by_name('buy_weapon['+str(weapNumber)+']')
    purchaseField.clear()
    purchaseField.send_keys(amount2buy)
    return webDriver

#grabbing data from user
def actuallyGrabbing():
    minTime=minBox.get()
    maxTime=maxBox.get()
    repeat=timeBox.get()
    userr=userEnt.get()
    passw=passEnt.get()
    return userr,passw,minTime,maxTime,repeat

    
def autoAttackGrab():
    userr=userEnt.get()
    passw=passEnt.get()
    minG=minGold.get()
    return userr,passw,minG

    

#scrapes then parses html for gold on hand
def getGold(webDriver,weapPrice):
    content = webDriver.page_source
    soup = BeautifulSoup(content, "lxml")
    table = soup.find("td", attrs={"class":"menu_cell_repeater_vert"})
    tableRow = table.find("tr")
    goldString = (tableRow.get_text())
    goldString=(goldString[31:])
    goldString=goldString[:-19]
    goldString = goldString.replace(',', '')
    amount2buy = (int(goldString)//weapPrice)
    return amount2buy,goldString
def getOwnTFF(webDriver):
    webDriver.get(('http://Kingsofchaos.com/train.php'))
    content = webDriver.page_source
    trainSoup = BeautifulSoup(content, "lxml")
    trainTable = trainSoup.find('table', attrs={'class':'table_lines personnel'})
    for row in trainTable.find_all('tr')[11:]:
        coll=row.find("td")
        tffS=(coll.get_text())
        tffS=tffS[:5]
        tffS = tffS.replace(',', '')
        tffS=int(tffS)
    return tffS
#logs user into KoC
def login(usernameStr,passwordStr):
    browser = webdriver.Chrome()
    browser.get(('http://Kingsofchaos.com'))
    time.sleep(6)
    username = browser.find_element_by_name('usrname')
    browser.find_element_by_name('usrname').click();
    username.send_keys(usernameStr)
    password = browser.find_element_by_name('peeword')
    password.send_keys(passwordStr)
    loginButton = browser.find_elements_by_class_name('login_input')
    loginButton[2].click()
    return browser
    #Sleep to make sure selenium doesnt break
    time.sleep(6)

def armoryClear(webDriver):
    attackField = webDriver.find_element_by_name('prefs[attack]')
    attackField.clear()
    attackField.send_keys('0')
    defendField = webDriver.find_element_by_name('prefs[defend]')
    defendField.clear()
    defendField.send_keys('0')
    spyField = webDriver.find_element_by_name('prefs[spy]')
    spyField.clear()
    spyField.send_keys('0')
    sentryField = webDriver.find_element_by_name('prefs[sentry]')
    sentryField.clear()
    sentryField.send_keys('0')
    updateButton = webDriver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/p[3]/table/tbody/tr/td[1]/form/table/tbody/tr[6]/td/input')
    updateButton.click()
    return webDriver

##################################################################################
##################################################################################
#################                                              ###################
#################          Evertyhing below this is UI         ###################
#################                                              ###################
##################################################################################
##################################################################################

#main window
master=Tk()
master.title("Swolo's Auto Buyer")
master.geometry("650x350")
#label creation
Label(master, text="Login Information:", fg="blue").grid(row=0, column=1)
Label(master, text="Auto banker Information:", fg="blue").grid(row=3, column=1)
Label(master, text="UserName:").grid(row=1)
Label(master, text="Password:").grid(row=2)
Label(master, text="Minimum Time to wait between spending:").grid(row=5)
Label(master, text="Maximum Time to wait between spending").grid(row=6)
Label(master, text="Number of times to bank:").grid(row=7)
Label(master, text="--------------").grid(row=10, column=0)
Label(master, text="--------------").grid(row=10, column=1)
Label(master, text="--------------").grid(row=10, column=3)
Label(master, text="Auto Attacker Settings:", fg="blue").grid(row=14)
Label(master, text="Minimum Gold to hit:").grid(row=15)
Label(master, text="Other Utilities:", fg="blue").grid(row=14, column=3)
Label(master, text="Made by fuseZED", fg="green").grid(row=16, column=1)
#inputbox creation
userEnt = Entry(master)
passEnt = Entry(master)
userEnt.grid(row=1, column=3)
passEnt.grid(row=2, column=3)
minBox = Entry(master)
minBox.grid(row =5, column = 3)
maxBox = Entry(master)
maxBox.grid(row=6,column=3)
timeBox=Entry(master)
timeBox.grid(row=7, column=3)
minGold = Entry(master)
minGold.grid(row=16,column=0)
#dropdown menu creation
mb = Menubutton(master, text='Select Weapon to bank (CLICK ME TO START AB!)', fg="red")
mb.menu=Menu(mb)
mb["menu"]=mb.menu
mb.menu.add_command(label="Knife",command=lambda: main(3,1000,master))
mb.menu.add_command(label="Chariot",command=lambda: main(72,450000,master))
mb.menu.add_command(label="Black Powder Missile",command=lambda: main(70,1000000,master))
mb.menu.add_command(label="DragonSkin",command=lambda: main(51,200000))
mb.menu.add_command(label="Invisibility Shield",command=lambda: main(71,1000000,master))
mb.menu.add_command(label="Nunchaku",command=lambda: main(75,1000000,master))
mb.menu.add_command(label="Lookout Tower",command=lambda: main(74,1000000,master))
mb.grid(row=9,column=1)
#buttons
wizardButton = Button(master, text="Wizard!", command=lambda: wizard(master))
wizardButton.grid(row=15,column=3)
sellButton = Button(master, text="Catch Sells!", command=lambda: sellCatch(master))
sellButton.grid(row=17,column=3)
attackButton = Button(master, text="Auto Attack!", command=lambda: autoAttack(master))
attackButton.grid(row=17,column=0)
#Checkbox implementation
CheckVar = IntVar()
checkBox = Checkbutton(master, text = "Use Current Armory Settings", variable = CheckVar, onvalue = 1, offvalue = 0,)
checkBox.grid(row=8, column=1)

master.mainloop()
