# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('categorycontent_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='content.CategoryContent')),
                ('url', models.URLField(null=True, verbose_name='Advertised URL', blank=True)),
                ('start_showing', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Start showing')),
                ('stop_showing', models.DateTimeField(default=datetime.datetime(9999, 12, 29, 23, 59, 59, 999999, tzinfo=utc), verbose_name='Stop showing')),
            ],
            options={
                'abstract': False,
            },
            bases=('content.categorycontent',),
        ),
        migrations.CreateModel(
            name='Advertiser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.CharField(max_length=255, verbose_name='Company Name')),
                ('website', models.URLField(verbose_name='Company Site')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('company_name',),
                'verbose_name': 'Ad Provider',
                'verbose_name_plural': 'Advertisers',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ad',
            name='advertiser',
            field=models.ForeignKey(verbose_name='Ad Provider', blank=True, to='content_ad.Advertiser', null=True),
            preserve_default=True,
        ),
    ]
