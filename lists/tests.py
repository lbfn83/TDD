from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
import sys

from lists.views import home_page


# Create your tests here.
class HomePageTest(TestCase):
    def test_uses_home_template(self):
        #urls.py와 views.py가 제대로 잘 동작하는지 정도만 확인하는 거지
        response = self.client.get('/')
        self.assertTemplateUsed(response,'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text':'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
        
