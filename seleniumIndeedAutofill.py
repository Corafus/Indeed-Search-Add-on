from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import openpyxl, time, bs4, requests

#openpyxl stuff for the input excel document
wb = openpyxl.load_workbook('jobSearchTerms.xlsx')
sheet = wb['Sheet1']


#openpyxl stuff for the output excel document
outputWB = openpyxl.load_workbook('example.xlsx')
outputSheet = outputWB['Sheet1']


#selenium requirements. Simply opens the browser to a specified page. The Advanced Search Page.
browser = webdriver.Chrome()
browser.get('https://www.indeed.com/advanced_search?q=&l=')



#Selenium will use this loop to go through the input excel document and enter all of the preferences
#at the end it copies a url that is needed for the beautiful soup (bs4) stuff
for Exact_Phrases in range(2,8):
    #this finds the field for exact phrase, and then enters the text 'paid training'.
    exactPhraseElem = browser.find_element_by_id('as_phr')

    for j in range(25):
        exactPhraseElem.send_keys(Keys.BACK_SPACE)


    exactPhraseElem.send_keys(sheet['B' + str(Exact_Phrases)].value)
    time.sleep(2)

    for Job_Titles in range(2,7):
        #this finds the field for terms included in the title of the job, and then enters the text 'welder'.
        includedInTitleElem = browser.find_element_by_id('as_ttl')

        for k in range(25):
            includedInTitleElem.send_keys(Keys.BACK_SPACE)

        includedInTitleElem.send_keys(sheet['A' + str(Job_Titles)].value)
        time.sleep(2)


        for Job_Locations in range(2,9):
            #this finds the field for location.
            jobLocationElem = browser.find_element_by_id('where')

            for l in range(25):
                jobLocationElem.send_keys(Keys.BACK_SPACE)

            jobLocationElem.send_keys(sheet['C' + str(Job_Locations)].value)
            time.sleep(2)



            #Press the submit key
            time.sleep(3)
            jobLocationElem.submit()


            #buttonToClick = browser.find_element_by_id('sja1')
            #buttonToClick.click()




            res = requests.get(browser.current_url)
            res.raise_for_status()
            exampleSoup = bs4.BeautifulSoup(res.text, 'html.parser')

            elems = exampleSoup.select('a[data-tn-element="jobTitle"]')

            if(len(elems))>0:

                browser.get("https://indeed.com" + elems[0].get('href'))
                res = requests.get("https://indeed.com" + elems[0].get('href'))
                exampleSoup = bs4.BeautifulSoup(res.text, 'html.parser')




                elems = exampleSoup.select('#jobDescriptionText')
                sheet['D2'].value = elems[0].getText()
                elems = exampleSoup.select('div[class="jobsearch-JobInfoHeader-title-container"]')
                sheet['A2'].value = elems[0].getText()
                elems = exampleSoup.select('a[target="_blank"]')
                sheet['B2'].value = elems[0].getText()
                elems = exampleSoup.select('div')
                sheet['C2'].value = elems[67].getText()
                wb.save('example.xlxs')
                time.sleep(3)
                browser.back()


            time.sleep(3)
            browser.back()




