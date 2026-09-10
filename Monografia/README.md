# PROJETO DE PESQUISA PARA APROVAÇÃO DO CEP/UNEB

## Protocolo de Pesquisa

**Projeto:** Cognitivo: Pensamento Computacional e Gamificação no Engajamento de Matemática para o Exame Nacional do Ensino Médio (ENEM)

**Pesquisador(a) Responsável:** Guilherme Dos Santos Modesto Teixeira  
**Instituição Proponente:** Universidade do Estado da Bahia (UNEB) — Departamento de Ciências Exatas e da Terra (DCET)  
**Curso:** Sistemas de Informação (Bacharelado)  
**Orientadora:** Prof.ª Ms. Monica de Souza Massa  
**Instituição da Orientadora:** UNEB — DCET  
**Local de Execução:** Salvador, Bahia, Brasil  
**Período de Execução:** Agosto a Novembro de 2026

---

## 1. Introdução

O Exame Nacional do Ensino Médio (ENEM) é a principal via de acesso ao ensino superior no Brasil, avaliando estudantes ao final da educação básica em quatro áreas do conhecimento: Linguagens e Códigos, Ciências Humanas, Ciências da Natureza e Matemática, além da redação. Os dados do ENEM 2024 revelam que, embora a média geral tenha subido de 543 para 546 pontos, a área de Matemática e suas Tecnologias caiu de 535 para 529 pontos, evidenciando uma dificuldade persistente dos estudantes nessa disciplina (INEP, 2025).

A matriz de referência do ENEM exige que o estudante compreenda e utilize sistemas simbólicos para organização cognitiva da realidade, interpretação de dados e tomada de decisões (INEP, 2023). Pesquisas indicam que as dificuldades não derivam apenas de lacunas de conhecimento, mas de esquemas cognitivos inadequados, baixa compreensão dos enunciados e desengajamento (Piton-Gonçalves & Almeida, 2018; Soares et al., 2026).

Diante disso, o Pensamento Computacional (PC) surge como habilidade analítica fundamental — segundo Jeannette M. Wing (2006), tão indispensável quanto a leitura, a escrita e a aritmética — ao promover decomposição de problemas, reconhecimento de padrões, abstração e elaboração de algoritmos.

A BNCC (2017) e a BNCC Computação (2022) estabelecem o PC como dimensão essencial para lidar com as tecnologias na sociedade contemporânea. Paralelamente, os elementos de gamificação — pontos, insígnias e leaderboards (PBL) — podem elevar o engajamento comportamental e cognitivo dos estudantes (Silpasuwanchai et al., 2016).

Este trabalho apresenta o **Cognitivo**, um software gamificado fundamentado nos quatro pilares do PC, projetado para aumentar o engajamento de estudantes em preparação para a prova de matemática do ENEM.

---

## 2. Resumo

O ENEM é a principal porta de entrada para o ensino superior no Brasil, porém os resultados mais recentes revelam queda persistente no desempenho em Matemática. Avaliações internacionais como o PISA 2022 confirmam esse cenário crítico: apenas 27% dos estudantes brasileiros atingiram o nível básico em matemática (INEP, 2026). Pesquisas apontam que essas dificuldades decorrem de estratégias cognitivas inadequadas, baixa compreensão dos enunciados e desengajamento. Apesar da ênfase da BNCC no Pensamento Computacional (PC) como habilidade fundamental para a resolução de problemas, poucas ferramentas educacionais integram efetivamente o PC a estratégias pedagógicas engajadoras. Este trabalho apresenta o **Cognitivo**, um software gamificado fundamentado nos quatro pilares do PC — decomposição, abstração, reconhecimento de padrões e algoritmos — projetado para aumentar o engajamento de estudantes em preparação para a prova de matemática do ENEM. Espera-se que a integração entre gamificação e PC estimule o engajamento, o raciocínio lógico e a autonomia dos alunos na resolução de problemas matemáticos contextualizados, contribuindo para mitigar as dificuldades identificadas no ensino de matemática e oferecendo uma ferramenta alinhada às diretrizes da BNCC.

**Palavras-chave:** Pensamento Computacional. Gamificação. Engajamento. Resolução de Problemas. ENEM. Matemática.

---

## 3. Hipótese

A integração sistemática dos quatro pilares do Pensamento Computacional (decomposição, abstração, reconhecimento de padrões e algoritmos) com mecânicas de gamificação (pontos de experiência, insígnias e leaderboards) em uma plataforma educacional pode aumentar significativamente o engajamento cognitivo e comportamental de estudantes em preparação para a prova de matemática do ENEM, comparativamente às abordagens tradicionais de resolução de exercícios.

---

## 4. Objetivos Primários

- Conceber e desenvolver o **Cognitivo**, um software gamificado educacional que opere os quatro pilares do Pensamento Computacional de forma sequencial e obrigatória na resolução de questões reais de matemática do ENEM.
- Avaliar a experiência e o engajamento dos estudantes por meio de instrumentos validados (ESM e UES).

---

## 5. Objetivos Secundários

