from django import forms

class AddSlide(forms.Form):
	title 		= forms.CharField()
	description = forms.CharField(required=False)
	slide 	= forms.FileField()
	slide2 	= forms.FileField(required=False)
	slide3 	= forms.FileField(required=False)
	slide4 	= forms.FileField(required=False)
	slide5 	= forms.FileField(required=False)
	slide6	= forms.FileField(required=False)
	slide7 	= forms.FileField(required=False)
	slide8 	= forms.FileField(required=False)
	slide9 	= forms.FileField(required=False)
	slide10	= forms.FileField(required=False)