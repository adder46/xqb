from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import Http404
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    TemplateView,
    UpdateView,
)
from django.shortcuts import get_object_or_404
from django.urls import reverse

from notes.forms import NoteForm
from notes.models import Note


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        form.instance.save()
        form.save(commit=False)
        form.save_m2m()
        for tag in form.instance.tags.all():
            tag.mytag.added_by = self.request.user
            tag.mytag.save()
        return super().form_valid(form)

    def get_initial(self):
        return {'notebook': self.kwargs.get('notebook_pk')}

    def get_success_url(self):
        return reverse(
            'notes:note-list', kwargs={'notebook_pk': self.request.POST.get('notebook')}
        )

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = 'notes'

    def get_queryset(self):
        return Note.objects.filter(
            added_by=self.request.user, notebook=self.kwargs['notebook_pk']
        )

    def get_context_data(self, *args, **kwargs):
        ctx = {'notebook': self.kwargs['notebook_pk']}
        context = super().get_context_data(*args, **kwargs)
        context.update(ctx)
        return context


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name_suffix = '_update_form'

    def get_object(self):
        return get_object_or_404(
            Note, pk=self.kwargs['note_pk'], added_by=self.request.user
        )

    def get_success_url(self):
        return reverse(
            'notes:note-list', kwargs={'notebook_pk': self.request.POST.get('notebook')}
        )

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note

    def get_object(self):
        return get_object_or_404(
            Note, pk=self.kwargs['note_pk'], added_by=self.request.user
        )

    def get_success_url(self):
        return reverse(
            'notes:note-list', kwargs={'notebook_pk': self.kwargs['notebook_pk']}
        )


class ShowNoteView(TemplateView):
    template_name = 'notes/note_detail.html'

    def get_context_data(self, *args, **kwargs):
        try:
            pk = int(self.request.GET.get('pk'))
        except ValueError:
            raise Http404
        note = Note.objects.get(added_by=self.request.user, pk=pk)
        context = super().get_context_data(*args, **kwargs)
        context['note'] = note
        return context


class SearchNotesView(TemplateView):
    template_name = 'notes/searched_notes.html'

    def get_context_data(self, *args, **kwargs):
        search_query = self.request.GET.get('query')
        notebook = self.kwargs['notebook_pk']
        by = self.kwargs['by']
        if by == 'all':
            notes = Note.objects.filter(
                Q(title__icontains=search_query)
                | Q(description__icontains=search_query)
                | Q(tags__name__in=[search_query]),
                added_by=self.request.user,
                notebook=notebook,
            ).distinct()
        elif by == 'title':
            notes = Note.objects.filter(
                title__icontains=search_query,
                added_by=self.request.user,
                notebook=notebook,
            ).distinct()
        elif by == 'description':
            notes = Note.objects.filter(
                description__icontains=search_query,
                added_by=self.request.user,
                notebook=notebook,
            ).distinct()
        elif by == 'tags':
            notes = Note.objects.filter(
                tags__name__icontains=search_query,
                added_by=self.request.user,
                notebook=notebook,
            ).distinct()
        else:
            raise Http404
        context = super().get_context_data(*args, **kwargs)
        context['notes'] = notes
        return context

