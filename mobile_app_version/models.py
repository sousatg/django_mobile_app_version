from django.db import models

class MobileAppVersion(models.Model):
    manufactor = models.CharField(max_length=200, blank=False)
    version = models.CharField(max_length=200)
    release_notes = models.TextField(blank=True)
    link = models.CharField(max_length=250, blank=False)

    class Meta:
        verbose_name = 'Mobile App Version'
        verbose_name_plural = 'Mobile App Version'

        constraints = [
            models.UniqueConstraint(fields=['manufactor'], name='unique manufactor')
        ]

    def serialize(self):
        return {
            'manufactor': self.manufactor,
            'version': self.version,
            'release_notes': self.release_notes,
            'link': self.link
        }
