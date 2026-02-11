-- Categorie che rendono maggiormente?

SELECT category,
    ROUND(AVG(profit_margin), 2) AS avg_margin
FROM superstore_sales
GROUP BY category
ORDER BY avg_margin DESC;
