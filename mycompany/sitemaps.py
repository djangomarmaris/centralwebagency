from django.contrib.sitemaps import  Sitemap


from django.urls import reverse

from .models import Category,Blog



class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8


    def items(self):
        return Category.objects.all()



class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8



    def items(self):
        return Blog.objects.all()


class StaticSitemap(Sitemap):
    i18 = True
    changefreq = "weekly"
    priority = 0.8


    def items(self):
        return ['cwa:contact','partner','cwa:blog-list','cwa:about','index']

    def location(self, item):
        return reverse(item)
