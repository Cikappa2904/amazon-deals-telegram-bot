# Configurazione Tracking Prodotti - Esempio

## Modifiche Implementate

Ho implementato un sistema di filtraggio avanzato che:

### 1. **Filtra per Dipartimenti Amazon**
- Informatica (schede video, componenti PC)
- Elettronica 
- Videogiochi

### 2. **Filtra per Parole Chiave**
Dopo lo scraping, ogni prodotto viene controllato per vedere se contiene parole chiave specifiche.

## Come Funziona

### File `tracked_products.py`
Questo file contiene tutte le configurazioni:

```python
TRACKED_CATEGORIES = {
    "smartphones": {
        "keywords": ["iphone", "samsung galaxy", "smartphone", ...],
        "enabled": True  # Abilita/disabilita questa categoria
    },
    "laptops": {
        "keywords": ["laptop", "notebook", "macbook", ...],
        "enabled": True
    },
    # ... altre categorie
}
```

### Personalizzazione

**Per trackare SOLO iPhone e schede video:**

```python
"smartphones": {
    "keywords": ["iphone"],  # Solo iPhone
    "enabled": True
},
"graphics_cards": {
    "keywords": ["scheda video", "gpu", "nvidia", "geforce", "rtx", "amd", "radeon"],
    "enabled": True
},
"laptops": {
    "enabled": False  # Disabilita i laptop
},
# ... disabilita tutte le altre categorie che non ti interessano
```

**Per trackare tutto il tech:**
Lascia tutte le categorie con `"enabled": True` (configurazione di default)

## Categorie Disponibili

1. **smartphones** - iPhone, Samsung Galaxy, Xiaomi, ecc.
2. **laptops** - Notebook, MacBook, laptop gaming
3. **graphics_cards** - NVIDIA RTX, AMD Radeon
4. **processors** - Intel Core, AMD Ryzen
5. **monitors** - Monitor gaming, 4K
6. **tablets** - iPad, Galaxy Tab
7. **smartwatches** - Apple Watch, Galaxy Watch
8. **headphones** - AirPods, cuffie wireless
9. **consoles** - PlayStation, Xbox, Nintendo Switch
10. **ssd_storage** - SSD, hard disk
11. **ram** - Memorie RAM
12. **motherboards** - Schede madri
13. **cameras** - Fotocamere, GoPro
14. **mice_keyboards** - Mouse e tastiere gaming

## Test

Il file `test_filtering.py` ti permette di testare il filtro:

```bash
cd amazon-deals-telegram-bot
python3 test_filtering.py
```

Output esempio:
```
✓ MATCH: Apple iPhone 15 Pro 128GB Blu
  Category: smartphones

✗ SKIP: Spazzolino elettrico Oral-B
  (Not a tech product)

✓ MATCH: NVIDIA GeForce RTX 4070 12GB
  Category: graphics_cards
```

## Output del Bot

Quando il bot trova un'offerta, ora mostra anche la categoria:

```
📱 Apple iPhone 15 Pro 128GB

💰 EUR 1099.00 (prima era EUR 1299.00)
🏷 15% di sconto
📂 Smartphones
🔗 Vai all'offerta Amazon
```

## Performance

- Il filtro viene applicato quando si scaricano le offerte (ogni 2 ore)
- Usa multithreading per controllare i prodotti velocemente
- Mostra il progresso: "Progress: 50/150 products checked..."

## Suggerimenti

1. **Inizia con tutte le categorie abilitate** per vedere cosa trova
2. **Monitora i log** per vedere quali prodotti vengono matchati
3. **Aggiungi parole chiave** se vedi che alcuni prodotti desiderati vengono esclusi
4. **Riduci le categorie** una volta che capisci cosa ti interessa

## Modifica Percentuale Sconto

In `amazon_page_analyser.py` linea 161, puoi modificare lo sconto minimo:

```python
# Cambia da 5% a 30% per vedere solo sconti significativi
selenium_driver.get(encode_amazon_deals_page(deals_page, percentOff_min=30, departments=tech_ids))
```
