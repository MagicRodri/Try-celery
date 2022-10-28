

from django import forms

from equations.models import Calculation


class CalculationForm(forms.ModelForm):

    class Meta:
        model = Calculation
        fields = ['input']