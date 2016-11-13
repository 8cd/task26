from django.conf.urls import url
from .views import test, question_list, popular, question_detail, ask, answer

urlpatterns = [
	url(r'^$', question_list, name='index'),
	url(r'^popular/', popular, name='popular'),
	url(r'^question/(?P<pk>\d+)/', question_detail, name='question_detail'),
	url(r'^ask/', ask, name='ask'),
	url(r'^answer/', answer, name='answer'),
	#url(r'^ask/', test, name='ask'),
	#url(r'^new/', test, name='new'),
	#url(r'^login/', test, name='login'),
	#url(r'^signup/', test, name='signup'),
]