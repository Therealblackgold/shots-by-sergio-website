from django.db import models
from django.urls import reverse
from datetime import date
from django.utils.safestring import mark_safe




# Post.
class Post(models.Model):
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True )
    view_image = models.ImageField(upload_to='uploads/', null=True, blank=True )
    title = models.CharField(max_length=200, blank=True, null=True )
    description = models.TextField( blank=True, null=True )
    date = models.DateField()

    # Resize image.
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

    # Disply image in admin.
    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))
        admin_photo.short_description = 'Image'
        admin_photo.allow_tags = True


    def __str__(self):
        return self.title



class Service(models.Model):
    title = models.CharField(null=True, blank=True, max_length=50)
    description = models.TextField( blank=True, null=True )
    date = models.DateField(("Date"), default=date.today)




    def __str__(self):
        return self.title


class Profile(models.Model):
    name = models.CharField(null=True, blank=True, max_length=50)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    pintrerest_url = models.CharField(max_length=255, null=True, blank=True)
    youtube_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name



class About(models.Model):
    bio = models.TextField( blank=True, null=True )   
    date = models.DateField(("Date"), default=date.today)
    


class Testimonials(models.Model):
    image = models.ImageField(upload_to='uploads/testimonial', null=True, blank=True )
    name = models.CharField(null=True, blank=True, max_length=50)
    testimony = models.TextField( blank=True, null=True )
    date = models.DateField(("Date"), default=date.today)


     # Disply image in admin.
    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))
        admin_photo.short_description = 'Image'
        admin_photo.allow_tags = True

    def __str__(self):
        return self.name 



   
