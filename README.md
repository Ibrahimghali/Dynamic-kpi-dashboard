# Dynamic & Scalable Dashboarding

This project provides a simple and scalable architecture to **connect Apache Superset to MongoDB via Trino**, enabling **dynamic dashboards** based on data-driven KPI definitions.

---

## 🎯 Goal

Allow teams to **visualize KPIs without writing Angular code** or deploying frontend components for each new metric.

---

## ❗ Problem

In the current setup, each KPI requires **manual creation of frontend code (Angular components)**, which:

- Takes **~1 day per KPI**
- Is **not scalable** as the number of metrics grows
- Adds **maintenance overhead**
- Makes **non-technical users dependent** on developers

---

## ✅ Solution

A dynamic dashboard system where:

- KPI metadata is stored in **MongoDB**
- Data is queried using **Trino**
- Dashboards are visualized via **Superset**

This avoids writing frontend code for each KPI and supports quick configuration updates.

---

## ⚙️ Architecture Overview

![Architecture Diagram](assets/architecture.png)

The architecture follows a simple data flow:

1. **MongoDB** stores both KPI definitions and actual data
2. **Trino** acts as a query engine, connecting to MongoDB
3. **Superset** provides the dashboard interface, querying data via Trino
4. **KPI Definitions** (JSON/MongoDB) will define dashboard layouts (future enhancement)

---

## 🧾 Sample KPI Definition (Stored in MongoDB)

We can define KPIs as documents in a `kpis` collection like this:

```json
{
  "kpi_id": "total_sales",
  "title": "Total Sales",
  "type": "metric",  // can be 'metric', 'table', 'bar_chart', etc.
  "query": "SELECT SUM(price) AS total FROM mongodb.testdb.sales",
  "visualization": {
    "format": "currency",
    "refresh_rate": "10min"
  },
  "roles_allowed": ["admin", "manager"]
}
```

Superset doesn't natively load visualizations from config files, but this architecture prepares the ground to:

* Either **auto-generate SQL Lab dashboards** based on configs
* Or use **Superset’s REST API** to automate dashboard creation from configs

---

## 🚀 Quick Start

```bash
docker-compose up -d
```

---

## 🔗 Access Services

* Superset: [http://localhost:8088](http://localhost:8088) (`admin` / `admin`)
* Trino UI: [http://localhost:8080](http://localhost:8080)
* MongoDB: `localhost:27017` (`admin` / `admin`)

---

## 🔌 Connect Superset to MongoDB via Trino

```text
trino://trino@trino:8080/mongodb
```

Create a connection in Superset using the above URL.

---

## 📦 Add Sample Data

```bash
docker exec -it mongodb mongosh -u admin -p admin
use testdb
db.sales.insertMany([
  { item: "Product A", price: 150 },
  { item: "Product B", price: 200 }
])
```

Query in Superset:

```sql
SELECT * FROM mongodb.testdb.sales
```

---

## 🧪 Load Testing with Locust

```bash
pip install locust

# Launch web UI
locust -f src/test/test_superset.py --host=http://localhost:8088
# Headless run
locust -f test_superset.py --host=http://localhost:8088 --users=10 --spawn-rate=2 --run-time=2m --headless
```

---

## ✅ Verified Versions

* Superset: `3.0.0`
* Trino: `443`
* Python `trino` package (w/ SQLAlchemy support)

---

## 🔮 Future Improvements

* Create a **KPI definition admin panel** to manage `kpis` collection
* Use Superset REST API to generate dashboards dynamically
* Implement **user-role-based filtering** and isolation
* Add support for **custom visualizations** based on config

---

