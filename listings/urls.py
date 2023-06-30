from django.urls import path
from .views import ( home, retrieve, update, register,
                    create, delete, login_view, logout, contact )


urlpatterns = [
    path('', home, name='home'),
    path('lists/<int:pk>/', retrieve, name='retrieve'),
    path('create-listing/', create, name='create'),
    path('listings/<int:pk>/edit/', update, name='update'),
    path('listings/<int:pk>/delete/', delete, name='delete'),
    path('register', register, name='register'),
    path('login', login_view, name='login'),
    path('logout', logout, name='logout'),
    path('contact', contact, name='contact'),
]
