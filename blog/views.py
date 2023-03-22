from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView

from django.views.generic.edit import FormView
from django.template.defaultfilters import slugify
from django.views.generic import ListView, DetailView
from django.views import View



from .models import Post, Comment
from .forms import CommentForm


# Create your views here.

all_posts = Post.objects.all()

class StartingPageView(ListView):
    template_name = "blog/blog.html"
    model = Post
    ordering = ["-data"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

class PostsView(ListView):
    template_name = "blog/posts.html"
    model = Post
    ordering = ["-data"]
    context_object_name = "all_posts"

    def get_queryset(self):
        return super().get_queryset()

class PostAdd(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/add_post.html"
    success_url = "/posts"


# class PostDetailView(DetailView):
#     template_name = "blog/post_detail.html"
#     model = Post

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         start = False
#         finish = False
#         try:
#             previous_post = Post.get_next_by_data(context)
#             next_post = Post.get_previous_by_data(context)
#         except:
#             try: 
#                 previous_post = context
#                 next_post = Post.get_previous_by_data(context)
#                 start = True
#             except:
#                 previous_post = Post.get_next_by_data(context)
#                 next_post = context
#                 finish = True
#         context["post"] = context
#         "post_tags": context.tag.all(),
#         "next_post": next_post.slug,
#         "previous_post": previous_post.slug,
#         "start": start,
#         "finish": finish
#         context[""] = 
#         return context


def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    start = False
    finish = False
    try:
        previous_post = Post.get_next_by_data(identified_post)
        next_post = Post.get_previous_by_data(identified_post)
    except:
        try: 
            previous_post = identified_post
            next_post = Post.get_previous_by_data(identified_post)
            start = True
        except:
            previous_post = Post.get_next_by_data(identified_post)
            next_post = identified_post
            finish = True

    return render(request, "blog/post_detail.html",{
        "post":identified_post,
        "post_tags": identified_post.tag.all(),
        "next_post": next_post.slug,
        "previous_post": previous_post.slug,
        "start": start,
        "finish": finish
    })