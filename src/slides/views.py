from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from slide_viewer.settings import CDN_DOMAIN

from .models import Slide, SlideUpload
from .forms import AddSlide


@login_required()
def add_slides(request):
	form = AddSlide(request.POST or None, request.FILES or None)
	errors = None
	if form.is_valid():
		if request.user.is_authenticated():
			
			# saving the details in the db
			obj = Slide.objects.create(
					title = form.cleaned_data.get('title'), 
					description = form.cleaned_data.get('description'),
					uploaded_by = request.user
				)

			# uploading the first slide with same id
			query = Slide.objects.latest('id')
			obj = SlideUpload.objects.create(
					slide_id = query.id,
					name = form.cleaned_data.get('title'),
					slide_url = form.cleaned_data.get('slide'),
				)

			# looping through all other slides and uploading with same id
			for i in range(2,11):
				extra = 'slide' + str(i)
				if (str(form.cleaned_data.get(extra)) != 'None'):
					obj = SlideUpload.objects.create(
						slide_id = query.id,
						name = form.cleaned_data.get('title'), 
						slide_url = form.cleaned_data.get(extra),
					)
			return redirect('slides:view')
			
	if form.errors:
		errors = form.errors

	template_name = 'slides/add_slides.html'
	context = {"form":form, "errors":errors}
	return render(request, template_name, context)


def display_slides(request):
	template_name = 'slides/display_slides.html'
	
	# querying Slide table from db
	queryset1 = Slide.objects.all().order_by('-pk')
	
	# querying SlideUpload table from db
	queryset2 = SlideUpload.objects.all()

	# domain of CDN where the slides will be uploaded
	cdn = CDN_DOMAIN

	context = {"object_list": queryset1, "slide_list":queryset2, "cdn":cdn}
	return render(request, template_name, context)


@login_required()
def user_slides(request):
	template_name = 'slides/user_slides.html'
	
	# querying Slide table from db
	queryset1 = Slide.objects.filter(uploaded_by=request.user).order_by('-pk')
	
	# querying SlideUpload table from db
	queryset2 = SlideUpload.objects.all()

	# domain of CDN where the slides will be uploaded
	cdn = CDN_DOMAIN

	context = {"object_list": queryset1, "slide_list":queryset2, "cdn":cdn}
	return render(request, template_name, context)


@login_required()
def delete_slide(request, pk):
	# querying Slide table from db to get single row and deleting it
	instance1 = get_object_or_404(Slide, pk=pk).delete()
	instance2 = SlideUpload.objects.filter(slide_id=pk).delete()

	messages.success(request, "Successfully deleted the slides")
	return redirect('slides:user_sld')