from django.test import TestCase

from . models import Check

class CheckTest(TestCase):
    def setUp(self):
        Check.objects.create(shop='Some Shop', total_amount=22.50)

    def test_we_can_get_some(self):
        checks = Check.objects.order_by('date_added')
        self.assertEqual(checks.__len__() , 1)

    def test_we_can_get_some(self):
        checks = Check.objects.filter(shop='Some Shop')
        self.assertEqual(checks.__len__(), 1)
        self.assertEqual(checks[0].total_amount, 22.50)
        self.assertEqual(checks[0].shop, 'Some Shop')