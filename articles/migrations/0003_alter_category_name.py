# Generated by Django 4.1.1 on 2022-10-09 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_remove_article_published_alter_comments_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]