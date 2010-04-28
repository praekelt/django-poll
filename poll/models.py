from django.db import models

from content.models import ModelBase


class Poll(ModelBase):
    
    class Meta:
        verbose_name = 'Poll'
        verbose_name_plural = 'Polls'
    
    def vote(self, option_id):
        # increment te number of votes on the option that has been selected
        option = self.options.permitted().get(id=option_id)
        
        if option:
            option.votes += 1
            option.save()
            return True
        return False
    
    def set_cookie(self, request, response):
        # set a cookie to the users browser if they have successfully voted
        voted_polls = request.COOKIES.get('voted_polls', [])
        
        if voted_polls: 
            voted_polls = voted_polls.split(',')

        voted_polls.append(str(self.id))
        response.set_cookie('voted_polls', value=','.join(voted_polls))
        
        return response
    
    def voted(self, request):
        # check if the user has voted on this poll object yet
        cookies = request.COOKIES
        return str(self.id) in cookies.get('voted_polls', '').split(',')
        
class PollOption(ModelBase):
    poll = models.ForeignKey(Poll, related_name='options')
    votes = models.PositiveIntegerField(default=0, editable=False)
    percentage = models.FloatField(default=0, editable=False)

    class Meta:
        verbose_name = 'Poll Option'
        verbose_name_plural = 'Poll Options'
    
    def save(self):
        # recalculate the percentages for all options relative to this one
        options = self.poll.options.all()
        total = float(0)
        
        for opt in options:
            total += opt.votes
            
        if total:
            for option in options:
                option.percentage = (option.votes / total) * 100
                option.save()
        
        super(PollOption, self).save()

    def __unicode__(self):
        return '%s - %s' % (self.poll, self.title)
