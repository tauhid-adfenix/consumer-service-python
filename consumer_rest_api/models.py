import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class ConsumerServiceMessages(models.Model):
    uuid = models.UUIDField(
        verbose_name=_('Unique Identifier'),
        help_text=_('Must be unique.'),
        editable=False,
        unique=True,
        default=uuid.uuid4
    )
    message = models.CharField(
        max_length=256,
        verbose_name=_('Message'),
        help_text=_('Message details.'),
        default='',
        blank=True
    )

    def __str__(self):
        return self.message

    class Meta:
        app_label = 'consumer_rest_api'
        verbose_name = _('Message')
        verbose_name_plural = _('Messages')
        db_table = 'consumer_service_messages'
