from selenium import webdriver


class Driver:
    driver = webdriver.Chrome()  # accesam driver-ul
    driver.maximize_window()  # maximizam fereastra
    driver.implicitly_wait(3)  # val maxima de secunde care se va astepta pt incarcare

    def close(self):
        self.driver.close()
