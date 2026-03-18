# Utilidades compartidas LIMITLESS
# Uso: 02 Data Quality, 03 Tailoring, 04 Pipeline, 05 Mock Interview

from pathlib import Path

SHARED_ROOT = Path(__file__).resolve().parent.parent

def get_shared_data_path(*parts):
    return SHARED_ROOT / "data" / Path(*parts)

def get_config_path(*parts):
    return SHARED_ROOT / "config" / Path(*parts)
