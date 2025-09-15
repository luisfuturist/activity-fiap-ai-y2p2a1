# CardioIA – Fase 2: Diagnóstico Automatizado – IA no Estetoscópio Digital

## Resumo
Este repositório contém a implementação da **Fase 2 – Diagnóstico Automatizado** do projeto **CardioIA (FIAP)**.  
O objetivo é simular um módulo de apoio ao diagnóstico em cardiologia usando **processamento de linguagem natural (NLP)** e **aprendizado de máquina (ML)** aplicado a relatos de sintomas e classificação de risco.

---

## Índice
- [Visão Geral](#visão-geral)
- [Objetivos](#objetivos)
- [Parte 1 — Extração de Sintomas e Sugestão de Diagnóstico](#parte-1--extração-de-sintomas-e-sugestão-de-diagnóstico)
- [Parte 2 — Classificador de Risco (TF-IDF + ML)](#parte-2--classificador-de-risco-tf-idf--ml)
- [Entregáveis e Estrutura do Repositório](#entregáveis-e-estrutura-do-repositório)
- [Como Executar (passo a passo)](#como-executar-passo-a-passo)
- [Dependências](#dependências)
- [Métricas de Avaliação e Observações Técnicas](#métricas-de-avaliação-e-observações-técnicas)
- [Rastreabilidade e Licenças](#rastreabilidade-e-licenças)
- [Equipe](#equipe)
- [Checklist de Entrega](#checklist-de-entrega)
- [Links Úteis / Referências](#links-úteis--referências)

---

## Visão Geral
A Fase 2 foca em duas tarefas obrigatórias:

1. **Parte 1** — Gerar 10 frases simuladas de pacientes, extrair sintomas via `mapa_conhecimento.csv` e sugerir diagnóstico por correspondência de padrões (string matching + regras simples).
2. **Parte 2** — Treinar um classificador de texto (TF-IDF → ML) que rotule frases em **alto risco** / **baixo risco**.

O objetivo prático é apresentar um **pipeline mínimo, reprodutível e documentado** para demonstrar conceitos de NLP, classificação e governança de dados aplicada ao domínio de saúde.

---

## Objetivos

**Geral**  
Implementar e demonstrar um sistema de apoio à triagem clínica baseado em NLP e ML, enfatizando clareza, rastreabilidade e responsabilidade de dados.

**Específicos**
- Extrair sintomas a partir de frases em linguagem natural.  
- Associar sintomas a possíveis diagnósticos via mapa de conhecimento.  
- Treinar e avaliar um classificador de risco simples usando TF-IDF e Scikit-learn.  
- Documentar e entregar repositório público com código, dados e vídeo demonstrativo.  

---

## Parte 1 — Extração de Sintomas e Sugestão de Diagnóstico

**Arquivos principais**
- `frases.txt` — 10 frases simuladas (uma frase por linha).  
- `mapa_conhecimento.csv` — mapa de conhecimento com colunas: `sintoma_1, sintoma_2, doenca_associada`.  
- `diagnostico.ipynb` / `diagnostico.py` — script/notebook que:
  - Lê `frases.txt`.  
  - Carrega `mapa_conhecimento.csv`.  
  - Normaliza o texto (minúsculas, remoção de pontuação básica).  
  - Faz pattern matching (frases → sintomas) e sugere diagnóstico.  
  - Gera `resultados_parte1.csv` com colunas: `frase, sintomas_encontrados, diagnostico_sugerido, confiança_basica`.

**Abordagem técnica**
- Tokenização simples + busca por bigramas/trigramas do mapa.  
- Regras heurísticas para conflitos (múltiplas doenças → escolher com maior número de sintomas coincidentes).  
- Notebook contém exemplos e comentários sobre limitações e vieses.  

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

## Entregáveis e Estrutura do Repositório
/fase2-cardioia
│── frases.txt
│── mapa_conhecimento.csv
│── diagnostico.ipynb
│── resultados_parte1.csv
│── base_risco.csv
│── classificador.ipynb
│── modelos/
│ └── tfidf_vectorizer.joblib
│ └── classifier.joblib
│── requirements.txt
│── README.md
│── .gitignore
│── video_demo_link.txt (link YouTube não listado)

yaml
Copy code

---

## Como Executar (passo a passo)

1. **Clonar repositório**
   ```bash
   git clone https://github.com/SEU_USUARIO/fase2-cardioia.git
   cd fase2-cardioia
Criar ambiente virtual

bash
Copy code
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows
Instalar dependências

bash
Copy code
pip install -r requirements.txt
Parte 1 — Executar diagnóstico

Notebook: abrir diagnostico.ipynb e rodar.

Script (se existir diagnostico.py):

bash
Copy code
python diagnostico.py --input frases.txt --mapa mapa_conhecimento.csv --output resultados_parte1.csv
Parte 2 — Treinar classificador

Abrir classificador.ipynb no Jupyter e executar.

Modelos são salvos em /modelos e relatórios gerados no notebook.

Dependências
Arquivo requirements.txt sugerido:

shell
Copy code
numpy>=1.21
pandas>=1.3
scikit-learn>=1.0
joblib>=1.2
jupyterlab
nltk>=3.6
unidecode>=1.3
Para usar lematização em PT-BR: instalar spacy + pt_core_news_sm.

Métricas de Avaliação e Observações Técnicas
Métricas usadas

Accuracy

Precision

Recall

F1-score (macro e micro)

Matriz de confusão

(Opcional) Curva ROC e AUC

Boas práticas

Documentar limitações (dados sintéticos, amostra pequena).

Indicar vieses e recomendações (necessidade de validação clínica).

Sistema não deve ser usado para diagnóstico real — apenas simulação educacional.

Rastreabilidade e Licenças
Todos os dados são sintéticos e gerados pela equipe.

Caso sejam usados materiais externos, incluir fonte e licença no README.

Licença recomendada: MIT ou CC BY-NC-SA → adicionar LICENSE.md.

Equipe
Gustavo Castro — RM560831 (coordenação do módulo NLP e README)

Luis Emidio — RM559976 (responsável por scripts e execução)

Matheus Conciani — RM559473 (responsável por dataset e notebooks)

Checklist de Entrega
 Repositório público no GitHub: fase2-cardioia

 frases.txt com 10 frases bem redigidas

 mapa_conhecimento.csv com ≥15 linhas

 diagnostico.ipynb / diagnostico.py funcionando

 base_risco.csv com ≥40 exemplos (classes balanceadas)

 classificador.ipynb com TF-IDF, modelos, validação e métricas

 requirements.txt e .gitignore

 Vídeo de até 4 minutos (YouTube não listado) + link no README

 Submissão do link na plataforma

Links Úteis / Referências
Scikit-learn

NLTK

TF-IDF – Scikit-learn Docs
