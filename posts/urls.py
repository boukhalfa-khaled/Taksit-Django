from django.urls import path
from . import views


urlpatterns = [
  # path('', .as_view(), name=""),
  # path('create_post/',CreatePostView.as_view(), name="create_post")  
  path('',views.posts, name="posts"),
  path('invester-market',views.investerMarket, name="invester-market"),
  path('create_post/',views.create_post, name="create_post"),
  path('<int:post_id>/', views.post_detail, name='post_detail'),
  path('create-order/<int:post_id>/', views.create_order, name='create_order'),
]