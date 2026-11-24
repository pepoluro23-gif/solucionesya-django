from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import PerfilForm, RegistroForm, UsuarioForm
from .models import Perfil


class RegistroView(CreateView):
    form_class = RegistroForm
    template_name = 'accounts/registro.html'
    success_url = reverse_lazy('accounts:perfil')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)  # queda logueado después de registrarse
        messages.success(self.request, '¡Cuenta creada! Completá tu perfil.')
        return response


class IngresoView(LoginView):
    template_name = 'accounts/login.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field in form.fields.values():
            field.widget.attrs['class'] = 'form-control'
        return form


class PerfilView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/perfil.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        Perfil.objects.get_or_create(usuario=self.request.user)
        return ctx


@login_required
def editar_perfil(request):
    perfil, _ = Perfil.objects.get_or_create(usuario=request.user)
    if request.method == 'POST':
        u_form = UsuarioForm(request.POST, instance=request.user)
        p_form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Perfil actualizado.')
            return redirect('accounts:perfil')
    else:
        u_form = UsuarioForm(instance=request.user)
        p_form = PerfilForm(instance=perfil)
    return render(request, 'accounts/editar_perfil.html',
                  {'u_form': u_form, 'p_form': p_form})


class CambiarPasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'accounts/cambiar_password.html'
    success_url = reverse_lazy('accounts:perfil')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field in form.fields.values():
            field.widget.attrs['class'] = 'form-control'
        return form

    def form_valid(self, form):
        messages.success(self.request, 'Contraseña actualizada.')
        return super().form_valid(form)
