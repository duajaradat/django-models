from django.test import TestCase
from django.urls import reverse
from .models import Snack

class SnacksTest(TestCase):

    def test_snack_list_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')

    def test_snack_list_status_code(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    
    def test_snack_base_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'base.html')

        

 