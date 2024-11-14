from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.urls import reverse

class BlogPostListViewTests(TestCase):
    def test_blog_post_list_title(self):
        response = self.client.get(reverse('post-list'))
        self.assertContains(response, 'All Blog Posts')

