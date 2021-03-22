from django.utils import timezone
from django.test import TestCase
from core.models import Hall, Table, Reservation


# Models test
class ModelTests(TestCase):
    hall_data = {'name': 'Test', 'width': 100.0, 'length': 100.0}
    table_data = {'number': 33, 'placements': 12, 'shape': 1, 'width': 1.5, 'length': 1.5, 'xlocation': 5.00, 'ylocation': 5.00}
    reservation_data = {'client_name': 'John', 'email': 'john@john.com', 'phone': '380505505505', 'comment': '4 persons'}
    res_date = timezone.now()+timezone.timedelta(days=7)
    
    @classmethod
    def setUpTestData(cls):
        h = Hall.objects.create(name='Test', width=100.0, length=100.0)
        t = Table.objects.create(number=33, placements=12, shape=1, width=1.5, length=1.5, xlocation=5.00, ylocation=5.00, hall=h)
        Reservation.objects.create(table=t, client_name='John', email='john@john.com', phone='380505505505', comment='4 persons', reservation_date=ModelTests.res_date)

    # Hall creation test    
    def test_hall_creation(self):
        w = Hall.objects.get(id=1)
        self.assertTrue(isinstance(w, Hall))
        self.assertEqual(w.__str__(), '{}: width {}, length {}'.format(self.hall_data['name'], self.hall_data['width'], self.hall_data['length']))

    # Table creation test
    def test_table_creation(self):
        w = Table.objects.get(id=1)
        self.assertTrue(isinstance(w, Table))
        self.assertEqual(w.width, 1.50)
        self.assertEqual(w.length, 1.50)
        self.assertEqual(w.__str__(), '{}: placements {}, shape {}'.format(self.table_data['number'], self.table_data['placements'], self.table_data['shape']))

    # Reservation creation test
    def test_reservation_creation(self):
        w = Reservation.objects.get(id=1)
        self.assertTrue(isinstance(w, Reservation))
        self.assertEqual(w.__str__(), '{}: client {}, date {}'.format(Table.objects.get(id=1), self.reservation_data['client_name'], self.res_date))

    # Admin panel test
    def test_get_table(self):
        table = Table.objects.get(id=1)
        obj = Reservation.objects.get(id=1)
        self.assertTrue(isinstance(obj, Reservation))
        self.assertEqual(obj.table, table)