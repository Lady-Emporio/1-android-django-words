
from .models import *
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView

class WordView(DetailView):
	model=Word
	template_name = 'word.html'
	context_object_name="MyOb"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class WordView_List(ListView):
	model=Word
	template_name = 'wordsList.html'
	context_object_name="MyObs"
	paginate_by = 5  # if pagination is desired
	def get_queryset(self):
		 return Word.objects.all()
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

#https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/
from django.forms import ModelForm
class WordForm(ModelForm):
	class Meta:
		model = Word
		fields ="__all__"

class WordUpdate(UpdateView):
	model=Word
	form_class=WordForm
	success_url="/"
	template_name = 'word.html'
	context_object_name="MyOb"
	def get_context_data(self, **kwargs):
		return super().get_context_data(**kwargs)