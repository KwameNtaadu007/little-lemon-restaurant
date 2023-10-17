from django.test import TestCase
from .models import Booking, Employee, Menu


class BookingModelTest(TestCase):
    def test_create_booking(self):
        booking = Booking.objects.create(
            first_name="John",
            last_name="Doe",
            guest_count=4,
            reservation_time="2023-01-15",
            comments="Test comment"
        )
        self.assertEqual(booking.first_name, "John")
        self.assertEqual(booking.last_name, "Doe")
        self.assertEqual(booking.guest_count, 4)
        self.assertEqual(booking.reservation_time, "2023-01-15")
        self.assertEqual(booking.comments, "Test comment")

class EmployeeModelTest(TestCase):
    def test_create_employee(self):
        employee = Employee.objects.create(
            first_name="Alice",
            last_name="Smith",
            role="Manager",
            shift=1
        )
        self.assertEqual(employee.first_name, "Alice")
        self.assertEqual(employee.last_name, "Smith")
        self.assertEqual(employee.role, "Manager")
        self.assertEqual(employee.shift, 1)

class MenuModelTest(TestCase):
    def test_create_menu_item(self):
        menu_item = Menu.objects.create(
            name="Burger",
            price=10
        )
        self.assertEqual(menu_item.name, "Burger")
        self.assertEqual(menu_item.price, 10)

