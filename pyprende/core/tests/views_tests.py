from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse


class HomeViewTest(TestCase):
    def test_home_status_code(self):
        client = Client()
        response = client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)

    def test_home_used_base(self):
        client = Client()
        response = client.get(reverse('core:home'))
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_home_not_used_contact(self):
        client = Client()
        response = client.get(reverse('core:home'))
        self.assertTemplateNotUsed(response, 'contact.html')

    def test_contact_status_code(self):
        client = Client()
        response = client.get(reverse('core:contact'))
        self.assertEqual(response.status_code, 200)

    def test_contact_used_base(self):
        client = Client()
        response = client.get(reverse('core:contact'))
        self.assertTemplateUsed(response, 'contact.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_contact_not_used_home(self):
        client = Client()
        response = client.get(reverse('core:contact'))
        self.assertTemplateNotUsed(response, 'home.html')