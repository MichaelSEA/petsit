from datetime import datetime, timedelta
from django.urls import resolve
from django.test import TestCase

from sitters.views import home_page
from sitters.models import Owner,Sitter,Stay


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


class Modeltest(TestCase):

    def setUp(self):
        self.owner = Owner.objects.create(name="Gomez Addams",
                                          phone_number="+15551212",
                                          email="gomez@addams.com")
        self.sitter = Sitter.objects.create(name="abcdefghijklm",
                                            phone_number="+19998883333",
                                            email="howie@gmail.com",)

        self.sitter_id = self.sitter.id

    def create_stays(self, upper_limit):
        initial_date = datetime.now().date()
        for i in range(upper_limit):
            Stay.objects.create(rating=5,
                                comments=str(i),
                                start_date=initial_date + timedelta(days=i),
                                end_date=initial_date + timedelta(days=i+2),
                                sitter=self.sitter,
                                owner=self.owner,
                                dogs="Fifi\|Fluffy",)


    def test_sitter_rank_no_stays(self):
        self.assertEqual(self.sitter.sitter_score, self.sitter.overall_sitter_rank)

    def test_sitter_rank_lt_10_stays(self):
        self.create_stays(1)
        self.sitter = Sitter.objects.get(id=self.sitter_id)
        self.assertEqual(2.75, self.sitter.overall_sitter_rank)

    def test_sitter_rank_ge_10_stays(self):
        self.create_stays(10)
        self.assertEqual(5.0, self.sitter.overall_sitter_rank)



