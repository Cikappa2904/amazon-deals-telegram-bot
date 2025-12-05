#!/usr/bin/env python3
"""
Test the ASIN tracking and similarity detection system.
"""

import tracked_asins

# Test data
test_cases = [
    # (base_title, comparison_title, expected_similarity_range)
    ("Apple iPhone 15 Pro Max 256GB", "Apple iPhone 15 Pro 128GB", (60, 90)),
    ("Apple iPhone 15 Pro Max 256GB", "Samsung Galaxy S24 Ultra", (10, 30)),
    ("NVIDIA GeForce RTX 4070 12GB", "NVIDIA GeForce RTX 4060 8GB", (60, 90)),
    ("NVIDIA GeForce RTX 4070 12GB", "AMD Radeon RX 7800 XT", (20, 40)),
    ("MacBook Air M2 13 pollici", "MacBook Pro M3 14 pollici", (50, 80)),
    ("MacBook Air M2 13 pollici", "Dell XPS 13", (10, 30)),
]

print("=" * 80)
print("TESTING ASIN SIMILARITY SYSTEM")
print("=" * 80)
print()

# Test keyword extraction
print("1. TESTING KEYWORD EXTRACTION")
print("-" * 80)
test_title = "Apple iPhone 15 Pro Max 256GB Titanio Blu"
keywords = tracked_asins.extract_keywords_from_title(test_title)
print(f"Title: {test_title}")
print(f"Keywords: {keywords}")
print()

# Test similarity calculation
print("2. TESTING SIMILARITY CALCULATION")
print("-" * 80)
for base_title, comp_title, (min_exp, max_exp) in test_cases:
    score = tracked_asins.calculate_similarity(base_title, comp_title)
    status = "✓" if min_exp <= score <= max_exp else "✗"
    print(f"{status} Score: {score:3d}% | {base_title[:40]:40} vs {comp_title[:40]:40}")
print()

# Test is_similar_to_tracked
print("3. TESTING SIMILARITY DETECTION")
print("-" * 80)

tracked_titles = [
    "Apple iPhone 15 Pro Max 256GB Titanio Blu",
    "NVIDIA GeForce RTX 4070 SUPER 12GB"
]

test_products = [
    "Apple iPhone 15 Pro 128GB Nero",
    "Apple iPhone 14 Pro Max 256GB",
    "Samsung Galaxy S24 Ultra 512GB",
    "NVIDIA GeForce RTX 4060 Ti 8GB",
    "AMD Radeon RX 7800 XT 16GB",
    "MacBook Air M2",
]

print("Tracked products:")
for title in tracked_titles:
    print(f"  📌 {title}")
print()

print(f"Testing with SIMILARITY_THRESHOLD = {tracked_asins.SIMILARITY_THRESHOLD}")
print()

for product in test_products:
    is_similar, best_match, score = tracked_asins.is_similar_to_tracked(
        product, tracked_titles, tracked_asins.SIMILARITY_THRESHOLD
    )
    
    if is_similar:
        print(f"✓ MATCH ({score:2d}%): {product}")
        print(f"           → Similar to: {best_match[:50]}")
    else:
        print(f"✗ SKIP  ({score:2d}%): {product}")
print()

# Test with different thresholds
print("4. TESTING DIFFERENT THRESHOLDS")
print("-" * 80)

test_product = "Apple iPhone 15 Plus 256GB"
tracked_title = "Apple iPhone 15 Pro Max 256GB"

print(f"Product:  {test_product}")
print(f"Tracked:  {tracked_title}")
print()

for threshold in [20, 30, 40, 50, 60]:
    score = tracked_asins.calculate_similarity(test_product, tracked_title)
    is_similar, _, _ = tracked_asins.is_similar_to_tracked(
        test_product, [tracked_title], threshold
    )
    status = "✓ MATCH" if is_similar else "✗ SKIP"
    print(f"Threshold {threshold:2d}%: {status} (Score: {score}%)")
print()

# Configuration recommendations
print("5. CONFIGURATION RECOMMENDATIONS")
print("-" * 80)
print()
print("Based on the tests above:")
print()
print("For STRICT matching (only very similar products):")
print("  SIMILARITY_THRESHOLD = 50-70")
print("  Example: Only iPhone 15 Pro variants, not iPhone 15 or 14")
print()
print("For BALANCED matching (same product line):")
print("  SIMILARITY_THRESHOLD = 30-50  ← RECOMMENDED")
print("  Example: All iPhone 15 models, but not iPhone 14")
print()
print("For FLEXIBLE matching (same category):")
print("  SIMILARITY_THRESHOLD = 10-30")
print("  Example: All iPhones, some other smartphones")
print()

# Current configuration
print("6. CURRENT CONFIGURATION")
print("-" * 80)
print(f"FIND_SIMILAR_PRODUCTS: {tracked_asins.FIND_SIMILAR_PRODUCTS}")
print(f"SIMILARITY_THRESHOLD:  {tracked_asins.SIMILARITY_THRESHOLD}%")
print(f"Tracked ASINs:         {len(tracked_asins.get_all_tracked_asins())}")
print()

if tracked_asins.get_all_tracked_asins():
    print("Your tracked ASINs:")
    for asin, desc in tracked_asins.TRACKED_ASINS.items():
        print(f"  {asin}: {desc}")
else:
    print("⚠️  No ASINs tracked yet!")
    print()
    print("To add ASINs:")
    print("  1. Use: python3 find_asin.py <amazon_url>")
    print("  2. Copy the ASIN into tracked_asins.py")
    print("  3. See GUIDA_ASIN.md for detailed instructions")

print()
print("=" * 80)
print("TEST COMPLETE")
print("=" * 80)
