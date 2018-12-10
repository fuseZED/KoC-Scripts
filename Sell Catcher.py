from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
#until login() is implented manually login during 15 second sleep
browser = webdriver.Chrome()
browser.get(('http://Kingsofchaos.com'))
time.sleep(15)
run=1
while run == 1:
    count = 1
    print("loop'd")
    while count < 42:
        pageNum=str(count)
        browser.get('https://www.kingsofchaos.com/battlefield.php?jump='+ pageNum)
        html_doc=browser.page_source
        soup = BeautifulSoup(html_doc, "lxml")
        table = soup.find('table', attrs={'class':'table_lines battlefield'})

        for row in table.find_all('tr')[2:21]:
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


