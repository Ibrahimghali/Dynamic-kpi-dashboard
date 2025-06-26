import os
import pymongo
from datetime import datetime, timedelta
import random

def populate_mongodb():
    """Generate simple data for MongoDB"""
    
    # Connect to MongoDB
    connection_string = os.getenv('MONGODB_URI', 'mongodb://admin:admin@mongodb:27017')
    client = pymongo.MongoClient(connection_string)
    db = client['financial_data']
    
    print("� Generating sample data...")
    
    # Simple data
    symbols = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']
    companies = ['Apple Inc.', 'Google Inc.', 'Microsoft Corp.', 'Amazon Inc.', 'Tesla Inc.']
    sectors = ['Technology', 'Technology', 'Technology', 'E-commerce', 'Automotive']
    
    all_stock_data = []
    
    for i, symbol in enumerate(symbols):
        print(f"  Creating data for {symbol}...")
        
        # Generate 30 days of data
        for day in range(30):
            date = datetime.now() - timedelta(days=day)
            price = 100 + random.randint(-20, 20)
            
            record = {
                'symbol': symbol,
                'company_name': companies[i],
                'sector': sectors[i],
                'date': date,
                'open': price + random.randint(-5, 5),
                'high': price + random.randint(0, 10),
                'low': price - random.randint(0, 10),
                'close': price,
                'volume': random.randint(1000000, 50000000),
                'year': date.year,
                'month': date.month,
                'day': date.day
            }
            all_stock_data.append(record)
    
    # Insert data
    db.stock_prices.delete_many({})
    db.stock_prices.insert_many(all_stock_data)
    print(f"✅ Inserted {len(all_stock_data)} records")
    
    client.close()
    print("🎯 Ready for Superset!")

if __name__ == "__main__":
    populate_mongodb()
