from django import forms
from .models import Entreprenuership, Ict, Subject, Course, Profile
from django.contrib.auth.models import User



class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)
	
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')
	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError('Passwords don\'t match.')
		return cd['password2']	


class UserEditForm(forms.ModelForm):
	
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')



class ProfileEditForm(forms.ModelForm):
	options = [('Male','Male'),('Female','Female')]
	gender = forms.ChoiceField(choices=options)

	class Meta:
		model = Profile
		fields = ('gender','phone_number', 'home_address')



class feedbackForm(forms.ModelForm):
	options =[('1','1'),('2','2'),('3','3'),
	('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10')]

	question_4 = forms.ChoiceField(label='4. Rate the class from 1-10', choices=options)
	
	class Meta:
		model = Entreprenuership

		fields = ('course_title','question_1', 'question_2', 'question_3', 'question_4')


		labels = {'course_title':'Course',
				'question_1':'1. How can you describe the class?',
				'question_2': '2. Are you satisfied with the course?',
				'question_3':'3. How can you describe the facilitator delivery and facilitation?'
				}





class ictFeedback(forms.ModelForm):
	options = [
	('Strongly Agree','Strongly Agree'), 
	('Agree','Agree'), 
	('Neutral','Neutral'), 
	('Disagree','Disagree'),
	 ('Strongly Disagree','Strongly Disagree')
	 ]

	question_1 = forms.ChoiceField(label="1. I will be able to apply the knowledge learned.", choices=options, widget=forms.RadioSelect())
	question_2 = forms.ChoiceField(label="2. Are you satisfied with the course?", choices=options, widget=forms.RadioSelect())
	question_3 = forms.ChoiceField(label="3. The training objectives for each topic were identified and followed.", choices=options, widget=forms.RadioSelect())
	question_4 = forms.ChoiceField(label="4. The content was organized and easy to follow.", choices=options, widget=forms.RadioSelect())
	question_5 = forms.ChoiceField(label="5. The trainer was knowledgeable.", choices=options, widget=forms.RadioSelect())
	question_6 = forms.ChoiceField(label="6. The quality of instruction was good.", choices=options, widget=forms.RadioSelect())
	question_7 = forms.ChoiceField(label="7. Class participation and interaction were encouraged.", choices=options, widget=forms.RadioSelect())
	
	


	class Meta:
		model = Ict
		fields = ('course_title','question_1', 'question_2', 'question_3',
		 'question_4', 'question_5', 'question_6', 'question_7', 'question_8', 'question_9')


		labels = {'course_title':'Course',
				'question_8':'8. How can you describe the class?',
				'question_9':'9. In your own word how can you describe the facilitator delivery and facilitation?'}

