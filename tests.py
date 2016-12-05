from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from urllib.parse import urljoin
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
class TestBasePage(StaticLiveServerTestCase):
    def setUp(self):
        url = urljoin(self.live_server_url,reverse('home'))
        self.driver = webdriver.Chrome()
        self.driver.get(url)

#    def test_nav(self):
#        import ipdb; ipdb.set_trace()
#        self.driver.set_window_size(800,600)
#        topnav_elem = self.driver.find_element_by_id('topnav')
#        self.assertEqual(topnav_elem.text,'Home\nContact\nAbout')
#        self.driver.set_window_size(679,600)
#        self.assertEqual(topnav_elem.text,'Home\n☰')
#        topnav_elem_list = self.driver.find_element_by_id('topnav_list') 
#        topnav_elem_list.click()
#        self.assertEqual(topnav_elem.text,'Home\nContact\nAbout\n☰')


    def tearDown(self):
#        import time; time.sleep(4)
        self.driver.close()

