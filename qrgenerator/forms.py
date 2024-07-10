from django import forms

class QRCodeForm(forms.Form):
    qr_text = forms.CharField(label='QR Text', max_length=200)
