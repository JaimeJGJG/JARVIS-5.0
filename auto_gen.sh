#!/bin/bash

REQUIREMENTS_FILE="requirements.txt"

# Verifique se um arquivo Python foi fornecido
if [ "$#" -ne 1 ]; then
    echo "Uso: $0 <arquivo_python>"
    exit 1
fi

arquivo_python="$1"

# Verifique se o arquivo existe
if [ ! -f "$arquivo_python" ]; then
    echo "Arquivo $arquivo_python não encontrado!"
    exit 1
fi

identificar_imports() {
    echo "Identificando módulos importados no script $arquivo_python..."

    # Extraindo os imports do script
    IMPORTS=$(grep -E "^import |^from " "$arquivo_python" | sed -e "s/from //g" -e "s/import //g" | sed "s/ .*//g" | sort -u)

    echo "Módulos importados identificados:"
    echo "$IMPORTS"

    # Salvando os módulos em um arquivo
    echo "$IMPORTS" > modules.txt
}

# Função para determinar a versão dos módulos e criar o requirements.txt
criar_requirements() {
    echo "Determinando versões dos módulos e criando $REQUIREMENTS_FILE..."

    # Limpar o arquivo requirements.txt existente
    > "$REQUIREMENTS_FILE"

    while read -r module; do
        if [ -n "$module" ]; then
            # Determina a versão do módulo
            version=$(pip3 show "$module" | grep Version: | awk '{print $2}')
            if [ -n "$version" ]; then
                echo "$module==$version" >> "$REQUIREMENTS_FILE"
            else
                echo NULL
            fi
        fi
    done < modules.txt

    echo "Arquivo $REQUIREMENTS_FILE criado com sucesso."
}

#Execução de indentificar os imports
identificar_imports

#cria o requirements.txt definitivo
criar_requirements

# Instalação de dependências
echo "Instalando dependências..."
pip3 install -r $REQUIREMENTS_FILE

# Instalação do PyInstaller
echo "Instalando PyInstaller..."
pip3 install pyinstaller

# Extrair módulos e pacotes importados
# Extrai linhas que começam com import ou from
# Remove a parte da versão (por exemplo, 'import module as alias' se houver)
imports=$(grep -E '^import |^from ' "$arquivo_python" | \
    sed -E 's/^import |^from //; s/ .*//; s/ as.*//; s/\..*//; s/^[[:space:]]*//; s/[[:space:]]*$//' | \
    sort -u)

# Gerar o comando PyInstaller em uma única linha
output_file="pyinstaller_command.txt"

# Inicia o comando PyInstaller
echo -n "pyinstaller --onefile --console " > "$output_file"

# Adiciona cada módulo com aspas e --collect-all na mesma linha
for module in $imports; do
    echo -n "--collect-all \"$module\" " >> "$output_file"
done

# Adiciona o arquivo Python ao final do comando
echo -n "$arquivo_python" >> "$output_file"

# Adiciona uma nova linha ao final
echo "" >> "$output_file"

echo "Comando PyInstaller gerado e salvo em '$output_file'."

# Executa o comando PyInstaller gerado
echo "Executando o comando PyInstaller..."
bash -c "$(cat "$output_file")"

# Antes da limpeza
BASE_NAME="${arquivo_python%.py}"
SPEC_FILE="${BASE_NAME}.spec"

# Limpeza
echo "Limpando arquivos temporários..."
rm -rf build
rm -rf __pycache__
rm -rf modules.txt
rm -rf $output_file
rm -rf $REQUIREMENTS_FILE
rm -rf $SPEC_FILE






