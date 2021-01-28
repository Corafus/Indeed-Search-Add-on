import requests, bs4, openpyxl


wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['Sheet1']
res = requests.get('https://www.indeed.com/viewjob?cmp=Container-Graphics-Corporation&t=Cutting+Die+Maker&jk=b064296895d0a575&sjdu=QwrRXKrqZ3CNX5W-O9jEvSlTLoJfzR7oNwR3hRrXYfCQrhQr_k5cpp6h8d7sP58g_yYgdHT1iF8-ZTjO2ZVbeQ&tk=1et24s6uit4uu801&adid=362976096&ad=-6NYlbfkN0BKgzQyzTF1Q9mOsR1amaS-juVGLjHt5Cdom-gEF9y-xUy4ZgYGvqpS6TlqqzTHvZdEo63JbcZy-Zto2dpr5oB9J_1IGtYSTXr6Hw3I6MtcXI_bomLjto9HPm4EhFXKItRUR4Nz_IOXcUZt0PmdX5-ZS3elvs1jwUW0FctWGgeakJIRr6RGtI6scgwTnjvi4e_HHHew-Z0_X9xIP6aDVk1PQsWNIWEyn3Vfk1E35WLpXdcdRy_2pUZ8dQ207QcYf2nJyBVpQ2Oc9BR0BX19FoxEp8nVyNhcTTqPuwHCDErfMHISbqkq57pEhdv63i5L350_r9l-aiWpuvg7zPVV6R03&pub=4a1b367933fd867b19b072952f68dceb&vjs=3')
res.raise_for_status()
exampleSoup = bs4.BeautifulSoup(res.text, 'html.parser')
elems = exampleSoup.select('#jobDescriptionText')
#print(len(elems))
#print(sheet['C1'].value)
sheet['C1'].value = 42
#print(sheet['C1'].value)
sheet['B1'].value = "the job description"
sheet['D2'].value = elems[0].getText()
elems = exampleSoup.select('div[class="jobsearch-JobInfoHeader-title-container"]')
sheet['A2'].value = elems[0].getText()
elems = exampleSoup.select('a[target="_blank"]')
sheet['B2'].value = elems[0].getText()

elems = exampleSoup.select('div')
print(len(elems))
#for i in range(1, len(elems)):
#    sheet['C' + str(i+1)].value = elems[i].getText()
sheet['C2'].value = elems[67].getText()
wb.save('example.xlxs')


#div class="jobsearch-InlineCompanyRating icl-u-xs-mt--xs jobsearch-DesktopStickyContainer-companyrating"
