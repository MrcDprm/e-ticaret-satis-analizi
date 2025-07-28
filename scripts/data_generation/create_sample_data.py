import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Rastgele sayı üretimi için seed
np.random.seed(42)

# Tarih aralığı oluştur
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
dates = pd.date_range(start_date, end_date, freq='D')

# Ürün kategorileri ve fiyatları
categories = {
    'Elektronik': {
        'products': ['iPhone 14 Pro', 'MacBook Air', 'Samsung Galaxy', 'iPad Pro', 'AirPods Pro', 'Apple Watch', 'Sony TV', 'Canon Kamera'],
        'price_range': (500, 50000)
    },
    'Giyim': {
        'products': ['Kot Pantolon', 'T-Shirt', 'Elbise', 'Ceket', 'Spor Ayakkabı', 'Çanta', 'Şapka', 'Kemer'],
        'price_range': (50, 2000)
    },
    'Ev & Yaşam': {
        'products': ['Çamaşır Makinesi', 'Robot Süpürge', 'Kahve Makinesi', 'Mikser', 'Tencere Seti', 'Yastık', 'Havlu', 'Çarşaf'],
        'price_range': (100, 10000)
    },
    'Spor': {
        'products': ['Nike Spor Ayakkabı', 'Yoga Matı', 'Dumbbell Set', 'Bisiklet', 'Koşu Bandı', 'Pilates Topu', 'Spor Çantası', 'Su Şişesi'],
        'price_range': (50, 5000)
    },
    'Kitap': {
        'products': ['Python Programlama', 'Roman', 'Bilim Kurgu', 'Tarih Kitabı', 'Felsefe', 'Psikoloji', 'Bilim', 'Çocuk Kitabı'],
        'price_range': (20, 500)
    }
}

# Şehirler
cities = ['İstanbul', 'Ankara', 'İzmir', 'Bursa', 'Antalya', 'Adana', 'Konya', 'Gaziantep']

# Ödeme yöntemleri
payment_methods = ['Kredi Kartı', 'Havale', 'Kapıda Ödeme']

# Veri oluştur
data = []
order_id = 1

for _ in range(1000):  # 1000 satış kaydı
    # Rastgele kategori seç
    category = np.random.choice(list(categories.keys()))
    category_info = categories[category]
    
    # Rastgele ürün seç
    product_name = np.random.choice(category_info['products'])
    
    # Fiyat aralığından rastgele fiyat
    min_price, max_price = category_info['price_range']
    unit_price = np.random.uniform(min_price, max_price)
    
    # Miktar (1-5 arası)
    quantity = np.random.randint(1, 6)
    
    # Toplam tutar
    total_amount = unit_price * quantity
    
    # Diğer bilgiler
    customer_id = np.random.randint(100, 1000)
    product_id = np.random.randint(1, 100)
    order_date = np.random.choice(dates)
    payment_method = np.random.choice(payment_methods)
    customer_city = np.random.choice(cities)
    customer_age = np.random.randint(18, 70)
    customer_gender = np.random.choice(['Erkek', 'Kadın'])
    is_returned = np.random.choice([0, 1], p=[0.9, 0.1])  # %10 iade oranı
    rating = np.random.randint(1, 6)
    
    data.append({
        'order_id': order_id,
        'customer_id': customer_id,
        'product_id': product_id,
        'product_name': product_name,
        'category': category,
        'order_date': order_date,
        'quantity': quantity,
        'unit_price': round(unit_price, 2),
        'total_amount': round(total_amount, 2),
        'payment_method': payment_method,
        'customer_city': customer_city,
        'customer_age': customer_age,
        'customer_gender': customer_gender,
        'is_returned': is_returned,
        'rating': rating
    })
    
    order_id += 1

# DataFrame oluştur
df = pd.DataFrame(data)

# CSV olarak kaydet
df.to_csv('data/raw/ecommerce_sales.csv', index=False)

print(f"1000 satış kaydı oluşturuldu ve kaydedildi!")
print(f"Veri seti boyutu: {df.shape}")
print(f"Kategoriler: {df['category'].unique()}")
print(f"Şehirler: {df['customer_city'].unique()}")
print(f"Toplam satış: {df['total_amount'].sum():,.2f} TL") 