from django.test import TestCase,Client
from django.urls import reverse
from ..models import Post

class PostViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_puslapis_pasiekiamas(self):
        response = self.client.get(reverse('post_list'))
        self.assertEquals(response.status_code, 200)


    def test_iraso_sukurimas_per_post(self):
        response = self.client.post(
            reverse('post_create'),
            {
                'title':'Testinis irasas',
                'body': 'Testinis turinys'
            }
        )
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Post.objects.count(), 1)