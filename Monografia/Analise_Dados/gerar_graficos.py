"""Gera, em Python, os gráficos das avaliações com alunos no estilo dos
gráficos exibidos pelo Google Forms: uma barra por nota (1 a 5) com a
quantidade e o percentual de respostas acima de cada barra.

Uso:
    python3 Analise_Dados/gerar_graficos.py

As planilhas de respostas devem estar na pasta Analise_Dados e as figuras
são salvas na pasta figuras, uma por seção do formulário.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

BASE = Path(__file__).resolve().parent
FIGURAS = BASE.parent / "figuras"

UES_FILE = BASE / "Avaliação de Engajamento do Usuário (UES) (respostas)(1).xlsx"
ESM_FILE = BASE / "Avaliação da Experiência do Usuário (respostas)(1).xlsx"

COR_FORMS = "#1a73e8"

UES_SECOES = {
    "secao1": (
        "UES — Seção 1: Atenção e Imersão",
        [
            ("Perdi-me na experiência", "Eu me perdi nesta experiência."),
            ("O tempo passou rápido", "O tempo que passei usando a plataforma passou rápido."),
            ("Absorvido na experiência", "Eu estava absorvido nesta experiência."),
        ],
    ),
    "secao2": (
        "UES — Seção 2: Usabilidade Percebida",
        [
            ("Senti frustração", "Eu me senti frustrado ao usar a plataforma."),
            ("Achei confuso de usar", "Achei a plataforma confusa de usar."),
            ("Uso desgastante", "Usar a plataforma foi desgastante."),
        ],
    ),
    "secao3": (
        "UES — Seção 3: Apelo Visual e Estético",
        [
            ("Visualmente atraente", "A plataforma foi visualmente atraente."),
            ("Design agradável", "A plataforma teve um design esteticamente agradável."),
            ("Agrado visual", "A plataforma agradou meus sentidos visuais."),
        ],
    ),
    "secao4": (
        "UES — Seção 4: Recompensa e Valor da Experiência",
        [
            ("Valeu a pena", "Usar a plataforma valeu a pena."),
            ("Experiência recompensadora", "Minha experiência foi recompensadora."),
            ("Interesse genuíno", "Senti interesse genuíno nesta experiência."),
        ],
    ),
}

ESM_SECOES = {
    "secao1": (
        "ESM — Dimensão 1: Imersão e Foco",
        [
            ("1.1 Concentração profunda", "1.1. Concentração Profunda (Esforço de Atenção)"),
            ("1.2 Distorção temporal", "1.2. Distorção Temporal (Percepção do Tempo)"),
        ],
    ),
    "secao2": (
        "ESM — Dimensão 2: Uso do Sistema",
        [
            ("2.1 Clareza do sistema", "2.1. Clareza do Sistema (Entendimento das Regras)"),
            ("2.2 Facilidade de uso", "2.2. Facilidade de Uso (Esforço de Interação)"),
            ("2.3 Qualidade do feedback", "2.3. Qualidade do Feedback (Resposta do Software)"),
        ],
    ),
    "secao3": (
        "ESM — Dimensão 3: Pensamento Computacional",
        [
            ("3.1 Decomposição", "3.1. Decomposição (Dividir para resolver)"),
            ("3.2 Reconhecimento de padrões", "3.2. Reconhecimento de Padrões (Identificar semelhanças)"),
            ("3.3 Abstração", "3.3. Abstração (Focar no que importa)"),
            ("3.4 Algoritmos e depuração", "3.4. Algoritmos e Depuração (Criar e corrigir sequências)"),
            ("3.5 Retenção e utilidade", "3.5. Retenção e Utilidade Percebida"),
        ],
    ),
}

plt.rcParams.update(
    {
        "font.size": 9,
        "axes.titlesize": 10,
        "axes.labelsize": 9,
        "xtick.labelsize": 9,
        "ytick.labelsize": 8,
        "figure.titlesize": 12,
    }
)


def plot_secao(df, titulo, perguntas, arquivo):
    n = len(perguntas)
    nrows = 1 if n <= 3 else 2
    altura = 3.9 * nrows

    fig = plt.figure(figsize=(13.2, altura))
    grade = fig.add_gridspec(
        nrows, 6, wspace=0.32, hspace=0.5 if nrows > 1 else 0.0
    )
    if nrows == 1:
        largura = 3 if n == 2 else 2
        celulas = [grade[0, i * largura : (i + 1) * largura] for i in range(n)]
    else:
        # Cinco itens: três no topo e dois centralizados na linha inferior,
        # mantendo o mesmo tamanho de painel das demais seções.
        celulas = [
            grade[0, 0:2],
            grade[0, 2:4],
            grade[0, 4:6],
            grade[1, 1:3],
            grade[1, 3:5],
        ]
    eixos = [fig.add_subplot(celula) for celula in celulas]

    for ax, (rotulo, coluna) in zip(eixos, perguntas):
        respostas = df[coluna].astype(int)
        contagens = np.array([(respostas == nota).sum() for nota in range(1, 6)])
        porcentagens = 100 * contagens / len(respostas)

        ax.bar(
            range(1, 6),
            contagens,
            color=COR_FORMS,
            edgecolor=COR_FORMS,
            linewidth=0.6,
            width=0.72,
        )
        for nota, (contagem, pct) in enumerate(zip(contagens, porcentagens), start=1):
            ax.text(
                nota,
                contagem + 0.12,
                f"{int(contagem)} ({int(round(pct))}%)",
                ha="center",
                va="bottom",
                fontsize=8,
            )

        ax.set_xticks(range(1, 6))
        ax.set_xlim(0.5, 5.5)
        ax.set_ylim(0, max(contagens.max() + 1, 3.2))
        ax.set_yticks(range(0, int(max(contagens.max() + 1, 3))))
        ax.set_xlabel("Nota")
        ax.set_ylabel("Respostas")
        ax.set_title(rotulo)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.tick_params(axis="x", length=0)

    # Sem título dentro da imagem: a identificação é feita pela legenda do LaTeX.
    if nrows == 1:
        fig.subplots_adjust(left=0.06, right=0.98, top=0.95, bottom=0.14)
    else:
        fig.subplots_adjust(left=0.06, right=0.98, top=0.96, bottom=0.08)

    destino = FIGURAS / arquivo
    fig.savefig(destino, dpi=300, bbox_inches="tight")
    plt.close(fig)

    print(f"Salvo: {destino}")
    for rotulo, coluna in perguntas:
        respostas = df[coluna].astype(int)
        contagens = [(respostas == nota).sum() for nota in range(1, 6)]
        pcts = [round(100 * c / len(respostas)) for c in contagens]
        print("  " + rotulo + ": " + ", ".join(f"{c}({p}%)" for c, p in zip(contagens, pcts)))


def plot_perfil(df, arquivo):
    coluna = "Fez ENEM ?"
    sim = int((df[coluna] == "Sim").sum())
    nao = int((df[coluna] == "Não").sum())
    tamanhos = [x for x in (sim, nao) if x > 0]
    rotulos = [x for x, v in (("Sim", sim), ("Não", nao)) if v > 0]
    cores = ["#1a73e8"] + ["#dadce0"]

    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    ax.pie(
        tamanhos,
        labels=[f"{r}\n{v} respostas" for r, v in zip(rotulos, tamanhos)],
        autopct=lambda pct: f"{int(round(pct))}%",
        startangle=90,
        colors=cores[: len(tamanhos)],
        wedgeprops={"edgecolor": "white", "linewidth": 1.2},
        textprops={"fontsize": 10},
    )
    ax.set_title("Fez ENEM?")
    fig.subplots_adjust(left=0.12, right=0.88, top=0.88, bottom=0.12)
    destino = FIGURAS / arquivo
    fig.savefig(destino, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"Salvo: {destino} (Sim = {sim}, Não = {nao})")


def main():
    FIGURAS.mkdir(parents=True, exist_ok=True)

    ues = pd.read_excel(UES_FILE)
    plot_perfil(ues, "grafico_perfil_enem.png")
    for chave, (titulo, perguntas) in UES_SECOES.items():
        plot_secao(ues, titulo, perguntas, f"grafico_ues_{chave}.png")

    esm = pd.read_excel(ESM_FILE)
    for chave, (titulo, perguntas) in ESM_SECOES.items():
        plot_secao(esm, titulo, perguntas, f"grafico_esm_{chave}.png")


if __name__ == "__main__":
    main()
