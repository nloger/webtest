# -*- coding: UTF-8 -*-
import os
import htmpl as tpl
import tditem as tdm
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def write_html_to_file(filename, htmlstr):
    f = os.open(filename, os.O_CREAT | os.O_TRUNC | os.O_RDWR)
    os.write(f, htmlstr.encode())
    os.close(f)

def get_tditem_list_by_urls(urls):
    tditemlist = []
    index = 1
    for url in urls:
        td = tdm.tditem()
        td.NO = index
        td.Url = url
        td.Status = ""
        tditemlist.append(td)
        index = index + 1
        #print(td.Url)
    return tditemlist

def gen_tabletd(tditemlist):
    tdstr = ""
    for td in tditemlist:
        tdstr += f'<tr><td>{td.NO}</td><td>{td.Url}</td><td>[{td.Status}]</td></tr>'
    
    #print(tdstr)
    #tabletd = """
    #   <tr><td>1</td><td>https://opensea.io/assets/matic/0xecc82095b2e23605cd95552d90216faa87606c40/3305</td><td>[Clicked, Queued, Error]</td></tr>
    #   """
    return tdstr

            
def gen_tabletd_by_urls(urls):
    tdlist = []
    index = 1
    for url in urls:
        td = td.tditem()
        td.NO = index
        td.Url = url
        td.Status = ""
        tdlist.append(td)
        index = index + 1
        #print(td.Url)
        
    #print(tdlist[0].Url)
    tdstr = ""
    for td in tdlist:
        tdstr += f'<tr><td>{td.NO}</td><td>{td.Url}</td><td>[{td.Status}]</td></tr>'
    
    print(tdstr)
    
    return tdstr

def test_click():
    driver = webdriver.Chrome("chromedriver.exe")
    try:
        driver.maximize_window()
        driver.get("https://opensea.io/assets/solana/AsAnB6TkWsdrUHfXxpKaZ2wy9Kdsc9ZAzfJTgBNR7p9a")
        element = driver.find_element(By.CSS_SELECTOR,  ".jdSrqf:nth-child(1)")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        
        driver.find_element(By.CSS_SELECTOR, ".kXZare:nth-child(1)  .Iconreact__Icon-sc-1gugx8q-0").click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".Toastreact__DivContainer-sc-6g7ouf-0 > .Blockreact__Block-sc-1xf18x6-0"))
        )
        element = driver.find_elements(By.CSS_SELECTOR, ".Toastreact__DivContainer-sc-6g7ouf-0  > .Blockreact__Block-sc-1xf18x6-0")
        print("vvvvvvv")
        if len(element) > 0:
            print("rrrrrrrrrrrrrrrrrrrrrrrrrrr")
        print(element)
        element = driver.find_element(By.ID, "Header react-aria-9")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        
        #btn_refresh    = driver.find_element_by_class_name('Blockreact__Block-sc-1xf18x6-0')
        #print(btn_refresh)
        #btn_refresh.click()
        #ActionChains(driver).click(btn_refresh).perform()
    except:
        print("Unexpected error:", sys.exc_info()[0])
    finally:
        time.sleep(10)
        driver.quit()

