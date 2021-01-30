from django.urls import path, include
from rest_framework.authtoken import views

from .views import home

urlpatterns = [
    path("", home, name="home_view"),
    path("category", include("api.category.urls")),
    path("products", include("api.product.urls")),
    path("orders", include("api.order.urls")),
    path('user/', include('api.user.urls')),
    path('api-token-auth/', views.obtain_auth_token, name='api_token_auth'),
    
]