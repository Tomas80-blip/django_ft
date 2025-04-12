from django.test import TestCase
from ..models import Post

class PostModelTest(TestCase):

    def test_post_sukurimas_ir_str_veikla(self):
        post = Post.objects.create(title='Testas', body='Testinis turinys')

        self.assertEqual(post.title, 'Testas')
        self.assertEqual(post.body, 'Testinis turinys')
        self.assertEqual(str(post), 'Testas')