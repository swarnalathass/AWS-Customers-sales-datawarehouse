CREATE TABLE dim_customer (
    customer_id VARCHAR(20) PRIMARY KEY,
    customer_name VARCHAR(100),
    email VARCHAR(150),
    city VARCHAR(100),
    state VARCHAR(100),
    country VARCHAR(100),
    registration_date DATE
);

CREATE TABLE dim_product (
    product_id VARCHAR(20) PRIMARY KEY,
    product_name VARCHAR(150),
    category VARCHAR(100),
    price DECIMAL(12,2),
    supplier VARCHAR(150)
);

CREATE TABLE dim_date (
    date_key INTEGER PRIMARY KEY,
    full_date DATE,
    year INTEGER,
    month INTEGER,
    month_name VARCHAR(20),
    quarter INTEGER
);

CREATE TABLE fact_sales (
    sale_id VARCHAR(30),
    order_id VARCHAR(20),
    customer_id VARCHAR(20),
    product_id VARCHAR(20),
    order_date DATE,
    quantity INTEGER,
    unit_price DECIMAL(12,2),
    revenue DECIMAL(14,2),
    payment_method VARCHAR(50)
);
