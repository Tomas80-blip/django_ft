from django.test import TestCase
from django.urls import reverse
from ..models import Note


class NoteViewsTest(TestCase):
    def test_note_list_view(self):
        response = self.client.get(reverse('note_list'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'note_list.html')

    def test_note_create_view_get(self):
        response = self.client.get(reverse('note_create'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'note_form.html')

    def test_note_create_view_post(self):
        data = {
            'title': 'Testinis',
            'content': 'Testinis turinys'
        }
        response = self.client.post(reverse('note_create'), data)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Note.objects.count(), 1)
