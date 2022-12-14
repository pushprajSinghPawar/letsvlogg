# Generated by Django 4.0.1 on 2022-08-23 17:00

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='xxyyzz', max_length=100)),
                ('phonenum', models.IntegerField(default='9399237742')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('querry', models.CharField(default='no querry', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Blogpost_title', models.CharField(default='title<xyz>', max_length=50)),
                ('Blogpost_desc', models.TextField(default='this is the description of blog', max_length=45)),
                ('Blogpost_blog', models.TextField(default='blog content test  <xyz>', max_length=5400)),
                ('Blogpost_category1', models.CharField(choices=[('education', 'educational'), ('lifestyle', 'lifestyle'), ('sports', 'sports'), ('diy', 'diy'), ('fashion', 'fashion'), ('entertainment', 'entertainment'), ('science', 'science'), ('health', 'health'), ('personal', 'personal'), ('others', 'others')], default='others', max_length=50)),
                ('Blogpost_date', models.DateField()),
                ('Blogpost_picture1', models.ImageField(default='blogapp/logo.png', upload_to='blogapp/images')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
