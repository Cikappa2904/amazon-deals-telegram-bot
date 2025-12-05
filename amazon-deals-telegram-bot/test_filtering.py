#!/usr/bin/env python3
"""
Test script to verify the keyword filtering system works correctly.
"""

import tracked_products

# Test product titles
test_products = [
    "Apple iPhone 15 Pro 128GB Blu",
    "Spazzolino elettrico Oral-B",
    "NVIDIA GeForce RTX 4070 12GB",
    "Coperta in pile morbida",
    "Samsung Galaxy S23 Ultra",
    "Set pentole antiaderenti",
    "MacBook Air M2 13 pollici",
    "AMD Ryzen 9 7950X Processore",
    "Asciugamani da bagno",
    "PlayStation 5 Console",
    "LG Monitor Gaming 27 pollici 144Hz",
    "Cuscino memory foam",
    "Apple Watch Series 9",
    "Tappeto per soggiorno",
    "Corsair Vengeance DDR5 32GB RAM"
]

print("=" * 70)
print("TESTING PRODUCT FILTERING")
print("=" * 70)

tech_count = 0
non_tech_count = 0

for title in test_products:
    is_tech = tracked_products.is_tech_product(title)
    category = tracked_products.get_matching_category(title)
    
    if is_tech:
        tech_count += 1
        print(f"✓ MATCH: {title}")
        print(f"  Category: {category}")
    else:
        non_tech_count += 1
        print(f"✗ SKIP: {title}")
        print(f"  (Not a tech product)")
    print()

print("=" * 70)
print(f"RESULTS: {tech_count} tech products, {non_tech_count} non-tech products filtered out")
print("=" * 70)

# Show enabled categories
print("\nENABLED CATEGORIES:")
for category, config in tracked_products.TRACKED_CATEGORIES.items():
    if config["enabled"]:
        print(f"  • {category.replace('_', ' ').title()} ({len(config['keywords'])} keywords)")

print(f"\nTotal keywords: {len(tracked_products.get_all_keywords())}")
