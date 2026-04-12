"""
Name: Evan Westcomb
Class: CIS 218
Date: 4/13/2026
"""

from django.test import SimpleTestCase
from django.urls import reverse

class DashboardTests(SimpleTestCase):
    """Tests for the dashboard home page."""

    def test_url_exists_at_correct_location_homepageview(self):
        """Tests that the URL for the dashboard exists in the correct location."""

        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage_view(self):
        """Tests that the dashboard home page is rendered correctly."""

        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "Dashboard")