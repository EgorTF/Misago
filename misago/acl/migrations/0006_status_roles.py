# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from django.utils.translation import ugettext as _


def create_default_roles(apps, schema_editor):
    Role = apps.get_model('misago_acl', 'Role')

    Role.objects.create(
        name=_(" Statusthreads"),
        permissions={
            # status threads
            'misago.threads.permissions.statusthreads': {
                'can_use_status_threads': 1,
                'can_start_status_threads': 1,
                'max_status_thread_participants': 3,
                'can_add_everyone_to_status_threads': 0,
                'can_report_status_threads': 1,
                'can_moderate_status_threads': 0,
            },
        }
    )

    Role.objects.create(
        name=_("Status threads moderator"),
        permissions={
            # status threads
            'misago.threads.permissions.statusthreads': {
                'can_use_status_threads': 1,
                'can_start_status_threads': 1,
                'max_status_thread_participants': 15,
                'can_add_everyone_to_status_threads': 1,
                'can_report_status_threads': 1,
                'can_moderate_status_threads': 1,
            },
        }
    )


class Migration(migrations.Migration):

    dependencies = [
        ('misago_acl', '0002_acl_version_tracker'),
    ]

    operations = [
        migrations.RunPython(create_default_roles),
    ]
