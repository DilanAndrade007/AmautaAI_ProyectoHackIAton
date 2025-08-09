import uuid
from datetime import datetime

def build_unified_json(empresa, sector, balance_vals, resultados_vals, urls=None, descripcion_empresa=None):
    urls = urls or []
    map_fields = {
        "ACTIVOS FINANCIEROS": "activos_financieros",
        "ACTIVO CORRIENTE": "activos_corrientes",
        "PASIVO": "pasivos",
        "PASIVO CORRIENTE": "pasivos_corrientes",
        "PATRIMONIO NETO": "patrimonio_neto",
        "CAPITAL": "capital",
        "GANANCIAS ACUMULADAS": "ganancias_acumuladas",
        "GANANCIA NETA DEL PERIODO": "ganancia_neta_periodo",
        "VENTA DE BIENES": "ventas"
    }

    datos_numericos = {
        "ventas": None,
        "pasivos": None,
        "activos_corrientes": None,
        "pasivos_corrientes": None,
    }

    for k, v in (balance_vals or {}).items():
        if k in map_fields:
            datos_numericos[map_fields[k]] = v
    for k, v in (resultados_vals or {}).items():
        if k in map_fields:
            datos_numericos[map_fields[k]] = v

    return {
        "id": str(uuid.uuid4()),
        "empresa": empresa,
        "sector": sector,
        "descripcion_empresa": descripcion_empresa,
        "fuente_tipo": "scvs",
        "fuente_nombre": "Superintendencia de Compañías, Valores y Seguros",
        "plataforma": "offline",
        "periodo": None,
        "evento_fecha": None,
        "informacion": None,
        "nlp": {"sentiment": None, "language": None, "keywords": []},
        "datos_numericos": datos_numericos,
        "datos_sociales": {
            "seguidores": None, "likes": None, "comentarios": None,
            "shares": None, "posts_count": None, "rating": None
        },
        "tags": ["finanzas", "scvs"],
        "url": urls if isinstance(urls, str) else (urls[0] if urls else None),
        "quality_flags": {
            "lang_conf": None, "ocr": None, "review_verified": None, "human_validated": True
        },
        "fetched_at": datetime.utcnow().isoformat() + "Z",
        "updated_at": datetime.utcnow().isoformat() + "Z"
    }
