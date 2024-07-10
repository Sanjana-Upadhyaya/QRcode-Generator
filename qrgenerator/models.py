from django.db import models

class QRCodeModel(models.Model):
    qr_code_data = models.TextField()
    qr_code_image = models.ImageField(upload_to='qr_codes/', default='qr_codes/default.png')
    created_at = models.DateTimeField(auto_now_add=True)
