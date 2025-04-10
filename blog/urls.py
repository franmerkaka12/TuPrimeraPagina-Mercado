from django.urls import path
from .views import (
    PostListView,
    PostCreateView,
    PostUpdateView,
    PostDetailView,
    PostDeleteView,
    informacion_personal,
)

app_name = 'blog'

urlpatterns = [
    path('post/list/', PostListView.as_view(), name='post_list'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),  # <- nombre corregido
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),         # <- nombre más claro
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),  # <- nombre coherente
    path('informacion/', informacion_personal, name='informacion_personal'),
]
