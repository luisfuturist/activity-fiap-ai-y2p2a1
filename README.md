# activity-fiap2-ai-p1a1 <!-- omit in toc -->

> Este projeto faz parte do curso de **Inteligência Artificial** da [FIAP](https://github.com/fiap) - Online 2024. Este repositório é a atividade "**Ano 2 - Fase 2** - Cap 1 - Desafio Integrador: IA entre Robôs, Sinapses e Medicina".

## Índice <!-- omit in toc -->

- [Visão Geral](#visão-geral)
- [Objetivo](#objetivo)
- [Demonstração](#demonstração)
- [Parte 1 — Extração de Sintomas e Sugestão de Diagnóstico](#parte-1--extração-de-sintomas-e-sugestão-de-diagnóstico)
  - [Arquivos Principais](#arquivos-principais)
  - [Estrutura dos Dados](#estrutura-dos-dados)
    - [Frases de Sintomas (`sentences.txt`)](#frases-de-sintomas-sentencestxt)
    - [Mapa de Conhecimento (`symptoms_map.txt`)](#mapa-de-conhecimento-symptoms_maptxt)
  - [Funcionamento do Sistema](#funcionamento-do-sistema)
    - [Algoritmo de Correspondência](#algoritmo-de-correspondência)
  - [Doenças Identificadas](#doenças-identificadas)
  - [Execução](#execução)
  - [Limitações e Considerações](#limitações-e-considerações)
- [Parte 2 — Classificador de Risco (TF-IDF + ML)](#parte-2--classificador-de-risco-tf-idf--ml)
  - [Arquivos Principais](#arquivos-principais-1)
  - [Estrutura dos Dados](#estrutura-dos-dados-1)
    - [Dataset (`diagnosticos.csv`)](#dataset-diagnosticoscsv)
    - [Representação Numérica (TF-IDF)](#representação-numérica-tf-idf)
  - [Funcionamento Técnico](#funcionamento-técnico)
    - [1. **Pré-processamento**](#1-pré-processamento)
    - [2. **Vetorização TF-IDF**](#2-vetorização-tf-idf)
    - [3. **Treinamento do Modelo**](#3-treinamento-do-modelo)
    - [4. **Avaliação e Métricas**](#4-avaliação-e-métricas)
  - [Resultados Detalhados](#resultados-detalhados)
    - [Performance do Modelo](#performance-do-modelo)
    - [Relatório de Classificação Detalhado](#relatório-de-classificação-detalhado)
    - [Análise de Performance por Classe](#análise-de-performance-por-classe)
  - [Testes de Inferência](#testes-de-inferência)
  - [Como Executar o Notebook](#como-executar-o-notebook)
  - [Saída Esperada](#saída-esperada)
  - [Limitações e Considerações](#limitações-e-considerações-1)
    - [Limitações Técnicas](#limitações-técnicas)
    - [Limitações de Domínio](#limitações-de-domínio)
    - [Oportunidades de Melhoria](#oportunidades-de-melhoria)
    - [Considerações Éticas](#considerações-éticas)
- [Estrutura do Repositório](#estrutura-do-repositório)
- [Como Executar (Passo a Passo)](#como-executar-passo-a-passo)
  - [Pré-requisitos](#pré-requisitos)
  - [Instalação Completa](#instalação-completa)
    - [1. **Clonar o Repositório**](#1-clonar-o-repositório)
    - [2. **Configurar Ambiente Virtual**](#2-configurar-ambiente-virtual)
    - [3. **Instalar Dependências**](#3-instalar-dependências)
  - [Parte 1 — Sistema de Diagnóstico](#parte-1--sistema-de-diagnóstico)
    - [Executar Script de Diagnóstico](#executar-script-de-diagnóstico)
  - [Parte 2 — Classificador de Risco](#parte-2--classificador-de-risco)
    - [VS Code (IDE Integrado)](#vs-code-ide-integrado)
  - [Verificação da Execução](#verificação-da-execução)
    - [Checklist de Execução Bem-Sucedida](#checklist-de-execução-bem-sucedida)
    - [Arquivos Gerados](#arquivos-gerados)
- [Equipe](#equipe)
  - [Membros](#membros)
  - [Professores](#professores)


---

## Visão Geral

O projeto simula um sistema de diagnóstico médico automatizado, utilizando técnicas de extração de informações e classificação de texto para identificar doenças cardiológicas e avaliar riscos com base em sintomas relatados por pacientes.

## Objetivo

Desenvolver um sistema básico que:
1. Extrai sintomas de frases de pacientes e sugere diagnósticos com base em um mapa de conhecimento (Parte 1).
2. Classifica frases médicas em "alto risco" ou "baixo risco" usando um modelo de Machine Learning (Parte 2).

## Demonstração

Assista ao vídeo de demonstração (4 minutos) no YouTube: [inserir link do vídeo não listado aqui]. // TODO: Add link

O vídeo mostra:
- Execução do script de extração de sintomas com exemplos de diagnósticos.
- Treinamento e teste do classificador de risco, com análise de acurácia.
- Reflexões sobre vieses nos dados e governança.

---

## Parte 1 — Extração de Sintomas e Sugestão de Diagnóstico

Esta parte implementa um sistema básico de diagnóstico automatizado que analisa frases de sintomas relatados por pacientes e sugere diagnósticos com base em um mapa de conhecimento estruturado.

### Arquivos Principais

- **`sentences.txt`** — 10 frases completas simulando descrições de sintomas de pacientes
- **`symptoms_map.txt`** — Mapa de conhecimento em formato CSV relacionando sintomas a doenças
- **`diagnosis.py`** — Script Python que processa as frases e sugere diagnósticos

### Estrutura dos Dados

#### Frases de Sintomas (`sentences.txt`)
Contém 10 frases variadas que simulam relatos reais de pacientes, incluindo:
- Descrição dos sintomas
- Duração temporal ("Há dois dias", "há uma semana")
- Contexto de agravamento ("piora quando faço esforço físico")
- Impacto na rotina ("precisando sentar para melhorar")

**Exemplos:**
```
Há dois dias estou com uma dor no peito que piora quando faço esforço físico.
Sinto cansaço constante há uma semana, mesmo depois de descansar.
Tenho falta de ar ao subir escadas e palpitações no coração.
```

#### Mapa de Conhecimento (`symptoms_map.txt`)
Estrutura CSV com três colunas:
- **Symptom1** — Primeiro sintoma ou expressão-chave
- **Symptom2** — Segundo sintoma ou contexto
- **DiseaseAssociated** — Doença associada

**Exemplos de associações:**
```csv
Symptom1,Symptom2,DiseaseAssociated
dor no peito,esforço físico,Infarto
cansaço constante,descansar,Insuficiencia Cardiaca
falta de ar,subir escadas,Angina
```

### Funcionamento do Sistema

O script `diagnosis.py` implementa a seguinte lógica:

1. **Carregamento dos dados**: Lê o mapa de conhecimento e as frases de sintomas
2. **Processamento**: Para cada frase, busca correspondências com os sintomas no mapa
3. **Sugestão de diagnóstico**: Retorna a doença associada ou "Diagnosis not found"

#### Algoritmo de Correspondência
```python
def suggest_diagnosis(sentence, knowledge_map):
    for _, row in knowledge_map.iterrows():
        symptom1 = row['Symptom1'].lower()
        symptom2 = row['Symptom2'].lower()
        if symptom1 in sentence.lower() or symptom2 in sentence.lower():
            return row['DiseaseAssociated']
    return "Diagnosis not found"
```

### Doenças Identificadas

O sistema identifica três principais condições cardiológicas:

- **Infarto** — Associado a dor no peito, esforço físico, braço esquerdo, suor frio
- **Insuficiência Cardíaca** — Relacionada a cansaço, fadiga, inchaço, dificuldade respiratória noturna
- **Angina** — Conectada a falta de ar, aperto no tórax, palpitações

### Execução

Siga os passos no [Como Executar (passo a passo)](#como-executar-passo-a-passo) - Parte 1.

**Saída esperada:**
```
Patient 1: Há dois dias estou com uma dor no peito que piora quando faço esforço físico.
Suggested diagnosis: Infarto

Patient 2: Sinto cansaço constante há uma semana, mesmo depois de descansar.
Suggested diagnosis: Insuficiencia Cardiaca
...
```

### Limitações e Considerações

- **Simplicidade**: Sistema básico para fins educacionais
- **Correspondência exata**: Busca por substring simples, sem processamento de linguagem natural avançado
- **Dataset limitado**: Apenas 10 frases e 13 associações sintoma-doença
- **Não substitui diagnóstico médico**: Sistema demonstrativo para aprendizado

---

## Parte 2 — Classificador de Risco (TF-IDF + ML)

Esta parte implementa um sistema inteligente de classificação automática que analisa frases de sintomas relatados por pacientes e determina se representam **alto risco** ou **baixo risco**, utilizando técnicas avançadas de **Processamento de Linguagem Natural (PLN)** e **aprendizado de máquina**.

### Arquivos Principais

- **`diagnosticos.csv`** — Base de dados com 20 frases médicas simuladas, rotuladas com nível de risco
- **`classificador_risco.ipynb`** — Notebook Jupyter com implementação completa do sistema
- **`models/`** — Diretório com modelos treinados salvos (gerado automaticamente)
  - `risk_classifier_model.pkl` — Modelo de Regressão Logística treinado
  - `tfidf_vectorizer.pkl` — Vetorizador TF-IDF para transformação de texto

### Estrutura dos Dados

#### Dataset (`diagnosticos.csv`)
Base contém **100 frases** em português, balanceadas entre as classes:

**Distribuição das Classes:**
- **Alto Risco**: 50 frases (50%)
- **Baixo Risco**: 50 frases (50%)

**Exemplos de Alto Risco:**
```
"sinto dor no peito e falta de ar"
"meu coração está acelerado e sinto tontura" 
"falta de ar intensa e dor no braço esquerdo"
```

**Exemplos de Baixo Risco:**
```
"tive um leve incômodo nas costas"
"sinto um cansaço leve depois de caminhar"
"estou com um resfriado comum"
```

#### Representação Numérica (TF-IDF)
- **Input**: Frases de texto em português
- **Processamento**: TF-IDF transforma texto em vetores numéricos
- **Output**: Classificação binária (alto risco / baixo risco)
- **Dimensões**: 146 features (palavras únicas no vocabulário)

### Funcionamento Técnico

O sistema implementa um pipeline completo de Machine Learning:

#### 1. **Pré-processamento**
```python
# Divisão dos dados: 80% treino, 20% teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

#### 2. **Vetorização TF-IDF**
```python
# Transformação de texto em vetores numéricos
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)
```

#### 3. **Treinamento do Modelo**
```python
# Regressão Logística para classificação binária
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)
```

#### 4. **Avaliação e Métricas**
- **Acurácia**: 85% no conjunto de teste
- **Precision/Recall**: Análise detalhada por classe
- **F1-Score**: Métrica balanceada de performance

### Resultados Detalhados

#### Performance do Modelo
- **Acurácia Geral**: **85%** (85/100 predições corretas)
- **Tempo de Treinamento**: < 1 segundo
- **Tamanho do Modelo**: ~6KB (modelo + vetorizador)

#### Relatório de Classificação Detalhado
```
              precision    recall  f1-score   support

  alto risco       1.00      0.75      0.86        12
 baixo risco       0.73      1.00      0.84         8

    accuracy                           0.85        20
   macro avg       0.86      0.88      0.85        20
weighted avg       0.89      0.85      0.85        20
```

#### Análise de Performance por Classe
- **Alto Risco**: 100% precisão, 75% recall
- **Baixo Risco**: 73% precisão, 100% recall
- **Balanceamento**: Modelo ligeiramente tendencioso para "baixo risco"

### Testes de Inferência

O sistema foi testado com **5 frases novas** não vistas durante o treinamento:

| Frase de Teste | Predição | Confiança |
|----------------|----------|-----------|
| "sinto uma dor muito forte no peito e estou suando frio" | **alto risco** | Alta |
| "estou com um pouco de tosse e dor de cabeça leve" | **baixo risco** | Alta |
| "minha perna está dormente e não consigo mexer o braço" | **baixo risco** | Média |
| "senti um pequeno desconforto no estômago depois de comer" | **baixo risco** | Alta |
| "febre alta e dificuldade para respirar" | **alto risco** | Alta |

**Taxa de Acerto nos Testes**: 80% (4/5 predições corretas)

### Como Executar o Notebook

Veja [Como Executar (Passo a Passo)](#como-executar-passo-a-passo) - Parte 2.

### Saída Esperada

Após executar o notebook, você verá:

1. **Carregamento dos Dados**
   ```
   Shape de X_train_vec: (80, 146)
   Shape de X_test_vec: (20, 146)
   ```

2. **Treinamento**
   ```
   Modelo treinado com sucesso.
   ```

3. **Avaliação**
   ```
   Acurácia do modelo: 0.85
   Relatório de Classificação:
   [tabela detalhada de métricas]
   ```

4. **Persistência**
   ```
   Modelo e vetorizador salvos com sucesso.
   ```

5. **Testes de Predição**
   ```
   Testando a função de predição:
   Frase: 'sinto uma dor muito forte no peito...' -> Risco: alto risco
   [mais exemplos...]
   ```

### Limitações e Considerações

#### Limitações Técnicas
- **Dataset Pequeno**: 20 amostras limitam a generalização
- **Vocabulário Restrito**: Apenas 144 palavras únicas
- **Simplicidade**: Sem pré-processamento avançado (stopwords, stemming)
- **Overfitting**: Risco de memorização com dataset pequeno

#### Limitações de Domínio
- **Contexto Médico**: Não considera histórico do paciente
- **Urgência Real**: Não substitui avaliação médica profissional
- **Viés Cultural**: Treinado apenas com frases em português brasileiro
- **Especificidade**: Focado apenas em sintomas cardiológicos

#### Oportunidades de Melhoria
- **Mais Dados**: Expandir para 1000+ frases
- **Pré-processamento**: Remoção de stopwords, lematização
- **Modelos Avançados**: Random Forest, SVM, redes neurais
- **Validação Cruzada**: K-fold para avaliação mais robusta
- **Análise de Viés**: Estudo de fairness e representatividade

#### Considerações Éticas
- **Responsabilidade**: Sistema educacional, não clínico
- **Transparência**: Código aberto para auditoria
- **Privacidade**: Dados simulados, sem informações reais
- **Governança**: Reflexão sobre qualidade e justiça dos dados

---

## Estrutura do Repositório

```bash
./activity-fiap-ai-y2p2a1/
├── .venv
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── TODO.md
├── part1
│   ├── diagnosis.py
│   ├── sentences.txt
│   └── symptoms_map.txt
└── part2
    ├── models
    │   ├── risk_classifier_model.pkl
    │   └── tfidf_vectorizer.pkl
    ├── diagnosticos.csv  
    └── classificador_risco.ipynb
```

---

## Como Executar (Passo a Passo)

### Pré-requisitos

- **Python 3.8+** ([Download](https://www.python.org/downloads/))
- **Git** ([Download](https://git-scm.com/downloads))
- **Jupyter Notebook** (instalado automaticamente com as dependências)

### Instalação Completa

#### 1. **Clonar o Repositório**
```bash
# Clonar o repositório
git clone https://github.com/luisfuturist/activity-fiap-ai-y2p2a1
cd activity-fiap-ai-y2p2a1
```

#### 2. **Configurar Ambiente Virtual**
```bash
# Criar ambiente virtual
python -m venv .venv

# Ativar ambiente virtual
# Linux/Mac:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate
```

#### 3. **Instalar Dependências**
```bash
# Instalar todas as dependências
pip install -r requirements.txt

# Verificar instalação
pip list
```

### Parte 1 — Sistema de Diagnóstico

#### Executar Script de Diagnóstico
```bash
# Certificar que está no diretório raiz do projeto
cd /caminho/para/activity-fiap-ai-y2p2a1

# Executar o script
python part1/diagnosis.py
```

**Saída Esperada:**
```
Patient 1: Há dois dias estou com uma dor no peito que piora quando faço esforço físico.
Suggested diagnosis: Infarto

Patient 2: Sinto cansaço constante há uma semana, mesmo depois de descansar.
Suggested diagnosis: Insuficiencia Cardiaca
...
```

### Parte 2 — Classificador de Risco

#### VS Code (IDE Integrado)

```bash
# 1. Abrir VS Code no diretório do projeto
code .

# 2. Instalar extensão Python (se não tiver)
# 3. Abrir part2/classificador_risco.ipynb
# 4. Selecionar kernel Python (.venv)
# 5. Executar células com Shift+Enter
```

### Verificação da Execução

#### Checklist de Execução Bem-Sucedida

**Durante a Execução, você deve ver:**

1. **Carregamento dos Dados** ✅
   ```
   Shape de X_train_vec: (80, 146)
   Shape de X_test_vec: (20, 146)
   ```

2. **Treinamento do Modelo** ✅
   ```
   Modelo treinado com sucesso.
   ```

3. **Avaliação de Performance** ✅
   ```
   Acurácia do modelo: 0.85
   Relatório de Classificação:
   [tabela com métricas detalhadas]
   ```

4. **Persistência dos Modelos** ✅
   ```
   Modelo e vetorizador salvos com sucesso.
   ```

5. **Testes de Predição** ✅
   ```
   Testando a função de predição:
   Frase: 'sinto uma dor muito forte no peito...' -> Risco: alto risco
   [mais exemplos de predições]
   ```

#### Arquivos Gerados

Após execução bem-sucedida, você encontrará:

```
part2/
├── classificador_risco.ipynb
├── diagnosticos.csv
└── models/                    # ← Criado automaticamente
    ├── risk_classifier_model.pkl
    └── tfidf_vectorizer.pkl
```

## Equipe

### Membros

- Gustavo Castro (RM560831)
- Luis Emidio (RM559976)

### Professores

- **Tutor**: [Leonardo Ruiz Orabona](https://www.linkedin.com/in/leonardoorabona/)  
- **Coordenador**: [André Godoi](https://www.linkedin.com/in/profandregodoi/)  

---

[LICENSE](LICENSE)
