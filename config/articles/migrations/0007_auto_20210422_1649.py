# Generated by Django 3.2 on 2021-04-22 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0006_office'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Office',
            new_name='Organunit',
        ),
        migrations.CreateModel(
            name='Ismsdoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctitle', models.CharField(max_length=150)),
                ('version', models.IntegerField()),
                ('serial', models.IntegerField()),
                ('codeexperision', models.CharField(max_length=20)),
                ('Organunit_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='docs_of_office', to='articles.organunit')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='docs_of_auther', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
