from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_nav_to_sitters_page(self):
        self.browser.get('http://localhost:8000')

        # She notices 'Find Sitters' on the home page
        assert 'Sitters' in self.browser.title
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Sitters', header_text)

        # She can see a list of sitters ordered by sitter rank

        # she can see sitter name, photo and average of stay ratings for each sitter

        # She can filter out sitters with poor average stay ratings


if __name__ == '__main__':
    unittest.main(warnings='ignore')


