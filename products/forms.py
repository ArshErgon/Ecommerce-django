
from django import forms

class ReviewForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(
												attrs={
														'class'				:			'form-control',
														'placeholder'		:			'Your name'
														}
												)
	)

	user_review = forms.CharField(widget=forms.Textarea(
														attrs={
																'class'			:		'form-control', 
																'placeholder'	:		'make it to the point'
																}
														)
	)

	def clean_name(self):
		name = self.cleaned_data.get('name')
		if len(name) < 5:
			raise forms.ValidationError("Name should not be greater than 5 letters, Sorry but it is important :)")
		return name
