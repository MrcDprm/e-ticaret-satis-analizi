import json
import os

def create_funnel_notebook():
    """
    Create the comprehensive funnel analysis notebook.
    """
    
    # Notebook structure
    notebook = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "# 🛒 E-Ticaret Funnel Analizi & Business Intelligence\n",
                    "\n",
                    "Bu notebook, e-ticaret platformlarındaki satış sürecini kapsamlı bir şekilde analiz eder.\n",
                    "\n",
                    "## 📊 Analiz Kapsamı:\n",
                    "- **Funnel Analizi:** Satış sürecindeki darboğazları tespit etme\n",
                    "- **RFM Analizi:** Müşteri segmentasyonu ve değer analizi\n",
                    "- **Trend Analizi:** Zaman serisi analizi ve gelecek tahminleri\n",
                    "- **Business Intelligence:** KPI dashboard ve stratejik öneriler\n",
                    "\n",
                    "---"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Gerekli kütüphaneleri import et\n",
                    "import pandas as pd\n",
                    "import numpy as np\n",
                    "import matplotlib.pyplot as plt\n",
                    "import seaborn as sns\n",
                    "import plotly.express as px\n",
                    "import plotly.graph_objects as go\n",
                    "from plotly.subplots import make_subplots\n",
                    "import warnings\n",
                    "warnings.filterwarnings('ignore')\n",
                    "\n",
                    "# Türkçe karakter desteği\n",
                    "plt.rcParams['font.family'] = 'DejaVu Sans'\n",
                    "sns.set_style('whitegrid')\n",
                    "\n",
                    "print(\"✅ Kütüphaneler başarıyla yüklendi!\")"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Veri setlerini yükle\n",
                    "try:\n",
                    "    # Ana satış verisi\n",
                    "    df = pd.read_csv('data/raw/ecommerce_sales.csv')\n",
                    "    df['date'] = pd.to_datetime(df['date'])\n",
                    "    \n",
                    "    # Funnel verisi\n",
                    "    funnel_df = pd.read_csv('data/raw/funnel_data.csv')\n",
                    "    \n",
                    "    # RFM verisi\n",
                    "    rfm_df = pd.read_csv('data/raw/rfm_data.csv')\n",
                    "    \n",
                    "    print(\"✅ Tüm veri setleri başarıyla yüklendi!\")\n",
                    "    print(f\"📊 Ana veri seti: {len(df):,} kayıt\")\n",
                    "    print(f\"📊 Funnel verisi: {len(funnel_df):,} kayıt\")\n",
                    "    print(f\"📊 RFM verisi: {len(rfm_df):,} kayıt\")\n",
                    "    \n",
                    "except FileNotFoundError as e:\n",
                    "    print(f\"❌ Veri dosyası bulunamadı: {e}\")\n",
                    "    print(\"📁 Lütfen 'data/raw/' klasöründeki dosyaları kontrol edin.\")"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 🎯 1. Funnel Analizi\n",
                    "\n",
                    "Satış sürecindeki her aşamayı analiz ederek darboğazları tespit ediyoruz."
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Funnel analizi\n",
                    "funnel_stages = ['page_view', 'add_to_cart', 'start_checkout', 'complete_purchase']\n",
                    "funnel_labels = ['Görüntüleme', 'Sepete Ekleme', 'Ödeme Başlatma', 'Tamamlama']\n",
                    "\n",
                    "# Her aşamadaki toplam sayıları hesapla\n",
                    "funnel_values = []\n",
                    "for stage in funnel_stages:\n",
                    "    total = funnel_df[stage].sum()\n",
                    "    funnel_values.append(total)\n",
                    "\n",
                    "# Conversion rate'leri hesapla\n",
                    "conversion_rates = []\n",
                    "for i in range(1, len(funnel_values)):\n",
                    "    rate = (funnel_values[i] / funnel_values[i-1]) * 100\n",
                    "    conversion_rates.append(rate)\n",
                    "\n",
                    "# Drop-off sayıları\n",
                    "drop_offs = []\n",
                    "for i in range(1, len(funnel_values)):\n",
                    "    drop_off = funnel_values[i-1] - funnel_values[i]\n",
                    "    drop_offs.append(drop_off)\n",
                    "\n",
                    "print(\"📊 Funnel Analizi Sonuçları:\")\n",
                    "print(\"=\" * 50)\n",
                    "for i, (stage, value) in enumerate(zip(funnel_labels, funnel_values)):\n",
                    "    print(f\"{stage}: {value:,}\")\n",
                    "    if i < len(conversion_rates):\n",
                    "        print(f\"  → Conversion Rate: %{conversion_rates[i]:.1f}\")\n",
                    "        print(f\"  → Drop-off: {drop_offs[i]:,}\")\n",
                    "    print()"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Funnel grafiği\n",
                    "fig = go.Figure(go.Funnel(\n",
                    "    y=funnel_labels,\n",
                    "    x=funnel_values,\n",
                    "    textinfo=\"value+percent initial\",\n",
                    "    textposition=\"inside\",\n",
                    "    marker={\"color\": [\"#1f77b4\", \"#ff7f0e\", \"#2ca02c\", \"#d62728\"]},\n",
                    "    connector={\"line\": {\"color\": \"royalblue\", \"width\": 3}}\n",
                    "))\n",
                    "\n",
                    "fig.update_layout(\n",
                    "    title=\"🛒 E-Ticaret Satış Funnel'i\",\n",
                    "    font=dict(size=14),\n",
                    "    showlegend=False,\n",
                    "    height=500\n",
                    ")\n",
                    "\n",
                    "fig.show()\n",
                    "\n",
                    "# En kritik drop-off noktasını belirle\n",
                    "max_drop_off_idx = np.argmax(drop_offs)\n",
                    "critical_stage = funnel_labels[max_drop_off_idx]\n",
                    "critical_rate = conversion_rates[max_drop_off_idx]\n",
                    "\n",
                    "print(f\"\\n🎯 En Kritik Drop-off Noktası: {critical_stage}\")\n",
                    "print(f\"📉 Conversion Rate: %{critical_rate:.1f}\")\n",
                    "print(f\"💡 Bu aşamada optimizasyon yapılması gerekiyor!\")"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 👥 2. RFM Analizi\n",
                    "\n",
                    "Müşterileri Recency, Frequency, Monetary kriterlerine göre segmentlere ayırıyoruz."
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# RFM analizi\n",
                    "print(\"📊 RFM Analizi Sonuçları:\")\n",
                    "print(\"=\" * 50)\n",
                    "\n",
                    "# Segment dağılımı\n",
                    "segment_counts = rfm_df['segment'].value_counts()\n",
                    "print(\"\\n👥 Müşteri Segmentleri:\")\n",
                    "for segment, count in segment_counts.items():\n",
                    "    percentage = (count / len(rfm_df)) * 100\n",
                    "    print(f\"{segment}: {count} müşteri (%{percentage:.1f})\")\n",
                    "\n",
                    "# Segment bazlı ortalama değerler\n",
                    "segment_stats = rfm_df.groupby('segment').agg({\n",
                    "    'recency_days': 'mean',\n",
                    "    'frequency': 'mean',\n",
                    "    'monetary': 'mean'\n",
                    "}).round(2)\n",
                    "\n",
                    "print(\"\\n📈 Segment İstatistikleri:\")\n",
                    "print(segment_stats)\n",
                    "\n",
                    "# Champions segmentinin değer katkısı\n",
                    "champions_value = rfm_df[rfm_df['segment'] == 'Champions']['monetary'].sum()\n",
                    "total_value = rfm_df['monetary'].sum()\n",
                    "champions_percentage = (champions_value / total_value) * 100\n",
                    "\n",
                    "print(f\"\\n🏆 Champions Segmenti Değer Katkısı: %{champions_percentage:.1f}\")"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# RFM Scatter Plot\n",
                    "fig = px.scatter(\n",
                    "    rfm_df, \n",
                    "    x='recency_days', \n",
                    "    y='monetary',\n",
                    "    color='segment',\n",
                    "    size='frequency',\n",
                    "    hover_data=['customer_id'],\n",
                    "    title=\"👥 RFM Müşteri Segmentasyonu\",\n",
                    "    labels={\n",
                    "        'recency_days': 'Son Alışveriş (Gün)',\n",
                    "        'monetary': 'Toplam Harcama (TL)',\n",
                    "        'frequency': 'Alışveriş Sıklığı',\n",
                    "        'segment': 'Segment'\n",
                    "    }\n",
                    ")\n",
                    "\n",
                    "fig.update_layout(\n",
                    "    font=dict(size=12),\n",
                    "    height=600\n",
                    ")\n",
                    "\n",
                    "fig.show()"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 📈 3. Trend Analizi\n",
                    "\n",
                    "Zaman serisi analizi ile satış trendlerini ve mevsimsel değişimleri inceliyoruz."
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Zaman serisi analizi\n",
                    "df['date'] = pd.to_datetime(df['date'])\n",
                    "df['month'] = df['date'].dt.month\n",
                    "df['day_of_week'] = df['date'].dt.dayofweek\n",
                    "\n",
                    "# Günlük satış trendi\n",
                    "daily_sales = df.groupby('date')['total_amount'].sum().reset_index()\n",
                    "\n",
                    "# Haftalık satış trendi\n",
                    "df['week'] = df['date'].dt.isocalendar().week\n",
                    "weekly_sales = df.groupby(['date.dt.year', 'week'])['total_amount'].sum().reset_index()\n",
                    "weekly_sales['year_week'] = weekly_sales['date.dt.year'].astype(str) + '-W' + weekly_sales['week'].astype(str)\n",
                    "\n",
                    "# Aylık satış trendi\n",
                    "monthly_sales = df.groupby(df['date'].dt.to_period('M'))['total_amount'].sum().reset_index()\n",
                    "monthly_sales['month_str'] = monthly_sales['date'].astype(str)\n",
                    "\n",
                    "print(\"📊 Trend Analizi Sonuçları:\")\n",
                    "print(\"=\" * 50)\n",
                    "print(f\"📅 Analiz edilen dönem: {df['date'].min().strftime('%Y-%m-%d')} - {df['date'].max().strftime('%Y-%m-%d')}\")\n",
                    "print(f\"📈 Toplam satış: ₺{daily_sales['total_amount'].sum():,.2f}\")\n",
                    "print(f\"📊 Ortalama günlük satış: ₺{daily_sales['total_amount'].mean():,.2f}\")\n",
                    "print(f\"🎯 En yüksek günlük satış: ₺{daily_sales['total_amount'].max():,.2f}\")"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Trend grafikleri\n",
                    "fig = make_subplots(\n",
                    "    rows=2, cols=2,\n",
                    "    subplot_titles=('Günlük Satış Trendi', 'Haftalık Satış Trendi', \n",
                    "                    'Aylık Satış Trendi', 'Kategori Bazlı Satış'),\n",
                    "    specs=[[{\"secondary_y\": False}, {\"secondary_y\": False}],\n",
                    "           [{\"secondary_y\": False}, {\"secondary_y\": False}]]\n",
                    ")\n",
                    "\n",
                    "# Günlük trend\n",
                    "fig.add_trace(\n",
                    "    go.Scatter(x=daily_sales['date'], y=daily_sales['total_amount'], \n",
                    "               mode='lines', name='Günlük Satış', line=dict(color='#1f77b4')),\n",
                    "    row=1, col=1\n",
                    ")\n",
                    "\n",
                    "# Haftalık trend\n",
                    "fig.add_trace(\n",
                    "    go.Scatter(x=weekly_sales['year_week'], y=weekly_sales['total_amount'], \n",
                    "               mode='lines', name='Haftalık Satış', line=dict(color='#ff7f0e')),\n",
                    "    row=1, col=2\n",
                    ")\n",
                    "\n",
                    "# Aylık trend\n",
                    "fig.add_trace(\n",
                    "    go.Scatter(x=monthly_sales['month_str'], y=monthly_sales['total_amount'], \n",
                    "               mode='lines+markers', name='Aylık Satış', line=dict(color='#2ca02c')),\n",
                    "    row=2, col=1\n",
                    ")\n",
                    "\n",
                    "# Kategori bazlı satış\n",
                    "category_sales = df.groupby('category')['total_amount'].sum().sort_values(ascending=True)\n",
                    "fig.add_trace(\n",
                    "    go.Bar(x=category_sales.values, y=category_sales.index, \n",
                    "           orientation='h', name='Kategori Satışları', marker_color='#d62728'),\n",
                    "    row=2, col=2\n",
                    ")\n",
                    "\n",
                    "fig.update_layout(\n",
                    "    title=\"📈 Kapsamlı Trend Analizi\",\n",
                    "    height=800,\n",
                    "    showlegend=False\n",
                    ")\n",
                    "\n",
                    "fig.show()"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 🎯 4. Business Intelligence Dashboard\n",
                    "\n",
                    "Ana performans göstergelerini ve stratejik önerileri sunuyoruz."
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# KPI hesaplamaları\n",
                    "print(\"📊 Business Intelligence Dashboard\")\n",
                    "print(\"=\" * 50)\n",
                    "\n",
                    "# Funnel KPI'ları\n",
                    "overall_conversion = (funnel_values[-1] / funnel_values[0]) * 100\n",
                    "cart_conversion = (funnel_values[1] / funnel_values[0]) * 100\n",
                    "checkout_conversion = (funnel_values[2] / funnel_values[1]) * 100\n",
                    "purchase_conversion = (funnel_values[3] / funnel_values[2]) * 100\n",
                    "\n",
                    "# RFM KPI'ları\n",
                    "avg_order_value = rfm_df['monetary'].mean()\n",
                    "customer_lifetime_value = avg_order_value * rfm_df['frequency'].mean()\n",
                    "champions_percentage = (rfm_df[rfm_df['segment'] == 'Champions']['monetary'].sum() / rfm_df['monetary'].sum()) * 100\n",
                    "\n",
                    "# Trend KPI'ları\n",
                    "total_sales = daily_sales['total_amount'].sum()\n",
                    "avg_daily_sales = daily_sales['total_amount'].mean()\n",
                    "sales_growth = ((daily_sales['total_amount'].iloc[-30:].mean() - daily_sales['total_amount'].iloc[:30].mean()) / daily_sales['total_amount'].iloc[:30].mean()) * 100\n",
                    "\n",
                    "print(f\"\\n🛒 Funnel KPI'ları:\")\n",
                    "print(f\"  • Genel Conversion Rate: %{overall_conversion:.1f}\")\n",
                    "print(f\"  • Sepete Ekleme Oranı: %{cart_conversion:.1f}\")\n",
                    "print(f\"  • Ödeme Başlatma Oranı: %{checkout_conversion:.1f}\")\n",
                    "print(f\"  • Satın Alma Oranı: %{purchase_conversion:.1f}\")\n",
                    "\n",
                    "print(f\"\\n👥 Müşteri KPI'ları:\")\n",
                    "print(f\"  • Ortalama Sipariş Değeri: ₺{avg_order_value:,.2f}\")\n",
                    "print(f\"  • Müşteri Yaşam Boyu Değeri: ₺{customer_lifetime_value:,.2f}\")\n",
                    "print(f\"  • Champions Segmenti Oranı: %{champions_percentage:.1f}\")\n",
                    "\n",
                    "print(f\"\\n📈 Satış KPI'ları:\")\n",
                    "print(f\"  • Toplam Satış: ₺{total_sales:,.2f}\")\n",
                    "print(f\"  • Ortalama Günlük Satış: ₺{avg_daily_sales:,.2f}\")\n",
                    "print(f\"  • Satış Büyüme Oranı: %{sales_growth:.1f}\")"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Stratejik öneriler\n",
                    "print(\"\\n🎯 Stratejik Öneriler:\")\n",
                    "print(\"=\" * 50)\n",
                    "\n",
                    "# Funnel önerileri\n",
                    "if purchase_conversion < 70:\n",
                    "    print(\"🛒 Funnel Optimizasyonu:\")\n",
                    "    print(\"  • Checkout sürecini basitleştirin\")\n",
                    "    print(\"  • Ödeme seçeneklerini artırın\")\n",
                    "    print(\"  • Güvenlik göstergelerini belirginleştirin\")\n",
                    "\n",
                    "if cart_conversion < 30:\n",
                    "    print(\"\\n🛍️ Sepete Ekleme Optimizasyonu:\")\n",
                    "    print(\"  • Ürün sayfalarını iyileştirin\")\n",
                    "    print(\"  • Fiyatlandırma stratejisini gözden geçirin\")\n",
                    "    print(\"  • Sosyal kanıtları artırın\")\n",
                    "\n",
                    "# RFM önerileri\n",
                    "if champions_percentage < 20:\n",
                    "    print(\"\\n👑 VIP Müşteri Stratejisi:\")\n",
                    "    print(\"  • Champions segmentine özel kampanyalar\")\n",
                    "    print(\"  • VIP hizmetler ve öncelikli destek\")\n",
                    "    print(\"  • Özel indirimler ve erken erişim\")\n",
                    "\n",
                    "# Trend önerileri\n",
                    "if sales_growth < 10:\n",
                    "    print(\"\\n📈 Büyüme Stratejisi:\")\n",
                    "    print(\"  • Yeni ürün kategorileri ekleyin\")\n",
                    "    print(\"  • Pazarlama kampanyalarını artırın\")\n",
                    "    print(\"  • Müşteri deneyimini iyileştirin\")\n",
                    "\n",
                    "print(\"\\n✅ Bu analiz kapsamlı bir e-ticaret funnel analizi sunuyor!\")"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 📊 5. Sonuç ve Özet\n",
                    "\n",
                    "Bu analiz, e-ticaret platformlarındaki satış sürecini kapsamlı bir şekilde inceledi ve önemli içgörüler sağladı.\n",
                    "\n",
                    "### 🎯 Ana Bulgular:\n",
                    "1. **Funnel Analizi:** En kritik drop-off noktası tespit edildi\n",
                    "2. **RFM Analizi:** Müşteri segmentasyonu tamamlandı\n",
                    "3. **Trend Analizi:** Zaman serisi analizi yapıldı\n",
                    "4. **Business Intelligence:** KPI dashboard oluşturuldu\n",
                    "\n",
                    "### 🚀 Sonraki Adımlar:\n",
                    "1. **A/B Testing:** Funnel optimizasyonu için testler\n",
                    "2. **Personalization:** Segment bazlı kişiselleştirme\n",
                    "3. **Automation:** Otomatik raporlama sistemi\n",
                    "4. **Monitoring:** Gerçek zamanlı KPI takibi\n",
                    "\n",
                    "---\n",
                    "\n",
                    "*Bu analiz, e-ticaret satış performansını artırmak için stratejik kararlar almanıza yardımcı olacaktır.*"
                ]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.5"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    
    # Save the notebook
    with open('notebooks/05_funnel_analizi.ipynb', 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=2, ensure_ascii=False)
    
    print("📊 Kapsamlı analiz hazır!")

if __name__ == "__main__":
    create_funnel_notebook() 