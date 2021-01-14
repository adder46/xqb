from django.urls import path

from notebooks.views import (
    NotebookCreateView,
    NotebookDeleteView,
    NotebookListView,
    NotebookUpdateView,
    SearchNotebooksView,
)


app_name = 'notebooks'
urlpatterns = [
    path('', NotebookListView.as_view(), name='notebook-list'),
    path('create/', NotebookCreateView.as_view(), name='notebook-create'),
    path('<int:notebook_pk>/delete/', NotebookDeleteView.as_view(), name='notebook-delete'),
    path('<int:notebook_pk>/update/', NotebookUpdateView.as_view(), name='notebook-update'),
    path('ajax/search/', SearchNotebooksView.as_view(), name='search-notebooks'),
]
