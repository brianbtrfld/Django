from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    #path(route = '', view = views.index, kwargs = '', name = 'index'),

    # ex: /polls/5/
    #path(route = 'detail/<int:question_id>/', view = views.detail, name = 'detail'),

    # ex: /polls/5/results/
    #path(route = '<int:question_id>/results/', view = views.results, name = 'results'),

    # ex: /polls/5/vote/
    #path(route = '<int:question_id>/vote/', view = views.vote, name = 'vote')

    path('', views.IndexView.as_view(), name = 'index'),
    path('<int:pk>/', views.DetailView.as_view(), name = 'detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name = 'results'),
    path('<int:question_id>/vote/', views.vote, name = 'vote'),
]