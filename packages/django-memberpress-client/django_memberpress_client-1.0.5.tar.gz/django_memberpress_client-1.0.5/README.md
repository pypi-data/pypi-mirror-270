# Django Plugin For memberpress REST API Client

[![pypi django-memberpress-client](https://img.shields.io/static/v1?label=pypi&style=flat-square&color=0475b6&message=django-memberpress-client)](https://pypi.org/project/django-memberpress-client/) [![memberpress](https://img.shields.io/static/v1?label=memberpress&style=flat-square&color=04d4e4&message=REST%20API)](https://memberpress.com/addons/developer-tools/) [![hack.d Lawrence McDaniel](https://img.shields.io/badge/hack.d-Lawrence%20McDaniel-orange.svg)](https://lawrencemcdaniel.com)

![memberpress](https://memberpress.com/wp-content/uploads/2022/01/memberpress-logo-color.svg)

A lightweight, performant Django plugin that implements REST api and Webhook integrations for the [Wordpress](https://wordpress.org/) [memberpress](https://memberpress.com/blog/memberpress-developer-tools/) Pro plugin.

## Installation

```bash
pip install django-memberpress-client
```

```python
from django.conf import settings

# required settings
settings.MEMBERPRESS_API_KEY = 'set-me-please'
settings.MEMBERPRESS_API_BASE_URL = 'https://set-me-please.com/'

# optional settings
settings.MEMBERPRESS_API_KEY_NAME = "MEMBERPRESS-API-KEY"
settings.MEMBERPRESS_CACHE_EXPIRATION = 60*60*24
settings.MEMBERPRESS_SENSITIVE_KEYS = [
    "password",
    "token",
    "client_id",
    "client_secret",
    "Authorization",
    "secret",
]
```

Alternatively, you can rename .env-sample, located in the same folder location
as this README.md, to .env:

```shell
# required settings
MEMBERPRESS_API_KEY=set-me-please
MEMBERPRESS_API_BASE_URL=https://set-me-please.com

# optional settings
MEMBERPRESS_CACHE_EXPIRATION=3600
MEMBERPRESS_API_KEY_NAME=MEMBERPRESS-API-KEY
MEMBERPRESS_SENSITIVE_KEYS=password,token,client_id,client_secret,Authorization,secret
```


You'll find the memberpress API Key in the Wordpress admin site.
![memberpress API Key](https://raw.githubusercontent.com/lpm0073/django-memberpress-client/main/doc/memberpress-api-key.png "memberpress API Key")

## Usage

### REST API

```python
# from a Python module inside your existing Django project.
from memberpress_client.member import Member

member = Member(username="jsmith")

if member.should_raise_paywall:
    # not a member, free trial has expired, subscription expired,
    # subscription renewal payment transaction declined, etc.
    your_custom_paywall_code()

# and, there is lots more detailed information about the member,
# their subscription status, their recent transactions history,
# and so on...
print(member.is_active_subscription)
print(member.is_trial_subscription)
print(member.latest_transaction.amount)
print(member.recent_subscriptions[0].created_at)
print(member.active_memberships[0].pricing_title)
```

### Webhooks

This plugin listens for events from memberpress' webhooks framework, a Pro 'developer tools' premium option of memberpress. Add a url of the form https://yourdomain.com/mp/api/v1/webhook to the Developer "Webhooks" page.
![memberpress webhooks](https://raw.githubusercontent.com/lpm0073/django-memberpress-client/main/doc/memberpress-api-webhook.png "memberpress webhooks")

urls:

- receive http POST requests: https://your-django-project.com/mp/api/v1/events/
- view the event log: https://your-django-project.com/admin/memberpress_client/memberpressevents/

![Django admin console](https://raw.githubusercontent.com/lpm0073/django-memberpress-client/main/doc/memberpress-django-admin2.png "Django admin console")

## Developers

### quick start

Keep in mind that this code package is intended to install as an add-on to your existing Django project. Therefore,
the 'production' settings and requirements intentionally ommit all Django and Django support packages
other than those that are unique to this repo. The 'local' settings and requirements compensate for this by including all of the settings and requirements that you'd typically find in 'common' and/or 'production'.

You should be able to follow the normal workflow for setting up a Django project for local development. This substantially
consists of the following:

- rename ./memberpress_client/settings/.env-sample to ./memberpress_client/settings/.env
- install all service-level dependencies on your local dev machine. This includes MySQL and Redis.
- clone this repo
- create and activate a Python virtual environment
- run make quickstart

Other common dev chores are automated in the Makefile, noting however that some syntax is specific to macOS environments (my sincerest apologies), plus, it assumes that you've installed mysql and redis using homebrew.


### class hierarchy

Use these class objects rather than working directly with the memberpress
json dicts returned by the api. These class objects include structural and type-checking validations,
plus they handle dict value data type conversations for you.



```python
class Memberpress:

    class MemberpressEvent(Memberpress):

    class MemberpressAPIClient(Memberpress):
        class Member(MemberpressAPIClient):
        class Membership(MemberpressAPIClient):
        class Subscriber(MemberpressAPIClient):
        class Transaction(MemberpressAPIClient):
```

### constants

Use these built-in constants rather than working directly with memberpress' dict key string values:

- MemberpressEvents: discrete list of memberpress event types. The str value exactly matches the event dict key "event".
- MemberpressEventTypes: discrete list of memberpress event_types

```python
from memberpress_client.constants import MemberpressEvents

print(MemberpressEvents.AFTER_CC_EXPIRES_REMINDER)
after-cc-expires-reminder

print(MemberpressEvents.AFTER_MEMBER_SIGNUP_REMINDER)
after-member-signup-reminder

print(MemberpressEvents.LOGIN)
login

print(MemberpressEvents.MEMBER_ACCOUNT_UPDATED)
member-account-updated

print(MemberpressEvents.SUBSCRIPTION_EXPIRED)
subscription-expired
# ...
# ectetera, etcetera, etcetera ...
# ...
print(MemberpressEvents.TRANSACTION_COMPLETED)
transaction-completed
```

Additionally, note that many of the constants include helper functions.
![memberpress_client constants](https://raw.githubusercontent.com/lpm0073/django-memberpress-client/main/doc/memberpress-constants.png "memberpress_client constants")
