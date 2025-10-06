# TODO - Fase 2: Diagnóstico Automatizado – IA no Estetoscópio Digital

A atividade da Fase 2 do projeto CardioIA está dividida em duas partes obrigatórias e duas opcionais ("Ir Além"), culminando na entrega de um repositório no GitHub com todos os artefatos.

Aqui estão os passos:

### Parte 1 – Frases de Sintomas + Extração de Informações

- [x] **Criar um arquivo `.txt`** com 10 frases completas que simulem descrições de sintomas de pacientes.
- [x] **Criar um arquivo `.csv`** (mapa de conhecimento) que associe sintomas a possíveis doenças (ex: `Sintoma 1 | Sintoma 2 | Doença Associada`).
- [x] **Desenvolver um código Python** (`.ipynb` ou `.py`) que:
    - [x] Lê as frases do arquivo `.txt`.
    - [x] Identifica os sintomas com base no mapa de conhecimento (`.csv`).
    - [x] Sugere um possível diagnóstico para cada frase.

### Parte 2 – Classificador Básico de Texto

- [x] **Montar uma base `.csv`** com frases médicas rotuladas com nível de risco (ex: `frase,situacao` -> `"sinto dor no peito",alto risco`).
- [x] **Desenvolver um código em um notebook `.ipynb`** que:
    - [x] Aplica o método **TF-IDF** para vetorizar as frases.
    - [x] Treina um **modelo de classificação** simples (ex: Decision Tree, Logistic Regression).
    - [x] Avalia o desempenho do modelo (ex: acurácia).

### Entregáveis Finais (Partes 1 e 2)

- [x] **Criar um repositório público** no GitHub.
- [x] **Adicionar todos os arquivos** das Partes 1 e 2 ao repositório:
    - [x] O arquivo `.txt` com as 10 frases.
    - [x] O arquivo `.csv` com o mapa de conhecimento.
    - [x] O código Python (`.ipynb` ou `.py`) da Parte 1.
    - [x] O arquivo `.csv` com as frases e rótulos de risco.
    - [x] O notebook `.ipynb` com o classificador da Parte 2.
- [x] **Gravar um vídeo de até 4 minutos** demonstrando o funcionamento completo da solução (Parte 2).
- [x] **Fazer o upload do vídeo** para o YouTube como **"Não Listado"**.
- [x] **Criar um arquivo `README.md`** completo no repositório.
- [x] **Incluir o link do vídeo** do YouTube no `README.md`.
- [x] **Submeter o link do repositório público** na plataforma.

---

## Ir Além (Opcional)

Escolha uma das opções abaixo para implementar.

### Opção 1 – Criando a Interface do CardioIA

- [ ] **Criar um repositório público** no GitHub com o nome `nome-do-grupo-cardioia-portal`.
- [ ] **Desenvolver uma aplicação em React + Vite** que contenha:
    - [ ] Autenticação simulada via Context API.
    - [ ] Listagem de pacientes (usando API fake ou JSON local).
    - [ ] Formulário de agendamento de consultas.
    - [ ] Dashboard simples.
    - [ ] Proteção de rotas.
    - [ ] Estilização (CSS Modules ou Styled Components).
- [ ] **Organizar o código-fonte** nas pastas `/contexts`, `/components`, `/services`, `/pages`.
- [ ] **Criar um `README.md`** com instruções de instalação, execução e lista dos integrantes.
- [ ] **Gravar um vídeo de até 4 minutos** demonstrando a interface.
- [ ] **Fazer o upload do vídeo** para o YouTube como **"Não Listado"** e incluir o link no `README.md`.

### Opção 2 – Diagnóstico Visual com Rede Neural

- [ ] **Criar um repositório público** no GitHub.
- [ ] **Desenvolver um notebook `.ipynb`** que:
    - [ ] Utiliza um dataset público de imagens de ECG.
    - [ ] Pré-processa as imagens (redimensiona, converte para tons de cinza).
    - [ ] Cria e implementa uma rede neural **MLP com Keras**.
    - [ ] Treina e testa o modelo.
    - [ ] Avalia a acurácia do classificador.
- [ ] **Adicionar o notebook e exemplos de imagens** ao repositório.
- [ ] **Criar um `README.md`** explicativo.
- [ ] **Gravar um vídeo de até 4 minutos** demonstrando o projeto.
- [ ] **Fazer o upload do vídeo** para o YouTube como **"Não Listado"** e incluir o link no `README.md`.
