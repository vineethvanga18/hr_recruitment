from django.test import TestCase, Client
from django.urls import reverse
from .models import Application
from .forms import ApplicantForm, ApplicationForm


# Create your tests here.
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
        self.apply_url = reverse('apply')
        self.app1 = Application.objects.create(Objective="abcdef", skills_required="abc")

    def test_index(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_apply(self):
        form = ApplicantForm(data={'name': "QWERTY", 'Applying_for': self.app1, 'skills': "abc"})
        self.assertTrue(form.is_valid())

    def test_apply_no_data(self):
        form = ApplicantForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

    def test_new_application(self):
        form = ApplicationForm(data={'Objective': "abcdef", 'skills_required': "abc"})
        self.assertTrue(form.is_valid())

    def test_new_application_with_no_data(self):
        form = ApplicationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
