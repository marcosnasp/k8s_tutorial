# backend/Dockerfile
FROM python:3.9.19-slim-bullseye
WORKDIR /app

# Criação de um grupo de usuário não-root
RUN groupadd -r calculatorapi && useradd -r -g calculatorapi -m -d /home/calculatorapiuser calculatorapiuser

# Copiando os arquivos necessários e ajustando permissões
COPY requirements.txt requirements.txt
RUN chown calculatorapiuser:calculatorapi requirements.txt

# Alterando permissões do WORKDIR /app
RUN chown -R calculatorapiuser:calculatorapi /app

# Alterando o usuário para calculatorapiuser
USER calculatorapiuser

# Ajustando permissões de /home/calculatorapiuser
RUN chown calculatorapiuser:calculatorapi -R /home/calculatorapiuser

# Ajuste a variável de ambiente para incluir o diretório local de pacotes Python no PATH
ENV PATH=/home/calculatorapiuser/.local/bin:$PATH

# Instalando as dependências com pip
RUN pip install --user --upgrade pip \
    && pip install --user -r requirements.txt

# Copiando o restante do código da aplicação e ajustando as permissões
COPY . .


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]