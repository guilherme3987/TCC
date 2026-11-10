# Roteiro para apresentação — Cognitivo: Pensamento Computacional e gamificação no engajamento de matemática para o ENEM

**Trabalho:** *Cognitivo: Pensamento Computacional e gamificação no engajamento de matemática para o Exame Nacional do Ensino Médio (ENEM)*  
**Autoria:** Guilherme dos Santos Modesto Teixeira  
**Orientação:** Prof.ª Monica de Souza Massa  
**Instituição:** Universidade do Estado da Bahia (UNEB) — Departamento de Ciências Exatas e da Terra (DCET)  
**Curso:** Bacharelado em Sistemas de Informação  
**Palavras-chave:** Pensamento Computacional; Gamificação; Engajamento; Resolução de Problemas; ENEM; Matemática.

> **Natureza deste documento:** este arquivo é um roteiro de consulta para a construção dos slides, e não uma apresentação pronta. Ele seleciona, organiza e hierarquiza os conteúdos da monografia, preservando sua terminologia e evitando reproduzir longos parágrafos.
>
> **Advertência sobre evidências:** a monografia diferencia o que foi efetivamente obtido do que era esperado. O **Cognitivo** foi concebido e desenvolvido; o **Ciclo 1** de validação com professores foi realizado e reportado; os **resultados quantitativos do Ciclo 2** com estudantes (ESM e UES) **não são apresentados na versão analisada**. Portanto, não se deve afirmar, como resultado comprovado, que houve aumento de engajamento ou de aprendizagem. Funcionalidades implementadas — XP, insígnias, ligas, penalidades — são **recursos do artefato**, não evidências de impacto.
>
> **Padrão visual das tabelas:** nos slides, as tabelas devem ser **abertas nas laterais, sem bordas verticais**. Usar apenas linhas horizontais (topo, cabeçalho e base), sem moldura externa. Ao montar no PowerPoint, Google Slides, Canva ou ferramenta equivalente, remover as bordas verticais e a moldura externa. Os pipes (`|`) deste Markdown servem apenas para organizar o conteúdo e não devem ser reproduzidos como bordas no slide.

---

## 1. Contextualização

### 1.1 Tema e cenário da pesquisa

- O **ENEM** é uma prova anual que avalia o desempenho dos estudantes ao final da educação básica, abrangendo quatro áreas — Linguagens e Códigos, Ciências Humanas, Ciências da Natureza e Matemática —, além da redação dissertativo-argumentativa.
- A nota do exame é uma das principais formas de acesso ao ensino superior no Brasil, incluindo universidades públicas e privadas, financiamento estudantil e oportunidades internacionais.
- A pesquisa situa-se na intersecção entre **ensino de Matemática**, **Pensamento Computacional (PC)** e **gamificação**, com foco na preparação para a prova de Matemática do ENEM.

### 1.2 O problema educacional que motiva o estudo

- Dados do **ENEM 2024**: a média geral subiu de **543 para 546 pontos**, mas Matemática e suas Tecnologias caiu de **535 para 529 pontos** (INEP, 2025).
- **SAEB 2023**:
  - 9º ano do Ensino Fundamental: média nacional de **257 pontos**, abaixo dos **263 pontos de 2019**;
  - **62,8%** dos alunos provavelmente não dominam nenhuma das habilidades mínimas testadas;
  - Ensino Médio: **19%** dos alunos não demonstram ter desenvolvido as competências mais basilares.
- **PISA 2022**:
  - apenas **27%** dos estudantes brasileiros atingiram o nível básico em Matemática;
  - cerca de **1%** alcançou alto desempenho (Níveis 5 ou 6);
  - entre 2012 e 2022, a proporção de alunos abaixo do Nível 2 aumentou **5 pontos percentuais**, indicando estagnação.
- As dificuldades não decorrem apenas da falta de conteúdo: envolvem **formulação dos enunciados**, **contextualização**, **complexidade linguística**, **tipo de representação** e **número de operações cognitivas** exigidas (Soares et al., 2026); **leitura e interpretação** (Piton-Gonçalves; Almeida, 2018); **esquemas cognitivos inadequados** e falta de estratégias de resolução (Pontes; Núñez, 2019); e **desengajamento**.
- A BNCC e a BNCC Computação reconhecem o PC como dimensão fundamental, mas **poucas ferramentas educacionais integram efetivamente o PC a estratégias pedagógicas engajadoras** (Resumo da monografia).

### 1.3 A resposta proposta pelo trabalho

- O trabalho propõe o **Cognitivo**, um *software* gamificado fundamentado nos **quatro pilares do PC** — decomposição, abstração, reconhecimento de padrões e algoritmos — para apoiar a resolução de questões reais de Matemática do ENEM.
- A proposta articula:
  - **PC** como estrutura analítica de resolução de problemas;
  - **gamificação** como estratégia de engajamento;
  - **questões reais do ENEM** como conteúdo pedagógico;
  - **BNCC e BNCC Computação** como referência curricular.

---

## 2. Problema de pesquisa

### 2.1 Questão central

> **“De que maneira um *software* gamificado, fundamentado no conceito do Pensamento Computacional, pode melhorar o engajamento dos estudantes durante o processo de preparação para a prova de matemática do ENEM?”**

### 2.2 Elementos articulados pela pergunta

- **Artefato:** *software* gamificado educacional.
- **Fundamento pedagógico:** pilares do Pensamento Computacional.
- **Dimensão investigada:** engajamento dos estudantes.
- **Contexto:** preparação para a prova de Matemática do ENEM.
- **Lacuna:** existência de poucas ferramentas que integrem, de forma efetiva, PC, gamificação e questões reais do ENEM.

### 2.3 Delimitação importante

- O foco declarado é o **engajamento** e a **experiência** dos estudantes durante a preparação.
- A avaliação do **impacto direto no desempenho acadêmico** e na aprendizagem é indicada nas considerações finais como possibilidade de **trabalho futuro**, não como resultado alcançado.

---

## 3. Objetivos

### 3.1 Objetivo geral

> **Conceber e avaliar um sistema educacional gamificado, fundamentado nos pilares do Pensamento Computacional, voltado ao engajamento de estudantes na resolução de questões de Matemática do ENEM.**

### 3.2 Objetivos específicos

1. **Mapear** as principais competências matemáticas das questões do ENEM e como o PC é desenvolvido.
2. **Conceber e testar** o sistema gamificado para operacionalizar a **abstração**, a **decomposição**, o **reconhecimento de padrões** e os **algoritmos** no contexto dessas questões.
3. **Validar** o artefato educacional com **professores de Matemática**.
4. **Avaliar** a experiência e o engajamento dos **estudantes**.

### 3.3 Leitura dos objetivos para a apresentação

- Os objetivos 1 e 2 estão associados à **identificação do problema** e à **construção do artefato**.
- O objetivo 3 foi trabalhado no **Ciclo 1** (grupo focal com professores).
- O objetivo 4 estava previsto para o **Ciclo 2** (alunos, com ESM e UES), mas **não apresenta resultados quantitativos na versão analisada**.
- Essa distinção deve aparecer com clareza nos slides, para não transformar uma etapa prevista em resultado conclusivo.

---

## 4. Justificativa

### 4.1 Relevância social

- A Matemática tem papel central no desenvolvimento de competências de análise e resolução de problemas.
- O baixo desempenho na área pode impactar diretamente o **acesso dos estudantes ao ensino superior**, dada a importância da nota do ENEM nos processos seletivos.
- O desengajamento e a dificuldade persistente em Matemática atingem especialmente estudantes em fase de preparação para o ENEM.

### 4.2 Relevância acadêmica e científica

- O trabalho contribui para o campo de **ensino de Computação** e para a metodologia **Design-Based Research (DBR)**, ao documentar o processo de concepção, desenvolvimento e validação de um artefato educacional.
- A pesquisa explora a articulação entre **PC** e **gamificação**, tema ainda pouco explorado em ferramentas voltadas especificamente às questões de Matemática do ENEM.
- O estudo gera **conhecimento aplicado** sobre o processo de concepção e validação e um **conjunto de dados** de questões enriquecidas por pilares do PC, que pode apoiar investigações futuras.

### 4.3 Relevância prática e pedagógica

- O Cognitivo operacionaliza os quatro pilares do PC de forma **sequencial e obrigatória**, diferentemente de abordagens que tratam o PC apenas como tema transversal.
- A proposta utiliza **questões reais do ENEM**, aproximando a ferramenta da realidade do exame.
- O sistema foi concebido para ser **alinhado à BNCC e à BNCC Computação**, com potencial de uso em contextos escolares e de preparação para o ENEM.

### 4.4 Cuidado argumentativo

- A justificativa se sustenta no **cenário de dificuldade** e na **lacuna de ferramentas**, não em resultados de impacto já comprovados.
- Evitar, nos slides, afirmações como “o Cognitivo melhora o engajamento”; o que se pode afirmar é que o trabalho **propõe e desenvolve** uma solução com essa finalidade e que o **Ciclo 1** indicou **aplicabilidade pedagógica** e pontos de melhoria.

---

## 5. Referencial teórico

### 5.1 Desempenho em Matemática e ENEM

