import unittest

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

from content.models import ModelBase
from poll.models import Poll, PollOption


class DummyModel(ModelBase):
    pass

models.register_models('poll', DummyModel)


class ModelTestCase(unittest.TestCase):
    def test_model_methods(self):
        # create a dummy model for the poll to relate too
        dummy_obj = DummyModel(
            title='title'
        )
        dummy_obj.save()
        
        # create poll obj
        poll_obj = Poll(
            title='poll_title',
        )
        poll_obj.save()
        poll_obj.content.add(dummy_obj)
        poll_obj.save()
        
        # create some poll options
        for i in range(1, 5):
            option_obj = PollOption(
                poll=poll_obj,
                content=dummy_obj.modelbase_ptr
            )
            option_obj.save()
        
        # test that the title is saved as the content object's title
        self.failUnless(option_obj.title == option_obj.content.title)
