from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import BlogModel
from django.views.generic import ListView, DetailView, CreateView
from .forms import CommentForm


class BlogListView(ListView):
    template_name = 'main/blog.html'
    queryset = BlogModel.objects.all()


class BlogDetailView(DetailView):
    template_name = 'main/blog-details.html'
    model = BlogModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class CommentCreateView(CreateView):
    template_name = 'main/blog-details.html'
    form_class = CommentForm

    def form_valid(self, form):
        blog = get_object_or_404(BlogModel, id=self.kwargs.get('pk'))
        form.instance.blog = blog
        form.instance.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blogs:detail', kwargs={'pk': self.kwargs.get('pk')})
