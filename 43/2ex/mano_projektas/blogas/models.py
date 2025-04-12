# Darbas per sell’a
# python manage.py shell
# sukuriam viena post’a ir du komentus ir pririsam juos posto:
# from blogas.models import Post, Comment
# Sukuriam kintamaji postas, nes po to ji idesim i Comment(kadangi turi relationa)
# postas = Post.objects.create(title='Pirmas irasas', body= 'Hello World')
# Sukuriam du Commntus:
# Comment.objects.create(post=postas, author_name='Jonas', content='Labai idomu')
# Comment.objects.create(post=postas, author_name='Aiste', content='Sutinku su Jono nuomone')
# visi_postai = Post.objects.all()
# print(visi_postai)
# <QuerySet [<Post: post1>, <Post: Pirmas irasas>]>
# visi_komentarai = postas.comment_set.all()
# for k in visi_komentarai:
#     ...:     print(k.author_name)  # du kartus ENTER
# Aiste
# Jonas
# In [19]: history
# from blogas.models import Post, Comment
# postas = Post.objects.create(tittle='Pirmas irasas', body= 'Hello World')
# print(postas)
# print(postas.id)
# Comment.objects.create(post=postas, author_name='Jonas', content='Labai idomu')
#  Comment.objects.create(post=postas, author_name='Aiste', content='Sutinku su Jono nuomone')
# visi_postai = Post.objects.all()
# print(visi_postai)
# visi_komentarai = postas.comment_set.all()
# for k in visi_komentarai:
#     print(k.author_name)
# history



from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    #Comment- komentaras
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    #CASCADE jei trinsim Post's, tai Coment'as taip pat issitrins
    author_name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author_name} apie "{self.post.title}"'

    class Meta:
        ordering = ['-created_at']
