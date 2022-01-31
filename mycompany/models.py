from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    header_image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    name = models.CharField(max_length=20, db_index=True)
    title = models.CharField(max_length=200, db_index=True)
    title_info = models.CharField(max_length=200, db_index=True)
    title2 = models.CharField(max_length=200, db_index=True)
    info = RichTextUploadingField(blank=True)
    info2 = RichTextUploadingField(blank=True)
    black = RichTextUploadingField(blank=True)
    personel = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    personel_info = RichTextUploadingField(blank=True)
    slug = models.SlugField(max_length=20, db_index=True, unique=True)





    def __str__(self):
        return self.name



    def get_absolute_url(self):
        return reverse('detail', args=[self.slug])



class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete = models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    description = RichTextUploadingField(blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    seo = models.CharField(max_length=500,default="Seo için Bilgi Giriniz.")
    key = models.CharField(max_length=550,default="Keyword için Giriş")


    class Meta:
        ordering = ('created',)
        index_together = (('id', 'slug',))

    def __str__(self):
        return self.name



    #def get_absolute_url(self):
        #return reverse('mimar:product_detail', args=[self.id, self.slug])



class Referance(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)




    def __str__(self):
        return self.name


class Blog(models.Model):
    title_image = models.ImageField(upload_to='products/%y/%m/%d', blank=True, verbose_name="Tittle resim:")
    title = models.CharField(max_length=50,verbose_name="Title:")
    slug = models.SlugField(max_length=200, db_index=True)
    title_info = models.CharField(max_length=50,verbose_name="Title İnfo:")
    date = models.DateTimeField(auto_now_add=True)
    info = RichTextUploadingField(blank=True,verbose_name="Açıklama:")
    info2 = RichTextUploadingField(blank=True,verbose_name="Açıklama 2:")
    red = RichTextUploadingField(blank=True,verbose_name="Kırmızı Alan:")
    info3 = RichTextUploadingField(blank=True,verbose_name="Açıklama 3:")
    big_image = models.ImageField(upload_to='products/%y/%m/%d', blank=True,verbose_name="Büyük resim:")
    title2 = models.CharField(max_length=50,verbose_name="Title Two:")
    info4 = RichTextUploadingField(blank=True,verbose_name="Açıklama 4:")
    black = models.CharField(max_length=100,verbose_name="Black:")
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cwa:blog_detail', args=[self.slug])
