from django.shortcuts import render ,redirect 
from .models import Web
from django.http import  HttpResponse ,HttpRequest
# Create your views here.
def add_blog_view(request: HttpRequest):

    #Creating a new entry into the database for a movie
    
    if request.method == "POST":
        new_Web = Web(Title =request.POST["Title"], Contant =request.POST["Contant"], is_published =request.POST["is_published"], published_at=request.POST["published_at"], category=request.POST["category"], poster=request.FILES["poster"])
        new_Web.save()
        blog_id=new_Web.id
        return redirect("lapblog:blog_detail_view",blog_id)

    return render(request, "lapblog/add.html", {"categories" : Web.categories})



def blog_home_view(request: HttpRequest):

    lapblog = Web.objects.all()

    return render(request, "lapblog/blog_home.html", {"lapblog" : lapblog})

def blog_detail_view(request:HttpRequest, blog_id):
    try:
        blog = Web.objects.get(id = blog_id)
    except Exception as e:
        return render(request, "lapblog/NotExist.html")
   

    return render(request, "lapblog/blog_detail.html", {"Web" : blog})

def NotExist_view(request:HttpRequest):

    return render (request , "NotExist.html" )
def update_blog_view(request:HttpRequest , blog_id):
    blog = Web.objects.get(id = blog_id)
    return render(request)

def update_blog_view(request: HttpRequest , blog_id ):
    blog = Web.objects.get(id = blog_id)
    if request .method == "POST":
        blog.Title = request.POST["Title"]
        blog.Contant = request.POST["Contant"]
        blog.is_published = request. POST["is_published"]
        blog.published_at = request . POST["published_at"]
        blog.category = request.POST["category"]
        blog.save()
        return redirect ('lapblog:blog_detail_view' , blog_id=blog.id)
    
    return render(request, "lapblog/update.html", {"blog" : blog, "categories"  : blog.categories})


def delete_blog_view(request: HttpRequest, blog_id):

    blog = Web.objects.get(id = blog_id)
    blog.delete()

    return redirect("lapblog:blog_home_view")                        