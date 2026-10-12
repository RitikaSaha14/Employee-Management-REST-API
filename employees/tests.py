from datetime import date
from decimal import Decimal

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Employee


class EmployeeAPITests(APITestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            full_name="Aarav Sharma",
            email="aarav@example.com",
            department="Engineering",
            job_title="Software Engineer",
            salary=Decimal("550000.00"),
            date_joined=date(2025, 1, 15),
        )
        self.list_url = reverse("employee-list")
        self.detail_url = reverse("employee-detail", args=[self.employee.id])

    def test_list_employees(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["email"], "aarav@example.com")

    def test_create_employee(self):
        payload = {
            "full_name": "Priya Das",
            "email": "priya@example.com",
            "department": "Product",
            "job_title": "Product Analyst",
            "salary": "600000.00",
            "date_joined": "2025-03-01",
        }
        response = self.client.post(self.list_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Employee.objects.filter(email="priya@example.com").exists())

    def test_reject_duplicate_email(self):
        payload = {
            "full_name": "Another Employee",
            "email": "aarav@example.com",
            "department": "Engineering",
            "job_title": "Developer",
            "salary": "500000.00",
            "date_joined": "2025-04-01",
        }
        response = self.client.post(self.list_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_employee(self):
        response = self.client.patch(
            self.detail_url,
            {"job_title": "Senior Software Engineer"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.employee.refresh_from_db()
        self.assertEqual(self.employee.job_title, "Senior Software Engineer")

    def test_delete_employee(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Employee.objects.filter(id=self.employee.id).exists())
