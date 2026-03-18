# Data Quality + KPI Pack — Defensa en entrevista

## 5 preguntas probables

1. **¿Qué comprobaciones de calidad incluyes y por qué?**  
2. **¿Cómo defines la reconciliación de KPIs?**  
3. **¿En qué formato entregas los resultados y a quién van dirigidos?**  
4. **¿Has usado herramientas de DQ en producción o solo scripts ad hoc?**  
5. **¿Cómo priorizas qué validar cuando hay poco tiempo?**

## 5 respuestas concisas

1. **Comprobaciones:** Nulos en columnas clave (ids, cantidad, precio), duplicados por clave de transacción, rangos (cantidad positiva, descuento 0–100%). Son las que más impacto tienen en reporting (totales erróneos, filas duplicadas).  
2. **Reconciliación:** Comparar el total de un KPI calculado desde la fuente (p. ej. suma de revenue en fact) con el mismo KPI obtenido por otra vía (p. ej. agregación por venta y luego suma). Si la diferencia es despreciable, el cálculo es consistente.  
3. **Formato:** CSV/Excel para detalle de issues y reconciliación; un reporte en Markdown con resumen ejecutivo para que negocio o control puedan revisar sin abrir tablas.  
4. **Herramientas:** En proyectos reales he usado validaciones en Power Query y Excel, y scripts en Python para checks repetibles. No he operado herramientas enterprise tipo Great Expectations o similar; el pack demuestra el criterio y la lógica, no un producto concreto.  
5. **Priorización:** Primero integridad referencial y nulos en claves; luego duplicados y rangos que afecten KPIs críticos (revenue, unidades). Lo que no afecte totales o decisiones se deja para una segunda vuelta.

## 3 insights de negocio

- **Trazabilidad:** Poder explicar de dónde sale cada número del reporte y que coincida con la fuente reduce errores de decisión y auditoría.  
- **Descuentos:** Validar que descuento esté en 0–100 evita totales de revenue negativos o inflados en reportes de margen.  
- **Un solo punto de verdad:** La reconciliación asegura que el dashboard y el export/Excel cuenten la misma historia.

## 3 limitaciones

- **Reglas fijas:** Las reglas están pensadas para este schema; en otro dominio habría que definir columnas y umbrales de nuevo.  
- **Sin orquestación:** Es un script batch; no hay scheduling ni alertas automáticas.  
- **Tolerancia numérica:** La reconciliación usa una tolerancia pequeña (0.01) por redondeos; en moneda real podría definirse un umbral de negocio.
