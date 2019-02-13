
from django import forms

class SignInForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput())
	email = forms.CharField(widget=forms.EmailInput())
	password = forms.CharField(widget=forms.PasswordInput())
	password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput())

	# I can use style here (class:'form-control') but it make the sign in pag wired AF 

	def clean(self):
		data = self.cleaned_data

		password1 = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')

		if password2 != password1:
			raise forms.ValidationError('Password should match')

		return data


class SignInDetail(forms.Form):
	street_address = forms.CharField(widget=forms.TextInput())
	zip_code = forms.CharField(widget=forms.NumberInput())
	state = forms.CharField(widget=forms.TextInput())
	phone_number =  forms.CharField(widget=forms.NumberInput())


	def clean_phone_number(self):
		phone_number = self.cleaned_data.get('phone_number')
		if len(phone_number) != 10:
			raise forms.ValidationError('Input a valid Phone Number')
		return phone_number



class TryForm(forms.Form):
	email = forms.CharField(widget=forms.EmailInput())

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if not "gmail.com" in email:
			raise forms.ValidationError('gmail')
		return email

