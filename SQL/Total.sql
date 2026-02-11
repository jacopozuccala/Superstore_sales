SELECT region,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM superstore_sales
GROUP BY region;
