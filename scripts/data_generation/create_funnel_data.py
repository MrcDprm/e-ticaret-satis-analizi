import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Funnel analizi için veri oluştur
np.random.seed(42)
random.seed(42)

# Tarih aralığı
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)

# Funnel verisi oluştur
def create_funnel_data():
    # Ana funnel verisi
    funnel_data = {
        'date': [],
        'page_view': [],
        'add_to_cart': [],
        'start_checkout': [],
        'complete_purchase': [],
        'session_id': [],
        'user_id': [],
        'product_id': [],
        'category': [],
        'device_type': [],
        'source': []
    }
    
    # Kategoriler
    categories = ['Elektronik', 'Giyim', 'Ev & Yaşam', 'Spor', 'Kitap', 'Kozmetik']
    devices = ['Desktop', 'Mobile', 'Tablet']
    sources = ['Google', 'Direct', 'Social Media', 'Email', 'Referral']
    
    # Her gün için veri oluştur
    current_date = start_date
    session_id = 1
    
    while current_date <= end_date:
        # Günlük ziyaretçi sayısı (mevsimsel değişim)
        base_visitors = 1000
        seasonal_factor = 1 + 0.3 * np.sin(2 * np.pi * current_date.timetuple().tm_yday / 365)
        daily_visitors = int(base_visitors * seasonal_factor)
        
        for _ in range(daily_visitors):
            # Funnel aşamaları
            page_view = 1
            add_to_cart = np.random.choice([0, 1], p=[0.7, 0.3])  # %30 sepet ekleme
            start_checkout = add_to_cart * np.random.choice([0, 1], p=[0.4, 0.6])  # %60 ödeme başlatma
            complete_purchase = start_checkout * np.random.choice([0, 1], p=[0.2, 0.8])  # %80 tamamlama
            
            # Veri ekle
            funnel_data['date'].append(current_date)
            funnel_data['page_view'].append(page_view)
            funnel_data['add_to_cart'].append(add_to_cart)
            funnel_data['start_checkout'].append(start_checkout)
            funnel_data['complete_purchase'].append(complete_purchase)
            funnel_data['session_id'].append(session_id)
            funnel_data['user_id'].append(f"user_{random.randint(1000, 9999)}")
            funnel_data['product_id'].append(f"prod_{random.randint(100, 999)}")
            funnel_data['category'].append(random.choice(categories))
            funnel_data['device_type'].append(random.choice(devices))
            funnel_data['source'].append(random.choice(sources))
            
            session_id += 1
        
        current_date += timedelta(days=1)
    
    return pd.DataFrame(funnel_data)

# Kullanıcı davranış verisi
def create_user_behavior_data():
    behavior_data = {
        'session_id': [],
        'user_id': [],
        'session_duration': [],
        'pages_viewed': [],
        'bounce_rate': [],
        'return_visitor': [],
        'purchase_value': [],
        'date': []
    }
    
    # 1000 session için veri
    for i in range(1000):
        session_duration = np.random.exponential(300)  # ortalama 5 dakika
        pages_viewed = np.random.poisson(8)  # ortalama 8 sayfa
        bounce_rate = np.random.beta(2, 8)  # düşük bounce rate
        return_visitor = np.random.choice([0, 1], p=[0.7, 0.3])
        purchase_value = np.random.exponential(150) if return_visitor else 0
        
        behavior_data['session_id'].append(f"session_{i+1}")
        behavior_data['user_id'].append(f"user_{random.randint(1000, 9999)}")
        behavior_data['session_duration'].append(session_duration)
        behavior_data['pages_viewed'].append(pages_viewed)
        behavior_data['bounce_rate'].append(bounce_rate)
        behavior_data['return_visitor'].append(return_visitor)
        behavior_data['purchase_value'].append(purchase_value)
        behavior_data['date'].append(start_date + timedelta(days=random.randint(0, 365)))
    
    return pd.DataFrame(behavior_data)

# RFM analizi için veri
def create_rfm_data():
    rfm_data = {
        'customer_id': [],
        'recency_days': [],
        'frequency': [],
        'monetary': [],
        'segment': [],
        'last_purchase_date': []
    }
    
    # 500 müşteri için RFM verisi
    for i in range(500):
        recency = np.random.exponential(30)  # ortalama 30 gün
        frequency = np.random.poisson(3) + 1  # en az 1 alışveriş
        monetary = np.random.exponential(200)  # ortalama 200 TL
        
        # RFM segmentasyonu
        if recency <= 30 and frequency >= 3 and monetary >= 200:
            segment = 'Champions'
        elif recency <= 60 and frequency >= 2:
            segment = 'Loyal Customers'
        elif recency <= 90:
            segment = 'At Risk'
        else:
            segment = 'Lost'
        
        rfm_data['customer_id'].append(f"customer_{i+1}")
        rfm_data['recency_days'].append(int(recency))
        rfm_data['frequency'].append(frequency)
        rfm_data['monetary'].append(monetary)
        rfm_data['segment'].append(segment)
        rfm_data['last_purchase_date'].append(end_date - timedelta(days=int(recency)))
    
    return pd.DataFrame(rfm_data)

# Veri setlerini oluştur ve kaydet
print("Funnel analizi veri setleri oluşturuluyor...")

# Ana funnel verisi
funnel_df = create_funnel_data()
funnel_df.to_csv('data/raw/funnel_data.csv', index=False)
print(f"Funnel verisi oluşturuldu: {len(funnel_df)} kayıt")

# Kullanıcı davranış verisi
behavior_df = create_user_behavior_data()
behavior_df.to_csv('data/raw/user_behavior.csv', index=False)
print(f"Kullanıcı davranış verisi oluşturuldu: {len(behavior_df)} kayıt")

# RFM verisi
rfm_df = create_rfm_data()
rfm_df.to_csv('data/raw/rfm_data.csv', index=False)
print(f"RFM verisi oluşturuldu: {len(rfm_df)} kayıt")

print("\n✅ Tüm veri setleri başarıyla oluşturuldu!")
print("📊 Funnel analizi için hazır!") 