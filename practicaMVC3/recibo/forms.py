
from django import forms

from . models import Recibo

class reciboForm(forms.ModelForm):
    class Meta:
        model=Recibo
        fields=('numRecibo','fechaPago','cantidad','cliente','concepto',)
