import datetime
import os
import tempfile

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from django.conf import settings as project_settings

from .models import Event


def create_event(title, publication_datetime, event_datetime):
    return Event.objects.create(title=title, publication_datetime=publication_datetime, content='',
                                event_datetime=event_datetime, image=create_temporary_image())


def create_temporary_image():
    tempfile.TemporaryFile(suffix='.png', dir=os.path.join(project_settings.MEDIA_ROOT, 'events/img'))


class EventIndexViewTests(TestCase):
    """
    Contains tests relating to what is shown when the user navigates to /events.
    """

    def test_no_events(self):
        """
        If no events exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('events:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['future_events'], [])
        self.assertQuerysetEqual(response.context['past_events'], [])

    def test_single_past_event_shown(self):
        """
        Events with a event and publication date in the past are displayed on the index page.
        """
        past_publication_datetime = timezone.now() - datetime.timedelta(days=20)
        past_event_datetime = timezone.now() - datetime.timedelta(days=13)
        _ = create_event('Past Published Event', past_publication_datetime, past_event_datetime)
        response = self.client.get(reverse('events:index'))
        self.assertQuerysetEqual(response.context['past_events'], [])
#
#    def test_future_question(self):
#        """
#        Questions with a pub_date in the future aren't displayed on
#        the index page.
#        """
#        create_question(question_text="Future question.", days=30)
#        response = self.client.get(reverse('polls:index'))
#        self.assertContains(response, "No polls are available.")
#        self.assertQuerysetEqual(response.context['latest_question_list'], [])
#
#    def test_future_question_and_past_question(self):
#        """
#        Even if both past and future questions exist, only past questions
#        are displayed.
#        """
#        create_question(question_text="Past question.", days=-30)
#        create_question(question_text="Future question.", days=30)
#        response = self.client.get(reverse('polls:index'))
#        self.assertQuerysetEqual(
#            response.context['latest_question_list'],
#            ['<Question: Past question.>']
#        )
#
#    def test_two_past_questions(self):
#        """
#        The questions index page may display multiple questions.
#        """
#        create_question(question_text="Past question 1.", days=-30)
#        create_question(question_text="Past question 2.", days=-5)
#        response = self.client.get(reverse('polls:index'))
#        self.assertQuerysetEqual(
#            response.context['latest_question_list'],
#            ['<Question: Past question 2.>', '<Question: Past question 1.>']
#        )
