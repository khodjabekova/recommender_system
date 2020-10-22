from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Product, Review
from .forms import ProductForm, ReviewForm


class ProductList(ListView):
    model = Product

    def get_queryset(self):
        return Product.objects.all()


class ProductDetail(DetailView):
    model = Product


class CreateProduct(CreateView):
    form_class = ProductForm
    model = Product
    redirect_field_name = 'products/product_detail.html'

    def form_valid(self, form):
        #self.object = form.save(commit=False)
        self.object.image = self.request.FILES
        self.object.save()
        return super().form_valid(form)



class UpdateProduct(UpdateView):
    model = Product
    fields = ['title', 'text', 'image']
    template_name_suffix = '_update'

class DeleteProduct(DeleteView):
    model = Product
    success_url = reverse_lazy('products:all')
    template_name = 'products/product_confirm_delete.html'

    def delete(self, *args, **kwargs):
        messages.success(self.request, 'Product Deleted')
        return super().delete(*args, **kwargs)


@login_required
def add_review_to_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.product = product
            review.save()
            return redirect('products:detail', pk=product.pk)
    else:
        form = ReviewForm 
    return render(request, 'products/review_form.html', {'form': form})


@login_required
def review_remove(request, pk):
    review = get_object_or_404(Review, pk=pk)
    product_pk = review.product.pk
    review.delete()
    return redirect('products:detail', pk=product_pk)