from django import forms

class AddSlide(forms.Form):
	title 		= forms.CharField()
	description = forms.CharField(required=False)
	slide 	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['ppt', 'pptx', 'pps']
												)])
	slide2 	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['ppt', 'pptx', 'pps']
												)], required=False)
	slide3 	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['ppt', 'pptx', 'pps']
												)], required=False)
	slide4 	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['ppt', 'pptx', 'pps']
												)], required=False)
	slide5 	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['ppt', 'pptx', 'pps']
												)], required=False)
	slide6	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['ppt', 'pptx', 'pps']
												)], required=False)
	slide7 	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['ppt', 'pptx', 'pps']
												)], required=False)
	slide8 	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['ppt', 'pptx', 'pps']
												)], required=False)
	slide9 	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['ppt', 'pptx', 'pps']
												)], required=False)
	slide10	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['ppt', 'pptx', 'pps']
												)], required=False)