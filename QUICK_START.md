# 🎯 Sistema di Tracking Avanzato - Quick Start

Il bot ora ha **3 livelli di filtraggio** per trovare esattamente i prodotti che ti interessano!

## 📋 Livelli di Filtraggio

### 1️⃣ **Dipartimenti Amazon** (Base)
Cerca solo in categorie tech: Informatica, Elettronica, Videogiochi

### 2️⃣ **Categorie Tech** (Configurabile in `tracked_products.py`)
14 categorie tech con parole chiave: smartphones, laptops, GPU, CPU, etc.

### 3️⃣ **ASIN Specifici** (Configurabile in `tracked_asins.py`) ⭐ NUOVO!
Traccia prodotti specifici e trova automaticamente prodotti simili!

---

## 🚀 Setup Rapido

### Opzione A: Usa Solo Categorie (Più Semplice)

1. Apri `tracked_products.py`
2. Abilita/disabilita categorie che ti interessano:
```python
"smartphones": {
    "enabled": True  # Cambia a False per disabilitare
}
```

### Opzione B: Traccia ASIN Specifici (Più Preciso)

1. **Trova l'ASIN del prodotto che ti interessa:**
```bash
python3 find_asin.py "https://www.amazon.it/dp/B0CSTJP37Y"
```

2. **Copia l'output in `tracked_asins.py`:**
```python
TRACKED_ASINS = {
    "B0CSTJP37Y": "iPhone 15 Pro Max",
}
```

3. **Configura la ricerca di prodotti simili:**
```python
FIND_SIMILAR_PRODUCTS = True  # Trova anche prodotti simili
SIMILARITY_THRESHOLD = 30     # Quanto simili (30 = bilanciato)
```

---

## 📚 File di Configurazione

| File | Scopo | Quando Usarlo |
|------|-------|---------------|
| `tracked_products.py` | Categorie tech generali | Vuoi tutti i prodotti di una categoria |
| `tracked_asins.py` | ASIN specifici | Vuoi solo certi modelli e prodotti simili |

---

## 🛠️ Comandi Utili

### Trova ASIN da URL Amazon
```bash
cd amazon-deals-telegram-bot
python3 find_asin.py "URL_AMAZON_QUI"
```

### Testa il Filtro Categorie
```bash
python3 test_filtering.py
```

### Testa il Sistema ASIN
```bash
python3 test_asin_tracking.py
```

---

## 💡 Esempi Pratici

### Esempio 1: Solo iPhone

**In tracked_asins.py:**
```python
TRACKED_ASINS = {
    "B0CHX3TW6N": "iPhone 15 128GB",
}
FIND_SIMILAR_PRODUCTS = True
SIMILARITY_THRESHOLD = 40
```

**Risultato:** iPhone 15, iPhone 15 Pro, iPhone 15 Plus

---

### Esempio 2: Setup Gaming Completo

**In tracked_asins.py:**
```python
TRACKED_ASINS = {
    "B0D6Q8KYCW": "NVIDIA RTX 4070",
    "B0BSKWZ3FN": "AMD Ryzen 7 7800X3D",
    "B0BWNHWFKP": "Samsung Odyssey Monitor",
}
FIND_SIMILAR_PRODUCTS = True
SIMILARITY_THRESHOLD = 35
```

**Risultato:** Schede video RTX, CPU Ryzen 7000, Monitor gaming

---

### Esempio 3: Tutti i Prodotti Tech (Default)

**In tracked_products.py:**
Lascia tutte le categorie con `"enabled": True`

**Risultato:** Tutti i prodotti tech trovati su Amazon

---

## 🎯 Sistema di Priorità

Il bot invia i prodotti in questo ordine:

1. **⭐ ASIN Tracciati** - I prodotti esatti che hai specificato
2. **🎯 Prodotti Simili** - Prodotti simili agli ASIN tracciati
3. **✓ Categorie Tech** - Altri prodotti tech dalle categorie abilitate

---

## 📊 Output Telegram

### Prodotto Tracciato (ASIN specifico)
```
⭐📱 Apple iPhone 15 Pro Max 256GB

💰 EUR 1299.00 (prima era EUR 1499.00)
🏷 13% di sconto
⭐ Prodotto Tracciato
📂 Smartphones
🔗 Vai all'offerta Amazon
```

### Prodotto da Categoria
```
📱 Samsung Galaxy S24 Ultra

💰 EUR 1099.00 (prima era EUR 1399.00)
🏷 21% di sconto
📂 Smartphones
🔗 Vai all'offerta Amazon
```

---

## ⚙️ Configurazioni Consigliate

### Per Principianti
```python
# tracked_asins.py
TRACKED_ASINS = {}  # Vuoto, usa solo categorie
```

```python
# tracked_products.py
# Lascia tutte le categorie abilitate
```

### Per Utenti Avanzati
```python
# tracked_asins.py
TRACKED_ASINS = {
    "B0CSTJP37Y": "iPhone 15 Pro Max",
    "B0D6Q8KYCW": "RTX 4070",
}
FIND_SIMILAR_PRODUCTS = True
SIMILARITY_THRESHOLD = 35
```

```python
# tracked_products.py
# Disabilita categorie che non ti interessano
"tablets": {
    "enabled": False
}
```

---

## 📖 Guide Complete

- **[GUIDA_ASIN.md](GUIDA_ASIN.md)** - Guida completa al tracking ASIN (🇮🇹)
- **[CONFIGURAZIONE.md](CONFIGURAZIONE.md)** - Guida alle categorie tech (🇮🇹)
- **[TRACKING_CONFIG.md](TRACKING_CONFIG.md)** - Technical documentation (🇬🇧)

---

## 🔍 Troubleshooting

**Non trovo prodotti:**
- Abbassa `SIMILARITY_THRESHOLD` a 25-30
- Abilita più categorie in `tracked_products.py`
- Verifica che gli ASIN siano validi con `find_asin.py`

**Troppi prodotti non pertinenti:**
- Aumenta `SIMILARITY_THRESHOLD` a 40-50
- Disabilita categorie non necessarie
- Usa `FIND_SIMILAR_PRODUCTS = False` per ASIN esatti

**Errori durante l'esecuzione:**
- Verifica la sintassi Python (virgole, parentesi)
- Controlla i log nella console
- Assicurati che gli ASIN siano validi per Amazon.it

---

## 🎉 Risultati

- ✅ **Niente più spazzolini e coperte!**
- ✅ Solo prodotti tech che ti interessano
- ✅ Priorità ai prodotti che specifichi
- ✅ Trova automaticamente prodotti simili
- ✅ Facilmente personalizzabile

---

**Buon tracking! 🚀**
