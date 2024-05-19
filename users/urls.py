from .import  views
from django.urls import path


urlpatterns = [
  path('register_seller', views.RegisterSellerView.as_view(), name="register_seller"),
  path('register_customer', views.RegisterCustomerView.as_view(), name="register_customer"),
  path('register_invester', views.RegisterInvesterView.as_view(), name="register_invester"),
  path('activate/<uidb64>/<token>', views.VerficationView.as_view(),name="activate"),
  path('login', views.LoginView.as_view(), name="login"),
  path('logout', views.LogoutView.as_view(), name="logout"),
  path('profile', views.ProfileView.as_view(), name="profile" )
]
