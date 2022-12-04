# Generated by Django 4.1.1 on 2022-11-02 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('intro', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': '宠物',
                'verbose_name_plural': '宠物们',
                'db_table': 'pet',
            },
        ),
    ]