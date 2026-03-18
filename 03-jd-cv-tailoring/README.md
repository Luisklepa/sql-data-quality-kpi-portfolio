# 03 — JD / CV Tailoring Assistant

## Objetivo

- **Qué es:** Utilidad local para adaptar aplicaciones a ofertas: parsing del JD, extracción de palabras clave, análisis de gaps y sugerencias de headline, summary y bullets.
- **Por qué existe:** Aumenta la probabilidad de entrevista alinear el CV y el resumen al lenguaje de la oferta sin inventar experiencia.
- **Empleabilidad:** Mejora el fit percibido y el ATS sin comprometer credibilidad.

## Alcance

- **Debe tener:** Análisis de JD (keywords, requisitos), gap analysis frente al perfil real, headline recomendado, resumen sugerido, sugerencias de bullets y “why I fit”.
- **Debería tener:** Respeto estricto de `no-claim-list` y `profile.yaml` para no alucinar herramientas o roles.
- **Opcional:** Salida en formato listo para pegar en portales.

## Herramientas

- Python 3, PyYAML. Perfil y restricciones en `_shared/config/`.

## Cómo ejecutar

1. Poner el texto del JD en un archivo (ej. `jd.txt`) o pasarlo por stdin.
2. `python tailor.py jd.txt` o `python tailor.py < jd.txt`
3. Revisar la salida en pantalla y, si se indica, en `output/tailoring_*.md`.

## Supuestos y limitaciones

- El análisis es heurístico (palabras clave y coincidencias); no sustituye la lectura crítica del JD.
- Las sugerencias deben revisarse manualmente para no afirmar nada que no sea cierto.

## Defensa en entrevista

Ver `INTERVIEW_DEFENSE.md`.
