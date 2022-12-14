# Generated by Django 4.0.6 on 2022-07-27 20:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0003_product_description_reviews_rating_like_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='product.category'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to=settings.AUTH_USER_MODEL, verbose_name='raiting owner'),
        ),
    ]
