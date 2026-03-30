import requests
import base64
import os
import unicodedata

# ==========================================
# 🔐 CONFIGURAÇÕES
# ==========================================
GITHUB_TOKEN = "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"
REPO = "BI-CIPP/ImagemSequencia"
BRANCH = "main"

# 📁 Caminho da imagem
FILE_PATH = r"C:\OneDrive\CIPP\GEOPP - GEOPP\03-CCO\SEQUÊNCIA POWER BI\Imagem\SEQUÊNCIA DE ATRACAÇÃO.png"

# ==========================================
# 🔤 FUNÇÃO: NORMALIZAR NOME
# ==========================================
def normalizar_nome(nome):
    nome = unicodedata.normalize('NFKD', nome).encode('ASCII', 'ignore').decode('ASCII')
    nome = nome.replace(" ", "_")
    return nome

# ==========================================
# 📌 PREPARAÇÃO
# ==========================================
if not os.path.exists(FILE_PATH):
    print("❌ Arquivo não encontrado:", FILE_PATH)
    exit()

FILE_NAME_ORIGINAL = os.path.basename(FILE_PATH)
FILE_NAME = normalizar_nome(FILE_NAME_ORIGINAL)
GITHUB_PATH = f"imagens/{FILE_NAME}"

print(f"📄 Arquivo original: {FILE_NAME_ORIGINAL}")
print(f"📄 Nome normalizado: {FILE_NAME}")

# ==========================================
# 📖 LER E CONVERTER
# ==========================================
try:
    with open(FILE_PATH, "rb") as file:
        content = base64.b64encode(file.read()).decode("utf-8")
except Exception as e:
    print("❌ Erro ao ler arquivo:", str(e))
    exit()

# ==========================================
# 🔗 URL GITHUB API
# ==========================================
url = f"https://api.github.com/repos/{REPO}/contents/{GITHUB_PATH}"

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

# ==========================================
# 🔎 VERIFICAR SE JÁ EXISTE (PEGAR SHA)
# ==========================================
try:
    response = requests.get(url, headers=headers)
except Exception as e:
    print("❌ Erro na requisição GET:", str(e))
    exit()

sha = None

if response.status_code == 200:
    sha = response.json().get("sha")
    print("🔄 Arquivo já existe — será atualizado")
elif response.status_code == 404:
    print("🆕 Arquivo novo — será criado")
else:
    print("❌ Erro ao verificar arquivo:", response.json())
    exit()

# ==========================================
# 📤 UPLOAD / UPDATE
# ==========================================
data = {
    "message": f"Upload automático: {FILE_NAME}",
    "content": content,
    "branch": BRANCH
}

if sha:
    data["sha"] = sha  # necessário para sobrescrever

try:
    upload = requests.put(url, json=data, headers=headers)
except Exception as e:
    print("❌ Erro na requisição PUT:", str(e))
    exit()

# ==========================================
# ✅ RESULTADO
# ==========================================
if upload.status_code in [200, 201]:
    print("✅ Upload realizado com sucesso!")

    raw_url = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/{GITHUB_PATH}"

    print("\n🌍 LINK RAW (usar no Power BI):")
    print(raw_url)

    print("\n📌 Teste no navegador antes de usar no Power BI!")

else:
    print("❌ Erro no upload:")
    print(upload.status_code)
    print(upload.json())