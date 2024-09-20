from django.urls import path
from test_api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippets/', views.SnippetList.as_view(), name='snippets_list'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippets_detail'),
    path('persons/', views.PersonList.as_view(), name='persons_list'),
    path('persons/<int:pk>/', views.PersonDetail.as_view(), name='persons_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)