"""
Lawrence McDaniel - https://lawrencemcdaniel.com
Oct-2022

memberpress REST API Client plugin for Django - Models.
"""
from email.policy import default
from django.utils.translation import ugettext as _
from django.db import models
from model_utils.models import TimeStampedModel

# To do: remove this when Open edX moves to Django 3.x
from jsonfield import JSONField

from memberpress_client.constants import MEMBERPRESS_EVENTS, MEMBERPRESS_EVENT_TYPES


class MemberpressEventLog(TimeStampedModel):
    """ """

    class Meta:
        verbose_name_plural = "memberpress event log"

    sender = models.URLField(
        blank=True,
        help_text=_("The site referrer. Example: https://wordpress-site.com/mb/webhooks/"),
    )

    username = models.CharField(
        blank=False,
        max_length=50,
        help_text=_("The username provided by memberpress."),
    )

    event = models.CharField(
        blank=False,
        choices=MEMBERPRESS_EVENTS,
        max_length=50,
        help_text=_("The memberpress event. Examples: recurring-transaction-completed"),
    )

    event_type = models.CharField(
        blank=False,
        choices=MEMBERPRESS_EVENT_TYPES,
        max_length=50,
        help_text=_("The type of memberpress event: transaction, subscription, member, membership"),
    )

    is_valid = models.BooleanField(
        blank=False,
        help_text=_("True if the json received was validated by memberpress_client. False otherwise."),
    )

    is_processed = models.BooleanField(
        blank=True,
        default=False,
        help_text=_("True if this event has been analyzed and acted upon."),
    )

    json = JSONField(
        blank=True,
        default={},
        help_text=_("A json dict sent by the webhook event in the request body."),
    )

    def __str__(self):
        return str(self.created) + "-" + self.event
