import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


class TestProductPage:
    
    def test_button_add_to_basket_is_visible(self, browser):
#         Тест проверяет, что страница товара
#         содержит кнопку добавления в корзину

        # Открываем страницу товара
        browser.get(link)
        
        # Установлено время принудительной задержки браузера
        # после открытия страницы, для визуальной проверки языка открытой страницы
        time.sleep(30)
        
        # Проверяем наличие кнопки добавления товара в корзину

#        assert browser.find_element_by_css_selector("button.btn-add-to-basket")
        assert browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")