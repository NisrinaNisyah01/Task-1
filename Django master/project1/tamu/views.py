from django.shortcuts import render

# Create your views here.
from . models import Post

def index(request):
    postingan=Post.objects.all()
    contex={'TampungPostingan': postingan}
    return render(request, 'tamu/index.html', contex)