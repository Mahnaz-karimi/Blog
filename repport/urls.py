
from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='repport-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),# det er nødvendig sti pejer på en rigtig view så derfor adder vi as_views to den method vi har brugt. i sted for pk kan også stor object atribitut
    path('post/new/', PostCreateView.as_view(), name='post-create'), # primrry key af post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('about/', views.about, name='repport-about'),
]
