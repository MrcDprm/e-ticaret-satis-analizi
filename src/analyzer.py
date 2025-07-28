"""
E-Ticaret Satış Analizi - Analiz Modülü
"""

import pandas as pd
import numpy as np
from typing import Dict, Tuple

class FunnelAnalyzer:
    """Funnel analizi sınıfı"""
    
    def __init__(self, funnel_df: pd.DataFrame):
        self.funnel_df = funnel_df
        
    def calculate_funnel_stages(self) -> Dict[str, int]:
        """Funnel aşamalarını hesapla"""
        stages = {
            'Görüntüleme': self.funnel_df['page_view'].sum(),
            'Sepete Ekleme': self.funnel_df['add_to_cart'].sum(),
            'Ödeme Başlatma': self.funnel_df['start_checkout'].sum(),
            'Tamamlama': self.funnel_df['complete_purchase'].sum()
        }
        return stages
    
    def calculate_conversion_rates(self) -> Dict[str, float]:
        """Conversion rate'leri hesapla"""
        stages = self.calculate_funnel_stages()
        conversion_rates = {}
        
        previous_value = None
        for stage, value in stages.items():
            if previous_value is not None:
                rate = (value / previous_value) * 100
                conversion_rates[stage] = rate
            previous_value = value
            
        return conversion_rates
    
    def find_bottleneck(self) -> Tuple[str, float]:
        """En büyük drop-off noktasını bul"""
        conversion_rates = self.calculate_conversion_rates()
        bottleneck = min(conversion_rates, key=conversion_rates.get)
        return bottleneck, conversion_rates[bottleneck]

class RFMAnalyzer:
    """RFM analizi sınıfı"""
    
    def __init__(self, rfm_df: pd.DataFrame):
        self.rfm_df = rfm_df
        
    def calculate_rfm_scores(self) -> pd.DataFrame:
        """RFM skorlarını hesapla"""
        df = self.rfm_df.copy()
        
        # RFM skorları
        df['R_score'] = pd.qcut(df['recency_days'], q=4, labels=[4, 3, 2, 1])
        df['F_score'] = pd.qcut(df['frequency'], q=4, labels=[1, 2, 3, 4])
        df['M_score'] = pd.qcut(df['monetary'], q=4, labels=[1, 2, 3, 4])
        
        # RFM skorunu birleştir
        df['RFM_score'] = df['R_score'].astype(str) + df['F_score'].astype(str) + df['M_score'].astype(str)
        
        return df
    
    def get_segment_summary(self) -> pd.DataFrame:
        """Segment bazlı özet"""
        return self.rfm_df.groupby('segment').agg({
            'customer_id': 'count',
            'recency_days': 'mean',
            'frequency': 'mean',
            'monetary': ['mean', 'sum']
        }).round(2)

class TrendAnalyzer:
    """Trend analizi sınıfı"""
    
    def __init__(self, funnel_df: pd.DataFrame):
        self.funnel_df = funnel_df
        
    def calculate_daily_trends(self) -> pd.DataFrame:
        """Günlük trendleri hesapla"""
        daily_trend = self.funnel_df.groupby('date').agg({
            'page_view': 'sum',
            'add_to_cart': 'sum',
            'start_checkout': 'sum',
            'complete_purchase': 'sum'
        }).reset_index()
        
        daily_trend['conversion_rate'] = (daily_trend['complete_purchase'] / daily_trend['page_view']) * 100
        return daily_trend
    
    def calculate_monthly_trends(self) -> pd.DataFrame:
        """Aylık trendleri hesapla"""
        daily_trend = self.calculate_daily_trends()
        daily_trend['month'] = daily_trend['date'].dt.month
        
        monthly_trend = daily_trend.groupby('month').agg({
            'page_view': 'sum',
            'complete_purchase': 'sum',
            'conversion_rate': 'mean'
        }).reset_index()
        
        return monthly_trend
