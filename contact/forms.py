
from django import forms

from .models import ContactModel

class ContactForm(forms.Form):
	full_name = forms.CharField(widget=forms.TextInput(
														attrs={
																'class'				:		'form-control',
																'placeholder'		:		'Name'
																}
														)
	)

	phone_number = forms.CharField(widget=forms.NumberInput(
															attrs={
																	'class'			:		'form-control'
																	}
															)
	)

	email = forms.CharField(widget=forms.EmailInput(
													attrs={
															'class'				:		'form-control',
															 'placeholder'		:		'example@gmail.com'
															 }
													)
	)

	message = forms.CharField(widget=forms.Textarea(
													attrs={
															'class'				:		'form-control'
															}
													)
	)

	def clean_phone_number(self):
		phone_number = self.cleaned_data.get('phone_number')
		if len(phone_number) != 10:
			raise forms.ValidationError("Phone Number length should be 10")
		return phone_number
