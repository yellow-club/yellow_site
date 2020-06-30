from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from django.contrib.flatpages.models import FlatPage


from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld 
from django.contrib.flatpages.forms import FlatpageForm as FlatPageFormOld


from .models import Category, Post


class FlatPageForm(FlatPageFormOld):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    
    class Meta:
        model = FlatPage
        fields = '__all__'


class FlatPageAdmin(FlatPageAdminOld):   
    form = FlatPageForm

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    
    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = PostAdminForm
    save_as = True
    save_on_top = True

    list_display  = ('id', 'title', 'slug', 'created_at', 'updated_at', 'get_photo', 'views','category')
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    list_filter = ('category',)

    list_editable = ('category',)
    readonly_fields = ('views', 'get_photo','created_at', 'updated_at')

    fields = ('title', 'slug', 'category', 'content', 'photo', 'get_photo', 'updated_at', 'created_at', 'views', 'author')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src = " {obj.photo.url} " width = "50">')
        return '-'    

    get_photo.short_description = 'Фото'

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}



admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)


