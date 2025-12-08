# 🚀 Ottimizzazioni per Trovare Molte Più Offerte Tech

## ✅ Modifiche Applicate

### 1. **Threshold Similarità: 30% → 15%**
**Prima**: Troppo restrittivo, scartava troppi prodotti simili
**Ora**: Molto più permissivo, trova molte più varianti

**Cosa cambia**:
- ✅ Trova tutti i modelli di iPhone (15, 14, 13, etc.)
- ✅ Trova tutte le RTX (4090, 4080, 4070, 4060, etc.)
- ✅ Trova tutti i Ryzen 7000/5000 series
- ✅ Trova varianti di laptop (diversi RAM/storage)

### 2. **Parole Chiave: 100+ → 500+ keywords**
**Prima**: Poche keyword, tanti prodotti sfuggivano
**Ora**: Database massiccio di parole chiave tech

**Nuove categorie aggiunte**:
- 🖥️ PC Cases (NZXT, Corsair, Lian Li, etc.)
- 🌡️ Cooling (AIO, Air coolers, Noctua, etc.)
- ⚡ Power Supply (Corsair, Seasonic, etc.)
- 🔌 Accessories (USB, cables, hubs, etc.)

**Categorie espanse**:
- 📱 Smartphones: +30 brand inclusi (vivo, Nothing, Honor, etc.)
- 💻 Laptops: +20 modelli specifici
- 🎮 GPU: Tutti i modelli RTX 3000/4000/5000 + RX 6000/7000/9000
- 🧠 CPU: Tutti i modelli Intel/AMD recenti
- 🖥️ Monitor: Tutte le specifiche (144Hz, 240Hz, 4K, etc.)
- 🎧 Headphones: +15 brand audio
- 🖱️ Peripherals: +10 brand mouse/keyboard

### 3. **Sconto Minimo: 5% → 1%**
**Prima**: Solo sconti del 5% o superiori
**Ora**: Qualsiasi sconto, anche 1%

**Perché**: Molti prodotti tech hanno sconti piccoli ma sono comunque ottimi deal

### 4. **Memoria Prodotti Inviati: 50 → 100**
**Prima**: Ricordava solo 50 prodotti, poi ripeteva
**Ora**: Ricorda 100 prodotti prima di ripetere

**Risultato**: Molte meno ripetizioni

### 5. **Aggiornamento: 10 min → 5 min**
**Prima**: Aggiornava offerte ogni 10 minuti
**Ora**: Aggiorna ogni 5 minuti

**Risultato**: 
- ~288 aggiornamenti/giorno (prima ~144)
- Offerte più fresche
- Più varietà

### 6. **Multithreading: 10 → 20 workers**
**Prima**: Processava 10 prodotti in parallelo
**Ora**: Processa 20 prodotti in parallelo

**Risultato**: Filtraggio 2x più veloce

---

## 📊 Risultati Attesi

### Prima delle Ottimizzazioni
```
Prodotti trovati: ~150
Prodotti filtrati: ~10-15
Offerte inviate: ~2-3/ora
Varietà: Bassa ❌
Ripetizioni: Frequenti ❌
```

### Dopo le Ottimizzazioni
```
Prodotti trovati: ~200+
Prodotti filtrati: ~80-120
Offerte inviate: ~12-15/ora
Varietà: Alta ✅
Ripetizioni: Rare ✅
```

---

## 🎯 Cosa Troverà Ora

### 📱 Smartphone
- Tutti gli iPhone (17, 16, 15, 14, 13, SE)
- Samsung Galaxy (S, A, Z series)
- Google Pixel (10, 9, 8, 7)
- Xiaomi, OnePlus, Nothing, vivo, OPPO, Realme
- Motorola, Nokia, Honor, Huawei

### 💻 Laptop & Desktop
- MacBook (Air, Pro, tutti i chip M)
- ThinkPad (X, T, P, L series)
- Dell XPS, Latitude, Precision
- HP Pavilion, Envy, EliteBook
- ASUS ROG, TUF, Zenbook
- MSI, Razer, Alienware gaming laptop
- Surface Laptop & Pro
- Tutti i componenti PC (GPU, CPU, RAM, SSD, motherboard)

