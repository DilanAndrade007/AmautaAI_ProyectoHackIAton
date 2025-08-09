import json, csv, sys
from pathlib import Path

# === Definir ruta raíz del proyecto ===
ROOT_DIR = Path(__file__).resolve().parent
sys.path.append(str(ROOT_DIR))  # añade carpeta actual
sys.path.append(str(ROOT_DIR / "data_financieros"))  # añade carpeta de módulos

from data_financieros.extractor_financiero import parse_balance_tables, parse_resultados_tables
from utils.construir_json import build_unified_json

if __name__ == "__main__":
    # PDFs dentro de extraccion/data/financiero
    PATH_BALANCE = (ROOT_DIR / "data" / "financiero" / "Balance_Estado_de_Situacion_Financiera.pdf").resolve()
    PATH_RESULTADOS = (ROOT_DIR / "data" / "financiero" / "Estado_de_Resultado_Integral.pdf").resolve()

    balance_vals = parse_balance_tables(PATH_BALANCE)
    resultados_vals = parse_resultados_tables(PATH_RESULTADOS)

    record = build_unified_json(
        empresa="NOMBRE EMPRESA S.A.",
        sector="(opcional)",
        balance_vals=balance_vals,
        resultados_vals=resultados_vals,
        urls=["https://www.supercias.gob.ec/"]
    )

    # === Guardar JSON ===
    json_path = ROOT_DIR / "data" / "data_financieros.json"
    json_path.parent.mkdir(parents=True, exist_ok=True)  # crea carpeta si no existe
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(record, f, ensure_ascii=False, indent=2)

    # === Guardar CSV ===
    csv_path = ROOT_DIR / "data" / "data_financieros.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["id", "empresa", "sector"] + list(record["datos_numericos"].keys())
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        row = {"id": record["id"], "empresa": record["empresa"], "sector": record["sector"]}
        row.update(record["datos_numericos"])
        writer.writerow(row)

    print(f"JSON guardado en: {json_path}")
    print(f"CSV guardado en: {csv_path}")
