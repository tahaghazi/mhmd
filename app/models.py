from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image
from django.utils.text import slugify

def arabic_slugify(str):
    str = str.replace(" ", "-")
    str = str.replace(",", "-")
    str = str.replace("(", "-")
    str = str.replace(")", "")
    str = str.replace("؟", "")
    return str
# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=50,verbose_name='الاسم الأول')
    last_name = models.CharField(max_length=50,verbose_name='الاسم الأخير')
    phone = models.CharField(max_length=15,verbose_name='رقم الهاتف ')
    email = models.EmailField(verbose_name='البريد الالكتروني')
    age = models.IntegerField(default=0,verbose_name='العمر')
    content = models.TextField(help_text='من انت ؟!',verbose_name='الوصف')
    address = models.CharField(max_length=10000,verbose_name='العنوان')
    nationality = models.CharField(max_length=50,verbose_name='الجنسيه')
    langages  = models.CharField(max_length=50,verbose_name='اللغات')
    exp = models.IntegerField(default=0,verbose_name='سنين الخبره')
    projects = models.IntegerField(default=0,verbose_name='المشاريع المكتمله')
    image = models.ImageField(default='img-mobile.jpg', upload_to='profile_pics',help_text='يفضل ان تكون بحجم 300x300',verbose_name='صورة الملف الشخصي')
    def __str__(self):
        return self.first_name+' '+self.last_name
    class Meta:
        verbose_name = ('الملف الشخصي')
        verbose_name_plural = ('الملف الشخصي')

class Portfolio(models.Model):
    title = models.CharField(max_length=1000,verbose_name='عنوان المشروع')
    cat = models.CharField(max_length=100,help_text='قم باختيار نوع التصميم لوجو او بانر ...الخ',verbose_name='نوع المشروع')
    client = models.CharField(max_length=1000,verbose_name='العميل/الزبون')
    skills = models.CharField(max_length=1000,verbose_name='المهارات المستخدمه')
    link = models.URLField(blank=True,null=True, verbose_name= 'رابط المشروع ان وجد')
    file = models.ImageField(help_text='قم باختيار صورة التصميم من جهازك',verbose_name='ملف المشروع')
    slug = models.SlugField(blank=True,null=True,unique=True,allow_unicode=True,editable=False)
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            if not self.slug:
                self.slug = arabic_slugify(self.title)
        super(Portfolio, self).save(*args, **kwargs)
    class Meta:
        verbose_name = ('مشروع ')
        verbose_name_plural = ('المشاريع/Portfolio')
        ordering = ('-date',)
class Contact(models.Model):
    name = models.CharField(max_length= 100 , verbose_name='الاسم')
    sub = models.CharField(max_length= 100 , verbose_name='الموضوع')
    email = models.EmailField(verbose_name='البريد الالكتروني')
    message = models.TextField(verbose_name='الرساله')
    date = models.DateTimeField(auto_now=True,verbose_name='تاريخ الاضافه')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = ('رساله')
        verbose_name_plural = ('الرسائل')
        ordering = ('-date',)