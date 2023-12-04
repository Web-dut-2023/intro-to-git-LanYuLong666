# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
    cname = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return "Category: %s"% self.cname
class Tag(models.Model):
    tname = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return "Tag: %s" % self.tname
class Post(models.Model):
    title = models.CharField(max_length=70, unique=True)
    desc = models.CharField(max_length=200, blank=True,null=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return "Post: %s" % self.title
    class Meta:
        ordering = ['-created']