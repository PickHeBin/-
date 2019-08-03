from selenium import webdriver

from selenium.webdriver.chrome.options import Options

import time


chrome_options = Options()


# chrome_options.add_argument('--headless')


driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='chromedriver.exe')


driver.get('https://www.wjx.cn/jq/37766520.aspx')
# driver.get('https://www.baidu.com')

# driver.save_screenshot('test_wenjuan.png')

# elements = driver.find_elements_by_xpath("//*[@class='div_question']")
# for element in elements:
#     print(element.text)


el = driver.find_element_by_xpath("//*[text()='男']/preceding-sibling::a")
el.click()
el = driver.find_element_by_xpath("//*[text()='理科']/preceding-sibling::a")
el.click()
el = driver.find_element_by_xpath("//*[text()='大四']/preceding-sibling::a")
el.click()

elements = driver.find_elements_by_xpath("//*[@class='ulradiocheck']")[3:]
for element in elements:
    el = element.find_element_by_xpath('./li[4]/a')
    print(el.get_attribute('title'))
    el.click()

el = driver.find_element_by_id('submit_button')
print(el.get_attribute('value'))


time.sleep(5)
#   关闭浏览器
driver.close()
