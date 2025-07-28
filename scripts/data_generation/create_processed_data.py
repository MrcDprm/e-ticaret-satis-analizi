import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json

print("🔄 Processed veri setleri oluşturuluyor...")

# 1. Funnel analizi için işlenmiş veri
def create_processed_funnel_data():
    # Raw funnel verisini yükle
    funnel_df = pd.read_csv('data/raw/funnel_data.csv')
    funnel_df['date'] = pd.to_datetime(funnel_df['date'])
    
    # Günlük funnel özeti
    daily_funnel = funnel_df.groupby('date').agg({
        'page_view': 'sum',
        'add_to_cart': 'sum', 
        'start_checkout': 'sum',
        'complete_purchase': 'sum'
    }).reset_index()
    
    # Conversion rate'leri hesapla
    daily_funnel['cart_conversion_rate'] = (daily_funnel['add_to_cart'] / daily_funnel['page_view']) * 100
    daily_funnel['checkout_conversion_rate'] = (daily_funnel['start_checkout'] / daily_funnel['add_to_cart']) * 100
    daily_funnel['purchase_conversion_rate'] = (daily_funnel['complete_purchase'] / daily_funnel['start_checkout']) * 100
    daily_funnel['overall_conversion_rate'] = (daily_funnel['complete_purchase'] / daily_funnel['page_view']) * 100
    
    # Haftalık ve aylık özetler
    daily_funnel['week'] = daily_funnel['date'].dt.isocalendar().week
    daily_funnel['month'] = daily_funnel['date'].dt.month
    
    weekly_funnel = daily_funnel.groupby('week').agg({
        'page_view': 'sum',
        'add_to_cart': 'sum',
        'start_checkout': 'sum', 
        'complete_purchase': 'sum',
        'overall_conversion_rate': 'mean'
    }).reset_index()
    
    monthly_funnel = daily_funnel.groupby('month').agg({
        'page_view': 'sum',
        'add_to_cart': 'sum',
        'start_checkout': 'sum',
        'complete_purchase': 'sum', 
        'overall_conversion_rate': 'mean'
    }).reset_index()
    
    # Kategori bazlı funnel
    category_funnel = funnel_df.groupby('category').agg({
        'page_view': 'sum',
        'add_to_cart': 'sum',
        'start_checkout': 'sum',
        'complete_purchase': 'sum'
    }).reset_index()
    
    category_funnel['conversion_rate'] = (category_funnel['complete_purchase'] / category_funnel['page_view']) * 100
    
    # Kaydet
    daily_funnel.to_csv('data/processed/daily_funnel_summary.csv', index=False)
    weekly_funnel.to_csv('data/processed/weekly_funnel_summary.csv', index=False)
    monthly_funnel.to_csv('data/processed/monthly_funnel_summary.csv', index=False)
    category_funnel.to_csv('data/processed/category_funnel_summary.csv', index=False)
    
    print(f"✅ Funnel processed verileri oluşturuldu:")
    print(f"   - Daily summary: {len(daily_funnel)} kayıt")
    print(f"   - Weekly summary: {len(weekly_funnel)} kayıt") 
    print(f"   - Monthly summary: {len(monthly_funnel)} kayıt")
    print(f"   - Category summary: {len(category_funnel)} kayıt")

