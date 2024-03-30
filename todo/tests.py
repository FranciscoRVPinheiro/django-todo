from django.test import TestCase
from .models import Task, User
from django.utils import timezone
from django.test import TestCase
from django.utils import timezone
from .models import Task, User
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

