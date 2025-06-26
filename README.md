# MongoDB + Trino + Superset

Simple setup to connect Superset to MongoDB using Trino.

## Start Services
```bash
docker-compose up -d
```

## Access
- **Superset**: http://localhost:8088 (admin/admin)
- **Trino**: http://localhost:8080
- **MongoDB**: localhost:27017 (admin/admin)

## Connect Superset to MongoDB
1. Login to Superset
2. Settings → Database Connections → + Database
3. Select "Other" or "Trino"
4. Connection: `trino://trino@trino:8080/mongodb`
5. Test & Save

## Add Sample Data to MongoDB
```bash
docker exec -it mongodb mongosh -u admin -p admin
use testdb
db.products.insertOne({name: "Test Product", price: 100})
```

Then query in Superset: `SELECT * FROM mongodb.testdb.products`

## Compatible Versions
- **Superset 3.0.0** ✅
- **Trino 443** ✅  
- **trino Python package** (includes SQLAlchemy support) ✅

## Performance Testing with Locust

### Install Locust
```bash
pip install locust
```

### Run Performance Tests
```bash
# Start Locust web interface
locust -f src/test/test_superset.py --host=http://localhost:8088

# Open http://localhost:8089 to configure and start tests
```

### Quick Automated Test
```bash
# Run 10 users for 2 minutes
locust -f test_superset.py --host=http://localhost:8088 --users=10 --spawn-rate=2 --run-time=2m --headless
```
