from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from exhibits.models import Exhibit, UserProfile

def make_user(username, access_level):
    user = User.objects.create_user(username = username, email = username.lower() + "@example.com", password = "Password1")
    UserProfile.objects.create(user = user, access_level = access_level)
    return user

class RBACTest(TestCase):

    def test_admin(self):
        user = make_user("Alice", "admin")
        self.assertTrue(user.profile.is_admin)
    
    def test_admin_inherits(self):
        user = make_user("Alice", "admin")
        self.assertTrue(user.profile.is_curator)

    def test_curator(self):
        user = make_user("Alice", "curator")
        self.assertTrue(user.profile.is_curator)

    def test_viewer_has_no_inheritance(self):
        user = make_user("Alice", "user")
        self.assertFalse(user.profile.is_admin)
        self.assertFalse(user.profile.is_curator)
    
    def test_default_access_level(self):
        user = User.objects.create_user(username = "Alice",
                                        email = "alice@example.com",
                                        password = "Password1")
        
        profile = UserProfile.objects.create(user = user)

        self.assertEqual(profile.access_level, "user")

class ExhibitRBACTest(TestCase):

    def setUp(self):
        self.client = Client()

        self.admin = make_user("Admin", "admin")
        self.curator = make_user("Curator", "curator")
        self.viewer = make_user("Viewer", "viewer")

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

    def test_viewer_can_view_exhibits(self):
        response = self.client.get(reverse("exhibits:list"))
        self.assertEqual(response.status_code, 200)
    
    def test_viewer_can_view_exhibit_detail(self):
        response = self.client.get(reverse("exhibits:detail", args=[self.exhibit.pk]))
        self.assertEqual(response.status_code, 200)
    
    def test_viewer_cannot_create_exhibit(self):
        self.client.login(username = "Viewer", password = "Password1")
        response = self.client.post(reverse("exhibits:create"), {
            "title": "Viewer Attempt",
            "domain": "Test",
            "deployment_context": "ctx",
            "intended_use": "use",
            "system_type": "type",
            "inputs_and_assumptions": "in",
            "outputs_presented": "out",
            "failure_description": "fail",
            "detection_method": "detect",
            "affected_parties": "people",
            "contributing_factor": "factors",
            "lessons_learned": "lessons",
        })

        self.assertEqual(response.status_code, 302)
    
    def test_viewer_cannot_edit_exhibit(self):
        self.client.login(username = "Viewer", password = "Password1")
        response = self.client.post(reverse("exhibits:edit", args = [self.exhibit.pk]), {
            "title": "Viewer Edit Attempt",
            "domain": "Test",
            "deployment_context": "ctx",
            "intended_use": "use",
            "system_type": "type",
            "inputs_and_assumptions": "in",
            "outputs_presented": "out",
            "failure_description": "fail",
            "detection_method": "detect",
            "affected_parties": "people",
            "contributing_factor": "factors",
            "lessons_learned": "lessons",
        })

        self.assertEqual(response.status_code, 302)
    
    def test_viewer_cannot_delete_exhibit(self):
        self.client.login(username = "Viewer", password = "Password1")
        response = self.client.delete(reverse("exhibits:delete", args = [self.exhibit.pk]))
        self.assertEqual(response.status_code, 302)
    
    def test_viewer_cannot_manage_quiz(self):
        self.client.login(username="viewer", password="pass")
        response = self.client.get(reverse("exhibits:quiz_manage", args = [self.exhibit.pk]))
        self.assertEqual(response.status_code, 302)
    
    
    def test_curator_can_view_exhibits(self):
        self.client.login(username = "Curator", password = "Password1")
        response = self.client.get(reverse("exhibits:list"))
        self.assertEqual(response.status_code, 200)
    
    def test_curator_can_view_exhibit_detail(self):
        self.client.login(username = "Curator", password = "Password1")
        response = self.client.get(reverse("exhibits:detail", args = [self.exhibit.pk]))
        self.assertEqual(response.status_code, 200)
    
    def test_curator_can_create_exhibit(self):
        self.client.login(username = "Curator", password = "Password1")
        response = self.client.post(reverse("exhibits:create"), {
            "title": "Curator Attempt",
            "domain": "Test",
            "deployment_context": "ctx",
            "intended_use": "use",
            "system_type": "type",
            "inputs_and_assumptions": "in",
            "outputs_presented": "out",
            "failure_description": "fail",
            "detection_method": "detect",
            "affected_parties": "people",
            "contributing_factor": "factors",
            "lessons_learned": "lessons",
        })

        self.assertEqual(response.status_code, 200)

    def test_curator_can_edit_exhibit(self):
        self.client.login(username = "Curator", password = "Password1")
        response = self.client.post(reverse("exhibits:edit", args = [self.exhibit.pk]), {
            "title": "Curator Edit Attempt",
            "domain": "Test",
            "deployment_context": "ctx",
            "intended_use": "use",
            "system_type": "type",
            "inputs_and_assumptions": "in",
            "outputs_presented": "out",
            "failure_description": "fail",
            "detection_method": "detect",
            "affected_parties": "people",
            "contributing_factor": "factors",
            "lessons_learned": "lessons",
        })

        self.assertEqual(response.status_code, 200)
    
    def test_curator_can_delete_exhibit(self):
        self.client.login(username = "Curator", password = "Password1")
        response = self.client.delete(reverse("exhibits:delete", args = [self.exhibit.pk]))
        self.assertEqual(response.status_code, 200)
    
    def test_curator_can_manage_quiz(self):
        self.client.login(username = "Curator", password = "Password1")
        response = self.client.get(reverse("exhibits:quiz_manage", args = [self.exhibit.pk]))
        self.assertEqual(response.status_code, 200)
    
    def test_curator_can_add_quiz(self):
        self.client.login(username = "Curator", password = "Password1")
        response = self.client.post(reverse("exhibits:quiz_add", args = [self.exhibit.pk]), {
            "question": "question",
            "options": '["A", "B", "C"]',
            "correct_answer_index": 0,
            "explanation": "because it is",
        })
        self.assertIn(response.status_code, [200, 201]) # has 302
    
    
    def test_admin_can_create_exhibit(self):
        self.client.login(username = "Admin", password = "Password1")
        response = self.client.post(reverse("exhibits:create"), {
            "title": "Admin Attempt",
            "domain": "Test",
            "deployment_context": "ctx",
            "intended_use": "use",
            "system_type": "type",
            "inputs_and_assumptions": "in",
            "outputs_presented": "out",
            "failure_description": "fail",
            "detection_method": "detect",
            "affected_parties": "people",
            "contributing_factor": "factors",
            "lessons_learned": "lessons",
        })

        self.assertEqual(response.status_code, 200)
    
    def test_admin_can_edit_exhibit(self):
        self.client.login(username = "Admin", password = "Password1")
        response = self.client.post(reverse("exhibits:edit", args = [self.exhibit.pk]), {
            "title": "Admin Attempt",
            "domain": "Test",
            "deployment_context": "ctx",
            "intended_use": "use",
            "system_type": "type",
            "inputs_and_assumptions": "in",
            "outputs_presented": "out",
            "failure_description": "fail",
            "detection_method": "detect",
            "affected_parties": "people",
            "contributing_factor": "factors",
            "lessons_learned": "lessons",
        })

        self.assertEqual(response.status_code, 200)
    
    def test_admin_can_delete_exhibit(self):
        self.client.login(username="admin", password="pass")
        response = self.client.delete(reverse("exhibits:delete", args=[self.exhibit.pk]))
        self.assertEqual(response.status_code, 200)
    
    def test_admin_can_manage_quiz(self):
        self.client.login(username = "Admin", password = "Password1")
        response = self.client.get(reverse("exhibits:quiz_manage", args = [self.exhibit.pk]))
        self.assertEqual(response.status_code, 200)
    
