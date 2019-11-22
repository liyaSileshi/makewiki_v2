# wiki/tests.py
from django.test import TestCase, Client
from django.contrib.auth.models import User
from wiki.models import Page
from wiki.forms import PageForm
from django.urls import reverse
# Create your tests here.
class WikiTestCase(TestCase):
    def test_true_is_true(self):
        """ Tests if True is equal to True. Should always pass. """
        self.assertEqual(True, True)

def test_page_slugify_on_save(self):
        """ Tests the slug generated when saving a Page. """
        # Author is a required field in our model.
        # Create a user for this test and save it to the test database.
        user = User()
        user.save()
        # or user = User.objects.create() 

        # Create and save a new page to the test database.
        page = Page(title="My Test Page", content="test", author=user)
        page.save()
        #  or page = Page.objects.create()

        # Make sure the slug that was generated in Page.save()
        # matches what we think it should be.
        self.assertEqual(page.slug, "my-test-page")

class PageListViewTests(TestCase):
    def test_multiple_pages(self):
        # Make some test data to be displayed on the page.
        user = User.objects.create()

        Page.objects.create(title="My Test Page", content="test", author=user)
        Page.objects.create(title="Another Test Page", content="test", author=user)

        # Issue a GET request to the MakeWiki homepage.
        # When we make a request, we get a response back.
        response = self.client.get('/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the number of pages passed to the template
        # matches the number of pages we have in the database.
        responses = response.context['pages']
        self.assertEqual(len(responses), 2)

        self.assertQuerysetEqual(
            responses,
            ['<Page: My Test Page>', '<Page: Another Test Page>'],
            ordered=False
        )

class PageDetailViewTests(TestCase):
    def test_one_page_detail(self):
        user = User.objects.create()

        #create a fake page
        Page.objects.create(title="My Test Page", content="test", author=user)

        # Issue a GET request to the details page.
        # When we make a request, we get a response back.
        response = self.client.get('/my-test-page/')
        self.assertEqual(response.status_code, 200)

        page = response.context['page']
        self.assertEqual(page.title, "My Test Page")
    
class PageCreateViewTests(TestCase):
    def test_page_create(self):
        # check that the creation page form loads when visiting
        response = self.client.get('/new/')
        self.assertEqual(response.status_code, 200)

        form = PageForm()
        self.assertTrue(form)

        self.assertIn(b'Title of your page.', response.content)
        self.assertIn(b'Write the content of your page here.', response.content)

    def test_page_form_post(self):
        #get a user object
        user = User.objects.create()

        #make a form dictionary
        form = {'title':"My Test Page",
                        'content':"testing", 'author': user.id}

        response = self.client.post('/new/', form = form)
        self.assertEqual(response.status_code, 302) #not working

        #create a page form with the form data and check if it's valid
        form_page = PageForm(data=form)
        form_page.save()
        self.assertTrue(form_page.is_valid())

        users = User.objects.all()
        self.assertEqual(len(users), 1)

        #check if the form is saved in the test db
        page = Page.objects.get(title = 'My Test Page')
        # print(page.author)
        # self.assertEqual(page.title, 'My Test Page')