# 📌 Guida al Tracking di ASIN Specifici

## Cos'è un ASIN?

Un **ASIN** (Amazon Standard Identification Number) è un codice univoco di 10 caratteri che Amazon assegna ad ogni prodotto.

Esempio: `B0CSTJP37Y` per iPhone 15 Pro Max

## Come Trovare un ASIN

### Metodo 1: Dall'URL Amazon

Quando visiti un prodotto su Amazon, l'URL contiene l'ASIN:
```
https://www.amazon.it/dp/B0CSTJP37Y/...
                         ^^^^^^^^^^
                         Questo è l'ASIN
```

### Metodo 2: Usando lo Script Helper

```bash
cd amazon-deals-telegram-bot
python3 find_asin.py "https://www.amazon.it/dp/B0CSTJP37Y"
```

Lo script ti mostrerà:
- ✓ L'ASIN estratto
- 📦 Dettagli del prodotto (titolo, prezzo, sconto)
- 📋 La riga da copiare in `tracked_asins.py`
- 🔍 Le parole chiave estratte per trovare prodotti simili

## Come Aggiungere ASIN da Tracciare

### 1. Trova l'ASIN del prodotto che ti interessa

Usa `find_asin.py` o estrai manualmente dall'URL.

### 2. Apri il file `tracked_asins.py`

```python
TRACKED_ASINS = {
    # Aggiungi i tuoi ASIN qui
}
```

### 3. Aggiungi l'ASIN con una descrizione

```python
TRACKED_ASINS = {
    "B0CSTJP37Y": "iPhone 15 Pro Max 256GB",
    "B0CWV17BK2": "Samsung Galaxy S24 Ultra",
    "B0D6Q8KYCW": "NVIDIA GeForce RTX 4070",
    "B09SX4YZFG": "MacBook Air M2 13 pollici",
}
```

**Nota**: La descrizione è opzionale, serve solo come riferimento per te.

## Configurazione Avanzata

### Trova Prodotti Simili

Nel file `tracked_asins.py`:

```python
# Se True, il bot cerca anche prodotti simili agli ASIN tracciati
FIND_SIMILAR_PRODUCTS = True  # Raccomandato!

# Soglia di similarità (0-100)
# Più alto = più rigido, meno prodotti
# Più basso = più flessibile, più varietà
SIMILARITY_THRESHOLD = 30
```

**Esempi di Threshold:**
- `50-70`: Molto rigido - solo prodotti molto simili (stesso brand e modello)
- `30-50`: Bilanciato - stesso tipo di prodotto (es. tutti gli iPhone)
- `10-30`: Flessibile - categoria simile (es. tutti gli smartphone)

### Disabilita Ricerca Prodotti Simili

Se vuoi tracciare **SOLO** gli ASIN esatti che hai specificato:

```python
FIND_SIMILAR_PRODUCTS = False
```

## Come Funziona il Sistema di Priorità

Il bot usa questo ordine di priorità:

1. **⭐ ASIN Tracciati**: I prodotti che hai specificato in `TRACKED_ASINS`
2. **🎯 Prodotti Simili**: Prodotti con alta similarità agli ASIN tracciati (se abilitato)
3. **✓ Categorie Tech**: Prodotti che matchano le categorie in `tracked_products.py`

### Esempio Output

```
⭐📱 Apple iPhone 15 Pro Max 256GB Blu

💰 EUR 1299.00 (prima era EUR 1499.00)
🏷 13% di sconto
⭐ Prodotto Tracciato
📂 Smartphones
🔗 Vai all'offerta Amazon
```

## Esempi Pratici

### Esempio 1: Tracciare Solo iPhone 15

```python
TRACKED_ASINS = {
    "B0CHX3TW6N": "iPhone 15 128GB",
    "B0CHX1W1XY": "iPhone 15 256GB",
    "B0CHX2F3SG": "iPhone 15 512GB",
}

FIND_SIMILAR_PRODUCTS = False  # Solo questi iPhone esatti
```

### Esempio 2: Tracciare iPhone e Prodotti Simili

```python
TRACKED_ASINS = {
    "B0CHX3TW6N": "iPhone 15 128GB",
}

FIND_SIMILAR_PRODUCTS = True
SIMILARITY_THRESHOLD = 40
```

Troverà: iPhone 15 Pro, iPhone 15 Plus, altri modelli iPhone

### Esempio 3: Tracciare Setup Gaming Completo

```python
TRACKED_ASINS = {
    "B0D6Q8KYCW": "NVIDIA RTX 4070",
    "B0BSKWZ3FN": "AMD Ryzen 7 7800X3D",
    "B0BWNHWFKP": "Samsung Odyssey G7 Monitor",
    "B0BCDMQ44Y": "Corsair Vengeance DDR5 32GB",
}

FIND_SIMILAR_PRODUCTS = True
SIMILARITY_THRESHOLD = 35
```

Troverà anche: RTX 4060/4080, altri Ryzen 7000, altri monitor gaming, altre RAM DDR5

### Esempio 4: Solo Specifici Modelli MacBook

```python
TRACKED_ASINS = {
    "B09SX4YZFG": "MacBook Air M2 13 pollici",
    "B0CM5R6PTW": "MacBook Pro M3 14 pollici",
}

FIND_SIMILAR_PRODUCTS = False  # Solo questi modelli
```

