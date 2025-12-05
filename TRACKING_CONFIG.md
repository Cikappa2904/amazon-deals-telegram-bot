# Product Tracking Configuration

This bot now filters deals to only show tech products that match specific categories you're interested in.

## How It Works

1. **Amazon Department Filtering**: The bot scrapes only from tech-related Amazon departments (Informatica, Elettronica, Videogiochi)

2. **Keyword Filtering**: After scraping, products are filtered based on keywords in their titles to match specific tech categories

3. **Category Tracking**: You can enable/disable specific product categories

## Configuration

Edit `tracked_products.py` to customize what products you want to track.

### Enable/Disable Categories

Set `"enabled": True` or `"enabled": False` for each category:

```python
"smartphones": {
    "keywords": [...],
    "enabled": True  # Change to False to disable this category
}
```

### Add Custom Keywords

Add keywords to any category to improve matching:

```python
"smartphones": {
    "keywords": [
        "iphone", "samsung galaxy", "smartphone",
        "your-custom-keyword-here"  # Add your own keywords
    ],
    "enabled": True
}
```

### Available Categories

- **smartphones**: iPhones, Samsung Galaxy, etc.
- **laptops**: Notebooks, MacBooks, gaming laptops
- **graphics_cards**: NVIDIA, AMD graphics cards
- **processors**: Intel, AMD CPUs
- **monitors**: Gaming monitors, 4K displays
- **tablets**: iPads, Android tablets
- **smartwatches**: Apple Watch, Galaxy Watch, etc.
- **headphones**: Wireless headphones, earbuds
- **consoles**: PlayStation, Xbox, Nintendo Switch
- **ssd_storage**: SSDs, hard drives
- **ram**: Memory modules
- **motherboards**: PC motherboards
- **cameras**: Digital cameras, action cams
- **mice_keyboards**: Gaming peripherals

## Tips

- **More keywords = more matches**: Add variations and common misspellings
- **Be specific**: Use brand names and model numbers for better filtering
- **Monitor logs**: Check console output to see which products are matched
- **Adjust percentOff_min**: In `amazon_page_analyser.py` line 161, you can change the minimum discount percentage

## Example

To track only iPhones and MacBooks:

1. Disable all categories except `smartphones` and `laptops`
2. Update keywords to be more specific:

```python
"smartphones": {
    "keywords": ["iphone"],
    "enabled": True
},
"laptops": {
    "keywords": ["macbook"],
    "enabled": True
}
```

## Performance

The filtering process checks each product's title against your keywords. This happens:
- When scraping deals (every 2 hours by default)
- Uses multithreading for faster processing
- Progress is logged to console

You'll see output like:
```
Found 150 unique products. Filtering for tracked categories...
✓ Matched: Apple iPhone 15 Pro... (Category: smartphones)
✓ Matched: NVIDIA GeForce RTX 4070... (Category: graphics_cards)
Progress: 50/150 products checked...
Filtered to 23 products matching tracked categories
```
