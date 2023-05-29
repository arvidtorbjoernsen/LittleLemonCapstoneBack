from django.test import TestCase

from restaurant.models import MenuItem
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        MenuItem.objects.create(title="Pizza", price=80, inventory=100)
        MenuItem.objects.create(title="Steak", price=80, inventory=100)
        MenuItem.objects.create(title="Hamburger", price=80, inventory=100)

    def test_getall(self):
        items = MenuItem.objects.all()
        serializer = MenuSerializer(data=items, many=True)
        if serializer.is_valid():
            self.assertEqual(serializer.data, "")
