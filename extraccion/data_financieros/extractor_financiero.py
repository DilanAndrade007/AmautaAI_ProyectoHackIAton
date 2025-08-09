from pathlib import Path
import pdfplumber
from utils.financiero_util import normalize_text, to_float

def extract_table_values_third_col(pdf_path: Path, targets):
    targets_norm = [normalize_text(t) for t in targets]
    found = {}
    if not pdf_path.exists():
        return found
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            for tbl in page.extract_tables() or []:
                for row in tbl:
                    raw_cells = [(c or "").strip() for c in row]
                    norm_cells = [normalize_text(c) for c in raw_cells]
                    for idx, tnorm in enumerate(targets_norm):
                        if tnorm in norm_cells:
                            nums = [to_float(c) for c in raw_cells if to_float(c) is not None]
                            if nums:
                                found[targets[idx]] = nums[-1]
            if all(t in found for t in targets):
                break
    return found

LABELS_BALANCE = [
    "ACTIVOS FINANCIEROS",
    "ACTIVO CORRIENTE",
    "PASIVO",
    "PASIVO CORRIENTE",
    "PATRIMONIO NETO",
    "CAPITAL",
    "GANANCIAS ACUMULADAS",
    "GANANCIA NETA DEL PERIODO"
]

LABELS_RESULTADOS = [
    "VENTA DE BIENES"
]

def parse_balance_tables(path_pdf: Path):
    return extract_table_values_third_col(path_pdf, LABELS_BALANCE)

def parse_resultados_tables(path_pdf: Path):
    return extract_table_values_third_col(path_pdf, LABELS_RESULTADOS)
