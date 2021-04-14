from django.test import TestCase

from .views import Counter

class CounterTests(TestCase):

    def test_increment(self):
        """Increment works"""
        counter = Counter()
        incremented = counter.increment()
        self.assertEqual(incremented, 1)

    def test_increment2(self):
        """Increment works"""
        counter = Counter()
        counter.increment()
        incremented = counter.count
        self.assertEqual(incremented, 1)
