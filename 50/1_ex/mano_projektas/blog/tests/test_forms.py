from django.test import TestCase
from ..forms import PostForm

class PostFormTest(TestCase):
    def test_forma_su_geraisid_duomenimis(self):
        form = PostForm(
            data={
                'title':'Testas',
                'body':'Turinys'
            }

        )
        self.assertTrue(form.is_valid())

    def test_forma_su_tusciais_duomenimis(self):
        form = PostForm(
            data={
                'title':'',
                'body':''
            }

        )
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
        self.assertIn('body', form.errors)
