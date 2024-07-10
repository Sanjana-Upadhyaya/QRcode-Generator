"""
URL configuration for qrcode_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from qrgenerator.views import QRCodeView, ShareQRCodeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', QRCodeView.as_view(), name='qr_code'),
    path('share/<int:qr_code_id>/', ShareQRCodeView.as_view(), name='share_qr_code'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)