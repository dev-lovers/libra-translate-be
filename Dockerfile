FROM python:3.11

# Define o diretório de trabalho
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt /app

# Atualiza o pip para a versão mais recente
RUN pip install --upgrade pip

# Instala as dependências do requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação
COPY . /app

CMD [ "python", "app.py" ]