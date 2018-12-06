from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
count = 10
#until login() is implented manually login during 15 second sleep
browser = webdriver.Chrome()
browser.get(('http://Kingsofchaos.com'))
time.sleep(15)
for i in range(35):
    pageNum=str(count)
    browser.get('https://www.kingsofchaos.com/battlefield.php?jump='+ pageNum)
    html_doc=browser.page_source
    soup = BeautifulSoup(html_doc, "lxml")
    table = soup.find('table', attrs={'class':'table_lines battlefield'})
    for row in table.find_all('tr')[2:22]:
        col=row.find_all("td")
        goldString=(col[5].get_text())
        goldString=(goldString[:-5])
        goldString = goldString.replace(',', '')
        if goldString != "???":
            goldString=int(goldString)
            if goldString > 21000000:
                userID=col[2].find('a').get('href')
                browser=browser.get('https://www.kingsofchaos.com'+ userID)
                #NOW DO THE ATTACKING
                attackButton = browser.find_element_by_name('attackbut')
                attackButton.click()
    count=count+1


