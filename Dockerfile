# Etapa 1: build de dependências em ambiente isolado
FROM python:3.12-slim AS builder

# Define diretório de trabalho
WORKDIR /app

# Instala dependências necessárias para compilar pacotes (serão removidas depois)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc \
    && rm -rf /var/lib/apt/lists/*

# Copia apenas requirements.txt para aproveitar cache
COPY requirements.txt .

# Instala dependências de produção em um diretório isolado
RUN pip install --upgrade pip \
    && pip install --prefix=/install -r requirements.txt

---

# Etapa 2: imagem final otimizada
FROM python:3.12-slim

# Define diretório de trabalho
WORKDIR /app

# Copia dependências já instaladas da etapa anterior
COPY --from=builder /install /usr/local

# Copia o código da aplicação
COPY . .

# Define variáveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Exemplo de comando padrão (ajuste conforme sua aplicação)
CMD ["python", "main.py"]
