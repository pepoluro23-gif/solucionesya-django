from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from .forms import ServicioForm
from .models import Servicio


class HomeView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['ultimos'] = Servicio.objects.select_related('autor')[:3]
        return ctx


class AboutView(TemplateView):
    template_name = 'pages/about.html'


class ServicioListView(ListView):
    """Listado de servicios con buscador (?q=) y filtro por categoría (?categoria=)."""
    model = Servicio
    template_name = 'pages/servicio_list.html'
    context_object_name = 'servicios'
    paginate_by = 6

    def get_queryset(self):
        qs = Servicio.objects.select_related('autor')
        q = self.request.GET.get('q', '').strip()
        categoria = self.request.GET.get('categoria', '')
        if q:
            qs = qs.filter(Q(titulo__icontains=q) | Q(subtitulo__icontains=q) |
                           Q(contenido__icontains=q))
        if categoria:
            qs = qs.filter(categoria=categoria)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['q'] = self.request.GET.get('q', '')
        ctx['categoria'] = self.request.GET.get('categoria', '')
        ctx['categorias'] = Servicio.CATEGORIAS
        return ctx


class ServicioDetailView(DetailView):
    model = Servicio
    template_name = 'pages/servicio_detail.html'
    context_object_name = 'servicio'


class ServicioCreateView(LoginRequiredMixin, CreateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'pages/servicio_form.html'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        messages.success(self.request, 'Servicio publicado correctamente.')
        return super().form_valid(form)


class EsAutorMixin(UserPassesTestMixin):
    """Solo el autor (o un admin) puede editar o borrar una publicación."""

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.autor or self.request.user.is_superuser


class ServicioUpdateView(LoginRequiredMixin, EsAutorMixin, UpdateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'pages/servicio_form.html'

    def form_valid(self, form):
        messages.success(self.request, 'Servicio actualizado.')
        return super().form_valid(form)


class ServicioDeleteView(LoginRequiredMixin, EsAutorMixin, DeleteView):
    model = Servicio
    template_name = 'pages/servicio_confirm_delete.html'
    context_object_name = 'servicio'
    success_url = reverse_lazy('pages:lista')

    def form_valid(self, form):
        messages.success(self.request, 'Servicio eliminado.')
        return super().form_valid(form)


@login_required
def mis_servicios(request):
    """Vista basada en función con decorador: publicaciones del usuario logueado."""
    servicios = Servicio.objects.filter(autor=request.user)
    return render(request, 'pages/mis_servicios.html', {'servicios': servicios})
