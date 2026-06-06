# 📊 Market News Intelligence Platform

### Plataforma de Inteligência para Notícias Financeiras e Macroeconômicas

O **Market News Intelligence Platform** é um projeto de Análise de Dados desenvolvido para automatizar a coleta, processamento, classificação e visualização de notícias financeiras e macroeconômicas.

A plataforma utiliza feeds RSS de fontes financeiras, análise de sentimento e regras de mercado para gerar insights sobre possíveis impactos em ativos como Ouro, Dólar, Bolsas e Bitcoin.

---

# 🎯 Objetivo do Projeto

Os mercados financeiros reagem constantemente a eventos macroeconômicos, decisões de bancos centrais, indicadores econômicos, tensões geopolíticas e notícias corporativas.

O objetivo deste projeto é criar uma plataforma capaz de:

- Coletar notícias financeiras automaticamente;
- Aplicar análise de sentimento em manchetes;
- Classificar possíveis impactos nos mercados;
- Auxiliar no monitoramento de cenários macroeconômicos;
- Fornecer visualizações interativas para análise de dados.

---

# 🚀 Funcionalidades

## 📰 Coleta Automatizada de Notícias

- Coleta de notícias via RSS;
- Integração com múltiplas fontes financeiras;
- Estruturação automática dos dados.

## 📊 Análise de Sentimento

- Classificação das manchetes em:
  - Positivo
  - Negativo
  - Neutro
- Score de sentimento utilizando VADER (NLTK).

## 📈 Classificação de Impacto nos Mercados

Análise baseada em regras para estimar impactos em:

- 🟡 Ouro
- 💵 Dólar
- 📈 Bolsas de Valores
- ₿ Bitcoin

Além disso, o sistema fornece:

- Nível de confiança;
- Justificativa da classificação.

## 🎛 Dashboard Interativo

- Filtro por fonte de notícia;
- Filtro por sentimento;
- Métricas em tempo real;
- Visualização tabular das notícias;
- Gráfico de distribuição de sentimentos;
- Gráfico de distribuição das fontes.

---

# 🛠 Tecnologias Utilizadas

### Linguagem

- Python

### Coleta de Dados

- Feedparser

### Processamento de Dados

- Pandas

### Análise de Sentimento

- NLTK
- VADER Sentiment Analyzer

### Visualização de Dados

- Streamlit
- Plotly

### Ambiente de Desenvolvimento

- Visual Studio Code
- Virtual Environment (venv)

---

# 📂 Estrutura do Projeto

```text
Market-News-Intelligence-Platform/

│
├── app.py
│
├── src/
│   ├── news_collector.py
│   ├── text_analyzer.py
│   ├── market_rules.py
│   └── ai_analyzer.py (experimental)
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

---

# 📊 Visão Geral do Dashboard

O dashboard apresenta:

## Indicadores Principais

- Total de Notícias Coletadas
- Fontes Ativas
- Notícias Positivas
- Notícias Negativas
- Notícias Neutras

## Tabela de Notícias

Cada notícia apresenta:

- Fonte
- Título
- Sentimento
- Score de Sentimento
- Impacto no Ouro
- Impacto nas Bolsas
- Impacto no Dólar
- Impacto no Bitcoin
- Confiança
- Justificativa

## Analytics

- Distribuição de Sentimentos
- Distribuição das Fontes de Notícias

---

# ▶️ Como Executar o Projeto

## 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/market-news-intelligence-platform.git
```

## 2. Acessar a Pasta

```bash
cd market-news-intelligence-platform
```

## 3. Criar Ambiente Virtual

```bash
python -m venv venv
```

## 4. Ativar Ambiente Virtual

### Windows

```bash
venv\Scripts\activate
```

## 5. Instalar Dependências

```bash
pip install -r requirements.txt
```

## 6. Executar o Dashboard

```bash
streamlit run app.py
```

---

# 🔬 Funcionalidades Experimentais

O projeto possui uma estrutura inicial para integração com Inteligência Artificial Local utilizando Ollama.

### Status Atual

⚠ Funcionalidade temporariamente desativada.

### Motivo

Durante os testes, o processamento local apresentou tempo de resposta elevado em hardware de entrada, impactando a experiência do usuário.

### Evoluções Futuras

- Tradução automática de manchetes;
- Interpretação contextual por IA;
- Análise avançada/profunda de impacto de mercado;
- Classificação de intensidade de impacto (Nível 1, 2 e 3).
- Integração com OpenAI API

---

# 🗺 Roadmap

## Versão 1.0

- [x] Coleta automática via RSS
- [x] Análise de sentimento
- [x] Classificação de impacto por regras
- [x] Dashboard interativo
- [x] Gráficos e analytics

## Versão 2.0

- [ ] Integração com OpenAI API
- [ ] Tradução automática de notícias
- [ ] Insights gerados por IA
- [ ] Classificação de intensidade de impacto (1–3)
- [ ] Resumo diário de mercado
- [ ] Banco de dados histórico de notícias

---

# 💡 Aprendizados do Projeto

Durante o desenvolvimento deste projeto foram aplicados conceitos de:

- Coleta de dados via APIs e RSS;
- Tratamento e transformação de dados;
- Análise de sentimento em linguagem natural;
- Visualização de dados;
- Desenvolvimento de dashboards interativos;
- Estruturação de projetos em Python;
- Integração experimental com modelos de Inteligência Artificial.

---

# 👨‍💻 Autor

**Talles Cunha**

Estudante de Análise de Dados | Ciência de Dados | Python | Mercados Financeiros

---

> Projeto desenvolvido com fins educacionais e para construção de portfólio em Análise de Dados, Business Intelligence e Inteligência de Mercado.