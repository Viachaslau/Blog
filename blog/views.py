from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView

from .models import Post
from .forms import PostForm


# Create your views here.

all_posts = Post.objects.all()

class PostAdd(CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/add_post.html"
    success_url = "posts/"

class Report(TemplateView):
    template_name = "blod/posts.html"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        # context['message'] = "This works"
        return context


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