- **ENEM:** a matriz de referência exige domínio de linguagens, construção de argumentação, compreensão de fenômenos, enfrentamento de situações-problema e interpretação de dados (INEP, 2023).
- **Piton-Gonçalves e Almeida (2018):** analisam a dificuldade e a discriminação de itens de Matemática do ENEM; destacam que os erros decorrem, em muitos casos, da **leitura e interpretação dos enunciados**, da organização textual e da desconsideração de informações visuais.
- **Pontes e Núñez (2019):** as dificuldades e os erros não são apenas falta de conhecimento, mas **esquemas cognitivos inadequados** e ausência de estratégias corretas; defendem o estímulo à argumentação lógica e ao pensamento matemático, em vez da mera repetição de fórmulas.
- **Soares et al. (2026):** a dificuldade dos itens envolve formulação do enunciado, grau de contextualização, complexidade linguística, representação mobilizada e número de operações cognitivas.
- **Jesus (2026):** defende experiências intelectualmente desafiadoras, metodologias de resolução de problemas e construção ativa de significados, com impacto na autorregulação e no engajamento.

### 5.2 Pensamento Computacional

- **Jeannette M. Wing (2006)** introduz formalmente o conceito no artigo *Computational Thinking*.
- O PC é uma **habilidade cognitiva fundamental para todos**, não restrita a cientistas da computação; é tão indispensável quanto a leitura, a escrita e a aritmética.
- Envolve:
  - **abstrair** — filtrar os aspectos importantes;
  - **decompor** — dividir uma tarefa grande em partes menores;
  - **reconhecer padrões** — investigar similaridades em grandes quantidades de dados;
  - **automatizar soluções** por meio de algoritmos.
- Wing (2006) relaciona o PC ao **raciocínio matemático** e ao **pensamento de engenharia**: a Matemática fornece fundamentos teóricos e formais; a Computação exige construir sistemas que interagem com o mundo real.
- Wing (2006) defende a **naturalização do PC**: ele deve se integrar ao cotidiano de forma tão orgânica que deixe de ser percebido como disciplina isolada, assim como a computação ubíqua se tornou presente sem ser notada.
- **Silva (2020):** investiga documentos oficiais e questões de Matemática de vestibulares/ENEM e evidencia que questões aparentemente convencionais demandam **decomposição**, **representação e automação de dados**, **abstração e generalização de padrões**, **simulação e controle de erros**.
  - Exemplos usados na monografia:
    - **Questão 143 do ENEM 2019:** leitura de gráfico, extração de dados, reconhecimento de taxa de variação constante e execução de procedimento sequencial;
    - **Questão 140 do ENEM 2018:** probabilidade, construção de hipóteses, enumeração de cenários e simulação;
    - **Questão 141 do ENEM 2018:** escala cartográfica, representação e conversão semântica entre sistemas e ordens de grandeza.

### 5.3 BNCC e BNCC Computação

- **BNCC (2017):** define as aprendizagens essenciais da Educação Básica e orienta os currículos; o PC aparece como dimensão fundamental para lidar com as tecnologias na sociedade contemporânea.
- A BNCC inicial tratava as tecnologias digitais e o PC de forma **pontual e transversal**; a BNCC Computação (2022) surge para definir **objetivos, competências e progressão curricular** próprios.
- **BNCC Computação (2022):** complemento à BNCC, estrutura o ensino de Computação em três eixos:
  1. **Pensamento Computacional**;
  2. **Mundo Digital**;
  3. **Cultura Digital**.
- O eixo do PC não se limita ao ensino de linguagens de programação: trata da capacidade de **formular, estruturar e resolver problemas** de maneira lógica, sistemática e metódica, com destaque para a **construção de algoritmos** como representação formal do raciocínio.
- A BNCC Computação também apresenta os **jogos** como ferramentas lúdicas para engajar os alunos, estimulando raciocínio lógico, resolução de problemas, reconhecimento de padrões, elaboração de algoritmos e tomada de decisões.

### 5.4 Jogos sérios e gamificação

- **Michael e Chen (2006):** definem **Jogo Sério** como um jogo cujo objetivo principal é a educação; regras, simulações, interação e feedback são compartilhados com jogos convencionais, mas a diversão assume papel secundário e a fidelidade/precisão dos processos representados torna-se prioritária.
- O envolvimento com jogos sérios favorece **aprendizagem contextualizada**, **tentativa e erro**, **feedback crítico constante** e **recompensas imediatas**.
- **Silpasuwanchai et al. (2016):** propõem um framework de engajamento para gamificação que considera motivação, objetivos, características da atividade e do usuário, além de aspectos emocionais e cognitivos.
  - Destacam o **PBL** — *Points, Badges and Leaderboards* — como conjunto de elementos de maior destaque.
  - O PBL eleva o engajamento **comportamental e cognitivo**, ampliando atenção visual, esforço e persistência voluntária.
  - Outras estratégias: desafios, *quizzes*, missões, níveis, tutoriais, dicas, barras de progresso, árvores de habilidades, avatares, compartilhamento e itens colecionáveis.
  - Ressalva importante: a percepção de diversão (**engajamento emocional**) não se traduz automaticamente em **resultados acadêmicos mais altos**.

### 5.5 Trabalhos correlatos e lacuna

| Trabalho | Contribuição | Limite/lacuna em relação ao Cognitivo |
|---|---|---|
| **Silva (2020)** | Mapeia conceitos de PC em documentos oficiais e questões de Matemática de vestibulares/ENEM. | **Não aborda gamificação**; serve como base para o mapeamento dos pilares. |
| **Lais et al. (2024)** — *Enigma Pirata* | Jogo digital gamificado de aventura para Matemática e PC (Teoria dos Conjuntos); avalia engajamento com **emoti-SAM** e **MEEGA+**, combinando Likert e questões qualitativas. | Foco em Teoria dos Conjuntos; não trata especificamente das competências de Matemática do ENEM. |
| **Teodosio e Vila Nova (2023)** | Atividade gamificada com planilhas eletrônicas e *pixel art*, usando PBL e estímulo visual. | **Não é um jogo digital** e fica limitada ao software de planilhas. |
| **Filho et al. (2025)** | Estudantes constroem artefatos digitais/games, aplicando PC para resolver problemas de Matemática e Física. | Não há **mecânicas de recompensa ou progressão estruturadas**. |
| **Este trabalho — Cognitivo** | Operacionaliza os **quatro pilares do PC de forma sequencial e obrigatória** na resolução de questões reais do ENEM; implementa **PBL completo** com XP, insígnias, ligas, matriz de penalidades e custo estratégico de dicas; processa questões reais por **pipeline ETL**. | — |

**Síntese da lacuna:** os trabalhos correlatos cobrem partes do problema — mapeamento do PC, jogos digitais, atividades gamificadas ou construção de artefatos —, mas não articulam, simultaneamente, **PC sequencial**, **gamificação estruturada** e **questões reais de Matemática do ENEM**.

### 5.6 Quadro-síntese dos principais autores

| Autor/obra | Contribuição central | Uso no trabalho |
|---|---|---|
| **Wing (2006)** | Define PC como habilidade fundamental para todos e apresenta seus pilares. | Base conceitual do Cognitivo. |
| **Silva (2020)** | Evidencia a presença do PC em questões de Matemática de vestibulares/ENEM. | Justifica o uso de questões reais e o mapeamento aos pilares. |
| **BNCC (2017) e BNCC Computação (2022)** | Estabelecem o PC como eixo curricular e os jogos como recurso pedagógico. | Alinhamento curricular e fundamentação pedagógica. |
| **Michael e Chen (2006)** | Definem jogos sérios e destacam feedback, tentativa e erro e aprendizagem contextualizada. | Base para o design do jogo e das mecânicas de feedback. |
| **Silpasuwanchai et al. (2016)** | Framework de engajamento e PBL. | Base das mecânicas de gamificação. |
| **Piton-Gonçalves e Almeida (2018)** | Dificuldades de leitura e interpretação em itens de Matemática do ENEM. | Fundamenta o foco no enunciado e no erro. |
| **Pontes e Núñez (2019)** | Erros decorrem de esquemas cognitivos e estratégias inadequadas. | Fundamenta a sequência lógica e a autorreflexão. |
| **Soares et al. (2026)** | Fatores de dificuldade dos itens de Matemática do ENEM. | Contextualiza a complexidade das questões. |
| **Jesus (2026)** | Metodologias de resolução de problemas e engajamento. | Sustenta a proposta pedagógica ativa. |
| **Brackmann et al. (2016)** | Panorama do ensino de Computação nas Américas. | Contextualiza a inserção do PC no currículo. |

---

## 6. Metodologia

### 6.1 Classificação e abordagem

- A pesquisa adota a **Design-Based Research (DBR)**, abordagem de pesquisa de design educacional (Van den Akker et al., 2006), que articula **rigor científico** e **relevância prática**.
- Características:
  - **caráter iterativo** — ciclos de análise, planejamento, desenvolvimento, avaliação e revisão;
  - **colaboração** entre pesquisadores e profissionais da educação;
  - **reflexão sistemática** e documentação explícita das decisões;
  - **postura pragmática** e contextualizada, com enfrentamento de problemas reais da escola.
- A DBR é organizada em **microciclos**: conjecturas prévias, implementação das atividades e reflexões imediatas com base nas reações e resultados observados.
- A pesquisa combina:
  - **dados qualitativos** — grupo focal com professores;
  - **dados quantitativos** — formulários ESM e UES com estudantes (previstos).

### 6.2 Etapas da DBR

