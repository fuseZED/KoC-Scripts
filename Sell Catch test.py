from bs4 import BeautifulSoup
data=[]
html_doc = ''.join(open("battTest.txt",'r').readlines())
soup = BeautifulSoup(html_doc, "lxml")
table = soup.find('table', attrs={'class':'table_lines battlefield'})
for row in table.find_all('tr')[2:22]:
    col=row.find_all("td")
    allianceString=(col[1].get_text())
    allianceString=allianceString[7:]
    print(allianceString)
