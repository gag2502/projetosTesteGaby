from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class user_default (User):
    pass

class Author(models.Model):
    name = models.CharField(max_length=200)

    def get_absolute_url(self):
        #return 'author_detail', (), {'slug': self.slug}
        return reverse('author-detail', kwargs={'pk': self.pk})
