# Generated by Django 5.1.2 on 2024-10-31 19:07

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('notas', '0002_rename_notas_nota_rename_content_nota_conteudo_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=255)),
                ('criado_em', models.DateTimeField(default=django.utils.timezone.now)),
                ('nota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='notas.nota')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
