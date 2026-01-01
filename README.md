# ✈️ Flight Operations Data Pipeline using Apache Airflow & Snowflake

## Description
This project is an end-to-end **data pipeline** for processing **live flight operations data** from an external API.  
It uses **Apache Airflow** to orchestrate workflows and **Snowflake** as the data warehouse.  
The pipeline follows the **Medallion Architecture** with **Bronze, Silver, and Gold layers** to ensure scalable, reliable, and analytics-ready data processing.  
Data flows from raw ingestion to cleaning and transformation, and finally to aggregation for reporting and dashboards.

---

## 🏗️ Architecture (Medallion Pattern)

### 🟤 Bronze Layer – Raw Ingestion
- Fetches **live flight operations data** from a REST API
- Stores **raw JSON data** without transformation
- Enables reprocessing and auditability

### ⚪ Silver Layer – Clean & Transform
- Parses raw JSON data
- Cleans, validates, and structures the data
- Stores cleaned data in the **Snowflake Silver layer**

### 🟡 Gold Layer – Aggregated & Analytics Ready
- Aggregates and summarizes data (flight status, delays, airline metrics)
- Creates analytics-ready tables optimized for reporting
- Enables BI dashboards and KPIs

