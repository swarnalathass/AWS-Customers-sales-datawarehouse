-- 1. Total revenue
SELECT SUM(revenue) AS total_revenue
FROM fact_sales;

-- 2. Revenue by product category
SELECT p.category, SUM(f.revenue) AS total_revenue
FROM fact_sales f
JOIN dim_product p ON f.product_id = p.product_id
GROUP BY p.category
ORDER BY total_revenue DESC;

-- 3. Top customers
SELECT c.customer_id, c.customer_name, SUM(f.revenue) AS total_spending
FROM fact_sales f
JOIN dim_customer c ON f.customer_id = c.customer_id
GROUP BY c.customer_id, c.customer_name
ORDER BY total_spending DESC
LIMIT 10;

-- 4. Monthly revenue
SELECT DATE_TRUNC('month', order_date) AS month,
       SUM(revenue) AS monthly_revenue
FROM fact_sales
GROUP BY 1
ORDER BY 1;

-- 5. Average order value
SELECT AVG(order_total) AS average_order_value
FROM (
    SELECT order_id, SUM(revenue) AS order_total
    FROM fact_sales
    GROUP BY order_id
) x;

-- 6. Revenue by city
SELECT c.city, SUM(f.revenue) AS revenue
FROM fact_sales f
JOIN dim_customer c ON f.customer_id = c.customer_id
GROUP BY c.city
ORDER BY revenue DESC;
