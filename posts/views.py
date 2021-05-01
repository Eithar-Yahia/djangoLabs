from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PostForm
from .models import Post
# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, "posts/index.html", {
        "posts" : posts 
    })

def create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("index")
    
    return render(request, "posts/create.html", {
        "form" : form 
    }) 

def edit(request, id):
    post = Post.objects.get(pk=id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect("index")
    
    return render(request, "posts/edit.html", {
        "form" : form,
        "post" : post
    }) 

def delete(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect("index")