| Etapa | Atividades previstas/desenvolvidas |
|---|---|
| **Identificação do problema** | Revisão Sistemática de Literatura; mapeamento das competências matemáticas das questões do ENEM e de como o PC é desenvolvido. |
| **Construção do artefato** | Definição da arquitetura e das mecânicas de gamificação; desenvolvimento da primeira versão funcional da plataforma. |
| **Ciclos de avaliação** | **Ciclo 1:** avaliação por professores de Matemática do curso de Sistemas de Informação. **Ciclo 2:** avaliação por alunos do segundo semestre do curso de Sistemas de Informação. |
| **Reflexões e melhorias** | **Ciclo 1:** refinamento do sistema a partir do feedback dos professores. **Ciclo 2:** uso do sistema pelos alunos, aplicação dos formulários ESM e UES, análise dos dados e geração de conhecimento. |

**Ressalva:** na versão analisada, o Ciclo 1 foi realizado e relatado; o Ciclo 2 é descrito no texto como etapa a ser aplicada (“Nessa etapa serão aplicados os formulários...”), sem resultados quantitativos apresentados.

### 6.3 Participantes

- **Ciclo 1 — professores:**
  - professores de Matemática do curso de Bacharelado em Sistemas de Informação;
  - grupo focal realizado **remotamente**, em **20 de outubro de 2026**, com duração de **45 minutos**;
  - a monografia refere-se a “alguns docentes”, sem detalhar o número exato de participantes.
- **Ciclo 2 — estudantes:**
  - previsto inicialmente com alunos da UPT;
  - devido a atrasos no cronograma e à coincidência com o período de aplicação do ENEM, a amostra original tornou-se inviável;
  - como plano de contingência, definiu-se a aplicação com **alunos do segundo semestre do curso de Sistemas de Informação**, utilizados como amostra representativa de estudantes que realizaram o ENEM em 2025.

### 6.4 Instrumentos de coleta

#### Grupo focal — Ciclo 1

- Técnica qualitativa para compreender percepções, experiências e significados atribuídos pelos participantes (Gil, 2021), realizada em ambiente virtual (Abreu et al., 2009).
- Sessão iniciada com **demonstração dirigida** do sistema, seguida de discussão livre e interativa.
- Critérios de avaliação:
  - exatidão dos conteúdos matemáticos (enunciados, dados e gabaritos);
  - eficiência do processamento das demandas cognitivas;
  - capacidade das mecânicas de gamificação de estimular o raciocínio;
  - aplicabilidade e relevância pedagógica do artefato.

#### ESM — *Experience Sampling Method*

- Formulário curto, com **Escala Likert de 5 pontos**, aplicado imediatamente após a interação com o sistema (Francisco, 2020).
- Tempo de preenchimento inferior a **1 minuto**.
- Três macrodimensões:
  1. **Imersão e foco** — concentração durante a resolução e equilíbrio entre desafio e dicas;
  2. **Uso do sistema** — clareza das regras, facilidade da interface e qualidade das dicas;
  3. **PC e utilidade percebida** — comparação com a resolução convencional em caderno e percepção de exercício dos quatro pilares.

#### UES — *User Engagement Scale*

- Instrumento com **12 itens obrigatórios**, em **Escala Likert de 5 pontos** (1 = Discordo totalmente; 5 = Concordo totalmente), conforme O’Brien, Cairns e Hall (2018).
- Quatro dimensões:
  1. **Atenção Focada (FA-S)** — foco, absorção e percepção temporal;
  2. **Usabilidade Percebida (PU-S)** — controle percebido e esforço de interação;
  3. **Apelo Estético (AE-S)** — atratividade e apelo visual da interface;
  4. **Recompensa (RW-S)** — benefício percebido, satisfação e disposição para recomendar o sistema.
- A estrutura com códigos padronizados viabiliza, conforme a metodologia, o cálculo do **Alfa de Cronbach** e **análises fatoriais**.

### 6.5 Análise dos dados

- **Ciclo 1:** análise qualitativa das percepções dos professores, com foco na validação dos conteúdos matemáticos, na acurácia dos gabaritos, na eficácia das mecânicas de gamificação e na adequação pedagógica do fluxo do PC.
- **Ciclo 2:** estavam previstos o cálculo do **Alfa de Cronbach** e **análises fatoriais** para verificar a consistência interna e a estrutura dimensional dos instrumentos.
- **Ressalva:** na versão analisada, não são apresentados os resultados quantitativos do Ciclo 2; portanto, as técnicas quantitativas devem ser mencionadas como **previstas**, não como concluídas.

---

## 7. Desenvolvimento da proposta

### 7.1 O que é o Cognitivo

- **Cognitivo** é um *software* educacional gamificado fundamentado nos **quatro pilares do Pensamento Computacional**.
- Finalidade: apoiar o **engajamento** de estudantes na resolução de **questões reais de Matemática do ENEM**.
- Diferencial: os pilares são operacionalizados de forma **sequencial e obrigatória**, e não apenas apresentados como conceitos transversais.

### 7.2 Fundamentação pedagógica

- **PC como estrutura de resolução de problemas:** o estudante percorre as etapas de **decomposição**, **abstração**, **reconhecimento de padrões** e **criação de algoritmos**.
- **BNCC e BNCC Computação:** alinhamento ao eixo do Pensamento Computacional e ao uso de jogos como recursos lúdicos.
- **Jogos sérios:** feedback imediato, tentativa e erro, correção rápida e aprendizagem contextualizada.
- **Gamificação:** PBL, desafios, níveis, dicas, progresso e recompensas.
- **Erro como oportunidade de aprendizagem:** as dicas orientam sem revelar a solução; as penalidades criam **custo estratégico** e estimulam a autorreflexão.
- **Usabilidade:** princípios de design de interação (Preece; Rogers; Sharp, 2013), com foco em eficácia, eficiência, segurança, utilidade, facilidade de aprendizado e facilidade de lembrança.

### 7.3 Arquitetura e tecnologias

O sistema é estruturado em **dois ambientes**, com arquitetura descrita a partir do modelo C4 (Brown, 2022) e casos de uso fundamentados em Sommerville (2011):

#### Ambiente 1 — Plataforma Educacional Gamificada

- **Front-end:** React + Tailwind CSS, com responsividade para *desktop* e *mobile*.
- **API Gateway:** FastAPI, ponto único de entrada, validação de *payloads* JSON e roteamento.
- **Motor Pedagógico e de Gamificação:** cálculo de XP, validação sequencial do progresso pelos pilares, persistência das interações.
- **Back-end:** Python 3.12 + Flask, padrão *Application Factory*, módulos de autenticação, usuários, questões e sessões.
- **Autenticação:** híbrida, com Google/Firebase e e-mail/senha; emissão de tokens JWT.
- **Banco de dados:** MySQL, com SQLAlchemy/ORM.
- **Modelo relacional:** usuários, ligas, questões, alternativas, imagens, dicas, atributos do PC, sessões de estudo, tentativas, uso de dicas, premiações de XP e insígnias.
- **Infraestrutura:** Docker, orquestrando API Flask, MySQL e servidor de desenvolvimento.

#### Ambiente 2 — Módulo ETL

- O módulo segue a concepção de fluxo de extração, transformação e carga de Kimball et al. (2004).
- **Extração:** Python com `requests` (consultas síncronas) e `httpx` (coleta assíncrona em lote) a partir de instância *self-hosted* da API ENEM DEV.
- **Transformação:** Python com Pandas e Pydantic, realizando normalização, validação e enriquecimento das questões.
- **Enriquecimento:** mapeamento de cada questão aos pilares do PC — decomposição, reconhecimento de padrões, abstração e algoritmos.
- **Armazenamento:** PostgreSQL, utilizado como área de *staging*.

**Resultado quantitativo do ETL:**

- extração de **636 registros** de questões de Matemática a partir de um conjunto inicial de **1.500 questões** disponibilizadas pela API;
- após transformação e tratamento, **551 questões** do ENEM;
- abrangência de **15 edições** do exame, no período de **2009 a 2023**.

### 7.4 Funcionamento e fluxo do estudante

- **Atores do sistema:**
  - **Estudante** — agente primário que aciona os estímulos lúdicos;
  - **Sistema** — ator externo responsável pelo processamento automatizado.
- **Casos de uso centrais:**
  - Autenticar usuário;
  - Iniciar sessão de estudo;
  - **Resolver questão** — núcleo da plataforma;
  - **Decompor enunciado**;
  - **Abstrair dados**;
  - **Reconhecer padrão**;
  - **Criar algoritmo**;
  - Solicitar dica;
  - Aplicar penalidade de XP;
  - Visualizar progresso.
- **Fluxo:** o estudante resolve a questão percorrendo as etapas do PC; pode solicitar dicas, mas isso reduz o XP; erros persistentes também reduzem o multiplicador; o sistema registra tentativas, dicas, vidas e pontuação.
- **Tela de resultados:** resume pontos, sequência de acertos, taxa de acertos, dicas utilizadas e vidas perdidas.

### 7.5 Gamificação implementada

#### PBL — *Points, Badges and Leaderboards*

- **Pontos:** PC Points (XP), concedidos por etapa concluída corretamente.
- **Insígnias:** conquistas por marcos de PC, ligas, níveis e atividade.
- **Leaderboards:** ranking geral ordenado por PC Points, paginado e com a posição do usuário destacada.

#### Distribuição de XP por etapa

| Etapa concluída | XP geral | XP de atributo |
|---|---:|---:|
| Decomposição | +2,0 | +2,0 |
| Abstração | +2,0 | +2,0 |
| Padrões | +2,0 | +2,0 |
| Algoritmos | +3,0 | +3,0 |
| Conclusão (bônus) | +1,0 | +0,25 em cada atributo |

