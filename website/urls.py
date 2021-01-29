
from django.urls import path
from . import views

# #we have to specify blog app incase we have mor than one app.
# app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    # path('<int:post_id>/', views.detail, name='detail'),
]



# urlpatterns = [
#     path('', views.home, name="home"),
# ]