- Mapear as principais competências matemáticas das questões do ENEM e identificar como os pilares do PC são mobilizados em cada uma delas.
- Implementar um pipeline ETL para extração, tratamento e enriquecimento de questões reais do ENEM a partir da API ENEM DEV (self-hosted).
- Projetar a arquitetura do sistema com separação de responsabilidades (Plataforma Educacional Gamificada e Módulo ETL).
- Conceber e validar diagramas de caso de uso e fluxo de navegabilidade da plataforma.
- Implementar mecânicas de gamificação (XP Geral, XP de Atributo, insígnias, ligas, matriz de penalidades e custo estratégico de dicas).
- Validar o artefato educacional com professores de matemática por meio de grupo focal (Ciclo 1).
- Validar o sistema com alunos da UNEB, aplicando os formulários ESM e UES (Ciclo 2).

---

## 6. Metodologia Proposta

### 6.1 Abordagem Metodológica

A pesquisa adota a **Design-Based Research (DBR)**, uma metodologia de pesquisa em soluções educacionais que combina rigor científico com relevância prática. Caracteriza-se por:

- **Caráter iterativo:** ciclos sucessivos de análise, planejamento, desenvolvimento, avaliação e revisão.
- **Colaboração entre pesquisadores e profissionais da educação:** participação ativa dos docentes na construção e validação do artefato.
- **Reflexão sistemática:** documentação explícita de todas as decisões, gerando novo arcabouço teórico e prático.
- **Postura pragmática:** enfrentamento direto dos problemas na realidade escolar.

### 6.2 Etapas da DBR

| Etapa do DBR | Atividades |
|---|---|
| **Identificação do problema** | Revisão Sistemática de Literatura; Mapeamento das competências matemáticas do ENEM e dos pilares do PC. |
| **Construção do artefato** | Definição da arquitetura, mecânicas de gamificação e design; Desenvolvimento da primeira versão funcional. |
| **Ciclos de avaliação** | Ciclo 1: Avaliação por professores de Matemática do curso de Sistemas de Informação (grupo focal). Ciclo 2: Avaliação por alunos da UNEB (formulários ESM e UES). |
| **Reflexões e melhorias** | Ciclo 1: Refinamento do sistema a partir do feedback dos professores. Ciclo 2: Uso pelos alunos e aplicação dos formulários; Análise dos dados e geração de conhecimento. |

### 6.3 Arquitetura do Sistema

O sistema é estruturado em dois ambientes:

**Ambiente 1 — Plataforma Educacional Gamificada:**
- **Front-end:** React + Tailwind CSS (responsividade desktop/mobile).
- **API Gateway:** FastAPI (recebe requisições HTTPS, valida payloads JSON, roteamento).
- **Motor Pedagógico e de Gamificação:** lógica de negócio (cálculo de XP, validação sequencial do progresso pelo PC, persistência).
- **Banco de dados relacional:** MySQL.

**Ambiente 2 — Módulo ETL (Extração, Transformação e Carga):**
- **Extração:** Python (requests e httpx) coletando dados da API ENEM DEV self-hosted em lote.
- **Transformação:** Python (Pandas, Pydantic) — normalização, validação, enriquecimento (mapeamento das questões aos pilares do PC).
- **Armazenamento:** PostgreSQL (área de staging).

### 6.4 Mecânicas de Gamificação

**Sistema de Pontos (PBL):**

| Etapa concluída | XP Geral | XP de Atributo |
|---|---|---|
| Decomposição | +2.0 | +2.0 |
| Abstração | +2.0 | +2.0 |
| Padrões | +2.0 | +2.0 |
| Algoritmos | +3.0 | +3.0 |
| Conclusão (Bônus) | +1.0 | +0.25 (cada atributo) |

**Matriz de Penalidades:**

| Ação do usuário | Penalidade | Impacto no XP |
|---|---|---|
| Tentativa errada | ×0.98 (−2%) | Mínimo |
| Erro persistente (3+) | ×0.90 (−10%) | Leve |
| Dica 1 | ×0.80 (−20%) | Médio |
| Dica 2 | ×0.50 (−50%) | Alto |
| Dica 3 | ×0.40 (−60%) | Crítico |

### 6.5 Diagrama de Caso de Uso

O diagrama mapeia dois atores:
- **Estudante** (agente primário): Autenticar Usuário, Iniciar Sessão de Estudo, Resolver Questão (com extensões: Decompor Enunciado, Abstrair Dados, Reconhecer Padrão, Criar Algoritmo), Solicitar Dica, Visualizar Progresso.
- **Sistema** (ator externo): processamento automatizado, aplicação de penalidades de XP.

### 6.6 Design e Usabilidade

O design é fundamentado em princípios de usabilidade, acessibilidade e engajamento (Preece, Rogers & Sharp, 2013), visando ser eficaz, eficiente, seguro, útil, fácil de aprender e fácil de lembrar. O fluxo de navegabilidade é validado nos ciclos iterativos da DBR.

### 6.7 Instrumentos de Coleta de Dados

