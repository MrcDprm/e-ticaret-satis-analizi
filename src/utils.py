# -*- coding: utf-8 -*-
"""
Utility functions for e-commerce sales analysis project.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

def create_sample_data():
    """
    Create sample e-commerce sales data for analysis.
    """
    np.random.seed(42)
    
    # Generate dates for the last year
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    
    # Categories
    categories = ['Elektronik', 'Giyim', 'Ev & Yaşam', 'Spor', 'Kitap', 'Kozmetik']
    
    # Generate data
    data = []
    for _ in range(1000):
        date = np.random.choice(dates)
        category = np.random.choice(categories)
        age = np.random.randint(18, 70)
        gender = np.random.choice(['Erkek', 'Kadın'])
        
        # Generate realistic prices based on category
        if category == 'Elektronik':
            price = np.random.uniform(100, 5000)
        elif category == 'Giyim':
            price = np.random.uniform(50, 500)
        elif category == 'Ev & Yaşam':
            price = np.random.uniform(30, 300)
        elif category == 'Spor':
            price = np.random.uniform(100, 1000)
        elif category == 'Kitap':
            price = np.random.uniform(20, 200)
        else:  # Kozmetik
            price = np.random.uniform(30, 400)
        
        # Add some randomness
        price = price * np.random.uniform(0.8, 1.2)
        
        # Generate quantity (1-5 items)
        quantity = np.random.randint(1, 6)
        total_amount = price * quantity
        
        data.append({
            'date': date,
            'category': category,
            'product_name': f'{category} Ürünü {np.random.randint(1, 100)}',
            'price': round(price, 2),
            'quantity': quantity,
            'total_amount': round(total_amount, 2),
            'customer_age': age,
            'customer_gender': gender,
            'payment_method': np.random.choice(['Kredi Kartı', 'Banka Kartı', 'Havale']),
            'region': np.random.choice(['İstanbul', 'Ankara', 'İzmir', 'Bursa', 'Antalya'])
        })
    
    return pd.DataFrame(data)

def get_project_info():
    """
    Get project information and metadata.
    """
    return {
        'name': 'E-Ticaret Satış Analizi',
        'version': '1.0.0',
        'description': 'Kapsamlı e-ticaret analizi projesi',
        'author': 'Data Analyst',
        'created_date': '2024-01-01',
        'last_updated': datetime.now().strftime('%Y-%m-%d'),
        'technologies': ['Python', 'Pandas', 'NumPy', 'Matplotlib', 'Seaborn', 'Plotly'],
        'analysis_types': ['Funnel Analysis', 'RFM Analysis', 'Trend Analysis', 'Customer Segmentation'],
        'data_sources': ['ecommerce_sales.csv', 'funnel_data.csv', 'user_behavior.csv', 'rfm_data.csv'],
        'notebooks': [
            '01_basit_analiz.ipynb',
            '02_detayli_analiz.ipynb', 
            '03_sonuclar.ipynb',
            '04_sonuclar_uyari_giderilmis.ipynb',
            '05_funnel_analizi.ipynb'
        ]
    }

def calculate_basic_stats(df):
    """
    Calculate basic statistics for the dataset.
    """
    stats = {
        'total_records': len(df),
        'total_sales': df['total_amount'].sum(),
        'average_order_value': df['total_amount'].mean(),
        'unique_customers': df['customer_age'].nunique(),  # Using age as proxy for customer
        'date_range': f"{df['date'].min().strftime('%Y-%m-%d')} to {df['date'].max().strftime('%Y-%m-%d')}",
        'categories': df['category'].nunique(),
        'top_category': df['category'].value_counts().index[0],
        'top_category_sales': df.groupby('category')['total_amount'].sum().max()
    }
    return stats

def create_age_groups(df):
    """
    Create age groups for analysis.
    """
    df['yas_grubu'] = pd.cut(df['customer_age'], 
                             bins=[0, 25, 35, 45, 55, 100],
                             labels=['18-25', '26-35', '36-45', '46-55', '55+'])
    return df

def format_currency(amount):
    """
    Format amount as Turkish Lira.
    """
    return f"₺{amount:,.2f}"

def format_percentage(value):
    """
    Format value as percentage.
    """
    return f"%{value:.1f}"

def get_color_palette():
    """
    Get consistent color palette for visualizations.
    """
    return ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

def save_plot(fig, filename, dpi=300):
    """
    Save plot with consistent settings.
    """
    fig.savefig(filename, dpi=dpi, bbox_inches='tight', facecolor='white')
    print(f"Plot saved as {filename}")

def print_separator(title=""):
    """
    Print a formatted separator with optional title.
    """
    if title:
        print(f"\n{'='*50}")
        print(f" {title}")
        print(f"{'='*50}")
    else:
        print(f"\n{'='*50}")

def validate_data(df):
    """
    Validate data quality and completeness.
    """
    issues = []
    
    # Check for missing values
    missing_values = df.isnull().sum()
    if missing_values.sum() > 0:
        issues.append(f"Missing values found: {missing_values[missing_values > 0].to_dict()}")
    
    # Check for negative values in numeric columns
    numeric_cols = ['price', 'quantity', 'total_amount']
    for col in numeric_cols:
        if col in df.columns and (df[col] < 0).any():
            issues.append(f"Negative values found in {col}")
    
    # Check date range
    if 'date' in df.columns:
        date_range = df['date'].max() - df['date'].min()
        if date_range.days < 30:
            issues.append("Data covers less than 30 days")
    
    return issues

def get_analysis_summary():
    """
    Get a summary of all analyses performed.
    """
    return {
        'funnel_analysis': {
            'status': 'completed',
            'stages': ['Görüntüleme', 'Sepete Ekleme', 'Ödeme', 'Tamamlama'],
            'drop_off_points': 'identified',
            'conversion_rates': 'calculated'
        },
        'rfm_analysis': {
            'status': 'completed',
            'segments': ['Champions', 'Loyal Customers', 'At Risk', 'Lost'],
            'customer_count': 500,
            'scoring_method': 'RFM'
        },
        'trend_analysis': {
            'status': 'completed',
            'time_periods': ['daily', 'weekly', 'monthly'],
            'seasonal_patterns': 'identified',
            'forecasting': 'implemented'
        },
        'customer_segmentation': {
            'status': 'completed',
            'segmentation_method': 'RFM + Demographics',
            'segments_count': 4,
            'insights': 'generated'
        }
    }
