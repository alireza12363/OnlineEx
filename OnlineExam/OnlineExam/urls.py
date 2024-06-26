"""OnlineExam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from django_registration.backends.one_step.views import RegistrationView
from django.contrib.auth import views as auth_views
from OnlineExam.forms import CustomAdminLogin
from users.forms import CustomUserForm, CustomLoginForm
from core.views import IndexTemplateView


admin.site.login_form = CustomAdminLogin

urlpatterns = [
    path('exam-management/', admin.site.urls),
    path("accounts/login/", auth_views.LoginView.as_view(
        authentication_form = CustomLoginForm,)),

    # path('accounts/register/', RegistrationView.as_view(
    #     form_class = CustomUserForm,
    #     success_url = '/',
    # ), name="django_registration_register"),

    path('accounts/', include('django.contrib.auth.urls')),
    path('captcha/', include('captcha.urls')),
    # path('accounts/', include('django_registration.backends.one_step.urls')),

    # path('api/rest-auth/', include('rest_auth.urls')),

    path('api/', include('users.api.urls')),

    path('api/', include('exam_sessions.api.urls')),

    path('api/<session_ref>/', include('questions.api.urls')),

    path('api-auth/', include('rest_framework.urls')),


    # path('api/rest-auth/registration/', 
    #     include('rest_auth.registration.urls')),

    path('exam-sessions/', include('exam_sessions.urls')),
    
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),

    re_path(r"^.*$", IndexTemplateView.as_view(), name="entry_point")

]

# if settings.DEBUG:
urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + urlpatterns
urlpatterns = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + urlpatterns


admin.site.site_header = 'Online Examination System'
