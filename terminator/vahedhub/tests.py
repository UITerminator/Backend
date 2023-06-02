from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.test import RequestsClient
from .query import *
from .models import *

class VahedhubTestCases(TestCase):

    def test_1(self):
        client = RequestsClient()
        response = client.get('http://localhost:8000/vahedhub/coursesfulldetail/')
        self.assertIs(response.status_code, 300)



