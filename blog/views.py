from django.views.generic import FormView
from django.core.paginator import Paginator

from .models import Blog, FormBlog


class BlogIndex(FormView):
    form_class = FormBlog
    template_name = 'blog/index.html'
    success_url = '/'
    paginate = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        list_blog = Blog.objects.filter(state=True).order_by('-created')
        paginator = Paginator(list_blog, self.paginate)
        page = self.request.GET.get('page')
        context['object_list'] = paginator.get_page(page)
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

