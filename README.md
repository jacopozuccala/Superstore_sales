# Superstore Sales Analysis

# Gestione e analisi di grandi quantità di dati forniti da uno store tramite l'utilizzo di Excel, SQL (postgreSQL), Visual Studio (Python) e Microsoft Power BI

Questo progetto analizza il dataset “Superstore Sales”, scaricato da Kaggle (https://www.kaggle.com/datasets/elijahconnectng/superstore-sales-dataset), con l’obiettivo di estrarre insight utili al supporto delle decisioni aziendali.

L’analisi si concentra su performance di vendita, redditività, segmentazione clienti, andamento temporale, distribuzione geografica e impatto degli sconti sul profitto.

Strumenti:
- Excel è stato utilizzato per una prima analisi esplorativa e per il controllo della qualità dei dati.
- PostgreSQL (pgAdmin 4) è stato utilizzato per la creazione del database e per l’esecuzione delle query SQL.
- Python (Visual Studio Code con supporto Copilot) è stato utilizzato per trasformazioni aggiuntive e analisi esplorative.
- Power BI è stato utilizzato per la creazione delle visualizzazioni e delle dashboard finali.

# Il dataset contiene informazioni sulle vendite, tra cui:

Order ID

Order Date e Ship Date

Customer ID e Customer Segment

Paese, città e regione

Categoria e sotto-categoria prodotto

Sales

Quantity

Discount

Profit


Pulizia e preparazione dei dati:
Il file CSV è stato aperto e verificato in Excel per:
Identificare eventuali valori mancanti
Controllare la coerenza delle colonne
Verificare i tipi di dato
Individuare possibili anomalie

Successivamente il dataset è stato importato in PostgreSQL, dove sono state definite le strutture delle tabelle e i tipi di dato appropriati.

# Creazione del database e analisi SQL; tramite query SQL sono state effettuate analisi su:

Vendite totali e profitto totale

Margine di profitto

Vendite per regione

Performance per categoria e sotto-categoria

Analisi dei segmenti cliente

Impatto degli sconti sulla redditività

Andamento temporale delle vendite (mensile e annuale)

Sono state inoltre create viste per facilitare l’aggregazione e l’analisi dei dati.


# Python è stato utilizzato per:

Supportare l’analisi esplorativa dei dati

Effettuare controlli incrociati sui risultati ottenuti tramite SQL

Preparare ulteriori aggregazioni utili per la fase di visualizzazione

# Visualizzazione dei dati

Le dashboard realizzate in Power BI mostrano:

Andamento delle vendite nel tempo

Distribuzione geografica delle vendite

Performance per categoria e sotto-categoria

Relazione tra sconti e profitto

Analisi dei segmenti cliente

Prodotti con performance migliori e peggiori

Le visualizzazioni sono state progettate per simulare un contesto reale di reporting aziendale.

# Risultati principali

L’analisi evidenzia una distribuzione non uniforme di vendite e profitti tra regioni e categorie. In diversi casi, sconti elevati riducono significativamente la marginalità. Alcune sotto-categorie generano volumi di vendita elevati ma con profitto contenuto, suggerendo possibili interventi su pricing o gestione dei costi.

Sono emersi inoltre pattern temporali utili per la pianificazione commerciale e l’ottimizzazione delle strategie promozionali.


// ENGLISH VERSION

# Superstore Sales Analysis

This project analyzes the “Superstore Sales” dataset, downloaded from Kaggle (https://www.kaggle.com/datasets/elijahconnectng/superstore-sales-dataset), with the objective of extracting insights useful for supporting business decision-making.

The analysis focuses on sales performance, profitability, customer segmentation, time trends, geographic distribution, and the impact of discounts on profit.

Tools used:

Excel was used for initial exploratory analysis and data quality control.

PostgreSQL (pgAdmin 4) was used for database creation and SQL query execution.

Python (Visual Studio Code with Copilot support) was used for additional transformations and exploratory analysis.

Power BI was used for creating the final visualizations and dashboards.

# The dataset contains sales information, including:

Order ID

Order Date and Ship Date

Customer ID and Customer Segment

Country, city, and region

Product category and sub-category

Sales

Quantity

Discount

Profit

Data cleaning and preparation:
The CSV file was opened and reviewed in Excel to:
Identify any missing values
Check column consistency
Verify data types
Detect possible anomalies

# The dataset was then imported into PostgreSQL, where table structures and appropriate data types were defined.

Database creation and SQL analysis; SQL queries were used to analyze:

Total sales and total profit

Profit margin

Sales by region

Performance by category and sub-category

Customer segment analysis

Impact of discounts on profitability

Sales trends over time (monthly and yearly)

Views were also created to facilitate data aggregation and analysis.

# Python was used to:

Support exploratory data analysis

Perform cross-checks on results obtained through SQL

Prepare additional aggregations useful for the visualization phase

# Data visualization

The dashboards created in Power BI show:

Sales trends over time

Geographic distribution of sales

Performance by category and sub-category

Relationship between discounts and profit

Customer segment analysis

Best and worst performing products

The visualizations were designed to simulate a real-world business reporting environment.

# Conclusions

The analysis highlights an uneven distribution of sales and profits across regions and categories. In several cases, high discounts significantly reduce profit margins. Some sub-categories generate high sales volumes but limited profit, suggesting potential improvements in pricing strategies or cost management.

Clear time-based patterns also emerged, supporting commercial planning and optimization of promotional strategies.
