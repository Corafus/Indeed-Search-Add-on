from selenium import webdriver
import bs4, requests
import time




browser = webdriver.Chrome()
browser.get('https://www.indeed.com/jobs?as_and=&as_phr=&as_any=&as_not=&as_ttl=cnc&as_cmp=&jt=all&st=&salary=&radius=25&l=nc&fromage=any&limit=10&sort=&psf=advsrch&from=advancedsearch')

res = requests.get(browser.current_url)
res.raise_for_status()
exampleSoup = bs4.BeautifulSoup(res.text, 'html.parser')


elems = exampleSoup.select('a[data-tn-element="jobTitle"]')
print(len(elems))
browser.get("https://indeed.com" + elems[1].get('href'))




#time.sleep(2)
#res = requests.get(browser.current_url)
##res.raise_for_status()
#exampleSoup = bs4.BeautifulSoup(res.text, 'html.parser')


#buttonToClick = browser.find_elements_by_id('sja1')
#buttonToClick[0].click()
#print(buttonToClick[0].href)
#try:
#    elem = browser.find_element_by_class_name('a[href="prev"]')
#    print(elem.text)
#except:
#    print('Was not able to find an element with that name.')




#prevLink = soup.select('#sja1')[0]
#url = prevLink.get('href')
#print(url)