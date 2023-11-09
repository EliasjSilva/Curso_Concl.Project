from django.db import models

# Create your models here.
# perfil do Usuário logado

class Profile_User(models.Model):

    GENDER = [
        ('Female', 'Feminino'),
        ('Male', 'Masculino'),
        ('Other', 'Outro'),
    ]

    LOCATE = [
        ('Acre - Rio Branco', 'Acre - Rio Branco'),
        ('Alagoas - Maceió', 'Alagoas - Maceió'),
        ('Amapá - Macapá', 'Amapá - Macapá'),
        ('Amazonas - Manaus', 'Amazonas - Manaus'),
        ('Bahia - Salvador', 'Bahia - Salvador'),
        ('Ceará - Fortaleza', 'Ceará - Fortaleza'),
        ('Espírito Santo - Vitória', 'Espírito Santo - Vitória'),
        ('Goiás - Goiânia', 'Goiás - Goiânia'),
        ('Maranhão - São Luís', 'Maranhão - São Luís'),
        ('Mato Grosso - Cuiabá', 'Mato Grosso - Cuiabá'),
        ('Mato Grosso do Sul - Campo Grande', 'Mato Grosso do Sul - Campo Grande'),
        ('Minas Gerais - Belo Horizonte', 'Minas Gerais - Belo Horizonte'),
        ('Paraíba - João Pessoa', 'Paraíba - João Pessoa'),
        ('Pernambuco - Recife', 'Pernambuco - Recife'),
        ('Piauí - Teresina', 'Piauí - Teresina'),
        ('Rio de Janeiro - Rio de Janeiro', 'Rio de Janeiro - Rio de Janeiro'),
        ('Rio Grande do Norte - Natal', 'Rio Grande do Norte - Natal'),
        ('Rio Grande do Sul - Porto Alegre', 'Rio Grande do Sul - Porto Alegre'),
        ('Rondônia - Porto Velho', 'Rondônia - Porto Velho'),
        ('Roraima - Boa Vista', 'Roraima - Boa Vista'),
        ('Santa Catarina - Florianópolis', 'Santa Catarina - Florianópolis'),
        ('São Paulo - São Paulo', 'São Paulo - São Paulo'),
        ('Sergipe - Aracaju', 'Sergipe - Aracaju'),
        ('Tocantins - Palmas', 'Tocantins - Palmas'),
        ('Distrito Federal - Brasília', 'Distrito Federal - Brasília'),
    ]


    user_photo = models.ImageField(upload_to='user-photo', blank=True, null=True)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100, choices=GENDER)
    email = models.EmailField(blank=True, null=True)
    tel = models.CharField(max_length=14, blank=True, null=True)
    endereco = models.CharField(max_length=200, blank=True,null=True)
    localidade = models.CharField(max_length=100, choices=LOCATE, blank=True, null=True)
    obs = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome