from django import forms
from .models import ExampleModel4


class ExampleForm(forms.ModelForm):
	class Meta:
		model = ExampleModel4
		fields = ['genericipaddressfield', 'nullbooleanfield', 'positiveintegerfield', 'positivesmallintegerfield', 'slugfield']
		labels = {'genericipaddressfield': 'IP address', 'positiveintegerfield': '>0', 'positivesmallintegerfield': '>0', 'slugfield': 'Input something'}