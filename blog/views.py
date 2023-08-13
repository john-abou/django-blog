from django.shortcuts import render

# Create your views here.
def home(req):
    return render(req, 'blog/home.html')

def posts(req):
    pass

def post_detail(req, slug):
    pass