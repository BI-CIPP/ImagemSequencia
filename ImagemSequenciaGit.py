import requests
import base64
import os

# 🔐 CONFIGURAÇÕES
GITHUB_TOKEN = "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"
REPO = "BI-CIPP/ImagemSequencia"
BRANCH = "main"

# 📁 Caminho da imagem
FILE_PATH = r"C:\OneDrive\CIPP\GEOPP - GEOPP\03-CCO\SEQUÊNCIA POWER BI\Imagem\SEQUÊNCIA DE ATRACAÇÃO.png"

# 📌 Nome dentro do repositório
FILE_NAME = os.path.basename(FILE_PATH)
GITHUB_PATH = f"imagens/{FILE_NAME}"

# 📖 Lê e converte para base64
with open(FILE_PATH, "rb") as file:
    content = base64.b64encode(file.read()).decode("utf-8")

# 🔎 Verifica se arquivo já existe (para atualizar)
url = f"https://api.github.com/repos/{REPO}/contents/{GITHUB_PATH}"

headers = {
    "Authorization": f"token {GITHUB_TOKEN}"
}

response = requests.get(url, headers=headers)

sha = None
if response.status_code == 200:
    sha = response.json()["sha"]

# 📤 Upload / Update
data = {
    "message": f"Upload {FILE_NAME}",
    "content": content,
    "branch": BRANCH
}

if sha:
    data["sha"] = sha  # necessário para update

upload = requests.put(url, json=data, headers=headers)

if upload.status_code in [200, 201]:
    print("✅ Upload realizado com sucesso!")

    # 🔗 LINK RAW (Power BI)
    raw_url = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/{GITHUB_PATH}"
    print("🌍 Link RAW:", raw_url)

else:
    print("❌ Erro:", upload.json())