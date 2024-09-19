#

from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.index, name='site_index'),
	path('persons/', views.PersonsList.as_view(), name='persons'),
	path('persons/<int:pk>/', views.PersonDetail.as_view(), name='person'),
]