- **Níveis:** a cada **100 XP** acumulados.
- **Ligas:** **sete** faixas — Bronze, Prata, Ouro, Platina, Diamante, Mestre e Lendário —, atribuídas automaticamente conforme a pontuação.

#### Matriz de penalidades

| Ação do usuário | Penalidade | Impacto no XP |
|---|---|---:|
| Tentativa errada | ×0,98 (−2%) | Mínimo |
| Erro persistente (3+) | ×0,90 (−10%) | Leve |
| Dica 1 | ×0,80 (−20%) | Médio |
| Dica 2 | ×0,50 (−50%) | Alto |
| Dica 3 | ×0,40 (−60%) | Crítico |

- Os fatores de erro e de dica são **cumulativos** sobre o valor base da questão.
- O aluno dispõe de **três vidas**; perde uma quando, na mesma fase, acumula três erros ou três dicas e responde incorretamente.
- Ao zerar as vidas, ocorre o *game over*, com encerramento da sessão como abandonada; os pontos conquistados permanecem.

#### Insígnias

- **24 conquistas** distribuídas em quatro categorias:
  1. **Pensamento Computacional** — 25 XP em cada pilar e uma insígnia geral aos 100 XP somados entre os pilares;
  2. **Ligas** — ascensão em cada uma das sete ligas;
  3. **Níveis** — marcos de 50, 100, 500, 1.500, 4.000 e 10.000 XP;
  4. **Atividade** — conclusão de 1, 5 ou 20 sessões e sequências de 5, 10 ou 20 acertos consecutivos.
- Cada insígnia possui nome, descrição, cor, ícone, raridade (comum, raro, épico ou lendário), categoria e critério de desbloqueio.

#### Outros recursos

- **Mascote** que oferece dicas, comenta acertos e erros e reage com expressões de alegria, tristeza e choro.
- **Efeitos sonoros**, animações de XP e tela de resultados.
- **Ranking** e progressão por ligas.
- **Dicas** com custo estratégico.
- **Vidas** e *game over*.

> **Atenção:** esses elementos são **funcionalidades implementadas**. Eles não comprovam, por si sós, aumento de engajamento ou de aprendizagem.

### 7.6 Design e usabilidade

- Design fundamentado em **usabilidade, acessibilidade e engajamento**.
- Interface limpa, organizada e com paleta de cores que favorece leitura e concentração.
- Navegação intuitiva, guiando o usuário pelas etapas de resolução de problemas.
- Metas de usabilidade: **eficácia, eficiência, segurança no uso, utilidade, facilidade de aprendizado e facilidade de lembrança**.
- O **fluxo de navegabilidade** representa a sequência de passos do usuário e é validado nos ciclos iterativos da DBR.

---

## 8. Resultados

### 8.1 Natureza dos resultados disponíveis

A monografia analisada apresenta três tipos de resultados:

1. **Resultados de desenvolvimento:** artefato construído, arquitetura, banco de dados, mecânicas de gamificação e pipeline ETL.
2. **Resultado quantitativo do ETL:** **636 registros → 551 questões**, de **15 edições** do ENEM (2009–2023).
3. **Resultados qualitativos do Ciclo 1:** percepções e sugestões dos professores no grupo focal.

**Não são apresentados, na versão analisada:**

- escores de engajamento dos estudantes (UES) ou resultados do ESM;
- Alfa de Cronbach ou análises fatoriais do Ciclo 2;
- comparação de desempenho em Matemática antes/depois do uso;
- evidência de ganho de aprendizagem.

### 8.2 Resultado do desenvolvimento e do ETL

- **636 registros** de questões de Matemática extraídos de um conjunto inicial de **1.500 questões**.
- **551 questões** após transformação e tratamento.
- **15 edições** do ENEM, de **2009 a 2023**.
- Questões enriquecidas com o mapeamento aos **quatro pilares do PC**.
- Pipeline com etapas de **extração, transformação e carga**, com armazenamento em PostgreSQL.

**O que esse resultado demonstra:** viabilidade técnica de construir uma base de questões reais do ENEM enriquecida com os pilares do PC. **O que ele não demonstra:** impacto no engajamento ou na aprendizagem.

### 8.3 Ciclo 1 — validação com professores

**Contexto:** grupo focal remoto, em **20 de outubro de 2026**, com duração de **45 minutos**, com professores de Matemática do curso de Sistemas de Informação.

#### Potencialidades identificadas

- O **erro** foi valorizado como elemento de **reforço da aprendizagem**, incentivando o estudante a refazer os passos e analisar criticamente a resolução.
- Ênfase no papel do aluno na **autoanálise** e na **reflexão sobre o próprio erro**, buscando correção autônoma.
- As **dicas** foram consideradas suporte relevante por orientarem sem revelar a solução imediata, preservando o esforço cognitivo.
- As mecânicas de gamificação — **fragmentação da questão em níveis**, **penalização de XP por erros recorrentes** e **custo estratégico do uso excessivo de auxílios** — foram percebidas como indutoras de **autorreflexão**.
- Os professores destacaram a importância de aplicar rigorosamente os conceitos de **abstração**, **decomposição** e **reconhecimento de padrões**, bem como de estruturar a **sequência lógica** das soluções.

#### Melhorias apontadas

- Aprimorar a **interação com o sistema** e a fluidez da interface.
- Reestruturar a etapa de **abstração** para focar nos pontos centrais do problema, evitando informações redundantes.
- Refinar a **decomposição** para uma fragmentação mais analítica e detalhada.
- Implementar **mecânicas de passos sequenciais** nas fases de decomposição e algoritmo, para melhor estruturação do raciocínio lógico.
- Criar um **folheto/guia de uso** com passo a passo para orientar o usuário.
- Implementar **mecanismos de orientação direcionada**, priorizando as fases com maior índice de erro.
- Oferecer **retorno mais específico e personalizado**, pois o sistema é determinístico e apresenta as mesmas respostas independentemente do contexto do estudante, limitando a personalização.

### 8.4 Ciclo 2 — estudantes

- O desenho metodológico previa a aplicação do sistema com alunos e a coleta por **ESM** e **UES**.
- A amostra foi ajustada para **alunos do segundo semestre de Sistemas de Informação**, como contingência.
- **A versão analisada da monografia não apresenta os resultados quantitativos desse ciclo.**
- Portanto, não é possível afirmar, com base nos dados disponíveis, que o Cognitivo aumentou o engajamento dos estudantes.

### 8.5 Dados de contexto não são resultados da intervenção

Os números do **ENEM 2024**, **SAEB 2023** e **PISA 2022** são **dados de contexto** utilizados para justificar a pesquisa. Eles não devem ser apresentados como resultados do Cognitivo.

### 8.6 Quadro-síntese: obtido versus esperado

| Dimensão | O que foi obtido | Status |
|---|---|---|
| **Artefato Cognitivo** | Sistema concebido e desenvolvido, com arquitetura, banco, fluxo e gamificação. | **Obtido** |
| **Base de questões** | 551 questões do ENEM, de 15 edições (2009–2023), enriquecidas com pilares do PC. | **Obtido** |
| **Validação pedagógica** | Grupo focal com professores; potencialidades e melhorias identificadas. | **Obtido** |
| **Engajamento dos estudantes** | ESM e UES previstos; resultados não apresentados na versão analisada. | **Não mensurado** |
| **Aprendizagem em Matemática** | Não avaliada diretamente. | **Não mensurado** |
| **Aumento de engajamento** | Apresentado no Resumo como expectativa (“espera-se que...”). | **Esperado, não comprovado** |

---

## 9. Discussão

### 9.1 Convergência entre os achados e o referencial teórico

- **Erro como aprendizagem:**
  - os professores valorizaram o erro como oportunidade de reflexão e correção;
  - isso dialoga com **Piton-Gonçalves e Almeida (2018)**, que destacam a compreensão do enunciado e a superação de erros, e com **Wing (2006)**, que entende o erro como parte intrínseca da resolução de problemas.
- **Gamificação e autorreflexão:**
  - a fragmentação em níveis, a penalização por erros recorrentes e o custo das dicas foram percebidos como indutores de autorreflexão;
  - isso converge com **Silpasuwanchai et al. (2016)**, que apontam pontos, recompensas e desafios como elementos de engajamento, e com **Michael e Chen (2006)**, que enfatizam feedback crítico, correção rápida e aprendizagem por tentativa e erro.
- **Pilares do PC e sequência lógica:**
  - a importância atribuída à abstração, decomposição e reconhecimento de padrões encontra respaldo em **Wing (2006)**;
  - a sugestão de passos sequenciais reforça **Pontes e Núñez (2019)**, que defendem estratégias corretas de resolução em vez de repetição de fórmulas.
- **Suporte estruturado e BNCC:**
  - a demanda por orientação direcionada e guia de uso se alinha ao eixo do PC da **BNCC**, que defende modelagem e resolução metódica de problemas com apoio de tecnologias digitais.
- **Validação da aplicabilidade:**
  - o grupo focal permitiu verificar a aplicabilidade e a relevância do artefato para além da idealização teórica, em linha com **Plomp et al. (2018)**.

### 9.2 Relação com os objetivos

