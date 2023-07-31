from .views import HomeView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home"),
    path('blog/',include('appblog.urls', namespace='appblog')),
]
