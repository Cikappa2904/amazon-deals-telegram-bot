#!/usr/bin/env python3
"""
Helper script to find ASINs from Amazon URLs or product IDs.
This makes it easy to add products to your tracked list.

Usage:
    python3 find_asin.py <amazon_url_or_asin>
    
Examples:
    python3 find_asin.py "https://www.amazon.it/dp/B0CSTJP37Y"
    python3 find_asin.py B0CSTJP37Y
"""

import sys
import re
import amazon_page_analyser as apa


def extract_asin_from_url(url_or_asin):
    """Extract ASIN from Amazon URL or return as-is if already an ASIN."""
    # If it's already an ASIN format (10 alphanumeric characters)
    if re.match(r'^[A-Z0-9]{10}$', url_or_asin):
        return url_or_asin
    
    # Try to extract from URL
    asin = apa.extract_product_id(url_or_asin)
    if asin:
        return asin
    
    return None


def get_product_details(asin):
    """Get product details for an ASIN."""
    try:
        product_info = apa.get_product_info(asin)
        if product_info:
            return product_info
        else:
            return None
    except Exception as e:
        print(f"Error fetching product info: {e}")
        return None


def format_for_config(asin, title):
    """Format ASIN entry for tracked_asins.py config file."""
    # Truncate title if too long
    short_title = title[:50] + "..." if len(title) > 50 else title
    return f'    "{asin}": "{short_title}",'


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 find_asin.py <amazon_url_or_asin>")
        print("\nExamples:")
        print("  python3 find_asin.py 'https://www.amazon.it/dp/B0CSTJP37Y'")
        print("  python3 find_asin.py B0CSTJP37Y")
        sys.exit(1)
    
    input_value = sys.argv[1]
    
    print("=" * 70)
    print("AMAZON ASIN FINDER")
    print("=" * 70)
    print()
    
    # Extract ASIN
    asin = extract_asin_from_url(input_value)
    
    if not asin:
        print(f"❌ Could not extract ASIN from: {input_value}")
        print("\nMake sure you're using:")
        print("  - A valid Amazon URL with /dp/ in it")
        print("  - Or a 10-character ASIN (like B0CSTJP37Y)")
        sys.exit(1)
    
    print(f"✓ Found ASIN: {asin}")
    print()
    
    # Get product details
    print("Fetching product details...")
    product_info = get_product_details(asin)
    
    if not product_info:
        print(f"❌ Could not fetch product details for ASIN: {asin}")
        print("\nThe ASIN might be:")
        print("  - Invalid or expired")
        print("  - Not available on Amazon.it")
        print("  - Behind a paywall or subscription")
        print("\nYou can still add it manually to tracked_asins.py:")
        print(f'    "{asin}": "Product description",')
        sys.exit(1)
    
    # Display product info
    print()
    print("=" * 70)
    print("PRODUCT DETAILS")
    print("=" * 70)
    print()
    print(f"Title:    {product_info['title']}")
    print(f"ASIN:     {product_info['product_id']}")
    print(f"Price:    {product_info['new_price']}")
    if 'old_price' in product_info and product_info['old_price'] != product_info['new_price']:
        print(f"Was:      {product_info['old_price']}")
        print(f"Discount: {product_info['discount_rate']}")
    print(f"URL:      {apa.url_from_id(asin)}")
    print()
    
    # Generate config entry
    config_entry = format_for_config(asin, product_info['title'])
    
    print("=" * 70)
    print("ADD TO TRACKED_ASINS.PY")
    print("=" * 70)
    print()
    print("Copy this line into the TRACKED_ASINS dictionary in tracked_asins.py:")
    print()
    print(config_entry)
    print()
    print("Example:")
    print()
    print("TRACKED_ASINS = {")
    print(config_entry)
    print("    # Add more ASINs here...")
    print("}")
    print()
    
    # Extract keywords for reference
    from tracked_asins import extract_keywords_from_title
    keywords = extract_keywords_from_title(product_info['title'])
    if keywords:
        print("=" * 70)
        print("EXTRACTED KEYWORDS (for reference)")
        print("=" * 70)
        print()
        print("These keywords will be used to find similar products:")
        print(", ".join(keywords[:15]))  # Show first 15 keywords
        print()


if __name__ == "__main__":
    main()
