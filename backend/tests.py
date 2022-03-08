from django.test import TestCase
from django.contrib.auth.models import User
from backend.models import Entreprise, Category


class Test_Create_Entreprise(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='SAS')

        testuser1 = User.objects.create_user(
            username='test_user1', password='123456789')
        testuser1.save()

        test_entreprise = Entreprise.objects.create(
            category_id=1, name='entreprise Title', content='entreprise Content', slug='entreprise-title', founder_id=1, status='in progress')
        test_entreprise.save()

    def test_blog_content(self):
        entreprise = Entreprise.entreprisebbjects.get(id=1)
        cat = Category.objects.get(id=1)
        founder = f'{entreprise.founder}'
        name = f'{entreprise.name}'
        content = f'{entreprise.content}'
        status = f'{entreprise.status}'

        self.assertEqual(founder, 'test_user1')
        self.assertEqual(name, 'entreprise Title')
        self.assertEqual(content, 'entreprise Content')
        self.assertEqual(status, 'in progress')
        self.assertEqual(str(entreprise), "entreprise Title")
        self.assertEqual(str(cat), "SAS")
