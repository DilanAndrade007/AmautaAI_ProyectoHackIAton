import re, unicodedata

def to_float(s):
    if s is None: return None
    s = str(s).strip()
    if not s: return None
    s = s.replace(" ", "")
    if s.count(",") > 0 and s.count(".") > 0:
        if s.rfind(",") > s.rfind("."):
            s = s.replace(".", "").replace(",", ".")
        else:
            s = s.replace(",", "")
    else:
        s = s.replace(",", "")
    try:
        return float(s)
    except:
        m = re.search(r"[-+]?\d{1,3}(?:[.,]\d{3})*(?:[.,]\d+)?", s)
        return float(m.group(0).replace(",", "")) if m else None

def normalize_text(s):
    if not s:
        return ""
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.upper().strip()
    s = re.sub(r"\s+", " ", s)
    return s
