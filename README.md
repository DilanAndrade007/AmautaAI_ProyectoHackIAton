# AmautaAI – Scoring Alternativo para PYMEs con IA y Datos No Tradicionales

## 📌 Descripción
**AmautaAI** es una plataforma impulsada por inteligencia artificial que evalúa el riesgo financiero de pequeñas y medianas empresas (PYMEs) en Ecuador utilizando datos no tradicionales.  
Integra análisis de estados financieros, comportamiento en redes sociales, reseñas en línea y referencias comerciales para generar un **scoring híbrido** que mejora el acceso al crédito y reduce el riesgo en las decisiones de las instituciones financieras.

## 🎯 Objetivo
- Determinar el acceso al crédito con mayor precisión.
- Identificar negocios saludables aunque carezcan de historial crediticio formal.
- Mejorar la objetividad y velocidad en el análisis de solicitudes.
- Sugerir umbrales de crédito y simular escenarios de mejora.

## 📊 Fuentes de Datos
AmautaAI procesa información estructurada y no estructurada desde múltiples fuentes:
1. **Estados financieros** (SCVS):
   - Estado de situación financiera.
   - Estado de resultados integral.
   - Estado de cambios en el patrimonio.
   - Estado de flujo de efectivo.
2. **Historial de pagos/entregas** (dataset propio o simulado).
3. **Redes sociales** (Twitter/X, Facebook):
   - Actividad, reputación, engagement y contenido.
4. **Reseñas de terceros**:
   - Google Maps, marketplaces, Facebook Reviews.
5. **Referencias comerciales**:
   - Proveedores, clientes, historial de cumplimiento.
6. **APIs externas**:
   - Ej. RapidAPI para fuentes adicionales de reputación o comercio.

## 🧠 Proceso de Análisis
1. **Ingesta y normalización**:
   - Conversión de datos a un esquema unificado.
   - Limpieza de texto y estandarización de formatos.
2. **Análisis NLP**:
   - Sentimiento, keywords, idioma, metadatos.
3. **Vectorización y almacenamiento**:
   - ChromaDB como vector store para RAG (Retrieval-Augmented Generation).
4. **Cálculo del Scoring**:
   - Modelo híbrido (reglas + modelo ligero).
   - Score base (finanzas + pagos).
   - Score alternativo (social + referencias).
5. **Clasificación de riesgo**:
   - Categorías: Bajo, Medio, Alto.
   - Umbral de crédito sugerido.
6. **Simulación de escenarios (“what-if”)**:
   - Impacto de mejorar ingresos, reputación o pagos a tiempo.

## 📐 Esquema Unificado de Datos
```json
{
  "id": "string",
  "empresa": "string",
  "sector": "string",
  "descripcion_empresa": "string|null",
  "fuente_tipo": "scvs | social_x | social_fb | google_reviews | proveedor | prensa | otro",
  "fuente_nombre": "string",
  "plataforma": "string|null",
  "periodo": "YYYY | YYYY-Qn | null",
  "evento_fecha": "YYYY-MM-DDTHH:MM:SSZ|null",
  "informacion": "string|null",
  "nlp": {"sentiment": "number|null", "language": "string|null", "keywords": ["string"]},
  "datos_numericos": {
    "ventas": "number|null",
    "ocf": "number|null",
    "activos": "number|null",
    "pasivos": "number|null",
    "activos_corrientes": "number|null",
    "pasivos_corrientes": "number|null",
    "monto": "number|null",
    "dias_mora": "number|null",
    "estado_pago_code": "number|null"
  },
  "datos_sociales": {
    "seguidores": "number|null",
    "likes": "number|null",
    "comentarios": "number|null",
    "shares": "number|null",
    "posts_count": "number|null",
    "rating": "number|null"
  },
  "tags": ["string"],
  "url": "string|null",
  "quality_flags": {
    "lang_conf": "number|null",
    "ocr": "boolean|null",
    "review_verified": "boolean|null",
    "human_validated": "boolean|null"
  },
  "fetched_at": "YYYY-MM-DDTHH:MM:SSZ",
  "updated_at": "YYYY-MM-DDTHH:MM:SSZ"
}
