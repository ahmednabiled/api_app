from django.urls import path
from . views import BlogPostListCreate , BlogPostRetrieveUpdateDestroy


urlpatterns = [
    path("blogposts/", BlogPostListCreate.as_view(),name = 'blogpost-view-create'),
    path("blogposts/<str:pk>/", BlogPostRetrieveUpdateDestroy.as_view(),name = 'blogpost-retrieve-update-destroy'),
]