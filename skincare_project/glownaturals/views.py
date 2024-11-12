from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, TemplateView
from .models import Producto
from glownaturals.forms import ProductoForm

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'crear_producto.html'
    success_url = '/productos/'

class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'editar_producto.html'
    success_url = '/productos/'

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'eliminar_producto.html'
    success_url = '/productos/'

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'ver_producto.html'


class IndexView(TemplateView):
    template_name = 'index.html'
