import requests
import base64
import os
import unicodedata

# 🔐 CONFIGURAÇÕES
GITHUB_TOKEN = "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"  # ⚠️ NUNCA exponha isso publicamente
REPO = "BI-CIPP/ImagemSequencia"
BRANCH = "main"

# 📁 Caminho da imagem
FILE_PATH = r"C:\OneDrive\CIPP\GEOPP - GEOPP\03-CCO\SEQUÊNCIA POWER BI\Imagem\SEQUÊNCIA DE ATRACAÇÃO.png"

# 🔤 Função para limpar nome do arquivo
def normalizar_nome(nome):
    nome = unicodedata.normalize('NFKD', nome).encode('ASCII', 'ignore').decode('ASCII')
    nome = nome.replace(" ", "_")
    return nome

# 📌 Nome tratado
FILE_NAME = normalizar_nome(os.path.basename(FILE_PATH))
GITHUB_PATH = f"imagens/{FILE_NAME}"

# 📖 Lê arquivo
if not os.path.exists(FILE_PATH):
    print("❌ Arquivo não encontrado:", FILE_PATH)
    exit()

with open(FILE_PATH, "rb") as file:
    content = base64.b64encode(file.read()).decode("utf-8")

# 🔗 URL GitHub API
url = f"https://api.github.com/repos/{REPO}/contents/{GITHUB_PATH}"

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

# 🔎 Verifica se já existe
response = requests.get(url, headers=headers)

sha = None
if response.status_code == 200:
    sha = response.json()["sha"]
    print("ℹ️ Arquivo já existe, será atualizado.")
elif response.status_code == 404:
    print("ℹ️ Arquivo não existe, será criado.")
else:
    print("❌ Erro ao verificar arquivo:", response.json())
    exit()

# 📤 Upload / Update
data = {
    "message": f"Upload {FILE_NAME}",
    "content": content,
    "branch": BRANCH
}

if sha:
    data["sha"] = sha

upload = requests.put(url, json=data, headers=headers)

# ✅ Resultado
if upload.status_code in [200, 201]:
    print("✅ Upload realizado com sucesso!")

    resposta = upload.json()
    download_url = resposta["content"]["download_url"]

    print("🌍 Link para usar no Power BI:")
    print(download_url)

else:
    print("❌ Erro no upload:")
    print(upload.status_code)
    print(upload.json())