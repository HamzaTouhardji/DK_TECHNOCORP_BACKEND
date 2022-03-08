from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from backend.models import Entreprise, Category
from django.contrib.auth.models import User
from rest_framework.test import APIClient


class PostTests(APITestCase):

    def test_view_entreprises(self):
        """
        Ensure we can view all objects.
        """
        url = reverse('backend_api:listEntrepriseCreated')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_account(self):
        """
        Ensure we can create a new Post object and view object.
        """
        self.test_category = Category.objects.create(name='SAS')

        self.testuser1 = User.objects.create_user(
            username='test_user1', password='123456789')

        data = {"name": "test", "founder": 1,
                "content": "test"}
        url = reverse('backend_api:listEntrepriseCreated')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 5)
        root = reverse(('backend_api:detailEntrepriseCreated'),
                       kwargs={'pk': 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_entreprise_update(self):

        client = APIClient()

        self.test_category = Category.objects.create(name='SAS')
        self.testuser1 = User.objects.create_user(
            username='test_user1', password='123456789')
        self.testuser2 = User.objects.create_user(
            username='test_user2', password='123456789')
        test_entreprise = Entreprise.objects.create(
            category_id=1, name='entreprise Title', content='entreprise Content', slug='entreprise-title', founder_id=1, status='in progress')

        client.login(username=self.testuser1.username,
                     password='123456789')

        url = reverse(('backend_api:detailEntrepriseCreated'),
                      kwargs={'pk': 1})

        response = client.put(
            url, {
                "name": "New",
                "founder": 1,
                "content": "New",
                "status": "in progress"
            }, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
