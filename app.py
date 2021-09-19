from selenium import webdriver
import time

def getPrice(urls):
    driver = webdriver.Chrome('C:/Users/ismet/OneDrive/Bureaublad/chromedriver_win32 (1)/chromedriver.exe')
    data = {}
    for url in urls:
        driver.get(url)
        try:
            accept_cookies = driver.find_element_by_xpath('//*[@id="sp-cc-accept"]').click()
        except:
            pass
        name = driver.find_element_by_xpath('//*[@id="title"]').text
        price = driver.find_element_by_xpath('//*[@id="olp_feature_div"]/div[2]/span[1]/a/span[2]').text
        data[name] = price
        time.sleep(3)
    driver.close()
    return data

urls = ['https://www.amazon.de/-/nl/dp/B08PFZ28CN/ref=sr_1_1?__mk_nl_NL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=3060+ti&qid=1632074314&sr=8-1',
        'https://www.amazon.de/-/nl/dp/B09BP1827M/ref=sr_1_2?__mk_nl_NL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=3060+ti&qid=1632074314&sr=8-2',
        'https://www.amazon.de/-/nl/dp/B09968R87B/ref=sr_1_4?__mk_nl_NL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=3060+ti&qid=1632074314&sr=8-4',
        'https://www.amazon.de/-/nl/dp/B096XZZ92Q/ref=sr_1_7?__mk_nl_NL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=3060+ti&qid=1632074314&sr=8-7',
        'https://www.amazon.de/-/nl/dp/B0971XRQR4/ref=pd_vtp_4/261-4342348-6051742?pd_rd_w=9ohe6&pf_rd_p=4e0c7b51-e41d-4568-8470-6e0da61f6c1d&pf_rd_r=Q41N66TP6TVN57DGNTKK&pd_rd_r=b133a321-24be-461c-883a-438e4ec487fb&pd_rd_wg=3IfWv&pd_rd_i=B0971XRQR4&psc=1'
       ]

if __name__ == "__main__":
    getPrice(urls)
