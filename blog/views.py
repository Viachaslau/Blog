from django.shortcuts import render, get_object_or_404

from .models import Post


# Create your views here.

all_posts = Post.objects.all()

def starting_page(request):
    latest_posts = all_posts.order_by("-data")[:3]
    return render(request, "blog/blog.html",{
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/posts.html",{
        "all_posts": all_posts.order_by("-data")
    })

def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post_detail.html",{
        "post":identified_post,
        "post_tags": identified_post.tag.all()
    })