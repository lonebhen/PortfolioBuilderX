# Generated by Django 4.2 on 2023-04-26 17:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_projectmodel_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='educationmodel',
            options={'ordering': ['-the_year']},
        ),
        migrations.AlterModelOptions(
            name='experiencemodel',
            options={'ordering': ['-the_year']},
        ),
        migrations.RenameField(
            model_name='educationmodel',
            old_name='year',
            new_name='the_year',
        ),
        migrations.RenameField(
            model_name='experiencemodel',
            old_name='year',
            new_name='the_year',
        ),
        migrations.AlterField(
            model_name='educationmodel',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='experiencemodel',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='informationmodel',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='messagemodel',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='projectmodel',
            name='projectRating',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='2', max_length=10),
        ),
        migrations.AlterField(
            model_name='projectmodel',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='skillsetmodel',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
