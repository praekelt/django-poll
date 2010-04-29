from django.db import models

from content.models import ModelBase


class Poll(ModelBase):
    content = models.ManyToManyField(
        ModelBase,
        related_name='related_content'
    )
    
    class Meta:
        verbose_name = 'Poll'
        verbose_name_plural = 'Polls'
        
class PollOption(models.Model):
    title = models.CharField(
        max_length=200, help_text='A short descriptive title.',
    )
    poll = models.ForeignKey(
        Poll,
        related_name='options'
    )
    content = models.ForeignKey(ModelBase)
    correct_answer = models.BooleanField()

    class Meta:
        verbose_name = 'Poll Option'
        verbose_name_plural = 'Poll Options'
        
    def save(self):
        if not self.title:
            self.title = self.content.title
        super(PollOption, self).save()

    def __unicode__(self):
        return '%s - %s' % (self.poll, self.title)
