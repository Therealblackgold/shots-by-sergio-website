from django.shortcuts import render
from .models import Post, Service, Profile, Testimonials, About



def home(request):
    posts = Post.objects.order_by('-date')
    service = Service.objects.all()
    profile = Profile.objects.all()
    testimonials = Testimonials.objects.all()
    about = About.objects.all()
    return render(request, 'home.html', {'posts':posts, 'service': service, 'profile':profile, 'testimonials':testimonials, 'about':about,})



