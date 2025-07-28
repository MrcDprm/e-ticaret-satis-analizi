"""
E-Ticaret Satış Analizi - Görselleştirme Modülü
"""

import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class FunnelVisualizer:
    """Funnel görselleştirme sınıfı"""
    
    @staticmethod
    def create_funnel_chart(funnel_stages: dict):
        """Funnel chart oluştur"""
        fig = go.Figure(go.Funnel(
            y=list(funnel_stages.keys()),
            x=list(funnel_stages.values()),
            textinfo="value+percent initial",
            textposition="inside",
            marker={"color": ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4"]},
            connector={"line": {"color": "royalblue", "width": 3}}
        ))
        
        fig.update_layout(
            title="🛒 E-Ticaret Satış Funnel'i",
            font=dict(size=14),
            showlegend=False,
            height=500
        )
        
        return fig
    
    @staticmethod
    def create_conversion_chart(conversion_rates: dict):
        """Conversion rate chart oluştur"""
        fig = px.bar(
            x=list(conversion_rates.keys()),
            y=list(conversion_rates.values()),
            title="Conversion Rate'ler",
            labels={'x': 'Aşama', 'y': 'Conversion Rate (%)'},
            color=list(conversion_rates.values()),
            color_continuous_scale='RdYlGn'
        )
        
        return fig

class RFMVisualizer:
    """RFM görselleştirme sınıfı"""
    
    @staticmethod
    def create_segment_pie(rfm_df: pd.DataFrame):
        """Segment dağılımı pie chart"""
        segment_counts = rfm_df['segment'].value_counts()
        
        fig = px.pie(
            values=segment_counts.values,
            names=segment_counts.index,
            title="Müşteri Segment Dağılımı",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        
        return fig
    
    @staticmethod
    def create_rfm_scatter(rfm_df: pd.DataFrame):
        """RFM scatter plot"""
        fig = px.scatter(
            rfm_df, 
            x='recency_days', 
            y='monetary',
            color='segment', 
            size='frequency',
            title="RFM Analizi - Müşteri Segmentasyonu",
            labels={
                'recency_days': 'Recency (Gün)',
                'monetary': 'Monetary (TL)',
                'frequency': 'Frequency'
            }
        )
        
        return fig

class TrendVisualizer:
    """Trend görselleştirme sınıfı"""
    
    @staticmethod
    def create_trend_line(daily_trend: pd.DataFrame):
        """Trend line chart"""
        fig = px.line(
            daily_trend, 
            x='date', 
            y='conversion_rate',
            title="Günlük Conversion Rate Trendi",
            labels={
                'conversion_rate': 'Conversion Rate (%)',
                'date': 'Tarih'
            }
        )
        
        return fig
    
    @staticmethod
    def create_monthly_bar(monthly_trend: pd.DataFrame):
        """Aylık bar chart"""
        fig = px.bar(
            monthly_trend, 
            x='month', 
            y='conversion_rate',
            title="Aylık Conversion Rate",
            labels={
                'conversion_rate': 'Conversion Rate (%)',
                'month': 'Ay'
            }
        )
        
        return fig
