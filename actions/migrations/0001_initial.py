# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('verb', models.CharField(max_length=255)),
                ('target_id', models.PositiveIntegerField(blank=True, null=True, db_index=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('target_ct', models.ForeignKey(blank=True, null=True, related_name='target_obj', to='contenttypes.ContentType')),
                ('user', models.ForeignKey(related_name='actions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
