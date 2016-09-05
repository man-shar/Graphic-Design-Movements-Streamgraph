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
links=["http://www.wikiart.org/en/paintings-by-style/outsider-art"]
driver = webdriver.Firefox()
#for i in range(len(links)):

driver.get(links[0])
time.sleep(1)
#assert "Python" in driver.title
#driver.wait(5)
error=False
csv_file=open("OutsiderArt.csv","a")
#pdb.set_trace()
#name=driver.find_element_by_id("h1Title").text
#csv_file.write("{0},".format(name))
while error is False:
	
	try:
		elem = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID, "btn-more")))
		time.sleep(3)
		elem.click()
	except ElementNotVisibleException:
		#pdb.set_trace()
		#elem_all=driver.find_elements_by_css_selector(".st-masonry-tile")
		html=driver.page_source
		soup=BeautifulSoup(html,"html.parser")
		elem_all=soup.findAll("ul",{"class":"title"})
		#pdb.set_trace()
		for i in range(len(elem_all)):
			#pdb.set_trace()
			str=elem_all[i].contents[1].contents[1].encode("utf-8")
			csv_file.write("{0},".format(str[-4:]))
		csv_file.write("\n")
		csv_file.close()
			
		#pdb.set_trace()
		print "bottom reached"
		error=True
print elem
#river.close()
