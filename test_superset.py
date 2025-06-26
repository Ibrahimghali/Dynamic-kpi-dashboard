"""
Script Locust simple pour tester Superset SQL Lab
"""

from locust import HttpUser, task, between
import random


class SupersetUser(HttpUser):
    wait_time = between(1, 3)
    
    def on_start(self):
        """Se connecter à Superset au démarrage"""
        self.login()
    
    def login(self):
        """Connexion simple à Superset"""
        # Aller à la page de login
        self.client.get("/login/")
        
        # Se connecter
        response = self.client.post("/login/", data={
            "username": "admin",
            "password": "admin"
        })
        
        if response.status_code == 200:
            print("✅ Connecté")
    
    @task(3)
    def visit_sql_lab(self):
        """Visiter SQL Lab"""
        self.client.get("/superset/sqllab/", name="SQL Lab")
    
    @task(2)
    def visit_dashboards(self):
        """Visiter les tableaux de bord"""
        self.client.get("/dashboard/list/", name="Dashboards")
    
    @task(1)
    def execute_simple_query(self):
        """Exécuter une requête SQL simple"""
        queries = [
            "SELECT 1",
            "SELECT COUNT(*) FROM mongodb.financial_data.stock_prices",
            "SELECT * FROM mongodb.financial_data.companies LIMIT 5"
        ]
        
        query = random.choice(queries)
        
        # Exécuter la requête
        self.client.post("/superset/sql_json/", json={
            "database_id": 1,
            "sql": query,
            "queryLimit": 100
        }, name="Execute SQL Query")
