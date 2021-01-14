from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    TemplateView,
    UpdateView,
)

from notebooks.models import Notebook


class NotebookCreateView(LoginRequiredMixin, CreateView):
    model = Notebook
    fields = ['name']

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('notebooks:notebook-list')


class NotebookListView(LoginRequiredMixin, ListView):
    model = Notebook
    context_object_name = 'notebooks'

    def get_queryset(self):
        return Notebook.objects.filter(added_by=self.request.user)


class NotebookUpdateView(LoginRequiredMixin, UpdateView):
    model = Notebook
    fields = [
        'name',
    ]
    template_name_suffix = '_update_form'

    def get_object(self):
        return get_object_or_404(
            Notebook, pk=self.kwargs['notebook_pk'], added_by=self.request.user
        )

    def get_success_url(self):
        return reverse('notebooks:notebook-list')


class NotebookDeleteView(LoginRequiredMixin, DeleteView):
    model = Notebook

    def get_object(self):
        return get_object_or_404(
            Notebook, pk=self.kwargs['notebook_pk'], added_by=self.request.user
        )

    def get_success_url(self):
        return reverse('notebooks:notebook-list')


class SearchNotebooksView(TemplateView):
    template_name = 'notebooks/searched_notebooks.html'

    def get_context_data(self, *args, **kwargs):
        search_query = self.request.GET.get('query')
        notebooks = Notebook.objects.filter(
            name__icontains=search_query, added_by=self.request.user
        )
        context = super().get_context_data(*args, **kwargs)
        context['notebooks'] = notebooks
        return context
