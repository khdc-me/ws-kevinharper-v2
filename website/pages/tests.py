from django.test import SimpleTestCase

from django.urls import reverse


# Create your tests here.
class HomepageTests(SimpleTestCase):
    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'pages/home.html')

    def test_homepage_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, "Kevin")
        self.assertNotContains(
    		response, 'This line of text prevent false positive results from previous\
                            line')


class ExperiencePageTests(SimpleTestCase):
    def test_experience_page_status_code(self):
        response = self.client.get('/experience')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url_name(self):
        response = self.client.get(reverse('experience'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_template(self):
        response = self.client.get('/experience')
        self.assertTemplateUsed(response, 'pages/experience.html')

    def test_homepage_contains_correct_html(self):
        response = self.client.get('/experience')
        self.assertContains(response, "Linux")
        self.assertNotContains(
                response, 'This line of text prevent false positive results from previous\
                            line')
