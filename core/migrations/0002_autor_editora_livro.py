# Generated by Django 4.1 on 2022-08-30 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Autor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
            ],
            options={
                "verbose_name_plural": "Autores",
            },
        ),
        migrations.CreateModel(
            name="Editora",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("site", models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Livro",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=255)),
                ("ISBN", models.CharField(max_length=32)),
                ("quantidade", models.IntegerField()),
                ("preco", models.DecimalField(decimal_places=2, max_digits=7)),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="livros",
                        to="core.categoria",
                    ),
                ),
                (
                    "editora",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="livros",
                        to="core.editora",
                    ),
                ),
            ],
        ),
    ]
