from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.indeed.com/advanced_search?q=&l=')



#this finds the field for exact phrase, and then enters the text 'paid training'.
exactPhraseElem = browser.find_element_by_id('as_phr')
exactPhraseElem.send_keys('paid training')


#this finds the field for terms included in the title of the job, and then enters the text 'welder'.
includedInTitleElem = browser.find_element_by_id('as_ttl')
includedInTitleElem.send_keys('welder')

#this finds the field for location.
includedInTitleElem = browser.find_element_by_id('where')
includedInTitleElem.send_keys('portland, OR')



#I think this just presses the submit key. The exactPhraseElem part isn't that important.
exactPhraseElem.submit()


