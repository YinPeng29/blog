# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse

class Article(models.Model):
    title = models.CharField('题目',max_length=100)
    category = models.CharField('博客标签',max_length=50,blank=True)
    date_time = models.DateTimeField('日期',auto_now_add=True)
    content = models.TextField('内容',blank=True,null=True)


    def get_absolute_url(self):
         path = reverse('detail', kwargs={'id':self.id})
         return "http://127.0.0.1:8000%s" % path

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']

