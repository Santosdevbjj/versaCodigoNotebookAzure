# Makefile para formatação e lint do projeto

.PHONY: format lint test all

# Formata o código com black e organiza imports com isort
format:
	@echo "🔧 Formatando código com black e isort..."
	black .
	isort .

# Roda o flake8 para verificar estilo e possíveis erros
lint:
	@echo "🔍 Rodando flake8..."
	flake8 .

# Executa os testes com pytest
test:
	@echo "🧪 Executando testes..."
	pytest tests/

# Executa tudo em sequência: formatar, lint e testes
all: format lint test
