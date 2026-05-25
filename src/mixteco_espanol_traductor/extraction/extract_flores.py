"""Extract Spanish sentences from FLORES-200.

This module downloads the Spanish subset of FLORES-200 from HuggingFace
and creates two outputs:

1. A CSV file for technical processing.
2. An Excel template for human Mixtec translation.

Extrae frases en español desde FLORES-200.

Este módulo descarga el subconjunto en español de FLORES-200 desde
HuggingFace y crea dos salidas:

1. Un archivo CSV para procesamiento técnico.
2. Una plantilla Excel para traducción humana al mixteco.
"""

from pathlib import Path
from urllib.request import urlretrieve

import pandas as pd

PARQUET_URL = (
    "https://huggingface.co/datasets/haoranxu/FLORES-200/"
    "resolve/refs%2Fconvert%2Fparquet/es-en/test/0000.parquet"
)

RAW_OUTPUT_PATH = Path("data") / "raw" / "flores200"
INTERIM_OUTPUT_PATH = Path("data") / "interim" / "flores200"
PROCESSED_OUTPUT_PATH = Path("data") / "processed" / "flores200"

RAW_PARQUET_FILE = RAW_OUTPUT_PATH / "flores200_es_en_test.parquet"
CSV_OUTPUT_FILE = INTERIM_OUTPUT_PATH / "spanish_flores200.csv"
EXCEL_OUTPUT_FILE = PROCESSED_OUTPUT_PATH / "spanish_flores200_template.xlsx"


def create_output_directories() -> None:
    """Create output directories if they do not exist.

    Crea los directorios de salida si no existen.
    """
    RAW_OUTPUT_PATH.mkdir(parents=True, exist_ok=True)
    INTERIM_OUTPUT_PATH.mkdir(parents=True, exist_ok=True)
    PROCESSED_OUTPUT_PATH.mkdir(parents=True, exist_ok=True)


def download_parquet_file() -> None:
    """Download the FLORES-200 Parquet file if it does not exist.

    Descarga el archivo Parquet de FLORES-200 si no existe.
    """
    if RAW_PARQUET_FILE.exists():
        print(f"Archivo Parquet existente: {RAW_PARQUET_FILE}")
        return

    print("Descargando archivo Parquet de FLORES-200...")
    urlretrieve(PARQUET_URL, RAW_PARQUET_FILE)
    print(f"Archivo Parquet descargado en: {RAW_PARQUET_FILE}")


def load_parquet_dataset() -> pd.DataFrame:
    """Load the FLORES-200 Parquet dataset.

    Carga el dataset FLORES-200 desde un archivo Parquet.

    Returns:
        DataFrame loaded from the Parquet file.
        DataFrame cargado desde el archivo Parquet.
    """
    return pd.read_parquet(RAW_PARQUET_FILE)


def build_translation_template(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Build the Spanish-to-Mixtec translation template.

    Construye la plantilla de traducción Español-Mixteco.

    Args:
        dataframe: Original FLORES-200 DataFrame.
            DataFrame original de FLORES-200.

    Returns:
        DataFrame formatted for human translation.
        DataFrame formateado para traducción humana.
    """
    rows = []

    for index, row in dataframe.iterrows():
        rows.append(
            {
                "id_frase": f"flores200_test_{index + 1:06d}",
                "division": "test",
                "idioma_origen": "espanol",
                "texto_espanol": row["es-en"]["es"],
                "idioma_destino": "mixteco",
                "variante_mixteco": "",
                "traduccion_mixteco": "",
                "nombre_traductor": "",
                "region_traductor": "",
                "estado_revision": "pendiente",
                "nombre_revisor": "",
                "notas": "",
            }
        )

    return pd.DataFrame(rows)


def export_dataset(dataframe: pd.DataFrame) -> None:
    """Export the dataset to CSV and Excel.

    Exporta el dataset a CSV y Excel.

    Args:
        dataframe: DataFrame to export.
            DataFrame que será exportado.
    """
    dataframe.to_csv(CSV_OUTPUT_FILE, index=False, encoding="utf-8")
    dataframe.to_excel(EXCEL_OUTPUT_FILE, index=False)


def main() -> None:
    """Run the FLORES-200 extraction process.

    Ejecuta el proceso de extracción de FLORES-200.
    """
    create_output_directories()
    download_parquet_file()

    raw_dataframe = load_parquet_dataset()
    template_dataframe = build_translation_template(raw_dataframe)

    export_dataset(template_dataframe)

    print(f"CSV creado en: {CSV_OUTPUT_FILE}")
    print(f"Excel creado en: {EXCEL_OUTPUT_FILE}")


if __name__ == "__main__":
    main()
