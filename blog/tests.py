from django.test import TestCase, Client

from .models import Blog, FormBlog


class BlogObject(object):
    """Model setup blog"""
    def setUp(self):
        self.obj1 = Blog.objects.create(text="Object1")


class TestBlogModel(BlogObject, TestCase):
    """Тест для модели блога"""
    def setUp(self):
        super().setUp()
        self.obj2 = Blog.objects.create(text='No visible', state=False)

    def test_create_blog(self):
        obj = Blog.objects.create(text='test')
        self.assertEqual(obj.text, 'test')

    def test_blog(self):
        self.assertEqual(self.obj1.text, 'Object1')

    def test_filtered_obj(self):
        self.assertFalse(self.obj2.state)

    def test_state_blog(self):
        self.assertTrue(self.obj1.state)


class TestBlogView(BlogObject, TestCase):
    """Тест для шалона блога"""
    def setUp(self):
        super().setUp()
        self.c = Client()

    def test_blog_view(self):
        resp = self.c.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_form(self):
        form = FormBlog({'text':'TESTFORM'})
        self.assertTrue(form.is_valid())
        blog = form.save()
        self.assertEqual(blog.text, 'TESTFORM')

    def test_form_invalid(self):
        form = FormBlog({'text':''})
        self.assertFalse(form.is_valid())
