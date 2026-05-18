
-- Top 5 Sales

    SELECT Category, SUM(Sales) as Total_Sales
    FROM superstore
    GROUP BY Category
    ORDER BY Total_Sales DESC
    LIMIT 5;
    

-- Profit By Region

    SELECT Region, SUM(Profit) as Total_Profit
    FROM superstore
    GROUP BY Region;
    

-- Average Discount

    SELECT AVG(Discount) as Avg_Discount
    FROM superstore;
    

-- Top Customers

    SELECT "Customer Name", SUM(Sales) as Total_Sales
    FROM superstore
    GROUP BY "Customer Name"
    ORDER BY Total_Sales DESC
    LIMIT 10;
    
