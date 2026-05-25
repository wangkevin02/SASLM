import fitz  # PyMuPDF
from pathlib import Path
from PIL import Image

PDF_PATH = Path(__file__).parent / "framework.pdf"
OUTPUT_PATH = Path(__file__).parent.parent / "framework.jpg"
DPI = 300


def pdf_to_img(pdf_path: Path, output_path: Path, dpi: int = 300) -> None:
    doc = fitz.open(str(pdf_path))
    page = doc[0]  # 取第一页

    zoom = dpi / 72  # PDF 默认 72 dpi
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat, alpha=False)

    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    img.save(str(output_path), "JPEG", quality=95, dpi=(dpi, dpi))
    print(f"Saved to {output_path} ({pix.width}x{pix.height} @ {dpi} dpi)")


if __name__ == "__main__":
    pdf_to_img(PDF_PATH, OUTPUT_PATH, DPI)
