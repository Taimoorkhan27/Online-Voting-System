from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
   path('', views.index, name='index'),
   path('question/<int:question_id>/', views.detail, name='detail'),
   path('question/<int:question_id>/results/', views.results, name='results'),
   path('question/<int:question_id>/vote/', views.vote, name='vote'),
   path('homepage/', views.homepage, name='homepage'),
]