from django.db import models

# Create your models here.

class Board(models.Model):
    content = models.CharField(max_length=2000)
    title = models.CharField(max_length=200)
    regdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Board(%s, %s, %s)' % (self.title, self.content, str(self.regdate))