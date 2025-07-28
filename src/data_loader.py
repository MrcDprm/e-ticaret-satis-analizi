"""
E-Ticaret Satış Analizi - Veri Yükleme Modülü
"""

import pandas as pd
import numpy as np
from pathlib import Path

def load_raw_data():
    """Ham veri setlerini yükle"""
    data_path = Path("data/raw")
    
    # Funnel verisi
    funnel_df = pd.read_csv(data_path / "funnel_data.csv")
    funnel_df['date'] = pd.to_datetime(funnel_df['date'])
    
    # Kullanıcı davranışı
    behavior_df = pd.read_csv(data_path / "user_behavior.csv")
    behavior_df['date'] = pd.to_datetime(behavior_df['date'])
    
    # RFM verisi
    rfm_df = pd.read_csv(data_path / "rfm_data.csv")
    
    # E-ticaret satış verisi
    sales_df = pd.read_csv(data_path / "ecommerce_sales.csv")
    
    return {
        'funnel': funnel_df,
        'behavior': behavior_df,
        'rfm': rfm_df,
        'sales': sales_df
    }

def load_processed_data():
    """İşlenmiş veri setlerini yükle"""
    data_path = Path("data/processed")
    
    processed_data = {}
    
    # Processed dosyaları yükle
    for file in data_path.glob("*.csv"):
        name = file.stem
        processed_data[name] = pd.read_csv(file)
    
    return processed_data

def get_data_info():
    """Veri setleri hakkında bilgi"""
    raw_data = load_raw_data()
    
    info = {}
    for name, df in raw_data.items():
        info[name] = {
            'rows': len(df),
            'columns': len(df.columns),
            'memory_usage': df.memory_usage(deep=True).sum() / 1024 / 1024  # MB
        }
    
    return info
