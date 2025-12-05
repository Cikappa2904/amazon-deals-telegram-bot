"""
ESEMPIO: Come tracciare iPhone 15 e schede video NVIDIA

Questo file mostra un esempio completo di configurazione.
Copia questi valori in tracked_asins.py per iniziare.
"""

# ============================================================================
# ESEMPIO 1: Tracciare iPhone 15 e trovare modelli simili
# ============================================================================

TRACKED_ASINS_ESEMPIO_1 = {
    "B0CHX3TW6N": "Apple iPhone 15 128GB",
    "B0CSTJP37Y": "Apple iPhone 15 Pro Max 256GB",
}

FIND_SIMILAR_PRODUCTS = True
SIMILARITY_THRESHOLD = 40

# Cosa troverà:
# ⭐ iPhone 15 128GB (tracciato)
# ⭐ iPhone 15 Pro Max 256GB (tracciato)
# 🎯 iPhone 15 Plus (simile)
# 🎯 iPhone 15 Pro (simile)
# 🎯 iPhone 14 Pro Max (simile, ma meno priorità)


# ============================================================================
# ESEMPIO 2: Tracciare setup gaming (GPU + CPU)
# ============================================================================

TRACKED_ASINS_ESEMPIO_2 = {
    # Schede video
    "B0D6Q8KYCW": "NVIDIA GeForce RTX 4070 12GB",
    "B0CM5KJLM5": "NVIDIA GeForce RTX 4060 Ti 16GB",
    
    # Processori
    "B0BSKWZ3FN": "AMD Ryzen 7 7800X3D",
    "B0BCDLFSJ8": "AMD Ryzen 9 7950X",
}

FIND_SIMILAR_PRODUCTS = True
SIMILARITY_THRESHOLD = 35

# Cosa troverà:
# ⭐ RTX 4070, RTX 4060 Ti (tracciati)
# ⭐ Ryzen 7 7800X3D, Ryzen 9 7950X (tracciati)
# 🎯 RTX 4080, RTX 4070 Super (simili)
# 🎯 Altri processori Ryzen 7000 (simili)


# ============================================================================
# ESEMPIO 3: Solo ASIN specifici (no prodotti simili)
# ============================================================================

TRACKED_ASINS_ESEMPIO_3 = {
    "B0CHX3TW6N": "Apple iPhone 15 128GB Nero",
    "B0CHX1W1XY": "Apple iPhone 15 256GB Nero",
    "B0CHX2F3SG": "Apple iPhone 15 512GB Nero",
}

FIND_SIMILAR_PRODUCTS = False  # Solo questi 3 modelli esatti
SIMILARITY_THRESHOLD = 30  # Ignorato quando FIND_SIMILAR_PRODUCTS = False

# Cosa troverà:
# ⭐ Solo i 3 iPhone 15 specifici (esattamente quelli)
# ✗ Niente iPhone 15 Plus, Pro, o altri colori


# ============================================================================
# ESEMPIO 4: Tracciare laptop Apple
# ============================================================================

TRACKED_ASINS_ESEMPIO_4 = {
    "B09SX4YZFG": "MacBook Air M2 13 pollici",
    "B0CM5R6PTW": "MacBook Pro M3 14 pollici",
}

FIND_SIMILAR_PRODUCTS = True
SIMILARITY_THRESHOLD = 45  # Più rigido per evitare altri brand

# Cosa troverà:
# ⭐ MacBook Air M2 13" (tracciato)
# ⭐ MacBook Pro M3 14" (tracciato)
# 🎯 MacBook Pro M3 16" (simile)
# 🎯 MacBook Air M3 (simile)
# ✗ Dell XPS, Lenovo ThinkPad (troppo diversi)


# ============================================================================
# ESEMPIO 5: Mix completo - smartphone, laptop, GPU
# ============================================================================

TRACKED_ASINS_ESEMPIO_5 = {
    # Smartphone
    "B0CSTJP37Y": "iPhone 15 Pro Max",
    "B0CWV17BK2": "Samsung Galaxy S24 Ultra",
    
    # Laptop
    "B09SX4YZFG": "MacBook Air M2",
    
    # GPU
    "B0D6Q8KYCW": "NVIDIA RTX 4070",
}

FIND_SIMILAR_PRODUCTS = True
SIMILARITY_THRESHOLD = 35

# Cosa troverà:
# ⭐ I 4 prodotti tracciati
# 🎯 Altri iPhone 15, Galaxy S24
# 🎯 Altri MacBook
# 🎯 Altre RTX 4000 series
# ✓ Altri prodotti tech dalle categorie abilitate


# ============================================================================
# COME USARE QUESTI ESEMPI
# ============================================================================

# 1. Scegli l'esempio che ti interessa
# 2. Apri tracked_asins.py
# 3. Copia il dizionario TRACKED_ASINS e le impostazioni
# 4. Sostituisci i valori esistenti
# 5. Salva il file
# 6. Esegui il bot!

# Per verificare che funzioni:
# python3 test_asin_tracking.py


# ============================================================================
# TROVARE NUOVI ASIN
# ============================================================================

# Usa lo script helper:
# python3 find_asin.py "https://www.amazon.it/dp/ASIN_QUI"

# Oppure manualmente:
# 1. Vai su amazon.it
# 2. Trova il prodotto
# 3. L'URL sarà tipo: amazon.it/dp/B0CSTJP37Y
# 4. Copia B0CSTJP37Y (l'ASIN)


# ============================================================================
# REGOLAZIONE SIMILARITY_THRESHOLD
# ============================================================================

# THRESHOLD = 60-70: Molto rigido
#   - Solo varianti dello stesso modello esatto
#   - Es: iPhone 15 128GB, iPhone 15 256GB (stesso modello, diversa memoria)

# THRESHOLD = 40-50: Bilanciato ✓ RACCOMANDATO
#   - Stessa linea di prodotti
#   - Es: iPhone 15, iPhone 15 Plus, iPhone 15 Pro

# THRESHOLD = 30-40: Flessibile
#   - Stesso brand e categoria
#   - Es: Tutti gli iPhone 15 e alcuni iPhone 14

# THRESHOLD = 20-30: Molto flessibile
#   - Stessa categoria generale
#   - Es: Tutti gli iPhone, alcuni Samsung

# THRESHOLD = 10-20: Troppo ampio (non raccomandato)
#   - Include troppi prodotti dissimili


# ============================================================================
# COMBINARE CON CATEGORIE
# ============================================================================

# Puoi usare sia ASIN che categorie insieme!

# In tracked_asins.py:
TRACKED_ASINS = {
    "B0CSTJP37Y": "iPhone 15 Pro Max",
}
FIND_SIMILAR_PRODUCTS = True

# In tracked_products.py:
# Lascia "smartphones" abilitato per trovare anche altri smartphone

# Priorità bot:
# 1. iPhone 15 Pro Max (ASIN tracciato) ⭐
# 2. Altri iPhone 15 (simili) 🎯
# 3. Altri smartphone (categoria) ✓


# ============================================================================
# TROUBLESHOOTING
# ============================================================================

# Problema: Nessun prodotto viene trovato
# Soluzione: Abbassa SIMILARITY_THRESHOLD a 25

# Problema: Troppi prodotti dissimili
# Soluzione: Aumenta SIMILARITY_THRESHOLD a 45

# Problema: Voglio SOLO gli ASIN esatti
# Soluzione: FIND_SIMILAR_PRODUCTS = False

# Problema: ASIN non valido
# Soluzione: Usa find_asin.py per verificare
