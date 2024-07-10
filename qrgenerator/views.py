# qrgenerator/views.py

from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from .forms import QRCodeForm
from .models import QRCodeModel
from io import BytesIO
import qrcode
import base64
import os
from django.conf import settings
from pathlib import Path

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    return buffer.getvalue()

class QRCodeView(View):
    def get(self, request):
        form = QRCodeForm()
        return render(request, 'qrgenerator/qrcode.html', {'form': form})

    def post(self, request):
        form = QRCodeForm(request.POST)
        if form.is_valid():
            qr_text = form.cleaned_data['qr_text']
            qr_code_data = base64.b64encode(generate_qr_code(qr_text)).decode()
            qr_code = QRCodeModel.objects.create(qr_code_data=qr_code_data)

            # Save the QR code image to a file
            qr_code_image_data = generate_qr_code(qr_text)
            file_path = Path(settings.MEDIA_ROOT) / 'qr_codes' / f'qr_{qr_text}.png'
            os.makedirs(file_path.parent, exist_ok=True)
            with open(file_path, 'wb') as f:
                f.write(qr_code_image_data)
            
            qr_code.qr_code_image = f'qr_codes/qr_{qr_text}.png'
            qr_code.save()

            qr_code_image_url = request.build_absolute_uri(settings.MEDIA_URL + str(qr_code.qr_code_image))

            return render(request, 'qrgenerator/qrcode.html', {
                'form': form,
                'qr_code_data': 'data:image/png;base64,' + qr_code_data,
                'qr_code_id': qr_code.id,
                'qr_code_image_url': qr_code_image_url,
                'share_url': reverse('share_qr_code', args=[qr_code.id])
            })
        return render(request, 'qrgenerator/qrcode.html', {'form': form})

class ShareQRCodeView(View):
    def get(self, request, qr_code_id):
        qr_code = get_object_or_404(QRCodeModel, id=qr_code_id)
        qr_code_image_url = request.build_absolute_uri(settings.MEDIA_URL + str(qr_code.qr_code_image))
        return render(request, 'qrgenerator/share.html', {
            'qr_code_data': 'data:image/png;base64,' + qr_code.qr_code_data,
            'qr_code_image_url': qr_code_image_url,
        })
