from django.test import TestCase
from resources.models import Category,Resource
from django.contrib.auth.models import User


class PortfolioTestCase(TestCase):
    def setUp(self):
        cat1 = Category.objects.create(title="korean",description="korean-desc")
        cat2 = Category.objects.create(title="tourism",description="tourism-desc")
        u = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        u.save()
        k1 = Resource.objects.create(site_title="android",description="test",curator="me", 
            writer=u,site_url="http://google.com",tags="tag", languages="english korean",
             objectId="abc")
        k1.category.add(cat1)



    def test_resource_has_title(self):
        p1 = Resource.objects.get(site_title="android")
        c1 = p1.category.all()[0]
        self.assertEqual(p1.site_title, 'android')
        self.assertEqual(c1.title, "korean")
        self.assertEqual(p1.writer.username,"john")



