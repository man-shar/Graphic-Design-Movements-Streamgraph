from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from selenium.common.exceptions import ElementNotVisibleException
import time
import urllib
from bs4 import BeautifulSoup
import pdb
from HTMLParser import  HTMLParser

#bauhaus#links=["http://www.wikiart.org/en/anni-albers","http://www.wikiart.org/en/paul-klee","http://www.wikiart.org/en/laszlo-moholy-nagy","http://www.wikiart.org/en/johannes-itten","http://www.wikiart.org/en/josef-albers","http://www.wikiart.org/en/wassily-kandinsky","http://www.wikiart.org/en/lyonel-feininger","http://www.wikiart.org/en/naum-gabo","http://www.wikiart.org/en/oskar-schlemmer"]
links=["https://www.artsy.net/gene/typography/artworks?for_sale=false&include_medium_filter_in_aggregation=true&sort=year"]
driver = webdriver.Firefox()
#for i in range(len(links)):

driver.get(links[0])
time.sleep(1)
#assert "Python" in driver.title
#driver.wait(5)
error=False
csv_file=open("Typography.csv","a")
#pdb.set_trace()
#name=driver.find_element_by_id("h1Title").text
#csv_file.write("{0},".format(name))
for i in range(0,300):
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	print i
	time.sleep(3)

#pdb.set_trace()
#elem = driver.find_element_by_css_selector(".filter-artworks-no-infinite-scroll[data-state='']").click()
#time.sleep(3)
#elem.click()
#pdb.set_trace()
#elem_all=driver.find_elements_by_css_selector(".st-masonry-tile")
#pdb.set_trace()
html=driver.page_source
soup=BeautifulSoup(html,"html.parser")
elem_all=soup.select(".artwork-item-title")
#pdb.set_trace()
for i in range(len(elem_all)):
	#pdb.set_trace()
	str=elem_all[i].text
	try:
		csv_file.write("{0},".format(str[-4:]))
	except UnicodeEncodeError:
		continue
csv_file.write("\n")
csv_file.close()
	
#pdb.set_trace()
print "bottom reached"
error=True
#print elem
#river.close()
