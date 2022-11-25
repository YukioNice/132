from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product, Category


class HomePageView(TemplateView):
    template_name = 'index.html'

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_new.html'
    fields = '__all__'

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_edit.html'
    fields = '__all__'

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')

class CategoryListView(ListView):
    model = Category
    template_name = 'master_list.html'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'master_detail.html'

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'master_new.html'
    fields = '__all__'

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'master_edit.html'
    fields = '__all__'

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'master_delete.html'
    success_url = reverse_lazy('haircut_list')