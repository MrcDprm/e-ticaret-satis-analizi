# 🛒 E-Ticaret Satış Analizi Projesi

## 📊 Proje Özeti

Bu proje, e-ticaret platformlarındaki satış verilerini analiz ederek kullanıcı davranışlarını, ürün trendlerini ve satış performansını incelemeyi amaçlamaktadır.

### 🎯 Ana Hedefler
- **Funnel Analizi** - Satış sürecindeki darboğazları tespit etme
- **Kullanıcı Davranışı** - Müşteri segmentasyonu ve davranış analizi
- **Trend Analizi** - Zaman serisi analizi ve gelecek tahminleri
- **Business Intelligence** - KPI dashboard ve stratejik öneriler

## 📁 Proje Yapısı

```
e-ticaret-satis-analizi/
├── 📁 data/                    # Veri setleri
│   ├── 📁 raw/                # Ham veriler (4 dosya, 24MB+)
│   └── 📁 processed/          # İşlenmiş veriler (15 dosya)
├── 📁 notebooks/              # Jupyter notebook'ları (7 adet)
│   ├── 01_basit_analiz.ipynb
│   ├── 02_detayli_analiz.ipynb
│   ├── 03_sonuclar.ipynb
│   ├── 04_sonuclar_uyari_giderilmis.ipynb
│   └── 05_funnel_analizi.ipynb
├── 📁 src/                    # Python kaynak kodları
│   ├── data_loader.py         # Veri yükleme
│   ├── analyzer.py            # Analiz fonksiyonları
│   ├── visualizer.py          # Görselleştirme
│   └── utils.py               # Yardımcı fonksiyonlar
├── 📁 reports/                # Raporlar ve görselleştirmeler
│   ├── 📁 figures/           # Interactive grafikler (7 HTML)
│   ├── 📁 executive_summary/ # Yönetici raporları (2 MD)
│   └── 📁 presentations/     # Sunum materyalleri (1 JSON)
├── 📁 scripts/                # Veri ve notebook oluşturma scriptleri
│   ├── 📁 data_generation/   # Veri oluşturma scriptleri
│   ├── 📁 notebook_generation/ # Notebook oluşturma scriptleri
│   └── 📁 report_generation/ # Rapor oluşturma scriptleri
├── 📁 docs/                   # Dokümantasyon
│   ├── proje_kontrol_raporu.md
│   ├── proje_ozeti.md
│   └── proje_gelistirme_plani.md
├── requirements.txt           # Gerekli kütüphaneler
├── README.md                 # Bu dosya
└── .gitignore               # Git ignore dosyası
```

## 🚀 Kurulum ve Çalıştırma

### 1. Gerekli Kütüphanelerin Kurulumu
```bash
pip install -r requirements.txt
```

### 2. Jupyter Notebook Başlatma
```bash
jupyter notebook
```

### 3. Analiz Notebook'larını Çalıştırma
1. `notebooks/01_basit_analiz.ipynb` - Temel analiz
2. `notebooks/02_detayli_analiz.ipynb` - Detaylı analiz
3. `notebooks/05_funnel_analizi.ipynb` - Kapsamlı funnel analizi

## 📊 Analiz Kapsamı

### 🎯 Funnel Analizi
- **Aşamalar:** Görüntüleme → Sepete Ekleme → Ödeme → Tamamlama
- **Drop-off Tespiti:** En kritik nokta belirlendi
- **Conversion Rate:** Her aşama için hesaplandı
- **Kategori Bazlı:** Her kategori için ayrı analiz

### 👥 RFM Analizi
- **500+ Müşteri:** Segmentasyon tamamlandı
- **Champions Segmenti:** %25 değer katkısı
- **Scoring System:** R-F-M skorları
- **Segment Özeti:** Detaylı raporlar

### 📈 Trend Analizi
- **Günlük Trend:** 366 gün veri
- **Haftalık Trend:** 52 hafta
- **Aylık Trend:** 12 ay
- **Kategori Trendi:** 2196 kayıt

### 🎯 Kullanıcı Davranışı
- **Session Analizi:** Süre, sayfa görüntüleme
- **Bounce Rate:** Sayfa terk analizi
- **Return Visitor:** Tekrar ziyaret oranı
- **Purchase Behavior:** Satın alma davranışı

## 📈 İş Sonuçları

### ✅ Funnel Optimizasyonu
- **Drop-off Noktası Tespiti:** En kritik aşama belirlendi
- **Conversion Rate İyileştirme:** %15 artış potansiyeli
- **Bottleneck Analizi:** Performans darboğazları tespit edildi

### ✅ Müşteri Segmentasyonu
- **RFM Analizi:** 500+ müşteri segmentasyonu
- **Champions Segmenti:** %25 değer katkısı
- **Targeted Marketing:** Segment bazlı stratejiler

### ✅ Trend Analizi
- **Seasonal Patterns:** Mevsimsel değişimler
- **Product Performance:** Kategori bazlı performans
- **Forecasting:** Gelecek tahminleri

## 🛠️ Teknik Stack

### Data Analysis
- **Pandas & NumPy:** 365,000+ kayıt analizi
- **Statistical Analysis:** Conversion rate, RFM, trend analizi

### Visualization
- **Plotly:** Interactive funnel charts
- **Matplotlib & Seaborn:** Trend ve segmentasyon grafikleri
- **Business Intelligence:** KPI dashboard'ları

### Business Intelligence
- **Funnel Analysis:** Drop-off noktaları tespiti
- **RFM Segmentation:** Müşteri segmentasyonu
- **Time Series Analysis:** Trend tahminleri
- **KPI Tracking:** Ana performans göstergeleri

## 📊 Raporlar ve Görselleştirmeler

### 📈 Interactive Grafikler
- **Funnel Chart:** Satış funnel'i görselleştirmesi
- **RFM Scatter:** Müşteri segmentasyonu
- **Trend Lines:** Zaman serisi analizi
- **KPI Dashboard:** Ana performans göstergeleri

### 📋 Raporlar
- **Executive Summary:** Yönetici özeti
- **Detailed Analysis:** Teknik detaylar
- **Business Insights:** Stratejik öneriler

## 📈 Proje Metrikleri

- **Veri Boyutu:** 365,000+ kayıt (24MB+)
- **Analiz Kapsamı:** 1 yıl (366 gün)
- **Notebook Sayısı:** 7 adet
- **Görselleştirme:** 10+ grafik tipi
- **Rapor Sayısı:** 10+ dosya

## 🚀 Sonraki Adımlar

1. **Jupyter'de `05_funnel_analizi.ipynb` dosyasını aç ve çalıştır**
2. **Interactive grafikleri incele**
3. **Raporları oku ve stratejik önerileri değerlendir**
4. **Analiz sonuçlarını kullanarak iş kararları al**

---

*Bu proje e-ticaret satış analizi için kapsamlı bir veri analizi çözümü sunmaktadır.*
=======
