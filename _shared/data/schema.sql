-- Schema retail para LIMITLESS (01 SQL Lab, 02 Data Quality, 04 Pipeline)
-- Modelo dimensional simplificado: ventas, clientes, productos, tiempo.
-- Uso: SQLite / SQL genérico para ejercicios y reconciliación KPI.

-- Dimensiones
CREATE TABLE IF NOT EXISTS dim_customer (
    customer_id   INTEGER PRIMARY KEY,
    customer_name TEXT,
    segment       TEXT,   -- e.g. Retail, Corporate
    region        TEXT,
    created_at    TEXT
);

CREATE TABLE IF NOT EXISTS dim_product (
    product_id    INTEGER PRIMARY KEY,
    product_name  TEXT,
    category      TEXT,
    subcategory   TEXT,
    unit_cost     REAL,
    created_at    TEXT
);

CREATE TABLE IF NOT EXISTS dim_date (
    date_id   INTEGER PRIMARY KEY,  -- YYYYMMDD
    date_full DATE,
    year      INTEGER,
    quarter   INTEGER,
    month     INTEGER,
    week      INTEGER
);

-- Hecho: transacciones de venta
CREATE TABLE IF NOT EXISTS fact_sales (
    sale_id      INTEGER PRIMARY KEY,
    sale_date_id INTEGER,
    customer_id  INTEGER,
    product_id   INTEGER,
    quantity     INTEGER,
    unit_price   REAL,
    discount_pct REAL DEFAULT 0,
    FOREIGN KEY (sale_date_id) REFERENCES dim_date(date_id),
    FOREIGN KEY (customer_id)  REFERENCES dim_customer(customer_id),
    FOREIGN KEY (product_id)   REFERENCES dim_product(product_id)
);

-- Vistas útiles para KPIs (reconciliación en 02)
-- Revenue = quantity * unit_price * (1 - discount_pct/100)
-- Cost = quantity * unit_cost (desde dim_product)
