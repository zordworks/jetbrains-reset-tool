# 🔄 DarkWorks JetBrains Trial Reset Tool

<p align="center">
  <img src="https://img.shields.io/badge/Version-3.0.0-blue" alt="Versão">
  <img src="https://img.shields.io/badge/Python-3.11+-yellow" alt="Python">
  <img src="https://img.shields.io/badge/Platform-Windows-lightgrey" alt="Plataforma">
  <img src="https://img.shields.io/badge/License-GPLv3-green" alt="Licença">
  <img src="https://img.shields.io/badge/Environment-.venv%20included-brightgreen" alt="Ambiente Virtual">
</p>

## 🌟 Recursos Principais

### 🔄 Reset Completo
- Remove arquivos de configuração em:
  - `%APPDATA%\JetBrains`
  - `%LOCALAPPDATA%\JetBrains` 
  - `%USERPROFILE%\.JetBrains`
- Limpa chaves de registro relacionadas

### 🛡️ Segurança Integrada
- Cria ponto de restauração automático (Windows)
- Verifica e fecha processos ativos antes da limpeza
- Log detalhado em `%TEMP%\jetbrains_reset_log.txt`

### 🖥️ Interface Amigável
- Menu interativo com opções claras
- Feedback visual durante operações
- Detecção automática de produtos instalados

## 📥 Download

Versões estáveis disponíveis na seção de [Releases](https://github.com/zordworks/jetbrains-reset-tool/releases).

⚠️ **Atenção**: Atualmente o `build.py` está com problemas. Recomendo usar o `buildportable.py` que oferece melhor estabilidade.

## 🛠️ Compilação e Uso

### ⚡ Versão Pronta para Uso (Recomendada)
O projeto já inclui um ambiente virtual (`.venv`) configurado com todas as dependências necessárias. Basta:

```bash
# 1. Clone o repositório
git clone https://github.com/DarkWorks/jetbrains-reset-tool.git
cd jetbrains-reset-tool

# 2. Ative o ambiente virtual incluso
# Windows:
.venv\Scripts\activate

# 3. Execute a versão portable (recomendado)
python buildportable.py

# 4. Acesse a pasta 'compilado' e execute:
launcher.exe
