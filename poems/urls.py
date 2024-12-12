from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.create_poem, name='add_poem'),  # Update here to match create_poem
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('poem_list/', views.poem_list, name='poem_list'),
    path('poem/<int:pk>/', views.poem_detail, name='poem_detail'),
    path('poem/new/', views.create_poem, name='create_poem'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/add/', views.add_to_wishlist, name='wishlist_add'),
    path('poem/<int:poem_id>/add_to_wishlist/', views.add_to_wishlist, name='add_to_wishlist'),
    path('poem/<int:pk>/remove_from_wishlist/', views.remove_from_wishlist, name='remove_from_wishlist'),
]
