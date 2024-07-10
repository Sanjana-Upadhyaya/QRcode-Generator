# qrgenerator/urls.py

from django.urls import path
from .views import QRCodeView, ShareQRCodeView

urlpatterns = [
    path('', QRCodeView.as_view(), name='qrcode_home'),
    path('share/<int:qr_code_id>/', ShareQRCodeView.as_view(), name='share_qr_code'),
]
