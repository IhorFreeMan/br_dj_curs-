from django.test import TestCase
from index.models import Category, Notes
from django.utils import timezone
from django.urls import reverse
from index.forms import NotesForm
# Create your tests here.


class IndexTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            title="робота"
        )

        self.notes = Notes.objects.create(
            category=self.category,
            title="нарада в керівника",
            text="...",
            created=timezone.now().isoformat(),
        )

        self.note2 = Notes.objects.create(title='робота222',
                                         text='тест',
                                         created=timezone.now(),
                                         category_id=1) # You need to replace category_id with a valid category ID

        self.url = reverse('index:edit_note', args=[self.note2.id])


    def test_category_list(self):
        response = self.client.get(reverse('index:index'))
        self.assertEqual(response.status_code, 200)


    def test_notes_list(self):
        response = self.client.get(reverse('index:category', kwargs={'category_id': self.category.id}))
        self.assertEqual(response.status_code, 200)



    def test_edit_note(self):
        response = self.client.get(reverse('index:edit_note', args=[self.note2.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index/forms/edit_note.html')
        self.assertIsInstance(response.context['form'], NotesForm)



class DeleteNoteTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(title='робота')
        self.note = Notes.objects.create(category=self.category, title='Test del', text='del')

    def test_delete_notes(self):
        response = self.client.post(reverse('index:delete_notes', args=[self.note.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Notes.objects.filter(id=self.note.id).count(), 0)
        self.assertRedirects(response, reverse('index:category', kwargs={'category_id': self.category.id}))




