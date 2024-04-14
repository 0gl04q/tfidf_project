from django.db import models


class File(models.Model):
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    count = models.IntegerField()
    text = models.TextField()
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-added',)

    def __str__(self):
        return self.file.name


class Word(models.Model):
    name = models.CharField(max_length=50)
    file = models.ManyToManyField(File)

    class Meta:
        ordering = ('name',)
        indexes = [models.Index(fields=['name'])]

    def __str__(self):
        return self.name