| Objetivo específico | Evidência disponível | Status |
|---|---|---|
| **Mapear competências matemáticas do ENEM e o PC** | Fundamentação teórica, exemplos de questões e enriquecimento do dataset com os quatro pilares. | **Atendido** |
| **Conceber e testar o sistema gamificado** | Arquitetura, casos de uso, banco de dados, fluxo de navegação e mecânicas implementadas. | **Atendido** |
| **Validar o artefato com professores** | Grupo focal com professores de Matemática; potencialidades e melhorias. | **Atendido** |
| **Avaliar experiência e engajamento dos estudantes** | ESM e UES previstos; resultados não apresentados na versão analisada. | **Pendente/não reportado** |

### 9.3 O que os resultados permitem afirmar

- O Cognitivo é **tecnicamente viável** e foi construído com uma arquitetura que separa plataforma e ETL.
- O sistema **operacionaliza os quatro pilares do PC** de forma sequencial e obrigatória.
- A validação com professores indica **aplicabilidade pedagógica**, **coerência com o referencial teórico** e **potencial de refinamento**.
- As sugestões dos professores fornecem um **roteiro concreto de melhorias** para as próximas versões.

### 9.4 O que os resultados não permitem afirmar

- Que o Cognitivo **aumentou o engajamento** dos estudantes.
- Que houve **ganho de aprendizagem** em Matemática.
- Que as mecânicas de gamificação foram eficazes em uma amostra representativa de estudantes.
- Que o sistema está pronto para uso em larga escala sem os ajustes apontados.

### 9.5 Limitações que emergem da discussão

- **Feedback determinístico:** o sistema apresenta as mesmas respostas independentemente do contexto do estudante, limitando a personalização.
- **Amostra de contingência:** o Ciclo 2 foi redirecionado para alunos do segundo semestre de Sistemas de Informação, e não para a amostra originalmente prevista.
- **Ausência de resultados quantitativos do Ciclo 2:** não há escores de engajamento ou análises psicométricas reportadas.
- **Integração ETL–plataforma ainda não automatizada:** a sincronização automatizada é indicada como trabalho futuro.
- **Validação concentrada no Ciclo 1:** a percepção dos professores é relevante, mas não substitui a avaliação com estudantes.

---

## 10. Considerações finais

### 10.1 Principais conclusões

- O trabalho **concebeu e desenvolveu** o Cognitivo, um *software* gamificado fundamentado nos quatro pilares do PC para a resolução de questões de Matemática do ENEM.
- Foi construído um **pipeline ETL** que resultou em uma base de **551 questões** de **15 edições** do ENEM (2009–2023), enriquecidas com os pilares do PC.
- A **validação com professores** indicou que o artefato tem aplicabilidade pedagógica, coerência com o referencial teórico e potencial para estimular a autorreflexão sobre o erro.
- O Ciclo 1 também produziu um conjunto de **melhorias concretas**, especialmente sobre abstração, decomposição, sequência lógica, orientação personalizada e guia de uso.
- A **avaliação de engajamento com estudantes** não está concluída nem reportada na versão analisada; logo, a expectativa de aumento de engajamento permanece como **hipótese/expectativa**, não como resultado comprovado.

### 10.2 Contribuições do trabalho

- **Contribuição prática:** desenvolvimento de um artefato educacional gamificado com questões reais do ENEM e fluxo baseado no PC.
- **Contribuição técnica:** arquitetura de *software*, modelo de dados, API, módulo ETL e mecânicas de gamificação documentadas.
- **Contribuição científica:** aplicação da DBR em um contexto de ensino de Computação, com documentação do processo de concepção, desenvolvimento e validação.
- **Contribuição metodológica:** proposição de um desenho de avaliação que integra PC, gamificação e medidas de experiência/engajamento por meio de ESM e UES.
- **Contribuição social:** potencial de apoiar estudantes na preparação para o ENEM e de contribuir para mitigar as dificuldades identificadas no ensino de Matemática.
- **Contribuição de dados:** base de questões enriquecida com os pilares do PC, reutilizável em pesquisas futuras.

### 10.3 Limitações

- Resultados quantitativos do Ciclo 2 **não apresentados**.
- Ausência de avaliação direta de **aprendizagem** ou de **desempenho acadêmico**.
- **Feedback determinístico**, com baixa personalização.
- **Amostra de contingência** no Ciclo 2.
- **Integração ETL–plataforma** ainda não automatizada.
- Validação com professores sem detalhamento do número de participantes.
- Necessidade de refinamentos pedagógicos e de usabilidade apontados pelo grupo focal.

### 10.4 Trabalhos futuros

- **Automatizar a integração entre o Módulo ETL e o Sistema Gamificado**, por meio de *endpoint* protegido no contêiner da API Gateway, eliminando a intervenção humana no pipeline e garantindo atualização contínua do acervo.
- **Avaliar o impacto direto do sistema no desempenho acadêmico e na aprendizagem em Matemática**, utilizando mineração de dados educacionais.
- Cruzar **históricos de cliques**, **tempos de resposta em cada pilar** e **curva de consumo de pistas** com o desempenho acadêmico real, para rastrear a evolução do aluno.
- Implementar as melhorias indicadas no Ciclo 1:
  - passos sequenciais na decomposição e no algoritmo;
  - orientação direcionada para fases com maior índice de erro;
  - guia/folheto de uso;
  - feedback mais específico e personalizado.

### 10.5 Mensagem final para a apresentação

> O Cognitivo representa uma proposta consistente de integração entre **Pensamento Computacional**, **gamificação** e **questões reais do ENEM**. O trabalho demonstra a **viabilidade técnica e pedagógica** do artefato e fornece uma base sólida para avaliações futuras de engajamento e aprendizagem. Os resultados disponíveis sustentam a **relevância da proposta**, mas não permitem afirmar, ainda, que houve aumento de engajamento ou de desempenho.

---

# Estrutura sugerida da apresentação

> **Sugestão geral:** 18 a 19 slides, com duração de 15 a 20 minutos. Para uma apresentação mais curta, fundir os slides 5 e 8, os slides 14 e 15, e os slides 17 e 18. Deixar como *backup*: modelo relacional do banco, diagramas C4 de back-end/front-end, formulários ESM e UES.
>
> **Tabelas:** montar todas no estilo aberto, sem bordas verticais e sem moldura externa, usando apenas linhas horizontais de separação.

## Slide 1 — Capa

- **Título:** Cognitivo: Pensamento Computacional e gamificação no engajamento de matemática para o ENEM.
- **Identificação:** autor, orientadora, UNEB/DCET, curso de Sistemas de Informação, ano.
- **Palavras-chave:** PC; Gamificação; Engajamento; Resolução de Problemas; ENEM; Matemática.

**Destaque:** apresentar o título e a articulação central do trabalho em uma frase.

**Sugestão visual:** capa institucional; sem figura da monografia.

---

## Slide 2 — Contextualização: o desafio da Matemática no ENEM

- O ENEM como principal via de acesso ao ensino superior.
- Queda em Matemática no ENEM 2024: **535 → 529**, enquanto a média geral subiu **543 → 546**.
- SAEB 2023: **257 pontos** no 9º ano; **62,8%** sem habilidades mínimas; **19%** no Ensino Médio sem competências basilares.
- PISA 2022: **27%** no nível básico; **1%** em alto desempenho; **+5 p.p.** abaixo do Nível 2 em uma década.

**Destaque:** os números que justificam a pesquisa.

**Sugestão visual:** tabela-síntese com as três avaliações, em estilo aberto (elaborada a partir dos dados do texto; a monografia não apresenta gráfico consolidado).

---

## Slide 3 — Problema de pesquisa

- Questão central em destaque.
- Elementos: *software* gamificado + PC + engajamento + Matemática do ENEM.
- Lacuna: poucas ferramentas integram PC, gamificação e questões reais do ENEM.

**Destaque:** ler a pergunta de pesquisa na íntegra e explicar seus três núcleos.

**Sugestão visual:** diagrama simples com os três núcleos (artefato, PC, engajamento); sem figura da monografia.

---

## Slide 4 — Objetivos

- **Objetivo geral:** conceber e avaliar um sistema educacional gamificado fundamentado nos pilares do PC.
- **Objetivos específicos:**
  1. mapear competências matemáticas do ENEM e o PC;
  2. conceber e testar o sistema;
  3. validar com professores;
  4. avaliar experiência e engajamento dos estudantes.

**Destaque:** “conceber e avaliar”; “quatro pilares”; “professores”; “estudantes”.

**Sugestão visual:** quadro que relacione cada objetivo específico à etapa da DBR, em estilo aberto (elaborado para o slide; inspirado no Quadro “Etapas do DBR”).

---

## Slide 5 — Justificativa e relevância

- **Social:** baixo desempenho em Matemática impacta o acesso ao ensino superior.
- **Acadêmica:** lacuna de ferramentas que integrem PC e gamificação; contribuição para o ensino de Computação e para a DBR.
- **Prática:** alinhamento à BNCC/BNCC Computação; uso de questões reais do ENEM.
- **Científica:** documentação do processo de concepção e validação e base de dados enriquecida.

**Destaque:** a justificativa se apoia no cenário e na lacuna, não em impacto já comprovado.

**Sugestão visual:** três colunas — relevância social, acadêmica e prática.

---

## Slide 6 — Fundamentação I: Pensamento Computacional

- **Wing (2006):** PC como habilidade fundamental para todos; não restrito a cientistas da computação.
- **Quatro pilares:** decomposição, abstração, reconhecimento de padrões e algoritmos.
- **Silva (2020):** o PC está presente em questões de Matemática de vestibulares/ENEM.
- Exemplos: **Questão 143/2019**, **Questão 140/2018**, **Questão 141/2018**.

