from django.db import models

class Client(models.Model):
    username = models.CharField( max_length=240)
    company_name = models.CharField(max_length=240)
    login_state = models.CharField(
        choices=(
            ('a', 'asking'),
            ('y', 'yes'),
            ('n', 'no')
        ),
        max_length=1,
        default='a'
    )

    def __str__(self):
        return self.username

