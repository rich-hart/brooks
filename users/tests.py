from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import Profile
from django.contrib.auth.models import User
class UserTests(APITestCase):
    def test_create_user(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('user-list')
        data = {
            'username': 'username',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'email': 'u@d.com',
            'profile': {
                'about': 'about',
                'image': 'https://image.com',
            }
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profile.objects.count(), 1)


    def test_update_user(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('user-list')
        data = {
            'username': 'username',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'email': 'u@d.com',
            'profile': {
                'about': 'about',
                'image': 'https://image.com',
            }
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profile.objects.count(), 1)
        response = self.client.put(url+'1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Profile.objects.count(), 1)

        user=User.objects.all()[0]
        self.assertEqual(user.email,data['email'])
