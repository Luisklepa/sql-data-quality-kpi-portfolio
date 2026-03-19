# 05 — Mock Interview Generator

## Objetivo

- **Qué es:** Sistema que transforma CV, experiencia de proyectos y JD en material de preparación para entrevistas: preguntas probables (reclutador y técnicas), esqueletos de respuesta y advertencias.
- **Por qué existe:** Aumenta la tasa de pase en entrevistas al tener respuestas consistentes, con framing de negocio y evitando respuestas débiles o contradictorias.
- **Empleabilidad:** Mejora la preparación y la credibilidad al alinear respuestas al perfil real y a la lista “no claim”.

## Alcance

- **Debe tener:** Preguntas tipo reclutador, preguntas técnicas, esqueletos de respuesta creíbles, follow-ups, advertencias de respuestas débiles, framing de negocio y talking points.
- **Debería tener:** Uso de perfil y no-claim-list para no sugerir respuestas que inventen experiencia.
- **Opcional:** Más variantes por tipo de rol o industria.

## Herramientas

- Python 3, PyYAML. Config en `_shared/config/`.

## Cómo ejecutar

1. Opcional: poner un JD en `jd.txt` para preguntas específicas de la oferta.
2. `python generate.py` o `python generate.py jd.txt`
3. Revisar `output/mock_interview_*.md`.

## Supuestos y limitaciones

- Las preguntas son plantillas basadas en perfil y JD; no sustituyen la preparación activa (ensayar en voz alta).
- Las respuestas son esqueletos; hay que personalizarlas con ejemplos concretos.

## Defensa en entrevista

Este proyecto es meta: sirve para preparar entrevistas. En la entrevista puedes mencionar que usas un sistema local para preparar respuestas alineadas a tu CV y al JD.
