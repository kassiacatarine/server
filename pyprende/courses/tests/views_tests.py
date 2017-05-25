from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse


class CoursesViewTest(TestCase):
    def test_courses_index_status_code(self):
        client = Client()
        response = client.get(reverse('courses:index'))
        self.assertEqual(response.status_code, 200)

    def test_courses_index_not_used_details(self):
        client = Client()
        response = client.get(reverse('courses:index'))
        self.assertTemplateNotUsed(response, 'details.html')