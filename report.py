# -*- coding: GBK -*-
import os
import htmpl as	tpl
import tditem as tdm
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support	import expected_conditions as EC
from selenium.webdriver.common.action_chains import	ActionChains

def	write_html_to_file(filename, htmlstr):
	f =	os.open(filename, os.O_CREAT | os.O_TRUNC |	os.O_RDWR)
	os.write(f,	htmlstr.encode())
	os.close(f)

def	get_tditem_list_by_urls(urls):
	tditemlist = []
	index =	1
	for	url	in urls:
		td = tdm.tditem()
		td.NO =	index
		td.Url = url
		td.Status =	""
		tditemlist.append(td)
		index =	index +	1
		#print(td.Url)
	return tditemlist

def	gen_tabletd(tditemlist):
	tdstr =	""
	for	td in tditemlist:
		tdstr += f'<tr><td>{td.NO}</td><td>{td.Url}</td><td>[{td.Status}]</td></tr>'
	
	#print(tdstr)
	#tabletd = """
	#	<tr><td>1</td><td>https://opensea.io/assets/matic/0xecc82095b2e23605cd95552d90216faa87606c40/3305</td><td>[Clicked,	Queued,	Error]</td></tr>
	#	"""
	return tdstr

			
def	gen_tabletd_by_urls(urls):
	tdlist = []
	index =	1
	for	url	in urls:
		td = td.tditem()
		td.NO =	index
		td.Url = url
		td.Status =	""
		tdlist.append(td)
		index =	index +	1
		#print(td.Url)
		
	#print(tdlist[0].Url)
	tdstr =	""
	for	td in tdlist:
		tdstr += f'<tr><td>{td.NO}</td><td>{td.Url}</td><td>[{td.Status}]</td></tr>'
	
	print(tdstr)
	
	return tdstr

def	test_click():
	driver = webdriver.Chrome("chromedriver.exe")
	try:
		driver.maximize_window()
		driver.get("https://opensea.io/assets/solana/AsAnB6TkWsdrUHfXxpKaZ2wy9Kdsc9ZAzfJTgBNR7p9a")
		element	= driver.find_element(By.CSS_SELECTOR,	".jdSrqf:nth-child(1)")
		actions	= ActionChains(driver)
		actions.move_to_element(element).perform()
		
		driver.find_element(By.CSS_SELECTOR, ".kXZare:nth-child(1)	.Iconreact__Icon-sc-1gugx8q-0").click()
		WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.CSS_SELECTOR, ".Toastreact__DivContainer-sc-6g7ouf-0	> .Blockreact__Block-sc-1xf18x6-0"))
		)
		element	= driver.find_elements(By.CSS_SELECTOR,	".Toastreact__DivContainer-sc-6g7ouf-0	> .Blockreact__Block-sc-1xf18x6-0")
		print("vvvvvvv")
		if len(element)	> 0:
			print("rrrrrrrrrrrrrrrrrrrrrrrrrrr")
		print(element)
		element	= driver.find_element(By.ID, "Header react-aria-9")
		actions	= ActionChains(driver)
		actions.move_to_element(element).perform()
		
		#btn_refresh	= driver.find_element_by_class_name('Blockreact__Block-sc-1xf18x6-0')
		#print(btn_refresh)
		#btn_refresh.click()
		#ActionChains(driver).click(btn_refresh).perform()
	except:
		print("Unexpected error:", sys.exc_info()[0])
	finally:
		time.sleep(10)
		driver.quit()
		
def	test_click_refresh_button_all():

	urls = {'https://opensea.io/assets/solana/AsAnB6TkWsdrUHfXxpKaZ2wy9Kdsc9ZAzfJTgBNR7p9a',
			'https://opensea.io/assets/solana/8BGRNpfcwwJbywSzMxLfDDNzNvSgbCMuSTibvopmUim9',
			'https://opensea.io/assets/solana/9SgcV2fXkW5G3cYzftpo6LEGcLZw3ZvQzqjbEqtVmdNt',
			'https://opensea.io/assets/solana/B6FSU5gS9XNtXDrjrJNkzkr7qSAU3iLEFELw5HGLb2mS'}
	
	tditemlist = get_tditem_list_by_urls(urls)
	
	for	ditem in tditemlist:
		try:
			driver = webdriver.Chrome("chromedriver.exe")
			driver.maximize_window()
			ditem.Status = ""
			driver.get(ditem.Url)
			element	= driver.find_element(By.CSS_SELECTOR,	".jdSrqf:nth-child(1)")
			actions	= ActionChains(driver)
			actions.move_to_element(element).perform()
			
			driver.find_element(By.CSS_SELECTOR, ".kXZare:nth-child(1)	.Iconreact__Icon-sc-1gugx8q-0").click()
			ditem.Status = "Clicked,"
			WebDriverWait(driver, 10).until(
				EC.presence_of_element_located((By.CSS_SELECTOR, ".Toastreact__DivContainer-sc-6g7ouf-0	> .Blockreact__Block-sc-1xf18x6-0"))
			)
			element	= driver.find_elements(By.CSS_SELECTOR,	".Toastreact__DivContainer-sc-6g7ouf-0	> .Blockreact__Block-sc-1xf18x6-0")
			if len(element)	> 0:
				ditem.Status = ditem.Status	+ "Queued,"
			#time.sleep(2)
		except:
			ditem.Status = ditem.Status	+ "Error,"
		
		finally:
			time.sleep(10)
			driver.quit()
		
	tabletd	= gen_tabletd(tditemlist)
	title =	"web auto test report"
	stylesheet = ""
	str	= tpl.HTML_TMPL	% dict(
				title =	title,
				stylesheet = stylesheet,
				tabletd	= tabletd
			)
			
	write_html_to_file("report.html", str)
	
#gen_tabletd_by_urls(urls)
test_click_refresh_button_all()