# Generated by Django 4.2.6 on 2023-10-18 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='наименование')),
                ('content', models.CharField(max_length=150, verbose_name='содержимое')),
                ('image_preview', models.ImageField(blank=True, max_length=1, null=True, upload_to='image_blogs')),
                ('creation_date', models.DateField(max_length=150, verbose_name='дата создания')),
                ('publication_attribute', models.BooleanField(default=True, verbose_name='признак публикации')),
                ('number_of_views', models.IntegerField(default=0, verbose_name='количество просмотров')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='image_preview',
            field=models.ImageField(blank=True, max_length=1, null=True, upload_to='image'),
        ),
    ]
