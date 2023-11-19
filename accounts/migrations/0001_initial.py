# Generated by Django 4.2.6 on 2023-11-11 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_photo', models.ImageField(blank=True, null=True, upload_to='user-photo')),
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(max_length=100)),
                ('sexo', models.CharField(choices=[('Female', 'Feminino'), ('Male', 'Masculino'), ('Other', 'Outro')], max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('tel', models.CharField(blank=True, max_length=14, null=True)),
                ('endereco', models.CharField(blank=True, max_length=200, null=True)),
                ('localidade', models.CharField(blank=True, choices=[('Acre - Rio Branco', 'Acre - Rio Branco'), ('Alagoas - Maceió', 'Alagoas - Maceió'), ('Amapá - Macapá', 'Amapá - Macapá'), ('Amazonas - Manaus', 'Amazonas - Manaus'), ('Bahia - Salvador', 'Bahia - Salvador'), ('Ceará - Fortaleza', 'Ceará - Fortaleza'), ('Espírito Santo - Vitória', 'Espírito Santo - Vitória'), ('Goiás - Goiânia', 'Goiás - Goiânia'), ('Maranhão - São Luís', 'Maranhão - São Luís'), ('Mato Grosso - Cuiabá', 'Mato Grosso - Cuiabá'), ('Mato Grosso do Sul - Campo Grande', 'Mato Grosso do Sul - Campo Grande'), ('Minas Gerais - Belo Horizonte', 'Minas Gerais - Belo Horizonte'), ('Paraíba - João Pessoa', 'Paraíba - João Pessoa'), ('Pernambuco - Recife', 'Pernambuco - Recife'), ('Piauí - Teresina', 'Piauí - Teresina'), ('Rio de Janeiro - Rio de Janeiro', 'Rio de Janeiro - Rio de Janeiro'), ('Rio Grande do Norte - Natal', 'Rio Grande do Norte - Natal'), ('Rio Grande do Sul - Porto Alegre', 'Rio Grande do Sul - Porto Alegre'), ('Rondônia - Porto Velho', 'Rondônia - Porto Velho'), ('Roraima - Boa Vista', 'Roraima - Boa Vista'), ('Santa Catarina - Florianópolis', 'Santa Catarina - Florianópolis'), ('São Paulo - São Paulo', 'São Paulo - São Paulo'), ('Sergipe - Aracaju', 'Sergipe - Aracaju'), ('Tocantins - Palmas', 'Tocantins - Palmas'), ('Distrito Federal - Brasília', 'Distrito Federal - Brasília')], max_length=100, null=True)),
                ('obs', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
    ]
