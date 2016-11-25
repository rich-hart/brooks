from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from urllib.parse import urljoin
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
class TestPages(StaticLiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_home_page(self):
        import ipdb; ipdb.set_trace()
        #url = reverse('home')
        url = urljoin(self.live_server_url,reverse('home'))
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        import time; time.sleep(4)

    def tearDown(self):
        self.driver.close()
       
#assert "Python" in driver.title
#elem = driver.find_element_by_name("q")
#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()


