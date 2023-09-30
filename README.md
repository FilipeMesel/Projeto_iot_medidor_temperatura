# Projeto_iot_medidor_temperatura
Projeto de sistema IoT usando Django e esp32 para elaborar medidores de temperatura WiFi

# Descrição
Projeto consiste em um sistema completo composto por hardware elaborado com ESP 32, programado usando o ESP-IDF framework sdk se comunicando com um sistema elaborado com django via requisições HTTP.

# Tecnologias Envolvidas
## ESP 32
O ESP32 é um microcontrolador de baixo custo e baixo consumo de energia que pertence à família de chips ESP (Espressif Systems Platform). Ele é amplamente utilizado para projetos de IoT (Internet das Coisas), automação residencial e uma variedade de outras aplicações em que a conectividade Wi-Fi e Bluetooth é necessária.

Abaixo, apresento detalhes do hardware
[FOTO DO HARDWARE]

## DS18B20
Sensor de temperatura a prova d'água utilizado

## DJANGo
Framework python usado para elaboração de aplicações Fullstack usando o conceito de MVC

Abaixo, apresento detalhes do sistema
[FOTO DO SITE DJANGO]
[EXPLICAR CADA UMA DAS FOTOS]

# Objetivo do projeto
Consolidar o alinhamento entre o que aprendi nas formações Python e HTML da DIO com o que venho utilizando ao longo do meu curso de mestrado.

# O que preciso saber para rodar esse projeto
É preciso saber um pouco de C++ para rodar o código ESP-IDF e um pouco de Python Django com HTML e conceitos de bancos de dados relacionais.

# Como rodar esse projeto

## Projeto Django

Navegue até o diretório do código, descubra o ip do seu PC, vá até "settings.py" e procure por "ALLOWED_HOSTS".

Nesse trecho do código, adicione o ip do seu computador, além do localhost

ALLOWED_HOSTS = ['SEU IP', 'localhost', '127.0.0.1']

Após isso, execute:

    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver 0.0.0.0:8000

Caso queira cadastrar um novo device, vá em:

    localhost:8000/cadastrar-dispositivo/

Caso queira visualizar os dados:

    localhost:8000/listar-dispositivos/

## Projeto ESP-IDF

Navegue até o diretório do código e adicione os dados da rede wifi e senha usando o arquivo "my_data.h"

Após, no CMD, digite "idf.py build" e "idf.py -p [PORTA COM] flash monitor"


# Licença
Esse projeto não tem licença, todos estão livres para comentar, discutir e me replicar meu projeto.
