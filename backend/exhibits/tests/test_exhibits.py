from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Group, Permission

from exhibits.models import Exhibit

class ExhibitsTest(TestCase):

    def setUp(self):
        self.curator = User.objects.create_user(username = "Alice",
                                                email = "alice@example.com",
                                                password = "Password1")
        
    def test_create_exhibit_successful(self):
        original_count = Exhibit.objects.count()

        self.exhibit = Exhibit.objects.create(
            title="Test Exhibit",
            domain="Test",
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

        self.assertEqual(Exhibit.objects.count(), original_count + 1)
        self.assertEqual(self.exhibit.title, "Test Exhibit")
        self.assertEqual(self.exhibit.domain, "Test")
        self.assertEqual(self.exhibit.deployment_context, "ctx")
        self.assertEqual(self.exhibit.intended_use, "use")
        self.assertEqual(self.exhibit.system_type, "type")
        self.assertEqual(self.exhibit.inputs_and_assumptions, "in")
        self.assertEqual(self.exhibit.outputs_presented, "out")
        self.assertEqual(self.exhibit.failure_description, "fail")
        self.assertEqual(self.exhibit.detection_method, "detect")
        self.assertEqual(self.exhibit.affected_parties, "people")
        self.assertEqual(self.exhibit.contributing_factors, "factors")
        self.assertEqual(self.exhibit.lessons_learned, "lessons")

    def test_create_exhibit_with_missing_title_fails(self):
        original_count = Exhibit.objects.count()

        self.exhibit = Exhibit.objects.create(
            title="",
            domain="Test",
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

        self.assertEqual(Exhibit.objects.count(), original_count)
    
    def test_duplicate_exhibit_fails(self):
        self.exhibit = Exhibit.objects.create(
            title="Test Exhibit",
            domain="Test",
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

        original_count = Exhibit.objects.count()

        self.exhibit = Exhibit.objects.create(
            title="Test Exhibit",
            domain="Test",
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

        self.assertEqual(Exhibit.objects.count(), original_count)
        