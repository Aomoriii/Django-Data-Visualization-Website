from django.urls import path
from analyse import views
from .views import TableView, LearningView, IndexView, LearningRecommendView

app_name = 'analyse'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('tables/', TableView.as_view(), name='tables'),
    path('chart/company/', views.company, name='company'),
    path('wordCloud/welfare/', views.welfare, name='welfare'),
    path('basic/salary/', views.salary, name='salary'),
    path('basic/degree/', views.degree, name='degree'),
    path('search/table/', views.search, name='search'),
    path('learning', LearningRecommendView.as_view(), name='learning'),
    path('resource/', LearningView.as_view(), name='resource'),
]