# 2. RFM analizi için işlenmiş veri
def create_processed_rfm_data():
    rfm_df = pd.read_csv('data/raw/rfm_data.csv')
    
    # RFM skorları hesapla
    rfm_df['R_score'] = pd.qcut(rfm_df['recency_days'], q=4, labels=[4, 3, 2, 1])
    rfm_df['F_score'] = pd.qcut(rfm_df['frequency'], q=4, labels=[1, 2, 3, 4])
    rfm_df['M_score'] = pd.qcut(rfm_df['monetary'], q=4, labels=[1, 2, 3, 4])
    
    # RFM skorunu birleştir
    rfm_df['RFM_score'] = rfm_df['R_score'].astype(str) + rfm_df['F_score'].astype(str) + rfm_df['M_score'].astype(str)
    
    # Segment bazlı özet
    segment_summary = rfm_df.groupby('segment').agg({
        'customer_id': 'count',
        'recency_days': 'mean',
        'frequency': 'mean', 
        'monetary': ['mean', 'sum']
    }).round(2)
    
    # Multi-level columns'ı düzelt
    segment_summary.columns = ['customer_count', 'avg_recency', 'avg_frequency', 'avg_monetary', 'total_monetary']
    segment_summary['percentage'] = (segment_summary['customer_count'] / len(rfm_df)) * 100
    
    # RFM skor bazlı özet
    rfm_score_summary = rfm_df.groupby('RFM_score').agg({
        'customer_id': 'count',
        'monetary': 'sum'
    }).reset_index()
    
    # Kaydet
    rfm_df.to_csv('data/processed/rfm_scored.csv', index=False)
    segment_summary.to_csv('data/processed/rfm_segment_summary.csv')
    rfm_score_summary.to_csv('data/processed/rfm_score_summary.csv', index=False)
    
    print(f"✅ RFM processed verileri oluşturuldu:")
    print(f"   - Scored RFM: {len(rfm_df)} kayıt")
    print(f"   - Segment summary: {len(segment_summary)} segment")
    print(f"   - Score summary: {len(rfm_score_summary)} skor")

# 3. Kullanıcı davranışı için işlenmiş veri
def create_processed_behavior_data():
    behavior_df = pd.read_csv('data/raw/user_behavior.csv')
    behavior_df['date'] = pd.to_datetime(behavior_df['date'])
    
    # Session analizi özeti
    session_summary = behavior_df.groupby('return_visitor').agg({
        'session_id': 'count',
        'session_duration': 'mean',
        'pages_viewed': 'mean',
        'bounce_rate': 'mean',
        'purchase_value': 'mean'
    }).round(2)
    
    # Günlük davranış özeti
    daily_behavior = behavior_df.groupby('date').agg({
        'session_id': 'count',
        'session_duration': 'mean',
        'pages_viewed': 'mean',
        'bounce_rate': 'mean',
        'return_visitor': 'mean',
        'purchase_value': 'sum'
    }).reset_index()
    
    # Kullanıcı segmentasyonu
    behavior_df['session_category'] = pd.cut(behavior_df['session_duration'], 
                                           bins=[0, 300, 600, 1200, float('inf')],
                                           labels=['Short', 'Medium', 'Long', 'Very Long'])
    
    session_category_summary = behavior_df.groupby('session_category').agg({
        'session_id': 'count',
        'purchase_value': 'mean',
        'return_visitor': 'mean'
    }).round(2)
    
    # Kaydet
    session_summary.to_csv('data/processed/session_summary.csv')
    daily_behavior.to_csv('data/processed/daily_behavior_summary.csv', index=False)
    session_category_summary.to_csv('data/processed/session_category_summary.csv')
    
    print(f"✅ Behavior processed verileri oluşturuldu:")
    print(f"   - Session summary: {len(session_summary)} kategori")
    print(f"   - Daily behavior: {len(daily_behavior)} gün")
    print(f"   - Session category: {len(session_category_summary)} kategori")

