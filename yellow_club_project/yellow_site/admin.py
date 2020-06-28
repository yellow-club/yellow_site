from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from .models import Category, Post


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

    list_display  = ('id', 'title', 'slug', 'event_date', 'get_photo', 'views','category')
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    list_filter = ('category',)

    list_editable = ('category',)
    readonly_fields = ('views', 'get_photo','created_at')

    fields = ('title', 'slug', 'category', 'content', 'photo', 'get_photo', 'event_date', 'created_at', 'views', 'speaker')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src = " {obj.photo.url} " width = "50">')
        return '-'    

    get_photo.short_description = 'Фото'

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)


