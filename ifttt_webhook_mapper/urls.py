"""ifttt_webhook_mapper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from webhook_mapper.views import make_post_request_to_webhook, fulfill_webhook_mapping

urlpatterns = [
    path('admin/', admin.site.urls),
    path("m/<str:tag>/", make_post_request_to_webhook),
    path("_f/<str:tag>/", fulfill_webhook_mapping),
]
