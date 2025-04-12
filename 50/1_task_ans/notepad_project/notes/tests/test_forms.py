from django.test import TestCase
from ..forms import NoteForm

class NoteFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'title': 'Testas',
            'content': 'Turinys',
        }
        form = NoteForm(data=form_data)

        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {
            'title': '',
            'content': '',
        }
        form = NoteForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
