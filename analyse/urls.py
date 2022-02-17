from django.urls import path
from analyse import views
from .views import TableView,LearningView

app_name = 'analyse'
urlpatterns = [
    path('',views.index,name='index'),
    # path('tables/' ,views.tables,name='tables'),
    path('tables/',TableView.as_view(),name='tables'),
    path('chart/company/' ,views.company,name='company'),
    path('chart/financing/' ,views.financing,name='financing'),
    path('chart/district/' ,views.district,name='district'),
    path('wordCloud/welfare/' ,views.welfare,name='welfare'),
    path('wordCloud/posts/' ,views.posts,name='posts'),
    path('basic/salary/' ,views.salsry,name='salary'),
    path('basic/degree/' ,views.degree,name='degree'),
    path('basic/experience/' ,views.experience,name='experience'),
    path('search/table/' , views.search,name='search'),
    path('learning/',views.learning,name='learning'),
    path('resource/',LearningView.as_view(),name='resource'),

]