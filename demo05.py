import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://testhotel.guomintrip.com")
driver.implicitly_wait(10)
driver.execute_script("window.open('https://admin.guomintrip.com')")
print(driver.current_window_handle,driver.current_url)
handles = driver.window_handles
print(handles,)


# for handle in handles:
#     if handle != driver.current_window_handle:
#         print("switch to"),handle
#         driver.switch_to.window(handle)
#         print(driver.current_window_handle,driver.current_url)
#         break

driver.switch_to.window(handles[1])
print(driver.current_url)
driver.switch_to.window(handles[0])
print(driver.current_url)
time.sleep(5)
