from django.http import HttpResponse
from django.db.models import Q
from django.views.generic import View, ListView, TemplateView, CreateView
from examplemodel.models import ExampleModel1, ExampleModel2, ExampleModel3, ExampleModel4, ExampleModel5
from examplemodel.forms import ExampleForm


class ExampleListView(ListView):
	model = ExampleModel4
	template_name = 'examplemodel4_list.html'

	def get_queryset(self):
		return ExampleModel4.objects.filter(Q(genericipaddressfield="127.0.0.1") | Q(nullbooleanfield=True))


class CreatePost(CreateView):
	model = ExampleModel4
	form_class = ExampleForm
	template_name = 'exampleform_list.html'
	success_url = '/'


class ExampleView(View):
	def get(self, request, *args, **kwards):
		return HttpResponse("Hello, it`s an example View")


class ExampleTemplateView(TemplateView):
	template_name = 'examplemodel_list.html'