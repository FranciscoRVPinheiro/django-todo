from django.test import TestCase
from .models import Task, User
from django.utils import timezone
from django.test import TestCase
from django.utils import timezone
from .models import Task, User
from django.test import TestCase
from rest_framework.test import APIClient


class TaskModelTest(TestCase):


    @classmethod
    def setUp(cls):
        now = timezone.now()
        User.objects.create(username='ricardo', password='password')
        user = User.objects.get(username='ricardo')
        Task.objects.create(title='Test task', description='Test description', completed=False, user=user, created_at=now)

    def test_title_content(self):
        task = Task.objects.get(title="Test task")
        expected_object_name = f'{task.title}'
        self.assertEqual(expected_object_name, 'Test task')

    def test_description_content(self):
        task = Task.objects.get(description='Test description')
        expected_object_name = f'{task.description}'
        self.assertEqual(expected_object_name, 'Test description')  

    def test_completed_content(self):
        task = Task.objects.get(completed=False)
        expected_object_name = f'{task.completed}'
        self.assertEqual(expected_object_name, 'False')


class TestEndPoints(TestCase):

    client = APIClient()

    def test_create_user(self):
        response = self.client.post('/auth/users/', {'username': 'ricardo ', 'email': 'ricardo@gmail.com','password': '12jdud|NhNyhndj541865'}, format='json')
        self.assertEqual(response.status_code, 201)

    def test_get_token(self):
        self.test_create_user()
        response = self.client.post('/auth/token/login/', {'username': 'ricardo', 'password': '12jdud|NhNyhndj541865'}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'auth_token')
        return response.data['auth_token']

    def test_get_user(self):
        token = self.test_get_token()
        response = self.client.get('/auth/users/', HTTP_AUTHORIZATION=f'Bearer {token}')
        self.assertEqual(response.status_code, 200)
    
    def test_create_task(self):
        token = self.test_get_token()
        response = self.client.post('/api/v1/create/', {'title': 'Test task', 'description': 'Test description', 'completed': False}, HTTP_AUTHORIZATION=f'Bearer {token}')
        self.assertEqual(response.status_code, 201)

    def test_task_list(self):
        token = self.test_get_token()
        response = self.client.get('/api/v1/list/', HTTP_AUTHORIZATION=f'Bearer {token}')
        self.assertEqual(response.status_code, 200)
    
    def test_create_tag(self):
        token = self.test_get_token()
        response = self.client.post('/api/v1/create-tag/', {'name': 'Test tag'}, HTTP_AUTHORIZATION=f'Bearer {token}')
        self.assertEqual(response.status_code, 201)

    def test_list_tags(self):
        token = self.test_get_token()
        response = self.client.get('/api/v1/list-tags/', HTTP_AUTHORIZATION=f'Bearer {token}')
        self.assertEqual(response.status_code, 200)