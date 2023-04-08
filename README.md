# Job-Insights

Neste projeto foram implementadas análises a partir de um conjunto de dados sobre empregos.

Os dados foram extraídos do site [Glassdoor](https://www.glassdoor.com.br/index.htm) e obtidos através do [Kaggle](https://www.kaggle.com/), uma plataforma disponiblizando conjuntos de dados para cientistas de dados.

## Instalação

```shell
git clone git@github.com:JovemAlex/Job-Insights.git
```

### Dependências

`wheel v0.37.1`  
`black v22.1.0`  
`flake8 v4.0.1`  
`pytest v7.0.1`  
`pytest-json v0.4.0`  
`git+https://github.com/betrybe/pytest-dependency`  

### Instalação do Projeto e criação do ambiente virtual

Criação do ambiente virtual
```shell
python3 -m venv .venv
```
Ativação do ambiente virtual
```shell
source .venv/bin/activate
```
Instalação das dependências no ambiente virtual
```shell
python3 -m pip install -r dev-requirements.txt
```

<details>
  <summary><strong>🧱 Estrutura do Projeto</strong></summary><br />

  ```
  Legenda:
  🔸Arquivos que não podem ser alterados
  🔹Arquivos a serem alterados para realizar os requisitos.
  .
  ├──🔸README.md
  ├──🔸Dockerfile
  ├──🔸docker-compose.yml
  ├──🔸dev-requirements.txt
  ├──🔸requirements.txt
  ├── data
  │   └──🔸jobs.csv
  ├── src
  │   ├── flask_app
  │   │   ├── templates
  │   │   │   ├── includes
  │   │   │   │   └──🔸nav.jinja2
  │   │   │   ├──🔸base.jinja2
  │   │   │   ├──🔸index.jinja2
  │   │   │   ├──🔸job.jinja2
  │   │   │   └──🔸list_jobs.jinja2
  │   │   ├──🔸app.py
  │   │   ├──🔸more_insights.py
  │   │   └──🔹routes_and_views.py
  │   ├── insights
  │   │   ├──🔹industries.py
  │   │   ├──🔹jobs.py
  │   │   └──🔹salaries.py
  │   ├── pre_built
  │   │   ├──🔸brazilian_jobs.py
  │   │   ├──🔸counter.py
  │   │   └──🔸sorting.py
  ├── tests
  │   ├──🔸__init__.py
  │   ├──🔸conftest.py
  │   ├──🔸marker.py
  │   ├── brazilian
  │   │   ├──🔸__init__.py
  │   │   ├──🔸conftest.py
  │   │   ├──🔸mocks.py
  │   │   ├──🔹test_brazilian_jobs.py
  │   ├── counter
  │   │   ├──🔸__init__.py
  │   │   ├──🔸conftest.py
  │   │   ├──🔸mocks.py
  │   │   ├──🔹test_counter.py
  │   ├── mocks
  │   │   ├──🔸job_1.html
  │   │   ├──🔸jobs.csv
  │   │   ├──🔸jobs_with_industries.csv
  │   │   ├──🔸jobs_with_salaries.csv
  │   │   └──🔸jobs_with_types.csv
  │   ├── sorting
  │   │   ├──🔸__init__.py
  │   │   ├──🔸conftest.py
  │   │   ├──🔸mocks.py
  │   │   └──🔹test_sorting.py
  │   ├──🔸test_flask_app.py
  │   ├──🔸test_industries.py
  │   ├──🔸test_jobs.py
  │   ├──🔸test_salaries.py
  │   ├──🔸test_more_insights.py
  │   └──🔸test_routes_and_views.py
  ```

  

</details>  

<details>
  <summary><strong>🛠 Testes</strong></summary><br />

  Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

  <strong>Executar os testes</strong>

  ```bash
  $ python3 -m pytest
  ```

  O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

  ```bash
  python3 -m pytest -s -vv
  ```

  Caso precise executar apenas um arquivo de testes basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py
  ```

  Caso precise executar apenas uma função de testes basta executar o comando:

  ```bash
  python3 -m pytest -k nome_da_func_de_tests
  ```

  Se desejar que os testes parem de ser executados quando acontecer o primeiro erro, use o parâmetro `-x`

  ```bash
  python3 -m pytest -x tests/test_jobs.py
  ```
  
  Para executar um teste específico de um arquivo, basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py::test_nome_do_teste
  ```

</details>