**Método de Amostragem de Experiência (ESM):**
- Formulário curto com Escala Likert (5 pontos), aplicado imediatamente após a interação com o sistema.
- Avalia três dimensões: Imersão e Foco, Usabilidade (interface e dicas), PC e Utilidade Percebida.
- Tempo estimado de preenchimento: menos de 1 minuto (Francisco, 2020).

**Escala de Engajamento do Usuário (UES):**
- 12 itens obrigatórios em Escala Likert (5 pontos), estruturados em quatro dimensões: Atenção Focada (FA-S), Usabilidade Percebida (PU-S), Apelo Estético (AE-S) e Recompensa (RW-S) (O'Brien, Cairns & Hall, 2018).

**Grupo Focal (Ciclo 1 — Professores):**
- Técnica qualitativa para compreender percepções, experiências e significados atribuídos pelos professores ao artefato (Gil, 2021).

---

## 7. Critérios de Inclusão

- Estudantes matriculados no curso de Sistemas de Informação da UNEB.
- Professores de matemática com experiência docente no ensino superior.
- Participantes que assinarem o Termo de Consentimento Livre Esclarecido (TCLE).
- Estudantes com acesso a dispositivo eletrônico com navegador web e conexão à internet.

---

## 8. Critérios de Exclusão

- Estudantes que não assinarem o TCLE.
- Participantes que não completarem a sessão de uso da plataforma ou não responderem aos formulários de avaliação.
- Professores sem vínculo com a disciplina de matemática ou área correlata.

---

## 9. Riscos

Conforme a Resolução CNS 466/12, não existem pesquisas sem riscos aos participantes. Os riscos envolvem todas as áreas inerentes à vida humana, incluindo danos às dimensões física, psíquica, moral, intelectual, social e profissional. A seguir, os riscos identificados e as estratégias de minimização:

| Risco | Descrição | Forma de Minimização |
|---|---|---|
| **Desconforto psíquico** | Possível frustração ou desconforto ao errar questões durante o uso da plataforma. | O sistema de gamificação é projetado para tornar o erro parte do aprendizado (penalidades leves de −2%), com dicas progressivas que incentivam a persistência sem punição excessiva. |
| **Constrangimento** | Possível constrangimento ao responder formulários de avaliação sobre desempenho. | Formulários anônimos; Escala Likert de 5 pontos para respostas rápidas; tempo de preenchimento < 1 minuto. |
| **Cansaço** | Possível fadiga cognitiva durante sessões prolongadas de uso da plataforma. | Sessões de uso com duração controlada; interface gamificada que mantém o engajamento; interrupção voluntária a qualquer momento. |
| **Risco à privacidade** | Possível exposição de dados pessoais durante a coleta de dados. | Dados coletados de forma anônima; ausência de coleta de dados identificáveis; armazenamento seguro em banco de dados; observância da Lei Geral de Proteção de Dados (Lei 13.709/18). |
| **Risco moral** | Possível uso indevido dos dados da pesquisa em detrimento dos participantes. | Compromisso ético do pesquisador de utilizar os dados exclusivamente para fins acadêmicos; confidencialidade garantida; dados descartados após a conclusão da pesquisa. |

**Ponderação entre riscos e benefícios:** Conforme orientação do CEP/UNEB, se os riscos excederem os benefícios, não se justifica a execução da pesquisa. Neste projeto, os riscos são mínimos e todos passíveis de minimização, enquanto os benefícios são relevantes para os participantes e para a sociedade, justificando a execução da pesquisa.

---

## 10. Benefícios

**Benefícios diretos para os participantes:**
- Acesso a uma ferramenta educacional gamificada que facilita a preparação para a prova de matemática do ENEM.
- Desenvolvimento de habilidades cognitivas (decomposição, abstração, reconhecimento de padrões e algoritmos) por meio da resolução de questões reais.
- Experiência de aprendizado ativa e psicologicamente estimulante, substituindo a postura passiva e a frustração comum no estudo de matemática.

**Benefícios indiretos para a sociedade:**
- Contribuição para o campo de Educação Computacional e Design-Based Research, com documentação aberta do processo de desenvolvimento e validação.
- Geração de dados educacionais que podem alimentar análises de mineração de dados educacionais em trabalhos futuros.
- Modelo replicável de integração entre PC e gamificação, alinhado às diretrizes da BNCC e da BNCC Computação.
- Potencial de mitigação do baixo desempenho em matemática no ENEM, impactando positivamente o acesso ao ensino superior.

**Forma de aplicação dos benefícios:**
- Disponibilização da plataforma Cognitivo para uso dos participantes durante a pesquisa.
- Retorno dos resultados da pesquisa aos participantes e à instituição, por meio de relatório e/ou apresentação acadêmica.

---

## 11. Metodologia de Análise de Dados

### 11.1 Dados Qualitativos (Ciclo 1 — Professores)
- **Técnica:** Grupo focal estruturado.
- **Análise:** Análise de conteúdo temática (Gil, 2021), com categorização a priori dos indicadores: validação dos conteúdos matemáticos, acurácia dos gabaritos, eficácia das mecânicas de gamificação e adequação pedagógica do fluxo do PC.

### 11.2 Dados Quantitativos (Ciclo 2 — Alunos)
- **Instrumentos:** ESM (Escala Likert 5 pontos) e UES (12 itens, 4 dimensões).
- **Análise:**
  - Cálculo do **Alfa de Cronbach** para validar a consistência interna de cada escala.
  - **Análises fatoriais** para verificar a estrutura dimensional dos instrumentos.
  - **Estatísticas descritivas** (média, mediana, desvio-padrão) por dimensão.
  - **Análise comparativa** entre as dimensões de atenção focada, usabilidade percebida, apelo estético e recompensa.
- **Software:** ferramentas estatísticas (ex.: SPSS, JASP ou Python com SciPy/Statsmodels).

---

## 12. Desfecho Primário

**Nível de engajamento dos estudantes** com a plataforma Cognitivo, mensurado pela Escala de Engajamento do Usuário (UES), considerando as quatro dimensões: Atenção Focada, Usabilidade Percebida, Apelo Estético e Recompensa.

---

## 13. Desfecho Secundário

- Percepção dos estudantes sobre a utilidade do Pensamento Computacional para a resolução de problemas matemáticos do ENEM (dimensão do formulário ESM).
- Usabilidade percebida e facilidade de utilização da interface (dimensão ESM).
- Feedback qualitativo dos professores sobre a validade pedagógica, acurácia dos conteúdos e eficácia das mecânicas de gamificação (grupo focal — Ciclo 1).

---

## 14. Tamanho da Amostra

- **Ciclo 1 (Professores):** grupo focal com professores de matemática do curso de Sistemas de Informação da UNEB (quantidade mínima recomendada para grupo focal: 6 a 10 participantes, conforme Gil, 2021).
- **Ciclo 2 (Alunos):** estudantes do curso de Sistemas de Informação da UNEB que voluntariamente participarem dos testes de uso da plataforma. A amostra será por conveniência, com adesão voluntária após assinatura do TCLE.

> **Nota:** O tamanho final da amostra será definido com base na disponibilidade dos participantes e na taxa de resposta aos formulários ESM e UES.

---

## 15. Detalhamento do Uso de Dados Secundários

Conforme definição da Resolução CNS 466/12 e da cartilha do CEP/UNEB, dados secundários são aqueles obtidos em fontes que não foram coletados diretamente pelo pesquisador com os participantes, incluindo arquivos publicados e não publicados.

### 15.1 Dados Secundários Utilizados no Projeto

O projeto utiliza **dados secundários** por meio do pipeline ETL:

- **Fonte:** API ENEM DEV (https://enem.dev/), hospedada em instância self-hosted.
- **Dados coletados:** questões reais de matemática do ENEM, incluindo enunciados, alternativas, gabaritos e metadados.
- **Natureza dos dados:** dados de domínio público e de acesso público, disponibilizados publicamente pela API ENEM DEV, que aggregate informações do INEP sobre questões do ENEM.

### 15.2 Processo de Extração e Tratamento

- **Extração:** requisições síncronas (biblioteca `requests`) para consultas pontuais e assíncronas (biblioteca `httpx`) para coleta massiva em lote.
- **Transformação:**
  - Normalização com Pandas (estruturação em tabelas, limpeza de caracteres corrompidos).
  - Validação com Pydantic (garantia de integridade dos dados).
  - Enriquecimento: mapeamento de cada questão aos quatro pilares do PC (decomposição, abstração, reconhecimento de padrões e algoritmos).
- **Armazenamento:** PostgreSQL (área de staging para rastreamento e integridade).

### 15.3 Dados Primários Coletados na Pesquisa

Além dos dados secundários, a pesquisa coleta **dados primários** diretamente com os participantes:

- **Formulários ESM e UES:** aplicados imediatamente após a interação dos alunos com a plataforma (coleta de dados diretamente com o participante).
- **Grupo focal com professores:** sessão de coleta de dados qualitativos diretamente com os docentes.

### 15.4 Apreciação Ética

Por envolver **dados primários** coletados diretamente com seres humanos (alunos e professores), o projeto **deve ser submetido à apreciação ética do CEP/UNEB**, conforme Resolução CNS 466/12 e 510/16. O uso de dados secundários de domínio público (questões do ENEM) não dispensa a apreciação ética, uma vez que a coleta de dados primários com participantes humanos é o elemento que demanda a análise do comitê.

---

## 16. Justificativa sobre o Uso do Termo de Consentimento Livre e Esclarecido (TCLE)

### 16.1 Necessidade de TCLE

O presente projeto **utiliza o TCLE**, não sendo solicitada a dispensa deste documento. A justificativa para a exigência do TCLE fundamenta-se nos seguintes argumentos:

1. **Coleta de dados primários com seres humanos:** a pesquisa envolve aplicação de formulários (ESM e UES) e sessão de grupo focal diretamente com participantes (alunos e professores da UNEB), configurando-se como pesquisa que utiliza dados primários, conforme definição da Resolução CNS 466/12.

2. **Princípio da Autonomia:** o TCLE cumpre o papel de garantir que os participantes, de forma autônoma e esclarecida, decidam sobre sua participação na pesquisa, conforme preceitos das Resoluções CNS 466/12 e 510/16.

3. **Princípio da Não Maleficência:** o TCLE informa claramente os potenciais riscos (desconforto psíquico, constrangimento, cansaço, riscos à privacidade e risco moral) e as formas de minimização, garantindo que os participantes tomem decisões informadas.

4. **Princípio da Beneficência:** o TCLE descreve os benefícios diretos e indiretos da pesquisa para os participantes e para a sociedade.

5. **Proteção de dados pessoais:** o TCLE esclarece sobre a confidencialidade, o anonimato e a observância da Lei Geral de Proteção de Dados Pessoais (Lei 13.709/18).

6. **Linguagem acessível:** o TCLE será redigido em linguagem clara e acessível ao segmento da sociedade que integrará a pesquisa (estudantes de graduação e professores), conforme orientação da cartilha do CEP/UNEB.

### 16.2 Conteúdo do TCLE

O TCLE conterá, conforme exigido pela Resolução CNS 466/12:
- Identificação do pesquisador e da instituição.
- Descrição clara dos objetivos da pesquisa.
- Descrição dos procedimentos metodológicos aos quais o participante se submeterá.
- Descrição dos potenciais riscos e formas de minimização.
- Descrição dos benefícios da pesquisa.
- Informações sobre confidencialidade e anonimato.
- Informação de que a participação é voluntária e que o participante pode desistir a qualquer momento, sem penalidade.
- Informações sobre o armazenamento e uso dos dados coletados.
- Dados de contato do pesquisador e da orientadora.

---

## 17. Cronograma de Execução

O cronograma foi elaborado conforme orientação do CEP/UNEB, contemplando prazo mínimo de **60 dias para apreciação ética antes do início da coleta de dados**. O projeto será submetido ao CEP/UNEB com antecedência mínima de 60 dias da data prevista para início da coleta de dados primários.

| Atividade | Ago | Set | Out | Nov | Dez |
|---|:---:|:---:|:---:|:---:|:---:|
| Definição do problema | ● | ● | | | |
| Revisão sistemática de literatura e definição da metodologia | ● | ● | ● | | |
| Diagramas de caso de uso, arquitetura e design da aplicação | | ● | ● | ● | |
| Monografia Parcial | | | ● | ● | |
| Front-End da aplicação | | | ● | ● | |
| Módulo ETL | | | ● | ● | |
| Diagrama ER, banco de dados e back-end | | | ● | ● | ● |
| Mecânicas de gamificação | | ● | ● | ● | ● |
| Infraestrutura | | | ● | ● | ● |
| **Submissão ao CEP/UNEB (Plataforma Brasil)** | | **●** | | | |
| **Apreciação ética do CEP/UNEB (≥60 dias)** | | **●** | **●** | | |
| Ciclos de avaliação com alunos e professores | | | | ● | ● |
| Análise dos resultados | | | | ● | ● |
| Escrita, revisão e monografia final | | | | ● | ● |

> **Nota importante (CEP/UNEB):** A coleta de dados primários (formulários ESM/UES e grupo focal) somente será iniciada após a emissão de parecer consubstanciado favorável pelo CEP/UNEB. O cronograma respeita o prazo mínimo de 60 dias para apreciação ética, conforme orientação da cartilha do CEP/UNEB. O projeto que constar executado antes da apreciação ética não será aprovado.

---

## 18. Orçamento Financeiro Detalhado

| Item | Descrição | Custo Estimado (R$) |
|---|---|---|
| **Hospedagem (servidor)** | Instância cloud para API Gateway, back-end e banco de dados (6 meses, tier básico) | 300,00 |
| **Domínio web** | Registro de domínio para a plataforma (1 ano) | 40,00 |
| **Infraestrutura de desenvolvimento** | Ferramentas de versionamento (GitHub), IDE, frameworks e bibliotecas (todos open-source) | 0,00 |
| **Impressão de materiais** | Impressão de TCLE, formulários ESM e UES para aplicação presencial | 50,00 |
| **Deslocamento** | Deslocamento para sessões presenciais de grupo focal e aplicação com alunos (estimativa) | 100,00 |
| **Bibliografia** | Aquisição de livros e artigos (acesso via biblioteca universitária e repositórios open-access) | 0,00 |
| **Total estimado** | | **R$ 490,00** |

> **Observação:** A maior parte das ferramentas utilizadas (React, FastAPI, PostgreSQL, Python, Pandas, Pydantic, Tailwind CSS) é de código aberto, minimizando significativamente os custos. A hospedagem pode ser custeada por plataformas com tier gratuito (ex.: Railway, Vercel, Render).

---

## 19. Outras Informações, Justificativas e Considerações

### 19.1 Justificativa da Escolha da DBR

A Design-Based Research foi escolhida por ser a metodologia mais adequada para pesquisas que visam gerar soluções práticas para problemas educacionais, combinando rigor científico com relevância prática. Seu caráter iterativo permite que os resultados de cada ciclo retroalimentem o desenvolvimento, promovendo melhorias contínuas.

### 19.2 Alinhamento com a BNCC

O projeto está alinhado com a BNCC Computação (2022), que estabelece o Pensamento Computacional como eixo fundamental para o desenvolvimento de habilidades cognitivas, sociais e éticas na Educação Básica. A plataforma operacionaliza os quatro pilares do PC de forma sequencial e obrigatória, indo além do letramento digital.

### 19.3 Diferencial em Relação a Trabalhos Correlatos

Conforme análise comparativa realizada na monografia, o Cognitivo se diferencia dos trabalhos correlatos por:
- Operacionalizar os quatro pilares do PC de forma **sequencial e obrigatória** na resolução de questões reais do ENEM.
- Implementar um **sistema completo de PBL** com XP, insígnias, ligas, matriz de penalidades e custo estratégico de dicas.
- Processar questões reais do ENEM por meio de **pipeline ETL**, mapeando competências matemáticas aos pilares do PC.

### 19.4 Princípios Éticos da Pesquisa

A pesquisa observa os cinco princípios éticos estabelecidos pela Resolução CNS 466/12:

- **Autonomia:** participação voluntária com TCLE; direito de desistência a qualquer momento.
- **Não maleficência:** planejamento de riscos mínimos e formas de minimização detalhadas.
- **Beneficência:** benefícios claros para participantes e sociedade.
- **Justiça:** seleção justa dos participantes, sem discriminação.
- **Equidade:** tratamento igualitário de todos os participantes.

### 19.5 Proteção de Dados

O projeto observa a Lei Geral de Proteção de Dados Pessoais (Lei 13.709/18):
- Dados coletados de forma anônima.
- Ausência de coleta de dados identificáveis.
- Armazenamento seguro em banco de dados.
- Uso dos dados exclusivamente para fins acadêmicos.
- Dados descartados após a conclusão da pesquisa.

### 19.6 Trabalhos Futuros

- Integração automatizada entre o Módulo ETL e o Sistema Gamificado via API interna.
- Avaliação do impacto direto do sistema no desempenho acadêmico por meio de mineração de dados educacionais.
- Expansão para outras áreas do conhecimento avaliadas no ENEM.

### 19.7 Submissão na Plataforma Brasil

O projeto será cadastrado e submetido à apreciação ética por meio da **Plataforma Brasil** (http://plataformabrasil.saude.gov.br/login.jsf), conforme orientação do CEP/UNEB. O pesquisador responsável realizará seu cadastro na plataforma e vinculará o projeto à instituição UNEB, apresentando o protocolo de pesquisa completo conforme orientações da Resolução 466/2012, Cap. III, e do Manual do Pesquisador.

---

## 20. Bibliografia

- BRACKMANN, C. et al. Computational thinking: panorama of the Americas. In: **Proceedings of the International Symposium on Computers in Education (SIIE)**, Salamanca, 2016. p. 1–6.
- BRASIL. **Base Nacional Comum Curricular**. Brasília: MEC/SEB, 2017.
- BRASIL. **Base Nacional Comum Curricular: Computação**. Brasília: Ministério da Educação, 2022.
- BROWN, S. **The C4 Model for Visualising Software Architecture**. Victoria, BC, Canada: Leanpub, 2022.
- FILHO, J. A. D. et al. O uso das plataformas Scratch e Code.org para o desenvolvimento do Pensamento Computacional na educação básica. In: **Anais do XXXI Workshop de Informática na Escola (WIE)**, 2025. p. 500–510.
- FRANCISCO, R. Experience Sampling Method (ESM). In: **Metodologia de Pesquisa Científica em Informática na Educação: abordagem quantitativa**. Porto Alegre: SBC, 2020. cap. 1, p. 1–24.
- GIL, A. C. **Como fazer pesquisa qualitativa**. Rio de Janeiro: Atlas, 2021.
- INEP. **Enem 2024: desempenho médio dos participantes aumentou**. 2025.
- INEP. **Matrizes de Referência do ENEM**. Brasília: INEP/MEC, 2023.
- JESUS, C. R. Ensino de Matemática e dificuldades de aprendizagem. **Revista Tópicos**, Rio de Janeiro, v. 4, n. 30, p. 1–20, 2026.
- KIMBALL, R. et al. **The Data Warehouse ETL Toolkit**. 2004.
- LAIS, R. et al. Enigma pirata: um jogo para exercitar Matemática e Pensamento Computacional através da Teoria dos Conjuntos. In: **CBIE**, 2023. p. 169–172.
- MICHAEL, D.; CHEN, S. **Serious Games: Games That Educate, Train, and Inform**. 2006.
- O'BRIEN, H. L.; CAIRNS, P.; HALL, M. A practical approach to measuring user engagement with the refined UES and new UES short form. **International Journal of Human-Computer Studies**, v. 112, p. 28–39, 2018.
- PITON-GONÇALVES, J.; ALMEIDA, A. M. Análise da dificuldade e da discriminação de itens de Matemática do ENEM. **REMAT**, v. 4, n. 2, p. 38–53, 2018.
- PONTES, J.; NÚÑEZ, I. Questões de Matemática do ENEM 2015: erros e dificuldades de aprendizagem. **Educação, Escola & Sociedade**, v. 12, n. 14, e201902, 2019.
- PLOMP, T.; NIEVEEN, N. (org.). **Pesquisa-Aplicação em Educação: uma introdução**. São Paulo: Artesanato Educacional, 2018.
- PREECE, J.; ROGERS, Y.; SHARP, H. **Design de interação**. 3. ed. Porto Alegre: Bookman, 2013.
- ROLIM, I. et al. Rabbit Code: um jogo voltado para a aprendizagem de matrizes. In: **Anais do 12. CBIE**, 2023. p. 141–144.
- SILPASUWANCHAI, C. et al. Developing a comprehensive engagement framework of gamification for reflective learning. In: **Proceedings of the 2016 ACM Conference on Designing Interactive Systems**, 2016. p. 459–472.
- SILVA, F. M. da. **Pensamento computacional: uma análise dos documentos oficiais e das questões de Matemática dos vestibulares**. Dissertação (Mestrado) — UNESP, Bauru, 2020.
- SOMMERVILLE, I. **Software Engineering**. 9. ed. Pearson, 2011.
- SOARES, D. J. M. et al. Diferenças na dificuldade dos itens de Matemática do ENEM. **Regae**, e96143, 2026.
- TEODOSIO, E. S.; VILA NOVA, A. B. Atividade de Matemática gamificada com pixel art. In: **Anais do 34. SBIE**, 2023. p. 255–263.
- VAN DEN AKKER, J. et al. **Educational Design Research**. London: Routledge, 2006.
- WING, J. M. Computational Thinking. **Communications of the ACM**, v. 49, n. 3, p. 33–35, 2006.

---

## 21. Anexos

### Anexo A — Modelo de Termo de Consentimento Livre e Esclarecido (TCLE)

---

**TERMO DE CONSENTIMENTO LIVRE E ESCLARECIDO (TCLE)**

**Pesquisador Responsável:** Guilherme Dos Santos Modesto Teixeira  
**Instituição:** Universidade do Estado da Bahia (UNEB) — Departamento de Ciências Exatas e da Terra (DCET)  
**Orientadora:** Prof.ª Ms. Monica de Souza Massa  
**Contato:** [e-mail do pesquisador] | Telefone: [telefone do pesquisador]  
**E-mail do CEP/UNEB:** cepuneb@uneb.br | Telefone: (71) 3621-1330

---

O(A) senhor(a) está sendo convidado(a) a participar, como voluntário(a), da pesquisa intitulada **"Cognitivo: Pensamento Computacional e Gamificação no Engajamento de Matemática para o ENEM"**, que tem como objetivo geral conceber e avaliar um software gamificado fundamentado nos pilares do Pensamento Computacional para aumentar o engajamento de estudantes na preparação para a prova de matemática do ENEM.

**1. Sobre os procedimentos:**

Sua participação consistirá em:
- Utilizar a plataforma Cognitivo por um período determinado pelo pesquisador;
- Responder a formulários de avaliação (ESM e UES) contendo perguntas sobre sua experiência com o sistema. Os formulários são curtos (tempo de preenchimento inferior a 1 minuto) e contêm perguntas em escala de concordância.
- Caso seja professor(a), poderá ser convidado(a) a participar de um grupo focal (sessão de discussão em grupo) para discutir percepções sobre o artefato educacional.

**2. Sobre os riscos:**

A participação nesta pesquisa apresenta riscos mínimos, que incluem:
- Possível desconforto psíquico ao errar questões durante o uso da plataforma;
- Possível constrangimento ao responder formulários sobre desempenho;
- Possível cansaço durante sessões de uso;
- Riscos à privacidade (exposição de dados pessoais).

**Formas de minimização dos riscos:**
- O sistema de gamificação é projetado para tornar o erro parte do aprendizado, com penalidades leves;
- Os formulários são anônimos e de preenchimento rápido;
- A participação é voluntária e o(A) senhor(a) pode interromper a qualquer momento;
- Os dados serão tratados de forma anônima e confidencial;
- Será observada a Lei Geral de Proteção de Dados Pessoais (Lei 13.709/18).

**3. Sobre os benefícios:**

- Acesso a uma ferramenta educacional gamificada para preparação em matemática do ENEM;
- Desenvolvimento de habilidades cognitivas (pensamento computacional) por meio da resolução de questões reais;
- Contribuição para a melhoria do ensino de matemática e para a produção científica na área de Educação Computacional.

**4. Sobre a confidencialidade:**

Todas as informações fornecidas serão tratadas com sigilo e utilizadas exclusivamente para fins acadêmicos da presente pesquisa. Os dados serão armazenados de forma anônima, sem possibilidade de identificação individual. Os dados serão mantidos pelo período necessário à conclusão da pesquisa e posteriormente descartados.

**5. Sobre a participação:**

Sua participação é inteiramente voluntária. A qualquer momento, o(A) senhor(a) poderá desistir da pesquisa, sem qualquer penalidade. A recusa em participar não acarretará nenhum prejuízo.

**6. Sobre o armazenamento e uso dos dados:**

Os dados coletados serão armazenados em ambiente seguro e utilizados exclusivamente para fins da presente pesquisa acadêmica. Não haverá compartilhamento dos dados com terceiros.

**7. Consentimento:**

Declaro que li e compreendi as informações acima. Tive a oportunidade de fazer perguntas e esclarecer minhas dúvidas. Compreendo que minha participação é voluntária e que posso desistir a qualquer momento. Consinto em participar voluntariamente desta pesquisa.

_______________________________  
**Assinatura do(a) participante**  

Nome completo: _______________________________

Data: ___/___/______

---

### Anexo B — Formulário ESM (Método de Amostragem de Experiência)

O formulário ESM é composto por 3 páginas e avalia três macrodimensões. Cada item utiliza Escala Likert de 5 pontos (1 = Discordo Totalmente a 5 = Concordo Totalmente).

**Página 1 — Imersão e Foco**
- Itens sobre concentração, equilíbrio entre desafio e habilidade, e envolvimento durante a resolução de questões.

**Página 2 — Usabilidade (Interface e Dicas)**
- Itens sobre clareza das regras, facilidade de utilização da interface e qualidade das dicas fornecidas pelo sistema.

**Página 3 — Pensamento Computacional e Utilidade Percebida**
- Itens comparando a experiência na plataforma com a resolução convencional de exercícios em caderno, avaliando se o fluxo guiou o estudante a exercitar os quatro pilares do PC.

---

### Anexo C — Formulário UES (Escala de Engajamento do Usuário)

O formulário UES é composto por 4 páginas com 12 itens obrigatórios em Escala Likert de 5 pontos (1 = Discordo Totalmente a 5 = Concordo Totalmente):

**Página 1 — Seção 1: Atenção e Imersão (FA-S)**
- 3 itens avaliando foco, absorção e percepção temporal gerados pelas mecânicas lúdicas.

**Página 2 — Seção 2: Usabilidade Percebida (PU-S)**
- 3 itens avaliando esforço de interação, controle percebido e facilidade de uso.

**Página 3 — Seção 3: Apelo Visual e Estético (AE-S)**
- 3 itens avaliando atratividade da interface e impacto do design visual na experiência.

**Página 4 — Seção 4: Recompensa e Valor da Experiência (RW-S)**
- 3 itens avaliando benefício percebido, satisfação com elementos de gamificação e disposição para recomendar o sistema.

> Os códigos de identificação (FA-S, PU-S, AE-S, RW-S) viabilizam a aplicação de técnicas estatísticas avançadas, incluindo Alfa de Cronbach e análises fatoriais.

---

### Anexo D — Projeto Completo

O projeto completo está disponível no arquivo `documento.pdf` na raiz deste repositório, bem como no arquivo `monografia_parcial_final_assinado.pdf`. O código-fonte LaTeX está organizado na seguinte estrutura:

```
Monografia/
├── documento.tex                    # Arquivo principal
├── elementos-pre-textuais/          # Resumo, abstract, listas
├── elementos-textuais/              # Capítulos (introdução, fundamentação, correlatos, metodologia, resultados, conclusão, cronograma)
├── elementos-pos-textuais/          # Referências (BibTeX), apêndices (formulários ESM e UES)
├── figuras/                         # Figuras e diagramas
├── lib/                             # Configurações e pacotes LaTeX
└── Makefile                         # Comando para compilação
```

Para compilar a monografia, execute `make` no diretório raiz do projeto (requer distribuição TeX Live ou MiKTeX com abnTeX2).

---

### Anexo E — Documentos Exigidos pelo CEP/UNEB para Protocolo de Pesquisa

Conforme Resolução CNS 466/12 e orientações da cartilha do CEP/UNEB, os seguintes documentos devem compor o protocolo de pesquisa para submissão na Plataforma Brasil:

1. **Projeto de pesquisa completo** (este documento) — timbrado e identificado pela UNEB/DCET.
2. **TCLE** (Anexo A) — redigido em linguagem acessível ao segmento participante.
3. **Formulários de coleta de dados** (Anexos B e C) — ESM e UES.
4. **Autorização da instituição coparticipante** (se aplicável) — com timbre da coparticipante.
5. **Currículo lattes** do pesquisador responsável e da orientadora.

**Prazos de tramitação no CEP/UNEB:**
- 10 dias para conferência documental.
- 30 dias para apreciação ética dos relatores e apresentação na plenária inter/multidisciplinar.
- Possível extensão de até 60 dias em caso de pendências.

**Importante:** A pesquisa só deve ser iniciada após a aprovação ética pelo CEP/UNEB. O cronograma deve contemplar o prazo de apreciação ética com carência mínima de 60 dias para execução da coleta/registro de dados.

---

*Documento elaborado conforme as orientações da Cartilha do CEP/UNEB e da Resolução CNS 466/12, para submissão ao Comitê de Ética em Pesquisa com Seres Humanos da Universidade do Estado da Bahia.*