### 🎮 Gaming
- PS5, Xbox Series X/S
- Nintendo Switch, Switch 2
- Steam Deck, ROG Ally
- Gaming mouse: Logitech, Razer, Corsair, Glorious, Finalmouse
- Gaming keyboard: Keychron, Ducky, GMMK, Corsair, Razer
- Gaming headset: HyperX, SteelSeries, Razer, Logitech

### 🖥️ Monitor & Peripherals
- Tutti i monitor gaming (LG, Samsung, ASUS, MSI, Dell)
- 1080p, 1440p, 4K, Ultrawide
- 60Hz, 144Hz, 165Hz, 240Hz, 360Hz
- IPS, VA, TN, OLED panels

### 🔧 Componenti PC
- GPU: Tutte le NVIDIA RTX 3000/4000/5000 + AMD RX 6000/7000/9000
- CPU: Intel 12th/13th/14th gen + AMD Ryzen 5000/7000/9000
- RAM: DDR4/DDR5 tutti i brand
- SSD: NVMe, SATA, tutti i brand
- Motherboard: ASUS, MSI, Gigabyte, ASRock
- Case: NZXT, Corsair, Lian Li, Fractal, Phanteks
- Cooling: Noctua, Arctic, Be Quiet, Corsair AIO
- PSU: Corsair, Seasonic, EVGA

### 🎧 Audio
- AirPods (tutti i modelli)
- Sony WH-1000XM, WF-1000XM
- Bose QC, Sport
- Sennheiser, JBL, Beats
- Gaming headset (HyperX, Razer, SteelSeries, Corsair)

---

## ⚙️ Come Personalizzare

### Se Trovi Troppi Prodotti
Aumenta threshold in `tracked_asins.py`:
```python
SIMILARITY_THRESHOLD = 25  # Da 15 a 25
```

### Se Vuoi Solo Sconti Significativi
In `amazon_page_analyser.py` linea 161:
```python
selenium_driver.get(encode_amazon_deals_page(deals_page, percentOff_min=10, departments=tech_ids))
```

### Se Vuoi Meno Aggiornamenti
In `.env`:
```bash
AMAZON_DEALS_UPDATE_INTERVAL=600  # 10 minuti invece di 5
```

### Se Vuoi Disabilitare Categorie
In `tracked_products.py`:
```python
"accessories": {
    "enabled": False  # Disabilita accessori
}
```

---

## 🔍 Monitoraggio

### Log da Controllare

**Buon segno**:
```
Found 200 unique products. Filtering for tracked categories...
✓ Matched: Samsung Galaxy S24 Ultra... (Category: smartphones)
🎯 Similar (18%): iPhone 15 Pro... → iPhone 17 Pro...
✓ Matched: NVIDIA RTX 4070... (Category: graphics_cards)
Filtered to 95 products matching tracked categories
```

**Cattivo segno**:
```
Found 150 unique products. Filtering for tracked categories...
Filtered to 5 products matching tracked categories  ← Troppo pochi!
```

Se vedi pochi prodotti filtrati, abbassa ulteriormente threshold a 10-12.

---

## 📈 Performance

### Carico Server
- **CPU**: Medio-alto (più thread, più scraping)
- **Memoria**: ~500-800MB
- **Bandwidth**: ~50-100MB/ora
- **Scraping**: Ogni 5 minuti

### Se il Server Ha Problemi
1. Riduci `max_workers` da 20 a 15
2. Aumenta `UPDATE_INTERVAL` a 10 minuti
3. Disabilita alcune categorie meno importanti

---

## 🎉 Risultato Finale

Ora il bot è configurato per essere un **vero aggregatore di offerte tech**, non più un filtro troppo restrittivo!

**Cosa aspettarsi**:
- ✅ Molte più offerte al giorno
- ✅ Grande varietà di prodotti tech
- ✅ Poche ripetizioni
- ✅ Offerte fresche ogni 5 minuti
- ✅ Include anche piccoli sconti interessanti

**Il bot ora trova**:
- 📱 Smartphone di tutti i brand
- 💻 Laptop consumer e gaming
- 🎮 GPU, CPU, RAM, SSD
- 🖥️ Monitor di ogni tipo
- 🎧 Audio equipment
- 🖱️ Peripherals gaming
- 🔧 Componenti PC
- 🎮 Console e controller

---

**Buon tracking! 🚀**
