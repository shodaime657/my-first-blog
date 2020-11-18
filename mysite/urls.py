from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('admin/', admin.site.urls),
  path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
  path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),
  path('', include('blog.urls')),
]
