from django.test import TestCase
from django.urls import reverse
from .models import Todo


class TodoModelTest(TestCase):
    def test_create_todo(self):
        todo = Todo.objects.create(title="Test task")
        self.assertEqual(str(todo), "Test task")
        self.assertFalse(todo.completed)

    def test_index_page_loads(self):
        response = self.client.get(reverse("todos:index"))
        self.assertEqual(response.status_code, 200)

    def test_add_todo(self):
        response = self.client.post(reverse("todos:index"), {"title": "New task"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Todo.objects.count(), 1)

    def test_toggle_todo(self):
        todo = Todo.objects.create(title="Toggle me")
        self.client.post(reverse("todos:toggle", args=[todo.pk]))
        todo.refresh_from_db()
        self.assertTrue(todo.completed)

    def test_delete_todo(self):
        todo = Todo.objects.create(title="Delete me")
        self.client.post(reverse("todos:delete", args=[todo.pk]))
        self.assertEqual(Todo.objects.count(), 0)
