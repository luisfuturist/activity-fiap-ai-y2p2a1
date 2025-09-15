# CardioIA - Diagnóstico Automatizado <!-- omit in toc -->

> Este projeto faz parte do curso de **Inteligência Artificial** da [FIAP](https://github.com/fiap) - Online 2024.  
> Este repositório corresponde à atividade "**Ano 2 - Fase 2** - Diagnóstico Automatizado".

## Índice <!-- omit in toc -->

- [Visão Geral do Projeto](#visão-geral-do-projeto)
- [Objetivos do Projeto](#objetivos-do-projeto)
  - [**Objetivo Geral:**](#objetivo-geral)
  - [**Objetivos Específicos:**](#objetivos-específicos)
  - [**Resultados Esperados:**](#resultados-esperados)
- [Parte 1 - Diagnóstico com Regressão Logística](#parte-1---diagnóstico-com-regressão-logística)
  - [Implementação](#implementação)
  - [Resultados Obtidos](#resultados-obtidos)
- [Parte 2 - Diagnóstico com Redes Neurais](#parte-2---diagnóstico-com-redes-neurais)
  - [Arquitetura da Rede](#arquitetura-da-rede)
  - [Treinamento e Validação](#treinamento-e-validação)
  - [Métricas de Avaliação](#métricas-de-avaliação)
- [Ir Além (Opcionais)](#ir-além-opcionais)
- [Equipe](#equipe)
  - [Membros](#membros)
  - [Professores](#professores)

---

## Visão Geral do Projeto

O **CardioIA** é um projeto acadêmico inovador do curso de Inteligência Artificial da FIAP.  
Na **Fase 2 – Diagnóstico Automatizado**, o foco está no desenvolvimento de modelos supervisionados para predição de risco cardiovascular a partir de dados clínicos.

Nesta fase, passamos da etapa de **coleta e governança de dados (Fase 1)** para a **construção de algoritmos de Machine Learning**, aplicando regressão logística e redes neurais artificiais (RNA) ao dataset de doenças cardíacas.

---

## Objetivos do Projeto

### **Objetivo Geral:**
Implementar modelos supervisionados capazes de diagnosticar a probabilidade de doença cardíaca a partir de dados clínicos estruturados.

### **Objetivos Específicos:**

1. Aplicar **Regressão Logística** para estimar probabilidades de risco.
2. Construir e treinar uma **Rede Neural Artificial** para classificação binária (doença / sem doença).
3. Comparar as métricas de desempenho entre os dois modelos.
4. Explorar melhorias opcionais, como tuning de hiperparâmetros ou outras arquiteturas.

### **Resultados Esperados:**
- Relatório comparativo de desempenho entre regressão logística e RNA.
- Visualizações das métricas de avaliação (curva ROC, matriz de confusão, acurácia, precisão, recall, F1).
- Base inicial de modelos inteligentes aplicáveis à triagem automatizada em cardiologia.

---

## Parte 1 - Diagnóstico com Regressão Logística

### Implementação
- Dataset: Cleveland Heart Disease (mesmo utilizado na Fase 1).  
- Pré-processamento: normalização dos dados e divisão em treino/teste (80/20).  
- Modelo: `LogisticRegression` (biblioteca **scikit-learn**).  

### Resultados Obtidos
- **Acurácia:** XX%  
- **Precisão:** XX%  
- **Recall:** XX%  
- **F1-score:** XX%  
- **Curva ROC-AUC:** XX  

*(Substituir pelos resultados reais após execução do notebook.)*

---

## Parte 2 - Diagnóstico com Redes Neurais

### Arquitetura da Rede
- Framework: **TensorFlow / Keras**  
- Estrutura:  
  - Camada de entrada: 13 variáveis clínicas  
  - 2 camadas ocultas (ativação ReLU)  
  - Camada de saída (sigmoide) para classificação binária  

### Treinamento e Validação
- Épocas: XX  
- Batch size: XX  
- Função de perda: `binary_crossentropy`  
- Otimizador: `adam`  
- Métricas monitoradas: `accuracy`  

### Métricas de Avaliação
- **Acurácia:** XX%  
- **Precisão:** XX%  
- **Recall:** XX%  
- **F1-score:** XX%  
- **Curva ROC-AUC:** XX  

*(Substituir pelos valores reais obtidos após treinamento.)*

---

## Ir Além (Opcionais)

Além do mínimo esperado, este projeto explorou/descreve (caso realizado):  

- 🔹 Tuning de hiperparâmetros (GridSearch / RandomSearch).  
- 🔹 Teste de arquiteturas alternativas (mais camadas ou dropout).  
- 🔹 Uso de métricas avançadas de validação cruzada.  

---

## Equipe

### Membros

- Gustavo Castro (RM560831)  
- Luis Emidio (RM559976)
  
### Professores

- **Tutor**: [Leonardo Ruiz Orabona](https://www.linkedin.com/in/leonardoorabona/)  
- **Coordenador**: [André Godoi](https://www.linkedin.com/in/profandregodoi/)  

---

[LICENSE.md](LICENSE.md)
