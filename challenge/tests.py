from django.test import TestCase
from challenge.models import Question
from django.test import Client
from django.core.urlresolvers import reverse

class QuestionTestCase(TestCase):

    def setUp(self):
        self.q_simple = Question.objects.create(title="問題１",
            content="問題の本文",
            flag="FooBar",
            point=500)

    def test_str(self):
        self.assertEquals(self.q_simple.__str__(), '問題１')

    def test_valid_point_answerd(self):
        q = Question.objects.create(point=500,
            hint1="", hint2="", answer="解説")
        self.assertEquals(q.valid_point(), 0)

    def test_valid_point_hint1_only(self):
        q = Question.objects.create(point=500,
            hint1="ヒントその１", hint2="", answer="")
        self.assertEquals(q.valid_point(), 500*0.8)

    def test_valid_point_hint1_hint2(self):
        q = Question.objects.create(point=500,
            hint1="ヒントその１", hint2="ヒントその２", answer="")
        self.assertEquals(q.valid_point(), 500*0.5)

class ViewTestCase(TestCase):

    def test_index(self):
        client = Client()
        response = client.get(reverse('index'))
        print("### {} ###".format(response))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "<title>CTF Site for EAST Branch</title>")
