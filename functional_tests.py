from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest 

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# visit webpage
		self.browser.get('http://localhost:8000')

		#title/header check
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		#user is invited to add list item right away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)
		
		#user typs buy peacock feathers as list item
		inputbox.send_keys('Buy peacock feathers')

		#user hits enter, page reloads and displays new item on list
		inputbox.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

		# There is still a text box inviting her to add another item. She
		# enters "Use peacock feathers to make a fly" (Edith is very
		# methodical)
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)
		# The page updates again, and now shows both items on her list
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
		self.assertIn(
			'2: Use peacock feathers to make a fly' ,
			[row.text for row in rows]
		)

		self.fail('Finish the test!')




if __name__=='__main__':
	unittest.main(warnings='ignore')

