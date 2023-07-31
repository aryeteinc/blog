from django.shortcuts import render
from django.views.generic import View

class BlogView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'title': 'Listado de Blogs'
        }
        return render(request,'blog/index.html',context)
        
