import sys
from pathlib import Path
 
try:
    import fitz  # PyMuPDF
except ImportError:
    print("Erro: Biblioteca 'PyMuPDF' não instalada. Instale com: pip install PyMuPDF")
    sys.exit(1)
 
 
def convert_pdf_to_png(pdf_path: Path, output_dir: Path, dpi: int = 300):
    """
    Converte um PDF em imagens PNG de alta qualidade usando PyMuPDF.
 
    Args:
        pdf_path: Caminho para o arquivo PDF.
        output_dir: Diretório de saída para as imagens.
        dpi: Resolução das imagens (padrão: 300).
    """
    try:
        # Abre o documento PDF
        doc = fitz.open(str(pdf_path))
 
        # Nome base do arquivo sem extensão
        base_name = pdf_path.stem
 
        # Processa cada página
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            # Renderiza a página em alta resolução
            pix = page.get_pixmap(dpi=dpi)
            # Salva como PNG
            output_path = output_dir / f"{base_name}.png"
            pix.save(str(output_path))
            print(f"Salva: {output_path}")
 
        doc.close()
 
    except Exception as e:
        print(f"Erro ao converter {pdf_path}: {e}")
 
 
def process_folder(input_dir: Path, output_dir: Path, dpi: int = 300):
    """
    Processa todos os PDFs em uma pasta e converte para PNG.
 
    Args:
        input_dir: Diretório com os PDFs.
        output_dir: Diretório para salvar as imagens.
        dpi: Resolução das imagens.
    """
    if not input_dir.exists():
        print(f"Erro: Diretório de entrada não existe: {input_dir}")
        return
 
    # Cria diretório de saída se não existir
    output_dir.mkdir(parents=True, exist_ok=True)
 
    # Encontra todos os PDFs
    pdf_files = list(input_dir.glob("*.pdf"))
    if not pdf_files:
        print(f"Nenhum arquivo PDF encontrado em: {input_dir}")
        return
 
    print(f"Encontrados {len(pdf_files)} arquivo(s) PDF. Convertendo...")
 
    for pdf_file in pdf_files:
        convert_pdf_to_png(pdf_file, output_dir, dpi)
 
    print("Conversão concluída.")
 
 
def main():
    # Configurações (ajuste conforme necessário)
    input_directory = Path(r"C:\OneDrive\CIPP\GEOPP - GEOPP\03-CCO\SEQUÊNCIA POWER BI")
    output_directory = input_directory / "imagem"  # Subpasta para saída
    resolution_dpi = 300  # Alta qualidade
 
    # Processa a pasta
    process_folder(input_directory, output_directory, resolution_dpi)
 
 
if __name__ == "__main__":
    main()