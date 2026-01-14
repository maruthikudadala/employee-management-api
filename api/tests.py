from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Employee
from django.contrib.auth.models import User

class EmployeeAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword123'
        )
        # Get token
        response = self.client.post(
            reverse('token_obtain_pair'),
            {'username': 'testuser', 'password': 'testpassword123'},
            format='json'
        )
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        
        # Create test employee
        self.employee = Employee.objects.create(
            name="John Doe",
            email="john@example.com",
            department="Engineering",
            role="Developer"
        )
    
    def test_create_employee(self):
        data = {
            "name": "Jane Smith",
            "email": "jane@example.com",
            "department": "HR",
            "role": "Manager"
        }
        response = self.client.post(reverse('employee-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_duplicate_email(self):
        data = {
            "name": "Another John",
            "email": "john@example.com",  # Already exists
            "department": "Sales"
        }
        response = self.client.post(reverse('employee-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_get_employees(self):
        response = self.client.get(reverse('employee-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_filter_by_department(self):
        response = self.client.get('/api/employees/?department=Engineering')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_pagination(self):
        # Create more employees
        for i in range(15):
            Employee.objects.create(
                name=f"Employee {i}",
                email=f"emp{i}@example.com",
                department="Engineering"
            )
        response = self.client.get('/api/employees/?page=2')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)