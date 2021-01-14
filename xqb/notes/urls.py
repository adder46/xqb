from django.urls import path

from notes.views import (
    NoteCreateView,
    NoteDeleteView,
    NoteListView,
    NoteUpdateView,
    SearchNotesView,
    ShowNoteView,
)


app_name = 'notes'
urlpatterns = [
    path('<int:notebook_pk>/', NoteListView.as_view(), name='note-list'),
    path('create/', NoteCreateView.as_view(), name='note-create'),
    path('<int:notebook_pk>/create/', NoteCreateView.as_view(), name='note-create'),
    path('<int:notebook_pk>/<int:note_pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),
    path('<int:notebook_pk>/<int:note_pk>/update/', NoteUpdateView.as_view(), name='note-update'),
    path('ajax/show-note/', ShowNoteView.as_view(), name='show-note'),
    path('ajax/search/<int:notebook_pk>/<str:by>/', SearchNotesView.as_view(), name='search-notes'),
]