# 4. KPI dashboard için özet veri
def create_kpi_dashboard_data():
    # Ana KPI'ları hesapla
    funnel_df = pd.read_csv('data/raw/funnel_data.csv')
    behavior_df = pd.read_csv('data/raw/user_behavior.csv')
    rfm_df = pd.read_csv('data/raw/rfm_data.csv')
    
    # Funnel KPI'ları
    total_views = funnel_df['page_view'].sum()
    total_cart_adds = funnel_df['add_to_cart'].sum()
    total_checkouts = funnel_df['start_checkout'].sum()
    total_purchases = funnel_df['complete_purchase'].sum()
    
    overall_conversion = (total_purchases / total_views) * 100
    cart_conversion = (total_cart_adds / total_views) * 100
    checkout_conversion = (total_checkouts / total_cart_adds) * 100
    purchase_conversion = (total_purchases / total_checkouts) * 100
    
    # Behavior KPI'ları
    avg_session_duration = behavior_df['session_duration'].mean() / 60  # dakika
    avg_pages_viewed = behavior_df['pages_viewed'].mean()
    avg_bounce_rate = behavior_df['bounce_rate'].mean() * 100
    return_visitor_rate = behavior_df['return_visitor'].mean() * 100
    
    # RFM KPI'ları
    avg_order_value = rfm_df['monetary'].mean()
    customer_lifetime_value = avg_order_value * rfm_df['frequency'].mean()
    champions_percentage = (rfm_df[rfm_df['segment'] == 'Champions']['monetary'].sum() / rfm_df['monetary'].sum()) * 100
    
    # KPI dashboard verisi
    kpi_data = {
        'metric': [
            'Total Page Views', 'Total Cart Adds', 'Total Checkouts', 'Total Purchases',
            'Overall Conversion Rate', 'Cart Conversion Rate', 'Checkout Conversion Rate', 'Purchase Conversion Rate',
            'Average Session Duration', 'Average Pages Viewed', 'Average Bounce Rate', 'Return Visitor Rate',
            'Average Order Value', 'Customer Lifetime Value', 'Champions Percentage'
        ],
        'value': [
            total_views, total_cart_adds, total_checkouts, total_purchases,
            overall_conversion, cart_conversion, checkout_conversion, purchase_conversion,
            avg_session_duration, avg_pages_viewed, avg_bounce_rate, return_visitor_rate,
            avg_order_value, customer_lifetime_value, champions_percentage
        ],
        'unit': [
            'views', 'adds', 'checkouts', 'purchases',
            '%', '%', '%', '%',
            'minutes', 'pages', '%', '%',
            'TL', 'TL', '%'
        ]
    }
    
    kpi_df = pd.DataFrame(kpi_data)
    kpi_df.to_csv('data/processed/kpi_dashboard.csv', index=False)
    
    print(f"✅ KPI dashboard verisi oluşturuldu: {len(kpi_df)} metrik")

# 5. Trend analizi için işlenmiş veri
def create_trend_analysis_data():
    funnel_df = pd.read_csv('data/raw/funnel_data.csv')
    funnel_df['date'] = pd.to_datetime(funnel_df['date'])
    
    # Günlük trend
    daily_trend = funnel_df.groupby('date').agg({
        'page_view': 'sum',
        'add_to_cart': 'sum',
        'start_checkout': 'sum',
        'complete_purchase': 'sum'
    }).reset_index()
    
    daily_trend['conversion_rate'] = (daily_trend['complete_purchase'] / daily_trend['page_view']) * 100
    
    # Haftalık trend
    daily_trend['week'] = daily_trend['date'].dt.isocalendar().week
    weekly_trend = daily_trend.groupby('week').agg({
        'page_view': 'sum',
        'complete_purchase': 'sum',
        'conversion_rate': 'mean'
    }).reset_index()
    
    # Aylık trend
    daily_trend['month'] = daily_trend['date'].dt.month
    monthly_trend = daily_trend.groupby('month').agg({
        'page_view': 'sum',
        'complete_purchase': 'sum', 
        'conversion_rate': 'mean'
    }).reset_index()
    
    # Kategori trendi
    category_trend = funnel_df.groupby(['date', 'category']).agg({
        'page_view': 'sum',
        'complete_purchase': 'sum'
    }).reset_index()
    
    category_trend['conversion_rate'] = (category_trend['complete_purchase'] / category_trend['page_view']) * 100
    
    # Kaydet
    daily_trend.to_csv('data/processed/daily_trend.csv', index=False)
    weekly_trend.to_csv('data/processed/weekly_trend.csv', index=False)
    monthly_trend.to_csv('data/processed/monthly_trend.csv', index=False)
    category_trend.to_csv('data/processed/category_trend.csv', index=False)
    
    print(f"✅ Trend analizi verileri oluşturuldu:")
    print(f"   - Daily trend: {len(daily_trend)} gün")
    print(f"   - Weekly trend: {len(weekly_trend)} hafta")
    print(f"   - Monthly trend: {len(monthly_trend)} ay")
    print(f"   - Category trend: {len(category_trend)} kayıt")

# Tüm processed verileri oluştur
print("🔄 Processed veri setleri oluşturuluyor...")
print("=" * 50)

create_processed_funnel_data()
create_processed_rfm_data() 
create_processed_behavior_data()
create_kpi_dashboard_data()
create_trend_analysis_data()

print("\n✅ Tüm processed veri setleri başarıyla oluşturuldu!")
print("📊 Dashboard ve analizler için hazır!") 