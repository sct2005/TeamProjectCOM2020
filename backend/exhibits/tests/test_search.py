from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from exhibits.models import Exhibit, UserProfile

def create_exhibit(title, domain):
    return Exhibit.objects.create(
        title = title,
        domain=domain,
        deployment_context="ctx",
        intended_use="use",
        system_type="type",
        inputs_and_assumptions="in",
        outputs_presented="out",
        failure_description="fail",
        detection_method="detect",
        affected_parties="people",
        contributing_factors="factors",
        lessons_learned="lessons",
    )


class SearchTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.exhibit1 = create_exhibit("The Snow", "Weather")
        self.exhibit2 = create_exhibit("Cosmic Microwave Background Radiation", "Energy")
        self.exhibit3 = create_exhibit("The Amazon Rainforest", "Deforestation")
    
    def test_search_is_correct(self):
        response = self.client.get(reverse("home"), {"q": "Snow"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "The Snow")
        self.assertNotContains(response, "Cosmic Microwave Background Radiation")
        self.assertNotContains(response, "The Amazon Rainforest")
    
    def test_search_is_not_case_sensitive(self):
        response = self.client.get(reverse("home"), {"q": "snow"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "The Snow")
        self.assertNotContains(response, "Cosmic Microwave Background Radiation")
        self.assertNotContains(response, "The Amazon Rainforest")
    
    def test_search_with_part_of_word(self):
        response = self.client.get(reverse("home"), {"q": "Sn"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "The Snow")
        self.assertNotContains(response, "Cosmic Microwave Background Radiation")
        self.assertNotContains(response, "The Amazon Rainforest")
    
    def test_search_no_results(self):
        response = self.client.get(reverse("home"), {"q": "nomatch"})
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "The Snow")
        self.assertNotContains(response, "Cosmic Microwave Background Radiation")
        self.assertNotContains(response, "The Amazon Rainforest")
    
    def test_search_all_results(self):
        response = self.client.get(reverse("home"), {"q": ""})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "The Snow")
        self.assertContains(response, "Cosmic Microwave Background Radiation")
        self.assertContains(response, "The Amazon Rainforest")
    
    def test_no_query_returns_all(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "The Snow")
        self.assertContains(response, "Cosmic Microwave Background Radiation")
        self.assertContains(response, "The Amazon Rainforest")
    
    def test_filter_category(self):
        response = self.client.get(reverse("home"), {"category": "Energy"})
        exhibits = response.context["exhibits"]
        titles = [ex.title for ex in exhibits]
        self.assertIn("Cosmic Microwave Background Radiation", titles)
        self.assertNotIn("The Snow", titles)
        self.assertNotIn("The Amazon Rainforest", titles)
    
    def test_filter_all(self):
        response = self.client.get(reverse("home"), {"category": "all"})
        exhibits = response.context["exhibits"]
        titles = [ex.title for ex in exhibits]
        self.assertIn("Cosmic Microwave Background Radiation", titles)
        self.assertIn("The Snow", titles)
        self.assertIn("The Amazon Rainforest", titles)
    
    def test_filter_unknown_category(self):
        response = self.client.get(reverse("home"), {"category": "Unknown Category"})
        exhibits = response.context["exhibits"]
        titles = [ex.title for ex in exhibits]
        self.assertNotIn("Cosmic Microwave Background Radiation", titles)
        self.assertNotIn("The Snow", titles)
        self.assertNotIn("The Amazon Rainforest", titles)
    
    def test_search_and_category(self):
        response = self.client.get(reverse("home"), {"q": "Rainforest", "category": "Deforestation"})
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "The Snow")
        self.assertNotContains(response, "Cosmic Microwave Background Radiation")
        self.assertContains(response, "The Amazon Rainforest")
    
    def test_incorrect_search_and_category(self):
        response = self.client.get(reverse("home"), {"q": "Incorrect Query", "category": "Unknown Category"})
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "The Snow")
        self.assertNotContains(response, "Cosmic Microwave Background Radiation")
        self.assertNotContains(response, "The Amazon Rainforest")
