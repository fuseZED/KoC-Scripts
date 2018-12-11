from bs4 import BeautifulSoup
data=[]
html_doc = ''.join(open("battTest.txt",'r').readlines())
train_doc=''.join(open("trainTest.txt",'r').readlines())
soup = BeautifulSoup(html_doc, "lxml")
trainSoup = BeautifulSoup(train_doc, "lxml")
table = soup.find('table', attrs={'class':'table_lines battlefield'})
"""for row in table.find_all('tr')[2:22]:
    col=row.find_all("td")
    tffString=(col[3].get_text())
    tffString = tffString.replace(',', '')
    tffString=int(tffString)
    #tffString=allianceString[7:]
    print(tffString)"""
trainTable = trainSoup.find('table', attrs={'class':'table_lines personnel'})

for row in trainTable.find_all('tr')[11:]:
        coll=row.find("td")
        tffS=(coll.get_text())
        tffS=tffS[:5]
        tffS = tffS.replace(',', '')
        tffS=int(tffS)
        print(tffS)
        




"""

<table class="table_lines personnel" width="100%" cellspacing="0" cellpadding="6" border="0">
    <tbody><tr>
        <th colspan="2"><span style="float: right" class="expando">-</span>Personnel</th>
    </tr>
    <tr>
        <td><b>Trained Attack Soldiers</b></td>
        <td align="right">2,565</td>
            </tr>
    <tr>
        <td><b>Trained Attack Mercenaries</b></td>
        <td align="right">84</td>
            </tr>
    <tr>
        <td><b>Trained Defense Soldiers</b></td>
        <td align="right">96</td>
            </tr>
    <tr>
        <td><b>Trained Defense Mercenaries</b></td>
        <td align="right">0</td>
            </tr>
    <tr>
        <td><b>Untrained Soldiers</b></td>
        <td align="right">1,696</td>
            </tr>
    <tr>
        <td><b>Untrained Mercenaries</b></td>
        <td align="right">0</td>
            </tr>
    <tr>
        <td class="subh"><b>Spies</b></td>
        <td class="subh" align="right">29</td>
            </tr>
    <tr>
        <td class="subh"><b>Sentries</b></td>
        <td class="subh" align="right">26</td>
            </tr>
		<tr>
				<td><b>Army Morale</b></td>
				<td align="right">-38</td>
        		</tr>
		<tr>
        <td><b>Total Fighting Force</b></td>
        <td align="right">4,441</td>
            </tr>
    <tr><td colspan="2" align="center" style="display:none">4,441 soldiers</td></tr>
</tbody></table>
"""
