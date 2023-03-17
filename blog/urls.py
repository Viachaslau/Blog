from django.urls import path

from . import views

urlpatterns = [
    path("", views.starting_page, name='starting-page'),
    path("posts/", views.posts, name='posts-page'),
    path("posts/add-post", views.PostAdd.as_view()),
    path("posts/<slug:slug>", views.post_detail, 
        name='post-detail-page') #/posts/my-first-post
]
