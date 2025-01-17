from django.contrib import admin
from django.urls import path

from CVGenerator import views
from CVGenerator.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('accept/', views.accept, name='accept'),
    path('<int:id>/', views.resume, name='resume'),
]