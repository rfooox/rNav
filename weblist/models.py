from django.db import models
from django.contrib.auth.models import User

# Django-taggit
from taggit.managers import TaggableManager


class WebType(models.Model):
    # 网站类型
    web_type = models.CharField(max_length=200, blank=False, null=True, verbose_name='网站类型')
    web_seq = models.IntegerField(default=100, blank=True, null=True, verbose_name='优先级')

    creator = models.ForeignKey(User, verbose_name='创建人', null=True, on_delete=models.SET_NULL)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    edited_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    class Meta:
        verbose_name = '网站分类'
        verbose_name_plural = '分类管理'

    def __str__(self):
        return self.web_type


class WebTag(models.Model):
    # 标签
    web_tag = models.CharField(max_length=200, blank=False, null=True, verbose_name='网站标签')
    web_seq = models.IntegerField(default=100, blank=True, null=True, verbose_name='优先级')

    creator = models.ForeignKey(User, verbose_name='创建人', null=True, on_delete=models.SET_NULL)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    edited_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签管理'

    def __str__(self):
        return self.web_tag


# Create your models here.
class WebList(models.Model):
    # WebList: 职位实体的翻译
    web_title = models.CharField(max_length=200, blank=False, null=True, verbose_name='网站标题')
    web_url = models.URLField(blank=False, null=True, verbose_name='网站链接')
    web_type = models.ForeignKey(to=WebType, on_delete=models.SET_NULL, verbose_name='网站类型', null=True, blank=True)
    web_description = models.TextField(blank=True, null=True, verbose_name='网站描述')
    web_icon = models.ImageField(blank=True, null=True, verbose_name='网站图标')
    # tag = TaggableManager(blank=True, verbose_name='标签')
    tag = models.ManyToManyField(to=WebTag, verbose_name='网站标签')

    creator = models.ForeignKey(User, verbose_name='创建人', null=True, on_delete=models.SET_NULL)
    created_time = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)
    edited_time = models.DateTimeField(verbose_name='修改日期', auto_now=True)

    class Meta:
        verbose_name = '网站'
        verbose_name_plural = '网站列表'

    def __str__(self):
        return self.web_title
