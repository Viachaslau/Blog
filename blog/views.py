from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.template.defaultfilters import slugify
from django.views.generic import ListView
from django.views import View



from .models import Post, Author, Tag
from .forms import PostForm


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

class PostsView(View):
    def get(self, request):
        posts  = Post.objects.all().order_by("-data")
        context = {
            "all_posts": posts
        }
        return render(request, "blog/posts.html", context)
    
    def post(self, request):
        posts  = Post.objects.all().order_by("-data")
        context = {
            "all_posts": posts
        }
        return render(request, "blog/posts.html", context)

class PostAdd(CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/add_post.html"
    success_url = "posts/add-post"

    def form_valid(self, form):
        self.slug = slugify(self.title)
        form.save()
        return super(Post, self).form_valid(form)



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