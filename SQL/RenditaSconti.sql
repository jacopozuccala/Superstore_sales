-- Gli sconti funzionano?

SELECT discount,
    COUNT(*) AS orders,
    ROUND(AVG(profit), 2) AS avg_profit
FROM superstore_sales
GROUP BY discount
ORDER BY discount;
