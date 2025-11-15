#!/usr/bin/env bash
set -e

echo "🔧 Formatando código com black..."
black .

echo "🔧 Organizando imports com isort..."
isort .

echo "🔍 Rodando flake8..."
flake8 .

echo "✅ Rotina de formatação e lint concluída com sucesso!"