**Destaque:** os quatro pilares e a relação com a resolução de problemas matemáticos.

**Sugestão visual:** Figura “Questão 143 do ENEM 2019” (`Questao_143.png`) ou “Questão 140 do ENEM 2018” (`Questao_140.png`), usada para mostrar a mobilização dos pilares.

---

## Slide 7 — Fundamentação II: BNCC, jogos sérios e gamificação

- **BNCC (2017)** e **BNCC Computação (2022):** três eixos — PC, Mundo Digital e Cultura Digital.
- **Jogos sérios (Michael; Chen, 2006):** educação como objetivo principal; feedback, tentativa e erro, aprendizagem contextualizada.
- **Gamificação (Silpasuwanchai et al., 2016):** PBL; desafios, níveis, dicas, progresso; engajamento comportamental, emocional e cognitivo.
- **Ressalva:** diversão não se converte automaticamente em resultado acadêmico.

**Destaque:** PBL e os três eixos da BNCC Computação.

**Sugestão visual:** Figura “Eixos fundamentais da BNCC Computação” (`bncc_computacao.png`).

---

## Slide 8 — Trabalhos correlatos e diferencial

- **Silva (2020):** mapeamento do PC; não aborda gamificação.
- **Lais et al. (2024):** *Enigma Pirata*; jogo digital, Teoria dos Conjuntos, avaliação de engajamento.
- **Teodosio e Vila Nova (2023):** atividade gamificada com planilhas e *pixel art*; não é jogo digital.
- **Filho et al. (2025):** construção de artefatos pelos estudantes; sem recompensas/progressão estruturadas.
- **Cognitivo:** PC sequencial e obrigatório + PBL completo + questões reais do ENEM via ETL.

**Destaque:** a linha “Este trabalho” do quadro comparativo.

**Sugestão visual:** Quadro “Análise comparativa dos trabalhos correlatos” (essencial).

---

## Slide 9 — Metodologia: Design-Based Research

- DBR: iterativa, colaborativa, pragmática e com reflexão sistemática.
- Quatro etapas: identificação do problema; construção do artefato; ciclos de avaliação; reflexões e melhorias.
- Microciclos: conjectura → implementação → reflexão.
- **Ciclo 1:** professores. **Ciclo 2:** alunos.

**Destaque:** o caráter iterativo e a separação entre os dois ciclos.

**Sugestão visual:** Figura “Fluxo geral do DBR” (`fluxo_dbr_final.png`) e/ou Quadro “Etapas do DBR e seus respectivos desenvolvimentos”.

---

## Slide 10 — Cognitivo: visão geral e arquitetura

- *Software* gamificado baseado nos quatro pilares do PC.
- Dois ambientes: **Plataforma Educacional Gamificada** e **Módulo ETL**.
- Tecnologias: React/Tailwind; FastAPI; Flask/Python 3.12; MySQL; PostgreSQL; Docker; JWT.
- Separação de responsabilidades e escalabilidade.

**Destaque:** a arquitetura em dois ambientes e o fluxo HTTPS/JSON.

**Sugestão visual:** Figura “Diagrama de Arquitetura” (`diagrama_arquitetura.png`). Guardar os diagramas C4 de back-end e front-end como *backup*.

---

## Slide 11 — Módulo ETL e base de questões

- **Extração:** API ENEM DEV *self-hosted*; `requests` e `httpx`.
- **Transformação:** Pandas e Pydantic; normalização, validação e enriquecimento.
- **Carga:** PostgreSQL como *staging*.
- **Resultado:** **1.500 questões → 636 registros → 551 questões**; **15 edições**; **2009–2023**.

**Destaque:** os números **636**, **551** e **15 edições**.

**Sugestão visual:** diagrama E-T-L simples (elaborado para o slide) ou a Figura “Diagrama de Arquitetura”. Não há figura específica do ETL na monografia.

---

## Slide 12 — Funcionamento: resolução guiada pelos pilares

- Atores: **Estudante** e **Sistema**.
- Caso de uso central: **Resolver Questão**.
- Extensões: **Decompor Enunciado**, **Abstrair Dados**, **Reconhecer Padrão**, **Criar Algoritmo**.
- Apoio: **Solicitar Dica**, **Aplicar Penalidade de XP**, **Visualizar Progresso**.
- Fluxo sequencial e obrigatório; dicas com custo; três vidas; tela de resultados.

**Destaque:** “quatro pilares de forma sequencial e obrigatória”.

**Sugestão visual:** Figura “Diagrama de Caso de Uso” (`Diagrma_de_Caso_De_Uso.png`) e/ou Figura “Fluxo de navegabilidade”.

---

## Slide 13 — Gamificação implementada

- **PBL:** pontos (XP), insígnias e *leaderboards*.
- **XP:** +2/+2/+2 nas etapas iniciais; +3 em algoritmos; bônus de +1 e +0,25 por atributo.
- **Níveis:** a cada 100 XP. **Ligas:** Bronze a Lendário (7 faixas).
- **Penalidades:** ×0,98; ×0,90; ×0,80; ×0,50; ×0,40; cumulativas.
- **24 insígnias** em 4 categorias; **3 vidas**; *game over*.
- Mascote, efeitos sonoros, animações e tela de resultados.

**Destaque:** Tabela de XP, matriz de penalidades e catálogo de insígnias.

**Sugestão visual:** Tabela “Distribuição de pontos de experiência (XP) por etapa concluída”; Tabela “Matriz de penalidades”; Quadro “Composição do catálogo de insígnias”. Escolher duas dessas três para não sobrecarregar o slide.

---

## Slide 14 — Validação com professores: resultados

- Grupo focal remoto, **20/10/2026**, **45 minutos**, professores de Matemática do curso de SI.
- **Potencialidades:**
  - erro como reforço e oportunidade de autorreflexão;
  - dicas que orientam sem revelar a solução;
  - fragmentação em níveis, penalidades e custo das dicas induzem reflexão;
  - importância dos pilares e da sequência lógica.
- **Natureza:** resultado **qualitativo**, não escore de engajamento.

**Destaque:** “validação de aplicabilidade pedagógica”, não “aumento de engajamento”.

**Sugestão visual:** quadro-síntese “Potencialidades identificadas” (elaborado a partir do capítulo “Análise de Dados”; não há tabela/gráfico de resultados na monografia).

---

## Slide 15 — Melhorias apontadas pelo grupo focal

- Aprimorar interação/UX.
- Abstração: focar nos pontos centrais, sem redundâncias.
- Decomposição: fragmentação mais analítica.
- Passos sequenciais em decomposição e algoritmo.
- Guia/folheto de uso.
- Orientação direcionada por índice de erro.
- Feedback mais específico e personalizado (sistema determinístico).

**Destaque:** as sugestões são **desdobramentos para as próximas versões**, não resultados de impacto.

**Sugestão visual:** quadro “Dimensão → sugestão” (elaborado a partir do texto; não presente na monografia).

---

## Slide 16 — Discussão: teoria e prática

- **Erro:** professores ↔ Piton-Gonçalves e Almeida (2018); Wing (2006).
- **Gamificação:** fragmentação, penalidades e dicas ↔ Silpasuwanchai et al. (2016); Michael e Chen (2006).
- **Pilares e sequência:** ↔ Wing (2006); Pontes e Núñez (2019).
- **Suporte estruturado:** ↔ BNCC/BNCC Computação.
- **Aplicabilidade:** ↔ Plomp et al. (2018).

**Destaque:** a convergência entre os achados e o referencial; a validação é de **aplicabilidade**, não de impacto.

**Sugestão visual:** tabela “Achado → autor(es) → contribuição” (elaborada para o slide). Se preferir, usar um mapa conceitual simples.

---

## Slide 17 — Limitações e o que não foi medido

- Ciclo 2 com estudantes: resultados **não apresentados**.
- Sem escores de UES/ESM, Alfa de Cronbach ou análises fatoriais reportadas.
- Sem avaliação de aprendizagem/desempenho acadêmico.
- Feedback determinístico e pouco personalizado.
- Amostra de contingência (alunos do 2º semestre de SI).
- Integração ETL–plataforma ainda não automatizada.
- Número de professores participantes não detalhado.

**Destaque:** separar claramente **obtido** de **esperado/não medido**.

**Sugestão visual:** tabela “Obtido versus esperado” (elaborada a partir do texto; não presente na monografia).

---

## Slide 18 — Considerações finais e contribuições

- O Cognitivo foi **concebido e desenvolvido**.
- Base de **551 questões** de **15 edições** do ENEM.
- Validação com professores indica **aplicabilidade pedagógica** e **coerência teórica**.
- Contribuições: prática, técnica, científica, metodológica, social e de dados.
- A expectativa de aumento de engajamento permanece **a ser avaliada** com estudantes.

**Destaque:** “viabilidade técnica e pedagógica” + “impacto ainda não mensurado”.

**Sugestão visual:** linha do tempo do percurso — problema → referencial → artefato → ETL → validação com professores → melhorias → avaliação futura.

---

## Slide 19 — Trabalhos futuros e referências principais

- **Trabalhos futuros:**
  - automatizar a integração ETL–plataforma via API interna;
  - avaliar impacto no desempenho acadêmico com mineração de dados educacionais;
  - implementar as melhorias do Ciclo 1.
