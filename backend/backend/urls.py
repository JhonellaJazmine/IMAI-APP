"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from web import views
from rest_framework import routers
from web.views import UserRegistrationAPIView, UserLoginAPIView, UserViewAPI, UserLogoutViewAPI
from web.views import UserListView, BranchAdminRegistrationView, BranchPersonnelRegistrationView

router = routers.DefaultRouter()
router.register(r'companies', views.CompanyViewSet)
router.register(r'branches', views.BranchViewSet)
router.register(r'suppliers', views.SupplierViewSet)
router.register(r'brands', views.BrandViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'carts', views.CartViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('api/', include('web.urls')),

    # Include your user authentication endpoints here
    path('user/register/', UserRegistrationAPIView.as_view(), name='user-register'),
    path('user/login/', UserLoginAPIView.as_view(), name='user-login'),
    path('user/', UserViewAPI.as_view(), name='user-view'),
    path('user/logout/', UserLogoutViewAPI.as_view(), name='user-logout'),
    path('users/', UserListView.as_view(), name='user-list'),

    path('create-branch-admin/', BranchAdminRegistrationView.as_view(), name='create-branch-admin'),
    path('create-branch-personnel/', BranchPersonnelRegistrationView.as_view(), name='create-branch-admin'),

]
