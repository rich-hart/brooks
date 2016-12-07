from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from urllib.parse import urljoin
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class TestBasePage(StaticLiveServerTestCase):
    fixtures = ['fixture.yaml']
    def setUp(self):
        url = urljoin(self.live_server_url,reverse('profile'))
        self.driver = webdriver.Chrome()
        self.driver.get(url)

    def test_nav(self):
        self.driver.set_window_size(800,600)
        topnav_elem = self.driver.find_element_by_id('topnav')
        self.assertEqual(topnav_elem.text,'Profile\nShows\nDonate')

    def tearDown(self):
        self.driver.close()


class TestProfilePage(StaticLiveServerTestCase):
    fixtures = ['fixture.yaml']
    def setUp(self):
        url = urljoin(self.live_server_url,reverse('profile'))
        self.driver = webdriver.Chrome()
        self.driver.get(url)

    def test_nav(self):
        self.driver.set_window_size(800,600)
        topnav_elem = self.driver.find_element_by_id('topnav')
        self.assertEqual(topnav_elem.text,'Profile\nShows\nDonate')


    def tearDown(self):
        self.driver.close()

class TestShowsPage(StaticLiveServerTestCase):
    fixtures = ['fixture.yaml']
    def setUp(self):
        url = urljoin(self.live_server_url,reverse('shows'))
        self.driver = webdriver.Chrome()
        self.driver.get(url)

    def test_nav(self):
        self.driver.set_window_size(800,600)
        topnav_elem = self.driver.find_element_by_id('topnav')
        self.assertEqual(topnav_elem.text,'Profile\nShows\nDonate')


    def tearDown(self):
        self.driver.close()

