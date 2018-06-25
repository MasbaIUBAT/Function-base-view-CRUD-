from django.forms import ModelForm, TextInput, Textarea
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = '__all__'
		widget = {
			'name': TextInput(attrs={'class':'form-control'}),
			'comment': Textarea(attrs={'class':'form-control'}),
		}
   