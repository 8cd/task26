from django import forms
from qa.models import Question, Answer

class AskForm(forms.Form):
	title = forms.CharField(max_length=50)
	text = forms.CharField(widget=forms.Textarea)

	def clean(self):
		return self.cleaned_data

	def save(self):
		self.cleaned_data['author'] = self._user
		return Question.objects.create(**self.cleaned_data)


class AnswerForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
	question = forms.IntegerField(widget=forms.HiddenInput)

	def clean(self):
		return self.cleaned_data

	def save(self):
		self.cleaned_data['author'] = self._user
		self.cleaned_data['question'] = Question.objects.get(pk=self._question)
		return Answer.objects.create(**self.cleaned_data)