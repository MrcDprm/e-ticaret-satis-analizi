import json

# Gerçek sonuçlar notebook yapısı
notebook = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# E-Ticaret Satış Analizi - Gerçek Sonuçlar\n",
                "\n",
                "Bu notebook'ta analiz sonuçlarını dinamik olarak hesaplayıp gerçek değerleri göreceğiz."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Gerekli kütüphaneleri import edelim\n",
                "import pandas as pd\n",
                "import numpy as np\n",
                "import matplotlib.pyplot as plt\n",
                "import seaborn as sns\n",
                "\n",
                "# Türkçe karakter desteği\n",
                "plt.rcParams['font.family'] = ['DejaVu Sans']\n",
                "\n",
                "print(\"Kütüphaneler başarıyla import edildi!\")"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Veri setini yükle\n",
                "df = pd.read_csv('../data/raw/ecommerce_sales.csv')\n",
                "print(\"Veri seti yüklendi!\")\n",
                "print(f\"Toplam satış: {df['total_amount'].sum():,.2f} TL\")\n",
                "print(f\"Toplam sipariş: {len(df)} adet\")"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Kategori analizi\n",
                "category_analysis = df.groupby('category')['total_amount'].sum().sort_values(ascending=False)\n",
                "en_cok_satan_kategori = category_analysis.index[0]\n",
                "en_cok_satan_kategori_satis = category_analysis.iloc[0]\n",
                "\n",
                "category_count = df.groupby('category')['order_id'].count().sort_values(ascending=False)\n",
                "en_cok_siparis_alan_kategori = category_count.index[0]\n",
                "en_cok_siparis_alan_kategori_sayisi = category_count.iloc[0]\n",
                "\n",
                "category_avg = df.groupby('category')['total_amount'].mean().sort_values(ascending=False)\n",
                "en_yuksek_ortalama_kategori = category_avg.index[0]\n",
                "en_yuksek_ortalama_kategori_deger = category_avg.iloc[0]\n",
                "\n",
                "category_rating = df.groupby('category')['rating'].mean().sort_values(ascending=False)\n",
                "en_yuksek_degerlendirme_kategori = category_rating.index[0]\n",
                "en_yuksek_degerlendirme_kategori_puan = category_rating.iloc[0]\n",
                "\n",
                "print(\"🏆 KATEGORİ ANALİZİ:\")\n",
                "print(f\"En çok satan kategori: {en_cok_satan_kategori} ({en_cok_satan_kategori_satis:,.2f} TL)\")\n",
                "print(f\"En çok sipariş alan kategori: {en_cok_siparis_alan_kategori} ({en_cok_siparis_alan_kategori_sayisi} sipariş)\")\n",
                "print(f\"En yüksek ortalama satış: {en_yuksek_ortalama_kategori} ({en_yuksek_ortalama_kategori_deger:,.2f} TL)\")\n",
                "print(f\"En yüksek değerlendirme: {en_yuksek_degerlendirme_kategori} ({en_yuksek_degerlendirme_kategori_puan:.2f} puan)\")"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Şehir analizi\n",
                "city_analysis = df.groupby('customer_city')['total_amount'].sum().sort_values(ascending=False)\n",
                "en_cok_satis_sehir = city_analysis.index[0]\n",
                "en_cok_satis_sehir_tutar = city_analysis.iloc[0]\n",
                "\n",
                "city_count = df.groupby('customer_city')['order_id'].count().sort_values(ascending=False)\n",
                "en_cok_siparis_sehir = city_count.index[0]\n",
                "en_cok_siparis_sehir_sayisi = city_count.iloc[0]\n",
                "\n",
                "city_age = df.groupby('customer_city')['customer_age'].mean().sort_values(ascending=False)\n",
                "en_yuksek_yas_sehir = city_age.index[0]\n",
                "en_yuksek_yas_sehir_yas = city_age.iloc[0]\n",
                "\n",
                "city_rating = df.groupby('customer_city')['rating'].mean().sort_values(ascending=False)\n",
                "en_yuksek_degerlendirme_sehir = city_rating.index[0]\n",
                "en_yuksek_degerlendirme_sehir_puan = city_rating.iloc[0]\n",
                "\n",
                "print(\"🏙️ ŞEHİR ANALİZİ:\")\n",
                "print(f\"En çok satış yapılan şehir: {en_cok_satis_sehir} ({en_cok_satis_sehir_tutar:,.2f} TL)\")\n",
                "print(f\"En çok sipariş alan şehir: {en_cok_siparis_sehir} ({en_cok_siparis_sehir_sayisi} sipariş)\")\n",
                "print(f\"En yüksek ortalama müşteri yaşı: {en_yuksek_yas_sehir} ({en_yuksek_yas_sehir_yas:.1f} yaş)\")\n",
                "print(f\"En yüksek değerlendirme: {en_yuksek_degerlendirme_sehir} ({en_yuksek_degerlendirme_sehir_puan:.2f} puan)\")"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Ödeme yöntemi analizi\n",
                "payment_analysis = df.groupby('payment_method')['total_amount'].sum().sort_values(ascending=False)\n",
                "en_populer_odeme = payment_analysis.index[0]\n",
                "en_populer_odeme_tutar = payment_analysis.iloc[0]\n",
                "\n",
                "payment_avg = df.groupby('payment_method')['total_amount'].mean().sort_values(ascending=False)\n",
                "en_yuksek_ortalama_odeme = payment_avg.index[0]\n",
                "en_yuksek_ortalama_odeme_deger = payment_avg.iloc[0]\n",
                "\n",
                "payment_rating = df.groupby('payment_method')['rating'].mean().sort_values(ascending=False)\n",
                "en_yuksek_degerlendirme_odeme = payment_rating.index[0]\n",
                "en_yuksek_degerlendirme_odeme_puan = payment_rating.iloc[0]\n",
                "\n",
                "print(\"💳 ÖDEME YÖNTEMİ ANALİZİ:\")\n",
                "print(f\"En popüler ödeme yöntemi: {en_populer_odeme} ({en_populer_odeme_tutar:,.2f} TL)\")\n",
                "print(f\"En yüksek ortalama satış: {en_yuksek_ortalama_odeme} ({en_yuksek_ortalama_odeme_deger:,.2f} TL)\")\n",
                "print(f\"En yüksek değerlendirme: {en_yuksek_degerlendirme_odeme} ({en_yuksek_degerlendirme_odeme_puan:.2f} puan)\")"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Müşteri segmentasyonu\n",
                "ortalama_yas = df['customer_age'].mean()\n",
                "\n",
                "# Yaş grupları oluştur\n",
                "df['yas_grubu'] = pd.cut(df['customer_age'], \n",
                "                         bins=[0, 25, 35, 45, 55, 100], \n",
                "                         labels=['18-25', '26-35', '36-45', '46-55', '55+'])\n",
                "\n",
                "age_group_sales = df.groupby('yas_grubu')['total_amount'].sum().sort_values(ascending=False)\n",
                "en_aktif_yas_grubu = age_group_sales.index[0]\n",
                "en_aktif_yas_grubu_satis = age_group_sales.iloc[0]\n",
                "\n",
                "gender_sales = df.groupby('customer_gender')['total_amount'].sum().sort_values(ascending=False)\n",
                "en_yuksek_satis_cinsiyet = gender_sales.index[0]\n",
                "en_yuksek_satis_cinsiyet_tutar = gender_sales.iloc[0]\n",
                "\n",
                "gender_rating = df.groupby('customer_gender')['rating'].mean().sort_values(ascending=False)\n",
                "en_yuksek_degerlendirme_cinsiyet = gender_rating.index[0]\n",
                "en_yuksek_degerlendirme_cinsiyet_puan = gender_rating.iloc[0]\n",
                "\n",
                "print(\"👥 MÜŞTERİ SEGMENTASYONU:\")\n",
                "print(f\"Ortalama müşteri yaşı: {ortalama_yas:.1f} yaş\")\n",
                "print(f\"En aktif yaş grubu: {en_aktif_yas_grubu} ({en_aktif_yas_grubu_satis:,.2f} TL)\")\n",
                "print(f\"En yüksek satış yapan cinsiyet: {en_yuksek_satis_cinsiyet} ({en_yuksek_satis_cinsiyet_tutar:,.2f} TL)\")\n",
                "print(f\"En yüksek değerlendirme yapan cinsiyet: {en_yuksek_degerlendirme_cinsiyet} ({en_yuksek_degerlendirme_cinsiyet_puan:.2f} puan)\")"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Performans metrikleri\n",
                "iade_orani = df['is_returned'].mean() * 100\n",
                "ortalama_degerlendirme = df['rating'].mean()\n",
                "toplam_satis = df['total_amount'].sum()\n",
                "toplam_siparis = len(df)\n",
                "\n",
                "print(\"📈 PERFORMANS METRİKLERİ:\")\n",
                "print(f\"İade oranı: %{iade_orani:.1f}\")\n",
                "print(f\"Ortalama değerlendirme: {ortalama_degerlendirme:.2f} puan\")\n",
                "print(f\"Toplam satış: {toplam_satis:,.2f} TL\")\n",
                "print(f\"Toplam sipariş: {toplam_siparis} adet\")"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Stratejik öneriler\n",
                "print(\"🎯 STRATEJİK ÖNERİLER:\")\n",
                "print(f\"1. Kategori odaklı: {en_cok_satan_kategori} kategorisinde daha fazla ürün çeşitliliği\")\n",
                "print(f\"2. Bölgesel: {en_cok_satis_sehir} bölgesinde daha fazla pazarlama\")\n",
                "print(f\"3. Müşteri odaklı: {en_aktif_yas_grubu} yaş grubuna özel kampanyalar\")\n",
                "print(f\"4. Ödeme: {en_populer_odeme} ödeme seçeneklerini artırma\")\n",
                "print(f\"5. İade yönetimi: %{iade_orani:.1f} iade oranını düşürmek için kalite artırımı\")\n",
                "print(f\"6. Müşteri memnuniyeti: {ortalama_degerlendirme:.2f} puan ortalamasını artırma\")"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Özet tablo\n",
                "print(\"📊 ÖZET TABLO:\")\n",
                "print(\"=\" * 60)\n",
                "print(f\"🏆 En Çok Satan Kategori: {en_cok_satan_kategori}\")\n",
                "print(f\"🏙️ En Çok Satış Yapılan Şehir: {en_cok_satis_sehir}\")\n",
                "print(f\"💳 En Popüler Ödeme Yöntemi: {en_populer_odeme}\")\n",
                "print(f\"👥 Ortalama Müşteri Yaşı: {ortalama_yas:.1f}\")\n",
                "print(f\"📈 İade Oranı: %{iade_orani:.1f}\")\n",
                "print(f\"⭐ Ortalama Değerlendirme: {ortalama_degerlendirme:.2f}\")\n",
                "print(f\"💰 Toplam Satış: {toplam_satis:,.2f} TL\")\n",
                "print(f\"📦 Toplam Sipariş: {toplam_siparis} adet\")\n",
                "print(\"=\" * 60)\n",
                "\n",
                "print(\"\\nBu gerçek analiz sonuçları e-ticaret stratejileri geliştirmek için kullanılabilir!\")"
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

# Notebook'u kaydet
notebook_path = "notebooks/03_sonuclar.ipynb"
with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=2, ensure_ascii=False)

print(f"Gerçek sonuçlar notebook'u başarıyla oluşturuldu: {notebook_path}")
print("Şimdi Jupyter'de bu dosyayı açabilirsin!") 