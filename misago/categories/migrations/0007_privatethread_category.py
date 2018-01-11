# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from django.utils.translation import ugettext as _

from misago.core.utils import slugify


def create_default_categories_tree(apps, schema_editor):
    Category = apps.get_model('misago_categories', 'Category')

    Category.objects.create(
        special_role='status_threads',
        name='Status',
        slug='Status',
        lft=1,
        rght=2,
        tree_id=0,
        level=0,
    )


class Migration(migrations.Migration):

    dependencies = [
        ('misago_categories', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_categories_tree),
    ]
