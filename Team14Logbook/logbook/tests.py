from django.test import LiveServerTestCase

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import time



class AddPostTest(LiveServerTestCase):

	def setUp(self):

		self.driver = webdriver.Chrome('/home/scenariouser123/.local/lib/python3.5/site-packages')

		super(AddPostTest, self).setUp()

	def tearDown(self):

		self.driver.quit()

		super(AddPostTest, self).tearDown()

	def test_addpost(self):

		driver = self.driver

		driver.get('http://51.140.71.34:8000/login/')

		time.sleep(1)

		driver.find_element_by_id("id_username").send_keys("admin")

		time.sleep(1)

		driver.find_element_by_id("id_password").send_keys("password123")

		time.sleep(1)

		driver.find_element_by_css_selector("input[type=submit]").click()

		time.sleep(1)



		driver.get('http://51.140.71.34:8000/create/')

		time.sleep(1)



		driver.find_element_by_id("id_title").send_keys("Papaver Rhoeas")

		time.sleep(1)

		driver.find_element_by_id("id_content").send_keys("This is a poppy.")

		time.sleep(1)

		driver.find_element_by_id("id_publish").send_keys("2017-11-03")

		time.sleep(1)

		driver.find_element_by_id("id_category").send_keys("Testing")

		time.sleep(1)



		driver.find_element_by_xpath('/html/body/div[2]/div/form/input[2]').send_keys(Keys.RETURN)



		time.sleep(1)