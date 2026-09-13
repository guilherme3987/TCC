#!/usr/bin/env bash
#
# Comprime os arquivos PDF do repositório com Ghostscript.
#
# Uso:
#   ./scripts/compress_pdfs.sh            # processa todos os PDFs do working tree
#   PDFSETTINGS=/printer ./scripts/compress_pdfs.sh   # força outro nível de qualidade
#
# Níveis de qualidade (Ghostscript -dPDFSETTINGS):
#   /screen   (72 dpi)   -> menor tamanho
#   /ebook    (150 dpi)  -> bom equilíbrio (padrão)
#   /printer  (300 dpi)  -> boa qualidade, maior
#   /prepress (300 dpi)  -> qualidade superior (preserva maior fidelidade)
#
# Comportamento: o arquivo original só é substituído se o comprimido ficar
# pelo menos MIN_RATIO (5%) menor; caso contrário a versão original é mantida.

set -euo pipefail

PDFSETTINGS="${PDFSETTINGS:-/ebook}"
MIN_RATIO="${MIN_RATIO:-0.05}"
COMPAT_LEVEL="${COMPAT_LEVEL:-1.5}"

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

command -v gs >/dev/null 2>&1 || { echo "erro: Ghostscript (gs) não encontrado"; exit 1; }

mapfile -t PDFS < <(find . -type f -name '*.pdf' -not -path './.git/*' | sort)
if [ "${#PDFS[@]}" -eq 0 ]; then
    echo "Nenhum arquivo PDF encontrado."
    exit 0
fi

TMP="$(mktemp --suffix=.pdf)"
trap 'rm -f "$TMP"' EXIT

total_original=0
total_final=0
compressed=0

for pdf in "${PDFS[@]}"; do
    original_size="$(stat -c %s "$pdf")"
    if [ "$original_size" -lt 1024 ]; then
        echo "  ignorado (muito pequeno): $pdf"
        continue
    fi

    gs -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite \
        -dPDFSETTINGS="$PDFSETTINGS" \
        -dCompatibilityLevel="$COMPAT_LEVEL" \
        -dAutoRotatePages=/None \
        -sOutputFile="$TMP" "$pdf" || {
            echo "  erro ao comprimir $pdf (mantendo original)"; continue; }

    new_size="$(stat -c %s "$TMP")"
    gain=$(( original_size - new_size ))
    # só substitui se a redução for maior que MIN_RATIO
    if [ "$gain" -gt 0 ] && awk -v a="$original_size" -v b="$new_size" -v r="$MIN_RATIO" \
        'BEGIN { exit !((a-b)/a > r) }'; then
        mv -f "$TMP" "$pdf"
        echo "  comprimido  $pdf  ($(numfmt --to=iec --suffix=B "$original_size") -> $(numfmt --to=iec --suffix=B "$new_size"), -$((100*gain/original_size))%)"
        total_final=$(( total_final + new_size ))
        compressed=$(( compressed + 1 ))
    else
        echo "  mantido     $pdf  (sem ganho suficiente)"
        total_final=$(( total_final + original_size ))
    fi
    total_original=$(( total_original + original_size ))
done

echo
echo "Processados: ${#PDFS[@]} PDF(s), ${compressed} comprimido(s)."
echo "Tamanho total: $(numfmt --to=iec --suffix=B "$total_original") -> $(numfmt --to=iec --suffix=B "$total_final")"