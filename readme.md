# 🔄 DarkWorks JetBrains Trial Reset Tool v3.0.0

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
- Suporte para todos os produtos JetBrains (IntelliJ, PyCharm, WebStorm, etc.)

### 🛡️ Segurança Integrada
- Cria ponto de restauração automático (Windows)
- Verifica e fecha processos ativos antes da limpeza
- Log detalhado em `%TEMP%\jetbrains_reset_log.txt`

### 🖥️ Interface Amigável
- Menu interativo com opções claras
- Feedback visual durante operações
- Detecção automática de produtos instalados

- ![image](https://github.com/user-attachments/assets/1e3d6cca-6c8c-4cf6-8216-ab6796014603)

![image](https://github.com/user-attachments/assets/d4d666bd-5558-4c54-af0b-fcb25df7b80e)


## 📥 Download

### 🚀 Versão Portable (Recomendada)
- `jetbrains_reset_tool_portable_v3.0.0.zip`
  - **Tamanho:** 7.985 KB
  - **Hashes:**
    ```
    MD5:    90b7f36bc4f75b4d0e1e61625224e6f7
    SHA1:   02dc33724b4a3f332d64553b43799559629352f6
    SHA256: e6a12371477d0c0d6821c5918325d7f0e91f033e04fd655a551004b1189eaef0
    ```

⚠️ **Atenção**: Utilize o `buildportable.py` para melhor estabilidade.

## 🛠️ Como Usar
1. **Download** da versão portable
2. **Extraia** o arquivo ZIP
3. **Execute** como administrador:
   ```bash
   launcher.exe
   ```
4. **Siga** as instruções no menu interativo

## ⚠️ Requisitos
- Windows 10/11
- Privilégios de administrador
- Python 3.11+ (já incluído na versão portable)

## 🔒 Verificação de Segurança
```powershell
Get-FileHash -Algorithm SHA256 .\jetbrains_reset_tool_portable_v3.0.0.zip
```

## 🛠️ Compilação para Desenvolvedores
```bash
# Clone e prepare o ambiente
git clone https://github.com/DarkWorks/jetbrains-reset-tool.git
cd jetbrains-reset-tool
.venv\Scripts\activate

# Build portable
python buildportable.py
```

> **Nota:** A versão portable contém tudo necessário e não requer instalação adicional.