- **Referências principais:** Wing (2006); Silva (2020); Michael e Chen (2006); Silpasuwanchai et al. (2016); Piton-Gonçalves e Almeida (2018); Pontes e Núñez (2019); BNCC (2017); BNCC Computação (2022); O’Brien, Cairns e Hall (2018); Gil (2021); Plomp et al. (2018).
- **Referências metodológicas/técnicas:** Van den Akker et al. (2006); Sommerville (2011); Brown (2022); Kimball et al. (2004).

**Destaque:** fechar com a contribuição do trabalho e o próximo passo de pesquisa.

**Sugestão visual:** slide de encerramento com agradecimento; sem figura.

---

## Resumo visual da sequência

| Bloco | Slides | Função |
|---|---|---|
| Abertura e problema | 1–3 | Situar o tema, os dados e a pergunta. |
| Objetivos e justificativa | 4–5 | Explicitar o que se pretende e por quê. |
| Fundamentação e lacuna | 6–8 | Sustentar teoricamente e mostrar o diferencial. |
| Metodologia e artefato | 9–13 | Explicar o percurso, a arquitetura e a gamificação. |
| Resultados e discussão | 14–17 | Apresentar o que foi obtido, interpretar e delimitar. |
| Fechamento | 18–19 | Concluir, contribuir e apontar continuidade. |

---

# Conteúdo dos slides (texto pronto para transpor)

> **Como usar:** esta seção complementa a estrutura sugerida acima. Cada bloco traz o texto enxuto que pode ir diretamente para o slide, a indicação do recurso visual e uma fala curta para orientar a exposição. Ajuste a quantidade de tópicos ao tempo disponível.

## Slide 1 — Capa

**Texto no slide:**
- **Cognitivo:** Pensamento Computacional e gamificação no engajamento de Matemática para o ENEM
- Guilherme dos Santos Modesto Teixeira
- Orientação: Prof.ª Monica de Souza Massa
- UNEB — DCET | Bacharelado em Sistemas de Informação | 2026

**Visual:** capa institucional da UNEB/DCET, sem figura da monografia.

> **Fala sugerida:** “Este trabalho investiga como um *software* gamificado, fundamentado no Pensamento Computacional, pode apoiar o engajamento de estudantes na preparação para a prova de Matemática do ENEM.”

---

## Slide 2 — Contextualização: o desafio da Matemática no ENEM

**Texto no slide:**
- O ENEM é uma das principais vias de acesso ao ensino superior no Brasil.
- **ENEM 2024:** média geral subiu de **543 para 546**; Matemática caiu de **535 para 529**.
- **SAEB 2023:** 9º ano com **257 pontos** (abaixo dos **263** de 2019); **62,8%** sem habilidades mínimas; **19%** do Ensino Médio sem competências basilares.
- **PISA 2022:** **27%** no nível básico; **~1%** em alto desempenho; **+5 p.p.** abaixo do Nível 2 em uma década.

**Tabela para o slide:**

| Avaliação | O que os dados mostram |
|---|---|
| **ENEM 2024** | Média geral subiu de 543 para 546; Matemática caiu de 535 para 529. |
| **SAEB 2023** | 9º ano: 257 pontos (2019: 263); 62,8% sem habilidades mínimas; 19% do EM sem competências basilares. |
| **PISA 2022** | 27% no nível básico; ~1% em alto desempenho; +5 p.p. abaixo do Nível 2 em uma década. |

> **Fala sugerida:** “Esses números não são resultados do Cognitivo; eles dimensionam o problema educacional que motiva a pesquisa.”

---

## Slide 3 — Problema de pesquisa

**Texto no slide:**
- **Pergunta central:** “De que maneira um *software* gamificado, fundamentado no conceito do Pensamento Computacional, pode melhorar o engajamento dos estudantes durante o processo de preparação para a prova de Matemática do ENEM?”
- **Núcleos:** artefato gamificado + Pensamento Computacional + engajamento + Matemática do ENEM.
- **Lacuna:** poucas ferramentas integram, simultaneamente, PC, gamificação e questões reais do ENEM.

**Visual:** diagrama simples com os três núcleos (artefato, PC e engajamento) ao redor da pergunta.

> **Fala sugerida:** “A pergunta articula três elementos centrais: o artefato, o fundamento pedagógico e a dimensão investigada — o engajamento na preparação para o ENEM.”

---

## Slide 4 — Objetivos

**Texto no slide:**
- **Objetivo geral:** conceber e avaliar um sistema educacional gamificado, fundamentado nos pilares do PC, voltado ao engajamento de estudantes na resolução de questões de Matemática do ENEM.
- **Objetivos específicos:**
  1. Mapear competências matemáticas do ENEM e o desenvolvimento do PC.
  2. Conceber e testar o sistema gamificado.
  3. Validar o artefato com professores de Matemática.
  4. Avaliar a experiência e o engajamento dos estudantes.

**Quadro para o slide:**

| Objetivo específico | Etapa da DBR |
|---|---|
| 1. Mapear competências e PC | Identificação do problema |
| 2. Conceber e testar o sistema | Construção do artefato |
| 3. Validar com professores | Ciclo 1 |
| 4. Avaliar experiência e engajamento | Ciclo 2 (previsto; resultados não apresentados) |

> **Fala sugerida:** “O objetivo geral é conceber e avaliar; os específicos mostram o percurso: mapear, construir, validar com professores e avaliar com estudantes.”

---

## Slide 5 — Justificativa e relevância

**Texto no slide:**
- **Social:** o baixo desempenho em Matemática impacta o acesso ao ensino superior.
- **Acadêmica:** lacuna de ferramentas que integrem PC e gamificação; contribuição para o ensino de Computação e para a DBR.
- **Prática:** alinhamento à BNCC e à BNCC Computação; uso de questões reais do ENEM.
- **Científica:** documentação do processo de concepção e validação e base de dados enriquecida com os pilares do PC.

**Visual:** três colunas — relevância social, acadêmica e prática.

> **Fala sugerida:** “A justificativa se sustenta no cenário de dificuldade e na lacuna de ferramentas, não em resultados de impacto já comprovados.”

---

## Slide 6 — Fundamentação I: Pensamento Computacional

**Texto no slide:**
- **Wing (2006):** o PC é uma habilidade fundamental para todos, não restrita a cientistas da computação.
- **Quatro pilares:** decomposição, abstração, reconhecimento de padrões e algoritmos.
- **Silva (2020):** o PC está presente em questões de Matemática de vestibulares e do ENEM.
- **Exemplos:** Questão 143/2019; Questão 140/2018; Questão 141/2018.

**Visual:** figura “Questão 143 do ENEM 2019” (`Questao_143.png`) ou “Questão 140 do ENEM 2018” (`Questao_140.png`), mostrando a mobilização dos pilares.

> **Fala sugerida:** “Os quatro pilares não são um conteúdo à parte: eles funcionam como estrutura para ler, decompor e resolver a questão.”

---

## Slide 7 — Fundamentação II: BNCC, jogos sérios e gamificação

**Texto no slide:**
- **BNCC (2017) e BNCC Computação (2022):** três eixos — Pensamento Computacional, Mundo Digital e Cultura Digital.
- **Jogos sérios (Michael; Chen, 2006):** a educação é o objetivo principal; feedback, tentativa e erro e aprendizagem contextualizada.
- **Gamificação (Silpasuwanchai et al., 2016):** PBL (*Points, Badges and Leaderboards*); engajamento comportamental, emocional e cognitivo.
- **Ressalva:** diversão não se converte automaticamente em resultado acadêmico.

**Visual:** figura “Eixos fundamentais da BNCC Computação” (`bncc_computacao.png`).

> **Fala sugerida:** “A BNCC Computação dá o enquadramento curricular; os jogos sérios e o PBL dão a estratégia de engajamento.”

---

## Slide 8 — Trabalhos correlatos e diferencial

**Texto no slide:**

| Trabalho | Foco | Limite/diferencial |
|---|---|---|
| **Silva (2020)** | Mapeamento do PC em questões de Matemática | Não aborda gamificação. |
| **Lais et al. (2024)** — *Enigma Pirata* | Jogo digital; Teoria dos Conjuntos; engajamento | Não foca nas competências de Matemática do ENEM. |
| **Teodosio e Vila Nova (2023)** | Atividade gamificada com planilhas e *pixel art* | Não é um jogo digital. |
| **Filho et al. (2025)** | Estudantes constroem artefatos digitais/games | Sem recompensas ou progressão estruturadas. |
| **Cognitivo** | **PC sequencial + PBL + questões reais do ENEM** | **Integra os três elementos.** |

**Visual:** quadro “Análise comparativa dos trabalhos correlatos” (essencial).

> **Fala sugerida:** “Os correlatos cobrem partes do problema; o diferencial do Cognitivo é articular, ao mesmo tempo, PC sequencial, gamificação estruturada e questões reais do ENEM.”

---

## Slide 9 — Metodologia: Design-Based Research

**Texto no slide:**
- **DBR:** abordagem iterativa, colaborativa, pragmática e com reflexão sistemática.
- **Etapas:** identificação do problema → construção do artefato → ciclos de avaliação → reflexões e melhorias.
- **Microciclos:** conjectura → implementação → reflexão.
- **Ciclo 1:** professores de Matemática. **Ciclo 2:** estudantes (previsto).

**Visual:** figura “Fluxo geral do DBR” (`fluxo_dbr_final.png`) e/ou quadro “Etapas do DBR e seus respectivos desenvolvimentos”.

