from django.test import LiveServerTestCase

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import time



class LoginTest(LiveServerTestCase):

	def setUp(self):

		self.driver = webdriver.Chrome('/home/scenariouser123/.local/lib/python3.5/site-packages')

		super(LoginTest, self).setUp()

	def tearDown(self):

		self.driver.quit()

		super(LoginTest, self).tearDown()

	def test_login(self):

		driver = self.driver

		driver.get('http://51.140.71.34:8000/login/')

		time.sleep(1)

		driver.find_element_by_xpath("/html/body/div[2]/div/h6/a").click()

		time.sleep(1)

		driver.find_element_by_id("id_username").send_keys("Lony")

		time.sleep(1)

		driver.find_element_by_id("id_first_name").send_keys("Lonicera")

		time.sleep(1)

		driver.find_element_by_id("id_last_name").send_keys("Peryclimenum")

		time.sleep(1)

		driver.find_element_by_id("id_email").send_keys("mail@mail.co.uk")

		time.sleep(1)

		driver.find_element_by_id("id_password").send_keys("doesntmatter")

		time.sleep(1)

		driver.find_element_by_id("id_password2").send_keys("doesntmatter")

		time.sleep(1)



		driver.find_element_by_xpath("/html/body/div[2]/div/form/input[2]").click()