#返回urls集合
def test_get_url(in_url = "https://opensea.io/collection/carton-kids", get_limit = 50):
    desired_capabilities = DesiredCapabilities.CHROME # 修改页面加载策略
    desired_capabilities["pageLoadStrategy"] = "none" # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出#注：2021/12/20 在谷歌浏览器96.0.4664.110上验证出效果。

    driver = webdriver.Chrome("chromedriver.exe")
    driver.maximize_window()
    driver.get(in_url)
    
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "Assetreact__AssetCard-sc-bnjqwy-2")))

    #write_html_to_file("at1.txt", driver.page_source)
    check_height = driver.execute_script("return document.body.scrollHeight;")
    
    
    # 执行这段代码，会获取到当前窗口总高度
    js = "return action=document.body.scrollHeight"
    # 初始化现在滚动条所在高度为0
    height = 0
    # 当前窗口总高度
    new_height = driver.execute_script(js)
    
    get_count = 0
    urls = set()
    # 翻页并取url
    #while get_count < get_limit and height < new_height:
    while get_count < get_limit:
        for i in range(height, new_height, 500):
            driver.execute_script('window.scrollTo(0, {})'.format(i))

            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "Assetreact__AssetCard-sc-bnjqwy-2")))
            elem =	driver.find_elements(By.CSS_SELECTOR,	".Assetreact__AssetCard-sc-bnjqwy-2	> .styles__StyledLink-sc-l6elh8-0")
            
            for	url	in elem:
                if url.get_attribute("href") is not None and get_limit > len(urls):
                    urls.add(url.get_attribute("href"))
                    #print(url.get_attribute("href"))
            #time.sleep(1)
            #print("-------------------------------------------------------")

        get_count = len(urls)
        height = new_height
        new_height = driver.execute_script(js)
        if height == new_height :
            time.sleep(5)
            new_height = driver.execute_script(js)
    
    driver.quit()
    return urls
        
def test_click_refresh_button_all(urls):

    #urls = {'https://opensea.io/assets/solana/AsAnB6TkWsdrUHfXxpKaZ2wy9Kdsc9ZAzfJTgBNR7p9a',
    #        'https://opensea.io/assets/solana/8BGRNpfcwwJbywSzMxLfDDNzNvSgbCMuSTibvopmUim9',
    #        'https://opensea.io/assets/solana/9SgcV2fXkW5G3cYzftpo6LEGcLZw3ZvQzqjbEqtVmdNt',
    #        'https://opensea.io/assets/solana/B6FSU5gS9XNtXDrjrJNkzkr7qSAU3iLEFELw5HGLb2mS'}
    
    tditemlist = get_tditem_list_by_urls(urls)
    #desired_capabilities = DesiredCapabilities.CHROME # 修改页面加载策略
    #desired_capabilities["pageLoadStrategy"] = "none" # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出#注：2021/12/20 在谷歌浏览器96.0.4664.110上验证出效果。

    driver = webdriver.Chrome("chromedriver.exe")
    driver.maximize_window()
    for ditem in tditemlist:
        try:
            #driver = webdriver.Chrome("chromedriver.exe")
            #driver.maximize_window()
            ditem.Status = ""
            driver.get(ditem.Url)
            element = driver.find_element(By.CSS_SELECTOR,  ".jdSrqf:nth-child(1)")
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            
            driver.find_element(By.CSS_SELECTOR, ".kXZare:nth-child(1)  .Iconreact__Icon-sc-1gugx8q-0").click()
            ditem.Status = "Clicked,"
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".Toastreact__DivContainer-sc-6g7ouf-0 > .Blockreact__Block-sc-1xf18x6-0"))
            )
            element = driver.find_elements(By.CSS_SELECTOR, ".Toastreact__DivContainer-sc-6g7ouf-0  > .Blockreact__Block-sc-1xf18x6-0")
            if len(element) > 0:
                ditem.Status = ditem.Status + "Queued,"
            #time.sleep(2)
        except:
            ditem.Status = ditem.Status + "Error,"
        
        finally:
            time.sleep(10)
            #driver.quit()
    driver.quit()    
    tabletd = gen_tabletd(tditemlist)
    title = "web auto test report"
    stylesheet = ""
    str = tpl.HTML_TMPL % dict(
                title = title,
                stylesheet = stylesheet,
                tabletd = tabletd
            )
            
    write_html_to_file("report.html", str)

def test_get_url_to_report():
    urls = test_get_url()
    tditemlist = get_tditem_list_by_urls(urls)
    tabletd = gen_tabletd(tditemlist)
    title = "web auto test report"
    stylesheet = ""
    str = tpl.HTML_TMPL % dict(
                title = title,
                stylesheet = stylesheet,
                tabletd = tabletd
            )
            
    write_html_to_file("report.html", str)
#gen_tabletd_by_urls(urls)
#test_click_refresh_button_all()
#test_get_url_to_report()
urls = test_get_url(in_url = "https://opensea.io/collection/carton-kids", get_limit = 5)
test_click_refresh_button_all(urls)