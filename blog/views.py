from django.views.generic import FormView

from .models import Blog, FormBlog


class BlogIndex(FormView):
    form_class = FormBlog
    template_name = 'blog/index.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_message'] = Blog.objects.filter(state=True).order_by('-created')
        return context
