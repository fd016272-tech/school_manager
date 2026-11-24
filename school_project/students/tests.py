from django.test import TestCase
from django.urls import reverse

from teachers.models import Teacher
from .models import Student


class StudentPagesTests(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            first_name='Awa',
            last_name='Diop',
            email='awa.diop@example.com',
            classe='L1',
        )
        Student.objects.create(
            first_name='Moussa',
            last_name='Fall',
            email='moussa.fall@example.com',
            classe='L2',
        )

    def test_student_list_shows_students(self):
        response = self.client.get(reverse('students:list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Awa')
        self.assertContains(response, 'Moussa')

    def test_student_search_matches_first_or_last_name(self):
        response = self.client.get(reverse('students:list'), {'q': 'diop'})

        self.assertContains(response, 'Awa')
        self.assertNotContains(response, 'Moussa')

    def test_students_can_be_filtered_by_class(self):
        response = self.client.get(
            reverse('students:by_class', args=['L1'])
        )

        self.assertContains(response, 'Awa')
        self.assertNotContains(response, 'Moussa')

    def test_student_detail_and_missing_student(self):
        response = self.client.get(
            reverse('students:detail', args=[self.student.pk])
        )

        self.assertContains(response, 'Awa Diop')
        self.assertEqual(
            self.client.get(reverse('students:detail', args=[999])).status_code,
            404,
        )

    def test_home_and_about_pages(self):
        home = self.client.get(reverse('pages:home'))
        about = self.client.get(reverse('pages:about'))

        self.assertContains(home, 'Bienvenue dans School Manager')
        self.assertContains(home, '2 étudiants')
        self.assertContains(about, 'À propos')

    def test_teacher_list_page(self):
        Teacher.objects.create(
            first_name='Mamadou',
            last_name='Ba',
            email='mamadou.ba@example.com',
            subject='Mathématiques',
        )

        response = self.client.get(reverse('teachers:list'))

        self.assertContains(response, 'Mamadou')
        self.assertContains(response, 'Mathématiques')
