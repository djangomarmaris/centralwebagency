from django.contrib import admin
from .models import Category , Product , Referance , Blog
# Register your models here.




class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug']
    prepopulated_fields = {'slug':('name',)}





class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug','category','available','created','updated']
    list_filter = ['available','created','updated','category']
    list_editable = ['available']
    prepopulated_fields = {'slug':('name',)}


class ReferanceAdmin(admin.ModelAdmin):
    list_display = ['name']




class BlogAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Referance,ReferanceAdmin)
admin.site.register(Blog,BlogAdmin)