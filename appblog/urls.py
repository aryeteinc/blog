from django.urls import path
from .views import BlogView

app_name = 'appblog'

urlpatterns = [
    path('', BlogView.as_view(), name="blogindex")
]
