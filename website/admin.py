from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Service, Profile, Testimonials, About



# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'slug')
#     prepopulated_fields = {'slug': ('name',)}

# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    list_display = ('admin_photo', 'id', 'title', 'date')
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    list_per_page = 5
    summernote_fields = ('description', )


class ServiceAdmin(SummernoteModelAdmin):
    list_display = ('title', 'date', 'description')
    list_display_links = ('title', 'date')
    search_fields = ('title',)
    list_per_page = 5
    summernote_fields = ('description', )

class AboutAdmin(SummernoteModelAdmin):
    list_display = ('bio',)
    list_display_links = ('bio', )
    summernote_fields = ('bio',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('facebook_url', 'twitter_url', 'pintrerest_url', 'instagram_url')
    list_display_links = ('facebook_url', 'twitter_url', 'pintrerest_url', 'instagram_url')
    list_per_page = 5


class TestimonialsAdmin(SummernoteModelAdmin):
    list_display = ('admin_photo', 'name', 'testimony', 'date')
    list_display_links = ('name', 'testimony', 'date')
    search_fields = ('name',)
    list_per_page = 5
    summernote_fields = ('testimony', )


admin.site.register(Post, PostAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Testimonials, TestimonialsAdmin)
# admin.site.register(Category, CategoryAdmin)