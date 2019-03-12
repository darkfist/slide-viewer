from django import forms
from django.core.validators import FileExtensionValidator


class AddSlide(forms.Form):
	title 		= forms.CharField()
	description = forms.CharField(required=False)
	slide 	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['odp', 'fodp']
												)])
	slide2 	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['odp', 'fodp']
												)], required=False)
	slide3 	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['odp', 'fodp']
												)], required=False)
	slide4 	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['odp', 'fodp']
												)], required=False)
	slide5 	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['odp', 'fodp']
												)], required=False)
	slide6	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['odp', 'fodp']
												)], required=False)
	slide7 	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['odp', 'fodp']
												)], required=False)
	slide8 	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['odp', 'fodp']
												)], required=False)
	slide9 	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['odp', 'fodp']
												)], required=False)
	slide10	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['odp', 'fodp']
												)], required=False)