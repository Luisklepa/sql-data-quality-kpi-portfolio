# SQL Interview Lab — Defensa en entrevista

## 5 preguntas probables

1. **¿Cómo estructuraste el modelo de datos para los ejercicios?**  
2. **¿Qué tipo de consultas incluye el lab (JOINs, CTEs, window functions)?**  
3. **¿Cómo defines revenue y margen en este contexto?**  
4. **¿Por qué usaste SQLite y no otro motor?**  
5. **Dame un ejemplo de una consulta que hayas escrito y explícame la lógica de negocio.**

## 5 respuestas concisas

1. **Estructura:** Modelo dimensional (star schema): tablas de hechos de ventas y dimensiones de cliente, producto y fecha. Permite agregaciones por negocio (revenue por cliente, por categoría, por mes) y es el mismo tipo de modelo que uso en Power BI.  
2. **Tipos de consultas:** JOINs entre hecho y dimensiones, CTEs para reutilizar lógica (p. ej. revenue por venta), agregaciones con GROUP BY, window functions como RANK y LAG para rankings por región y comparación mes a mes.  
3. **Revenue y margen:** Revenue = cantidad × precio unitario × (1 - descuento/100). Margen = revenue menos coste (cantidad × coste unitario del producto); el coste viene de la dimensión producto.  
4. **SQLite:** Para portabilidad y reproducibilidad: un solo archivo, sin servidor, suficiente para ejercicios y para demostrar nivel de SQL. En trabajo real uso el motor que tenga el cliente (a menudo SQL Server o PostgreSQL para BI).  
5. **Ejemplo:** La consulta de revenue por segmento con % sobre el total: una CTE con revenue por segmento, otra con el total, y luego cociente para el porcentaje. Responde la pregunta de negocio “qué segmento aporta más y en qué proporción”.

## 3 insights de negocio que puedo comentar

- **Recurrencia:** Identificar clientes con más de una compra (HAVING COUNT > 1) es la base de métricas de retención y repeat rate en retail.  
- **Impacto del descuento:** Filtrar o segmentar por descuento permite analizar si el revenue con descuento compensa en volumen lo que se pierde en margen.  
- **Segmento vs total:** El % de revenue por segmento (Corporate vs Retail) sirve para priorizar canal y estrategia comercial.

## 3 limitaciones / trade-offs que defiendo con honestidad

- **Dataset pequeño y sintético:** Pensado para práctica y demostración, no para rendimiento ni escalabilidad. En producción los volúmenes y la optimización serían otros.  
- **SQLite:** No tiene todas las funciones de SQL Server o PostgreSQL (p. ej. algunas de fechas o ventana); para entrevistas técnicas con otro motor adaptaría la sintaxis.  
- **Sin historización de dimensiones:** El modelo es tipo snapshot simple; en un entorno real podría necesitar SCD o versionado para historial.