> **Fala sugerida:** “A DBR organiza o trabalho em ciclos: o Ciclo 1 validou o artefato com professores; o Ciclo 2, com estudantes, está previsto e não apresenta resultados quantitativos na versão analisada.”

---

## Slide 10 — Cognitivo: visão geral e arquitetura

**Texto no slide:**
- *Software* gamificado fundamentado nos quatro pilares do PC.
- **Dois ambientes:** Plataforma Educacional Gamificada e Módulo ETL.
- **Tecnologias:** React + Tailwind CSS; FastAPI; Flask/Python 3.12; MySQL; PostgreSQL; Docker; JWT.
- Separação de responsabilidades entre interface, API, motor pedagógico e pipeline de dados.

**Visual:** figura “Diagrama de Arquitetura” (`diagrama_arquitetura.png`). Guardar os diagramas C4 de *back-end* e *front-end* como *backup*.

> **Fala sugerida:** “A arquitetura separa a plataforma que o estudante usa do módulo que prepara e enriquece a base de questões.”

---

## Slide 11 — Módulo ETL e base de questões

**Texto no slide:**
- **Extração:** API ENEM DEV *self-hosted*; `requests` e `httpx`.
- **Transformação:** Pandas e Pydantic; normalização, validação e enriquecimento.
- **Carga:** PostgreSQL como área de *staging*.
- **Resultado:** **1.500 questões → 636 registros → 551 questões**; **15 edições**; **2009–2023**.

**Visual:** diagrama E-T-L simples (elaborado para o slide) ou a figura “Diagrama de Arquitetura”. Não há figura específica do ETL na monografia.

> **Fala sugerida:** “O ETL demonstra a viabilidade técnica de construir uma base de questões reais enriquecida com os pilares do PC — mas não mede impacto no engajamento.”

---

## Slide 12 — Funcionamento: resolução guiada pelos pilares

**Texto no slide:**
- **Atores:** Estudante e Sistema.
- **Caso de uso central:** Resolver Questão.
- **Etapas:** Decompor Enunciado → Abstrair Dados → Reconhecer Padrão → Criar Algoritmo.
- **Apoio:** Solicitar Dica; Aplicar Penalidade de XP; Visualizar Progresso.
- Fluxo sequencial e obrigatório; três vidas; tela de resultados.

**Visual:** figura “Diagrama de Caso de Uso” (`Diagrma_de_Caso_De_Uso.png`) e/ou figura “Fluxo de navegabilidade”.

> **Fala sugerida:** “O estudante não pula etapas: ele percorre os quatro pilares na ordem, e as dicas têm custo estratégico.”

---

## Slide 13 — Gamificação implementada

**Texto no slide:**
- **PBL:** pontos (XP), insígnias e *leaderboards*.
- **Níveis:** a cada 100 XP. **Ligas:** Bronze a Lendário (7 faixas).
- **24 insígnias** em 4 categorias; **3 vidas**; *game over*.
- Mascote, efeitos sonoros, animações e tela de resultados.

**Tabela de XP:**

| Etapa | XP geral | XP de atributo |
|---|---:|---:|
| Decomposição | +2,0 | +2,0 |
| Abstração | +2,0 | +2,0 |
| Padrões | +2,0 | +2,0 |
| Algoritmos | +3,0 | +3,0 |
| Conclusão (bônus) | +1,0 | +0,25 por atributo |

**Matriz de penalidades:**

| Ação | Penalidade |
|---|---:|
| Tentativa errada | ×0,98 |
| Erro persistente (3+) | ×0,90 |
| Dica 1 | ×0,80 |
| Dica 2 | ×0,50 |
| Dica 3 | ×0,40 |

**Visual:** escolher duas das três opções — tabela de XP, matriz de penalidades ou quadro “Composição do catálogo de insígnias” — para não sobrecarregar o slide.

> **Fala sugerida:** “Esses elementos são funcionalidades implementadas; eles não comprovam, por si sós, aumento de engajamento ou de aprendizagem.”

---

## Slide 14 — Validação com professores: resultados

**Texto no slide:**
- **Grupo focal remoto:** 20/10/2026, 45 minutos, professores de Matemática do curso de Sistemas de Informação.
- **Potencialidades identificadas:**
  - erro como reforço e oportunidade de autorreflexão;
  - dicas que orientam sem revelar a solução;
  - fragmentação em níveis, penalidades e custo das dicas induzindo reflexão;
  - importância dos pilares e da sequência lógica.
- **Natureza:** resultado qualitativo, não escore de engajamento.

**Visual:** quadro-síntese “Potencialidades identificadas” (elaborado a partir do capítulo “Análise de Dados”).

> **Fala sugerida:** “O grupo focal indica aplicabilidade pedagógica e coerência teórica; não é uma medida de aumento de engajamento.”

---

## Slide 15 — Melhorias apontadas pelo grupo focal

**Texto no slide:**
- Aprimorar a interação e a fluidez da interface.
- **Abstração:** focar nos pontos centrais, sem redundâncias.
- **Decomposição:** fragmentação mais analítica.
- Passos sequenciais em decomposição e algoritmo.
- Guia/folheto de uso.
- Orientação direcionada por índice de erro.
- Feedback mais específico e personalizado (sistema determinístico).

**Visual:** quadro “Dimensão → sugestão” (elaborado a partir do texto).

> **Fala sugerida:** “As sugestões são desdobramentos concretos para as próximas versões, não resultados de impacto.”

---

## Slide 16 — Discussão: teoria e prática

**Texto no slide:**

| Achado | Autor(es) | Contribuição |
|---|---|---|
| Erro como aprendizagem | Piton-Gonçalves e Almeida (2018); Wing (2006) | Reforça a compreensão do enunciado e a correção autônoma. |
| Gamificação e autorreflexão | Silpasuwanchai et al. (2016); Michael e Chen (2006) | Pontos, desafios e feedback crítico induzem reflexão. |
| Pilares e sequência lógica | Wing (2006); Pontes e Núñez (2019) | Estrutura o raciocínio em vez de repetir fórmulas. |
| Suporte estruturado | BNCC/BNCC Computação | Orienta a resolução metódica com tecnologias digitais. |
| Aplicabilidade | Plomp et al. (2018) | Validação para além da idealização teórica. |

**Visual:** a própria tabela “Achado → autor(es) → contribuição”.

> **Fala sugerida:** “Os achados convergem com o referencial; a validação é de aplicabilidade, não de impacto.”

---

## Slide 17 — Limitações e o que não foi medido

**Texto no slide:**
- Ciclo 2 com estudantes: resultados **não apresentados**.
- Sem escores de UES/ESM, Alfa de Cronbach ou análises fatoriais reportadas.
- Sem avaliação de aprendizagem ou desempenho acadêmico.
- Feedback determinístico e pouco personalizado.
- Amostra de contingência (alunos do 2º semestre de SI).
- Integração ETL–plataforma ainda não automatizada.
- Número de professores participantes não detalhado.

**Tabela para o slide:**

| Dimensão | Obtido | Status |
|---|---|---|
| Artefato Cognitivo | Sistema concebido e desenvolvido | **Obtido** |
| Base de questões | 551 questões, 15 edições (2009–2023) | **Obtido** |
| Validação pedagógica | Grupo focal com professores | **Obtido** |
| Engajamento dos estudantes | ESM e UES previstos | **Não mensurado** |
| Aprendizagem em Matemática | Não avaliada diretamente | **Não mensurado** |
| Aumento de engajamento | Expectativa do Resumo | **Esperado, não comprovado** |

> **Fala sugerida:** “É importante separar o que foi obtido do que era esperado ou não foi medido.”

---

## Slide 18 — Considerações finais e contribuições

**Texto no slide:**
- O Cognitivo foi **concebido e desenvolvido**.
- Base de **551 questões** de **15 edições** do ENEM (2009–2023).
- Validação com professores indica **aplicabilidade pedagógica** e **coerência teórica**.
- Contribuições: prática, técnica, científica, metodológica, social e de dados.
- A expectativa de aumento de engajamento permanece **a ser avaliada** com estudantes.

**Visual:** linha do tempo do percurso — problema → referencial → artefato → ETL → validação com professores → melhorias → avaliação futura.

> **Fala sugerida:** “O trabalho demonstra viabilidade técnica e pedagógica; o impacto no engajamento ainda não foi mensurado.”

---

## Slide 19 — Trabalhos futuros e referências principais

**Texto no slide:**
- **Trabalhos futuros:**
  - automatizar a integração ETL–plataforma via API interna;
  - avaliar o impacto no desempenho acadêmico com mineração de dados educacionais;
  - implementar as melhorias indicadas no Ciclo 1.
- **Referências principais:** Wing (2006); Silva (2020); Michael e Chen (2006); Silpasuwanchai et al. (2016); Piton-Gonçalves e Almeida (2018); Pontes e Núñez (2019); BNCC (2017); BNCC Computação (2022); O’Brien, Cairns e Hall (2018); Gil (2021); Plomp et al. (2018).
- **Referências metodológicas/técnicas:** Van den Akker et al. (2006); Sommerville (2011); Brown (2022); Kimball et al. (2004).

**Visual:** slide de encerramento com agradecimento; sem figura.

> **Fala sugerida:** “O próximo passo é automatizar a integração e avaliar, com dados de uso, o impacto do Cognitivo no desempenho e no engajamento.”
