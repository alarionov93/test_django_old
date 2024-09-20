#

from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.index, name='site_index'),
	path('persons/', views.PersonsList.as_view(), name='persons'),
	path('persons/<int:pk>/', views.PersonDetail.as_view(), name='person'),
	path('persons/<int:pk>/update/', views.PersonUpdate.as_view(), name='person_update'),
]