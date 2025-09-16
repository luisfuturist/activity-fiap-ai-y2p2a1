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
- [Estrutura do Repositório](#estrutura-do-repositório)
- [Como Executar (passo a passo)](#como-executar-passo-a-passo)
  - [Pré-requisitos](#pré-requisitos)
  - [Instalação](#instalação)
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

**Arquivos principais**
- `base_risco.csv` — dataset sintético no formato: `frase, situacao (alto risco/baixo risco)` (~40–120 exemplos).  
- `classificador.ipynb` — notebook com:
  - Pré-processamento (limpeza, stopwords pt-BR, lematização opcional).  
  - Vetorização TF-IDF.  
  - Treinamento de **LogisticRegression** e **DecisionTreeClassifier** (comparação).  
  - Validação: `train_test_split` + métricas de avaliação.  
  - Salvamento do modelo e vetor (`joblib`).  

**Abordagem técnica**
- Pipeline do Scikit-learn para encadear TF-IDF + classificador.  
- Validação: **k-fold cross-validation (k=5)**.  
- Discussão sobre viés e limitações do dataset sintético.  

---

## Estrutura do Repositório

```bash
/activity-fiap2-ai-p1a1
.
├── .venv
├── .gitignore
├── part1
│   ├── diagnosis.py
│   ├── sentences.txt
│   └── symptoms_map.txt
├── README.md
└── TODO.md
```

---

## Como Executar (passo a passo)

### Pré-requisitos

- [Python 3.8+](https://www.python.org/downloads/)

### Instalação

1. **Clonar repositório**
   ```bash
   git clone https://github.com/luisfuturist/activity-fiap2-ai-p1a1
   cd activity-fiap2-ai-p1a1
   ```

2. **Criar ambiente virtual**
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # macOS/Linux
   .venv\Scripts\activate      # Windows
   ```

3. **Instalar dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Parte 1 — Executar diagnóstico**
   - Script:
     ```bash
     python part1/diagnosis.py
     ```

5. **Parte 2 — Treinar classificador**
   - Abrir classificador.ipynb no Jupyter e executar.
   - Modelos são salvos em /modelos e relatórios gerados no notebook.

---

## Equipe

### Membros

- Gustavo Castro (RM560831)
- Luis Emidio (RM559976)

### Professores

- **Tutor**: [Leonardo Ruiz Orabona](https://www.linkedin.com/in/leonardoorabona/)  
- **Coordenador**: [André Godoi](https://www.linkedin.com/in/profandregodoi/)  

---

[LICENSE](LICENSE)
