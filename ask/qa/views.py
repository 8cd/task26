# Create your views here.
from django.core.paginator import Paginator, EmptyPage
from django.core.urlresolvers import reverse
from .models import Question
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from qa.forms import AskForm, AnswerForm
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST

def paginate(request, qs):
	try:
		limit = int(request.GET.get('limit', 10))
	except ValueError:
		limit = 10
	if limit > 100:
		limit = 10

	try:
		page = int(request.GET.get('page', 1))
	except ValueError:
		raise Http404

	paginator = Paginator(qs, limit)

	try:
		page = paginator.page(page)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)
	return page, paginator


def test(request, *args, **kwargs):
	return HttpResponse('OK')

def question_list(request):
	#qs = Question.objects.all()
	#qs = qs.order_by('-added_at')
	qs = Question.objects.new()
	page, paginator = paginate(request, qs)
	paginator.baseurl = reverse('index') + '?page='

	return render(request, 'index.html', {
		'questions': page.object_list,
		'page': page,
		'paginator': paginator,
	})

def popular(request):
	#qs = Question.objects.all()
	#qs = qs.order_by('-rating')
	qs = Question.objects.popular()
	page, paginator = paginate(request, qs)
	paginator.baseurl = reverse('popular') + '?page='

	return render(request, 'popular.html', {
		'questions': page.object_list,
		'page': page,
		'paginator': paginator,
	})	


@csrf_exempt

def question_detail(request, pk):
	if request.method is 'POST':
		return answer(request)
	question = get_object_or_404(Question, id=pk)
	answers = question.answer_set.all()

	form = AnswerForm()
	return render(request, 'question.html', {'question': question,'answers': answers, 'form':form,})	

			

def ask(request):
	author = User.objects.get(id='1')
	if request.method == 'POST':
		form = AskForm(request.POST)
		if form.is_valid():
			form._user = author
			q = form.save()
			return HttpResponseRedirect(q.get_absolute_url())
	else:
		form = AskForm()
		return render(request, 'ask.html', {'form': form,})

def answer(request):
	author = User.objects.get(id='1')
	if request.method == 'POST':
		form = AnswerForm(request.POST)
		if form.is_valid():
			form._user = author
			form._question = request.POST.get('question')
			q = form.save()
			return HttpResponseRedirect(q.get_absolute_url())
