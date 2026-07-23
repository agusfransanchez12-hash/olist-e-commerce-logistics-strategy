SQL
-- ============================================================
-- OLIST E-COMMERCE PROJECT: LOGISTICS & GMV GROWTH STRATEGY
-- Database Engine: SQLite
-- Author: Agustín F. Sánchez
-- ============================================================

-- 1. MASTER TABLE CREATION (Relational JOINs & Calculated Fields)
-- Combines orders, customers, items, products, and reviews into a unified analytical table
CREATE TABLE IF NOT EXISTS master_table AS
SELECT 
    o.order_id,
    o.customer_id,
    c.customer_state,
    c.customer_city,
    o.order_purchase_timestamp,
    o.order_delivered_customer_date,
    o.order_estimated_delivery_date,
    
    -- Actual delivery time in days calculated via JULIANDAY
    CAST(
        JULIANDAY(o.order_delivered_customer_date) - JULIANDAY(o.order_purchase_timestamp) 
        AS INTEGER
    ) AS delivery_time_days,
    
    -- Difference in days against original SLA estimation (delay_days)
    CAST(
        JULIANDAY(o.order_delivered_customer_date) - JULIANDAY(o.order_estimated_delivery_date) 
        AS INTEGER
    ) AS delay_days,
    
    -- Delay flag: 1 if order arrived late, 0 if delivered on time
    CASE 
        WHEN JULIANDAY(o.order_delivered_customer_date) > JULIANDAY(o.order_estimated_delivery_date) THEN 1
        ELSE 0
    END AS is_delayed,
    
    i.price,
    i.freight_value,
    p.product_category_name,
    r.review_score
FROM orders o
-- INNER JOIN: Links customers and order items
INNER JOIN customers c ON o.customer_id = c.customer_id
INNER JOIN order_items i ON o.order_id = i.order_id
-- LEFT JOIN: Retains sales even if category or review score is missing
LEFT JOIN products p ON i.product_id = p.product_id
LEFT JOIN reviews r ON o.order_id = r.order_id
-- Filter equivalent to df[df['order_status'] == 'delivered'] in Python
WHERE o.order_status = 'delivered' 
  AND o.order_delivered_customer_date IS NOT NULL;


-- 2. TOP PRODUCT CATEGORIES BY REVENUE
SELECT 
    product_category_name,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(price), 2) AS total_revenue
FROM master_table
GROUP BY product_category_name
ORDER BY total_revenue DESC
LIMIT 5;


-- 3. IMPACT OF DELIVERY DELAYS ON REVIEW SCORES
SELECT 
    CASE 
        WHEN is_delayed = 1 THEN 'Delayed'
        ELSE 'On Time'
    END AS delivery_status,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(AVG(review_score), 2) AS avg_rating
FROM master_table
GROUP BY delivery_status;


-- 4. GEOGRAPHIC BOTTLENECK ANALYSIS (By Customer State)
SELECT 
    customer_state,
    COUNT(DISTINCT order_id) AS total_orders,
    SUM(is_delayed) AS delayed_orders,
    -- Direct delay rate percentage calculated by summing delay flags
    ROUND((CAST(SUM(is_delayed) AS FLOAT) / COUNT(DISTINCT order_id)) * 100, 2) AS delay_rate_pct
FROM master_table
GROUP BY customer_state
HAVING total_orders > 100 -- Filters out low-volume states to prevent bias
ORDER BY delay_rate_pct DESC
LIMIT 5;