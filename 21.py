from selenium import webdriver

# my_driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
#my_driver.get("https://github.com")
def calculate_tip():
    my_driver = webdriver.Chrome()
    my_driver.get("file:///Users/snae/Downloads/tip_calc/index.html")
    my_driver.find_element_by_id("billamt").send_keys("100")
    # /html/body/div/div[1]/form/p[4]/select/option[3] full xpath
    # //*[@id="serviceQual"]/option[3] xpath
    my_driver.find_element_by_xpath("//*[@id=\"serviceQual\"]/option[3]").click()
    my_driver.find_element_by_id("peopleamt").send_keys("5")
    my_driver.find_element_by_id("musicgrade").send_keys("2")
    my_driver.find_element_by_id("calculate").click()
    return my_driver.find_element_by_id("tip").text


expected = "24.00"
actual = calculate_tip()
if expected == actual:
    print("all good")
else:
    print("oh no something went bad")
assert expected == actual
