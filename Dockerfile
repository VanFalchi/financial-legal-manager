# Dockerfile

# 1. Imagem base: Usamos uma imagem oficial do Python 3.11
FROM python:3.11-slim

# 2. Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# 3. Copia o arquivo de dependências para o contêiner
# Copiamos primeiro para aproveitar o cache do Docker. Se o requirements.txt não mudar,
# o Docker não reinstala tudo de novo a cada build.
COPY requirements.txt .

# 4. Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copia todo o resto do código do projeto para o diretório de trabalho
COPY . .

# 6. Expõe a porta que o Flask vai usar para rodar
EXPOSE 5000

# 7. Comando para iniciar a aplicação quando o contêiner rodar
# Usamos o host 0.0.0.0 para que seja acessível de fora do contêiner.
# --debug habilita o modo de desenvolvimento do Flask (recarrega ao salvar).
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000", "--debug"]
