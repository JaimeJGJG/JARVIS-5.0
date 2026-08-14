# Assistente Virtual J.A.R.V.I.S
### Just A Rather Very Intelligent System

<img width="1131" height="517" alt="Captura de tela_JARVIS" src="https://github.com/user-attachments/assets/d98f788b-7d43-4954-9c44-5a4b5877be46" />


```text
        ______J.A.R.V.I.S______
(Just A Rather Very Intelligent System)
```

> **Status do Projeto:** ⚠️ Versão Alpha (Não oficial)
> Surgido quase do zero e desenvolvido inteiramente por apenas **1 pessoa**, este projeto está em fase de testes contínuos. Criado com esforço para funcionar de forma sólida e estável, atualizações são lançadas quase diariamente. Podem ocorrer erros e bugs, e muita coisa pode mudar até a versão final. Obrigado pelo apoio!

---

*   **Versão Atual:** `5.0.8`
*   **Último Update:** 26/07/2026
*   **Desenvolvedor:** [JaimeJGJG](https://github.com)
*   **Compatibilidade Básica:** Debian, Ubuntu e Linux Mint
*   **Homologação:** Testado especificamente no **Linux Mint 22.3** (Apto a rodar em distros mais recentes baseadas em Ubuntu e Debian)

---

## 🚀 Características e Recursos

*   **Reconhecimento de Voz Offline:** Sistema de processamento local utilizando o motor **VOSK** (Garante privacidade total, pois atende aos comandos básicos de voz do usuário de forma 100% offline).
*   **Interface Gráfica (GUI):** Construída com **PyQt5** para uma experiência visual fluida e moderna.
*   **Foco em Estabilidade:** Desenvolvido com foco em execução sólida e consistência de código.

---

## 🛠️ Guia de Instalação e Configuração

Siga rigorosamente a ordem dos comandos abaixo no terminal da sua distribuição Linux para garantir o funcionamento correto do J.A.R.V.I.S.

### 1. Preparação do Sistema

Atualize os repositórios e instale o gerenciador de pacotes do Python junto com o suporte a ambientes virtuais e ferramentas de extração:

```bash
sudo apt update
sudo apt install python3-pip python3-venv wget unzip -y
```

### 2. Instalação de Módulos e Dependências do Sistema

Instale as bibliotecas e ferramentas nativas necessárias para áudio, interface e automação:

```bash
sudo apt install python3-pyaudio portaudio19-dev espeak python3-dbus python3-pyqt5 xdotool playerctl -y
```

### 2.5. Baixando e Configurando o Modelo de Voz (VOSK)

Para que o J.A.R.V.I.S reconheça seus comandos em português, o motor VOSK precisa da pasta do modelo nomeada como `PTBR` exatamente na raiz do projeto. 

Abra o seu terminal **dentro da pasta principal do JARVIS** e execute a sequência abaixo:

```bash
# 1. Faz o download do modelo oficial do VOSK para Português
wget https://alphacephei.com

# 2. Extrai o arquivo compactado no diretório atual
unzip vosk-model-small-pt-0.3.zip

# 3. Renomeia a pasta extraída original para PTBR
mv vosk-model-small-pt-0.3 PTBR

# 4. Remove o arquivo zip que foi baixado para limpar o projeto
rm vosk-model-small-pt-0.3.zip
```

### 3. Configuração do Ambiente Virtual (VENV)

Ainda na pasta principal do projeto, execute os passos abaixo para isolar o ambiente do Python:

```bash
# Criar o ambiente virtual
python3 -m venv .venv

# Ativar o ambiente virtual
source .venv/bin/activate

# Atualizar o gerenciador pip3
pip3 install -U pip
```

### 4. Instalação dos Módulos Python (via pip3)

Com o ambiente virtual ativado (indicado por `(.venv)` no terminal), instale todas as bibliotecas do projeto:

```bash
pip3 install SpeechRecognition jsonlib-python3 playsound3 xdotool pyaudio geocoder \
random2 pyttsx3 datetime espeakng psutil PyQt5 vosk plyer wikipedia \
numpy pytube pyperclip clipboard speedtest-cli pydbus requests
```

---

## 📦 Compilação e Criação de Executáveis

Se deseja transformar o código em um executável independente, instale primeiro as ferramentas de compilação dentro do ambiente virtual:

```bash
pip3 install pyinstaller auto-py-to-exe
```

### Método 1: Gerando Executável Manualmente (Interface Gráfica)
1. No terminal ativo, digite: `auto-py-to-exe` (uma interface abrirá no seu navegador).
2. Insira o caminho até o seu script `.py` principal.
3. Selecione a opção **"One File"** (arquivo único).
4. Escolha o modo de exibição correspondente (**Terminal** ou **Janela**).
5. Vá em **"Settings"** e adicione as dependências e imports em **"collect-all"**.
6. Clique no botão **"CONVERT .PY TO EXE"**.

### Método 2: Gerando Automaticamente (Scripts inclusos)
Abra o terminal na pasta do projeto e execute o script correspondente ao modo que deseja gerar:

*   **Modo Terminal:**
    ```bash
    sh ./auto_gen.sh Assistente.py
    ```
*   **Modo Janela (Interface Gráfica):**
    ```bash
    sh ./auto_gen_janela.sh JARVIS.py
    sh ./auto_gen_janela.sh ListaC.py
    sh ./auto_gen_janela.sh Configurar.py
    ```

> Após finalizar a utilização ou compilação no ambiente virtual, você pode fechá-lo digitando: `deactivate`

---

## 🗜️ Gerando Pacote de Instalação `.deb`

Para empacotar o J.A.R.V.I.S e distribuí-lo de forma nativa em sistemas baseados em Debian/Ubuntu/Mint:

1. Abra o terminal.
2. Execute o comando de empacotamento apontando para as pastas corretas:
   ```bash
   dpkg-deb -b <Caminho_Do_Executavel> <Pasta_Onde_Ficara_O_Deb>
   ```

---

## ⚠️ Isenção de Responsabilidade (Disclaimer)

O uso deste software é por sua conta e risco. O desenvolvedor **não se responsabiliza** por qualquer mau uso do sistema, tampouco por eventuais danos causados ao seu sistema operacional, arquivos, dados ou dispositivo físico.

## 📄 Licença

Este projeto está sob os termos da licença **Apache 2.0** - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
