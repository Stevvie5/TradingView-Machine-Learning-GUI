from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

from functions.webdriver import driver


def settings_button(wait):
    """click settings button."""
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class='icon-button "
                                                           "js-backtesting-open-format-dialog "
                                                           "apply-common-tooltip']")))
    settings_button = driver.find_element_by_xpath(
        "//*[@class='icon-button js-backtesting-open-format-dialog "
        "apply-common-tooltip']")
    settings_button.click()


def strategy_tester():
    """check if strategy tester tab is active if not click to open tab."""
    strategy_tester = driver.find_elements_by_xpath("//*[@class='title-37voAVwR']")[2]
    active = strategy_tester.get_attribute('data-active')
    if active == 'false':
        strategy_tester.click()
    else:
        pass


def overview():
    strategy_tester = driver.find_elements_by_xpath("//*[@class='title-37voAVwR']")[2]
    active = strategy_tester.get_attribute('data-active')
    if active == 'false':
        strategy_tester.click()
        # time.sleep(.3)
        overview = driver.find_element_by_class_name("report-tabs").find_elements_by_tag_name("li")[0]
        overview.click()
    else:
        overview = driver.find_element_by_class_name("report-tabs").find_elements_by_tag_name("li")[0]
        overview.click()


def performance_summary():
    strategy_tester = driver.find_elements_by_xpath("//*[@class='title-37voAVwR']")[2]
    active = strategy_tester.get_attribute('data-active')
    if active == 'false':
        strategy_tester.click()
        # time.sleep(.3)
        performance_tab = driver.find_element_by_class_name("report-tabs").find_elements_by_tag_name("li")[1]
        performance_tab.click()
    else:
        performance_tab = driver.find_element_by_class_name("report-tabs").find_elements_by_tag_name("li")[1]
        performance_tab.click()


def list_of_trades():
    strategy_tester = driver.find_elements_by_xpath("//*[@class='title-37voAVwR']")[2]
    active = strategy_tester.get_attribute('data-active')
    if active == 'false':
        strategy_tester.click()
        time.sleep(.3)
        list_of_trades = driver.find_element_by_class_name("report-tabs").find_elements_by_tag_name("li")[2]
        list_of_trades.click()
    else:
        list_of_trades = driver.find_element_by_class_name("report-tabs").find_elements_by_tag_name("li")[2]
        list_of_trades.click()


def stoploss_input(count, wait):
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class='innerInput-21h1g6jU']")))
    stoploss_input_box = driver.find_elements_by_xpath("//*[@class='innerInput-21h1g6jU']")[0]
    stoploss_input_box.send_keys(Keys.BACK_SPACE + Keys.BACK_SPACE + Keys.BACK_SPACE + Keys.BACK_SPACE)
    stoploss_input_box.send_keys(str(count))
    stoploss_input_box.send_keys(Keys.ENTER)
    ok_button = driver.find_element_by_name("submit")
    ok_button.click()


def takeprofit_input(count, wait):
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class='innerInput-21h1g6jU']")))
    takeprofit_input_box = driver.find_elements_by_xpath("//*[@class='innerInput-21h1g6jU']")[1]
    takeprofit_input_box.send_keys(Keys.BACK_SPACE + Keys.BACK_SPACE + Keys.BACK_SPACE + Keys.BACK_SPACE)
    takeprofit_input_box.send_keys(str(count))
    takeprofit_input_box.send_keys(Keys.ENTER)
    ok_button = driver.find_element_by_name("submit")
    ok_button.click()


def both_inputs(stoploss_value, takeprofit_value, wait):
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class='innerInput-21h1g6jU']")))
    stoploss_input_box = driver.find_elements_by_xpath("//*[@class='innerInput-21h1g6jU']")[0]
    takeprofit_input_box = driver.find_elements_by_xpath("//*[@class='innerInput-21h1g6jU']")[1]
    stoploss_input_box.send_keys(Keys.BACK_SPACE + Keys.BACK_SPACE + Keys.BACK_SPACE + Keys.BACK_SPACE)
    stoploss_input_box.send_keys(str(stoploss_value))
    takeprofit_input_box.send_keys(Keys.BACK_SPACE + Keys.BACK_SPACE + Keys.BACK_SPACE + Keys.BACK_SPACE)
    takeprofit_input_box.send_keys(str(takeprofit_value))
    takeprofit_input_box.send_keys(Keys.ENTER)
    time.sleep(.5)
    ok_button = driver.find_element_by_name("submit")
    ok_button.click()
