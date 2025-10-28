# Controladoria API

Este projeto é uma API desenvolvida em Python utilizando o framework FastAPI. A API é projetada para gerenciar documentos jurídicos, permitindo a extração de informações relevantes utilizando modelos de linguagem avançados da Google GenAI.

## Inicialização

O projeto é gerenciado usando o [uv](https://uv.run/), uma ferramenta para gerenciamento de repósitorios Python. Para iniciar o ambiente de desenvolvimento, execute:
```bash
uv sync
```

Caso você ainda não tenha o `uv` instalado, você pode instalá-lo via pip:
```bash
pip install uv
# ou via requirements.txt do projeto
pip install -r requirements.txt
```

## Estrutura do Projeto
As aplicações estão localizadas na pasta `apps/`. Atualmente, o projeto contém as seguintes aplicações:
- `extract`: Responsável pela extração de informações de documentos jurídicos.

Para adicionar novas aplicações, utilize o comando:
```bash
uv init --app apps/<nome_da_aplicacao>
```

## Dependências
As principais dependências do projeto incluem:
- FastAPI: Framework web para construção de APIs.
- Pydantic: Validação de dados e gerenciamento de configurações.
- Uvicorn: Servidor ASGI para execução da aplicação FastAPI.
- Google GenAI: Biblioteca para integração com modelos de linguagem da Google.

Para adicionar dependências espécificas ao ambiente de desenvolvimento, utilize o grupo de dependências `dev` no arquivo `pyproject.toml` por meio do comando:
```bash
uv add --group dev <nome_da_dependencia>
```

Para adicionar dependências específicas à sua aplicação, utilize o comando:
```bash
uv add <nome_da_dependencia> --package <nome_da_aplicacao>
# ou
uv --project apps/<nome_da_aplicacao> add <nome_da_dependencia>
```

## Testes
Os testes são escritos utilizando o framework `pytest`. Para executar os testes, utilize o comando:
```bash
uv run pytest
```
