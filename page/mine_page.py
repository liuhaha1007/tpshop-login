from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MinePage(BaseAction):
    mine_button = By.XPATH, "//*[@text='登录/注册']"

    def mine_click(self):
        self.click(self.mine_button)
