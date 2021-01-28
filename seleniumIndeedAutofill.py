from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import openpyxl, time
wb = openpyxl.load_workbook('jobSearchTerms.xlsx')
sheet = wb['Sheet1']
browser = webdriver.Chrome()
browser.get('https://www.indeed.com/advanced_search?q=&l=')


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



            #I think this just presses the submit key. The exactPhraseElem part isn't that important.
            time.sleep(3)
            jobLocationElem.submit()
            time.sleep(3)
            browser.back()



