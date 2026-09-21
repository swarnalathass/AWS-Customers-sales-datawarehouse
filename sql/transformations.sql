-- Example staging-to-fact transformation.
INSERT INTO fact_sales (
    sale_id, order_id, customer_id, product_id, order_date,
    quantity, unit_price, revenue, payment_method
)
SELECT
    oi.order_item_id,
    o.order_id,
    o.customer_id,
    oi.product_id,
    o.order_date,
    oi.quantity,
    oi.unit_price,
    oi.quantity * oi.unit_price AS revenue,
    o.payment_method
FROM staging_orders o
JOIN staging_order_items oi
  ON o.order_id = oi.order_id
WHERE o.order_status = 'Completed';
