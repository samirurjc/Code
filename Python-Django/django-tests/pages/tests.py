from django.test import TestCase
from django.test import Client

from .views import Counter

class CounterTests(TestCase):

    def test_creation(self):
        """Creation works"""
        counter = Counter()
        self.assertEqual(counter.count, 0)

    def test_increment(self):
        """Increment works"""
        counter = Counter()
        incremented = counter.increment()
        self.assertEqual(incremented, 1)

    def test_increment2(self):
        """Increment works (check internal count)"""
        counter = Counter()
        counter.increment()
        incremented = counter.count
        self.assertEqual(incremented, 1)

class GetTests (TestCase):

    def test_root(self):
        """Check root resource"""

        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')
        self.assertIn('<h1>Django CMS</h1>', content)

    def test_empty(self):
        """Empty resource"""

        c = Client()
        response = c.get('/empty')
        self.assertEqual(response.status_code, 404)
        content = response.content.decode('utf-8')
        self.assertIn('<a href="/">Main page</a>', content)

    def test_create(self):
        """Empty resource"""

        item_content = "This is the content for item."
        c = Client()
        response = c.post('/item', {'content': item_content})
        self.assertEqual(response.status_code, 200)
        response = c.get('/item')
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')
        self.assertIn(item_content, content)
        self.assertIn('<form action="/item" method="post">', content)
