from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.urls import reverse

class BlogPostListViewTests(TestCase):
    def test_blog_post_list_title(self):
        response = self.client.get(reverse('post-list'))
        self.assertContains(response, 'All Blog Posts')

from django.test import TestCase
from django.urls import reverse

class BlogPostListViewTests(TestCase):
    def test_blog_post_list_title(self):
        response = self.client.get(reverse('post-list'))
        self.assertContains(response, 'All Blog Posts')

from django.test import TestCase
from django.urls import reverse

class HomePageTests(TestCase):
    def test_homepage_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'ようこそ〜私のブログ！')

from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostNavigationTests(TestCase):
    def setUp(self):
        self.post1 = Post.objects.create(title='Post 1', content='Content 1')
        self.post2 = Post.objects.create(title='Post 2', content='Content 2')
        self.post3 = Post.objects.create(title='Post 3', content='Content 3')

    def test_post_navigation(self):
        response = self.client.get(reverse('post-detail', args=[self.post2.pk]))
        self.assertContains(response, reverse('post-detail', args=[self.post1.pk]))
        self.assertContains(response, reverse('post-detail', args=[self.post3.pk]))