## Workflow Completo

### 1. Trova ASIN

```bash
python3 find_asin.py "https://www.amazon.it/dp/B0CSTJP37Y"
```

Output:
```
✓ Found ASIN: B0CSTJP37Y

PRODUCT DETAILS
Title:    Apple iPhone 15 Pro Max (256 GB) - Titanio blu
...

ADD TO TRACKED_ASINS.PY
    "B0CSTJP37Y": "Apple iPhone 15 Pro Max (256 GB) - Titanio bl...",
```

### 2. Copia in tracked_asins.py

```python
TRACKED_ASINS = {
    "B0CSTJP37Y": "Apple iPhone 15 Pro Max (256 GB) - Titanio bl...",
}
```

### 3. Configura Similarità

```python
FIND_SIMILAR_PRODUCTS = True
SIMILARITY_THRESHOLD = 40
```

### 4. Testa (Opzionale)

Puoi testare manualmente:

```python
from tracked_asins import is_tracked_asin, calculate_similarity

# Verifica se un ASIN è tracciato
print(is_tracked_asin("B0CSTJP37Y"))  # True

# Testa similarità
title1 = "Apple iPhone 15 Pro Max 256GB"
title2 = "Apple iPhone 15 Pro 128GB"
score = calculate_similarity(title1, title2)
print(f"Similarità: {score}%")  # Circa 75-85%
```

### 5. Esegui il Bot

Il bot ora darà priorità ai tuoi ASIN tracciati!

## Tips & Tricks

### ✅ Best Practices

1. **Inizia con pochi ASIN** (3-5) per vedere come funziona
2. **Usa FIND_SIMILAR_PRODUCTS = True** per più risultati
3. **Regola SIMILARITY_THRESHOLD** in base ai risultati che vedi
4. **Monitora i log** per vedere quali prodotti vengono matchati
5. **Aggiorna regolarmente** gli ASIN quando escono nuovi modelli

### ⚠️ Cose da Evitare

1. **Non aggiungere troppi ASIN** (> 20) - rallenta il processo
2. **Non usare threshold troppo basso** (< 20) - troppi falsi positivi
3. **Non dimenticare le virgole** nella configurazione Python
4. **Non tracciare prodotti non tech** - usa solo prodotti nelle categorie supportate

### 🔧 Troubleshooting

**Problema**: "Could not fetch product details"
- **Soluzione**: L'ASIN potrebbe essere invalido o non disponibile su Amazon.it

**Problema**: Troppi prodotti dissimili vengono matchati
- **Soluzione**: Aumenta `SIMILARITY_THRESHOLD` a 40-50

**Problema**: Nessun prodotto viene trovato
- **Soluzione**: Abbassa `SIMILARITY_THRESHOLD` a 25-30

**Problema**: Voglio solo gli ASIN esatti
- **Soluzione**: Imposta `FIND_SIMILAR_PRODUCTS = False`

## Combinare ASIN con Categorie

Puoi usare sia `tracked_asins.py` che `tracked_products.py` insieme!

**In tracked_asins.py:**
```python
TRACKED_ASINS = {
    "B0CSTJP37Y": "iPhone 15 Pro Max",
}
FIND_SIMILAR_PRODUCTS = True
```

**In tracked_products.py:**
```python
"smartphones": {
    "keywords": [...],
    "enabled": True  # Mantieni abilitato
}
```

Il bot troverà:
1. iPhone 15 Pro Max (ASIN esatto) - **Priorità Alta** ⭐
2. Altri iPhone 15 (prodotti simili) - **Priorità Media** 🎯
3. Altri smartphone (categoria) - **Priorità Normale** ✓

## Monitoraggio

### Log di Sistema

Quando il bot gira, vedrai:
```
Loading tracked ASINs for similarity comparison...
  Tracking: Apple iPhone 15 Pro Max (256 GB) - Titanio blu...
Found 150 unique products. Filtering for tracked categories...
⭐ TRACKED ASIN: B0CSTJP37Y
🎯 Similar (78%): Apple iPhone 15 Pro 128GB... → Apple iPhone 15 Pro Max...
✓ Matched: Samsung Galaxy S24 Ultra... (Category: smartphones)
Progress: 50/150 products checked...
```

### Messaggio Telegram

I prodotti tracciati hanno un marker speciale:
```
⭐📱 Apple iPhone 15 Pro Max
...
⭐ Prodotto Tracciato
```

## FAQ

**Q: Posso tracciare prodotti non tech?**
A: Tecnicamente sì, ma il bot è ottimizzato per prodotti tech. I prodotti devono comunque essere in categorie Amazon tech.

**Q: Quanti ASIN posso tracciare?**
A: Raccomandato 5-15 ASIN. Più ASIN = più tempo per il filtraggio.

**Q: Gli ASIN scadono?**
A: Gli ASIN sono permanenti, ma i prodotti possono diventare non disponibili.

**Q: Posso usare ASIN da Amazon.com?**
A: No, usa solo ASIN da Amazon.it (il bot è configurato per Amazon Italia).

**Q: Come trovo ASIN di prodotti futuri?**
A: Aspetta che il prodotto sia listato su Amazon, poi prendi l'ASIN.

---

**Hai domande?** Controlla i log del bot o apri un issue su GitHub!
