# Libra Translate - Backend

Este é o backend do projeto Libra Translate, desenvolvido para suportar a tradução de linguagem de sinais, em particular a Língua Brasileira de Sinais (Libras), para texto. O objetivo é processar vídeos ou imagens de sinais capturados pelo aplicativo e fornecer uma transcrição textual dos gestos.

## Tecnologias

- Python
- FastAPI

## Pré-requisitos

- Python 3.x
- pip (gerenciador de pacotes do Python)

## Instruções de Instalação

1. Clone o repositório

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```

2. Instale as dependências

   ```bash
   cd seu-repositorio
   pip install -r requirements.txt
   ```

3. Inicie o servidor FastAPI

   ```bash
   uvicorn main:app --reload
   ```

   O servidor FastAPI será iniciado e estará disponível em `http://localhost:8000`.

## Endpoints API

  - `/predict`: Endpoint para enviar imagens de sinais em Libras para a IA prever a letra correspondente.

## Contribuição

Contribuições são bem-vindas. Para mudanças importantes, abra primeiro uma issue para discutir o que você gostaria de mudar.

## Licença

[LICENSE](LICENSE)

---

Criado por [DevLovers](https://github.com/dev-lovers)
