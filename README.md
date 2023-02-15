# Target Map

Tagert Map é uma aplicação web, desenvolvida com Framework Django, para lidar com o gerenciamento de alvos em um mapa de forma dinâmica. Permite que o usuário visualize alvos em um mapa e seus detalhes, bem como a edição, cadastro ou exclusão de um alvo.

Entre as funcionalidades, pode se destacar:
- CRUD de Alvos em um mapa.
- Gerenciamento via painel administrativo.


## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/lucasribeirorsousa/target-map.git
cd target-map
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py loaddata fixtures/*.json 
```

# Usuários para teste
- Admnistrador
```
    User = admin
    Password user = @adminAdmin123
```