from django.shortcuts import render
from django.http import HttpResponse
from .models import  Course, Entreprenuership, Subject, Ict, Profile
from .forms import feedbackForm, ictFeedback, UserRegistrationForm, UserEditForm, ProfileEditForm 
from django.contrib.auth.decorators import login_required




# Create your views here.

#Registration page
def register(request):
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
			# Create a new user object but avoid saving it yet
			new_user = user_form.save(commit=False)
			# Set the chosen password
			new_user.set_password(user_form.cleaned_data['password'])
			# Save the User object
			new_user.save()
			# Create the user profile
			Profile.objects.create(user=new_user)
			return render(request, 'registration_done.html', {'new_user': new_user})
	else:
		user_form = UserRegistrationForm()
	return render(request, 'register.html', {'user_form': user_form})






#Edit page
@login_required
def edit(request):
	if request.method == 'POST':
		user_form = UserEditForm(instance=request.user, data=request.POST)
		profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
		
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			return render(request, 'profile.html')
	else:
		user_form = UserEditForm(instance=request.user)
		profile_form = ProfileEditForm(instance=request.user.profile)

	return render(request,'edit_profile.html',{'user_form': user_form, 'profile_form': profile_form})

# home page
@login_required
def index(request):
	course_title = Course.objects.all( )
	return render(request, 'index.html', {'section': 'index','course_title':course_title})


#profile page
@login_required
def profile(request):
	profile = Profile.objects.all()
	return render(request,'profile.html', {'profile': profile})


# view page for feeback response 
@login_required
def feedback(request):
	ict = Course.objects.filter( subject_id=1)
	entreprenuership = Course.objects.filter( subject_id=2)
	return render(request, 'feedback.html', {'ict':ict, 'entreprenuership':entreprenuership})


# page for submitting entreprenuership feedback
@login_required
def entrepreneurship(request):
	form = feedbackForm()
	form.fields["course_title"].queryset = Course.objects.filter(subject_id=2)

	if request.method == 'POST':
		form = feedbackForm(request.POST)
		
		if form.is_valid:
			form.save()
			return render(request, 'Thank_you.html')
	
	return render(request, 'entrepreneurship.html', {'form':form})


# page for submitting ICT feedback
@login_required
def ict(request):
	form = ictFeedback()
	form.fields["course_title"].queryset = Course.objects.filter(subject_id=1)
	if request.method == 'POST':
		form = ictFeedback(request.POST)
		
		if form.is_valid:
			form.save()
			return render(request, 'Thank_you.html')

	return render(request, 'ict.html', {'form':form})


# view page for ict feeback submitted by user
@login_required
def ict_feedback(request, course_id):
	response = Ict.objects.filter(course_title_id=course_id)
	course = Course.objects.filter(id=course_id)

	return render(request, 'ict_feedback.html', {'response':response, 'course':course })


# view page for ict Entreprenuership submitted by user
@login_required
def entreprenuership_feedback(request, course_id):
	response = Entreprenuership.objects.filter(course_title_id=course_id)
	course = Course.objects.filter(id=course_id)

	return render(request, 'entreprenuership_feedback.html', {'response':response, 'course':course })




