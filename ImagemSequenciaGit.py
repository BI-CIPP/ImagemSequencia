import requests
import base64
import os

# 🔐 CONFIGURAÇÕES (use variável de ambiente)
GITHUB_TOKEN = "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"
REPO = "BI-CIPP/ImagemSequencia"
BRANCH = "main"

# 📁 Caminho da imagem
FILE_PATH = r"C:\OneDrive\CIPP\GEOPP - GEOPP\03-CCO\SEQUÊNCIA POWER BI\Imagem\SEQUÊNCIADEATRACAÇÃO.png"

# 📌 Nome dentro do repositório
FILE_NAME = os.path.basename(FILE_PATH)
GITHUB_PATH = f"imagens/{FILE_NAME}"

# 📖 Lê e converte para base64
with open(FILE_PATH, "rb") as file:
    content = base64.b64encode(file.read()).decode("utf-8")

# 🔗 URL da API
url = f"https://api.github.com/repos/{REPO}/contents/{GITHUB_PATH}"

headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

# 🔎 Verifica se arquivo já existe
response = requests.get(url, headers=headers)

sha = None
if response.status_code == 200:
    sha = response.json()["sha"]
    print("🔄 Arquivo já existe → será ATUALIZADO")
elif response.status_code == 404:
    print("🆕 Arquivo não existe → será CRIADO")
else:
    print("❌ Erro ao verificar arquivo:", response.json())
    exit()

# 📤 Upload / Update
data = {
    "message": f"Upload automático: {FILE_NAME}",
    "content": content,
    "branch": BRANCH
}

if sha:
    data["sha"] = sha  # necessário para update

upload = requests.put(url, json=data, headers=headers)

# 📊 RESULTADO
if upload.status_code in [200, 201]:
    print("✅ Upload realizado com sucesso!")

    raw_url = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/{GITHUB_PATH}"
    html_url = f"https://github.com/{REPO}/blob/{BRANCH}/{GITHUB_PATH}"

    print("🌍 Link RAW (Power BI):")
    print(raw_url)

    print("📂 Link GitHub:")
    print(html_url)

else:
    print("❌ Erro no upload:")
    print("Status:", upload.status_code)
    print(upload.json())