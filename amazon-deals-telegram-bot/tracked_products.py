"""
Configuration file for tracking specific product types.
Add product IDs or keywords to filter deals to specific tech categories.
"""

# Tracked product categories with keywords
# The system will only show deals that match these keywords
TRACKED_CATEGORIES = {
    "smartphones": {
        "keywords": [
            "iphone", "samsung galaxy", "smartphone", "cellulare", "telefono",
            "pixel", "xiaomi", "oneplus", "oppo", "realme", "huawei", "motorola",
            "android", "ios", "5g", "smartphone"
        ],
        "enabled": True
    },
    "laptops": {
        "keywords": [
            "laptop", "notebook", "portatile", "macbook", "chromebook",
            "ultrabook", "thinkpad", "dell xps", "asus", "hp pavilion",
            "lenovo", "acer", "msi", "razer", "gaming laptop"
        ],
        "enabled": True
    },
    "graphics_cards": {
        "keywords": [
            "scheda video", "gpu", "nvidia", "geforce", "rtx", "gtx",
            "radeon", "amd", "graphics card", "scheda grafica", "rx "
        ],
        "enabled": True
    },
    "processors": {
        "keywords": [
            "processore", "cpu", "intel", "amd", "ryzen", "core i",
            "threadripper", "processor", "i3", "i5", "i7", "i9"
        ],
        "enabled": True
    },
    "monitors": {
        "keywords": [
            "monitor", "schermo", "display", "gaming monitor", "4k",
            "ultrawide", "curved", "hz", "ips", "oled", "qled"
        ],
        "enabled": True
    },
    "tablets": {
        "keywords": [
            "tablet", "ipad", "galaxy tab", "surface", "kindle fire"
        ],
        "enabled": True
    },
    "smartwatches": {
        "keywords": [
            "smartwatch", "apple watch", "galaxy watch", "fitbit",
            "garmin", "orologio smart", "wearable"
        ],
        "enabled": True
    },
    "headphones": {
        "keywords": [
            "cuffie", "auricolari", "headphones", "earbuds", "airpods",
            "wireless", "bluetooth", "noise cancelling", "sony wh",
            "bose", "sennheiser"
        ],
        "enabled": True
    },
    "consoles": {
        "keywords": [
            "playstation", "ps5", "ps4", "xbox", "nintendo switch",
            "console", "gaming console", "steam deck"
        ],
        "enabled": True
    },
    "ssd_storage": {
        "keywords": [
            "ssd", "nvme", "hard disk", "storage", "memoria",
            "samsung evo", "crucial", "western digital", "hdd"
        ],
        "enabled": True
    },
    "ram": {
        "keywords": [
            "ram", "memoria ram", "ddr4", "ddr5", "corsair",
            "kingston", "g.skill", "memory"
        ],
        "enabled": True
    },
    "motherboards": {
        "keywords": [
            "scheda madre", "motherboard", "mainboard", "asus rog",
            "gigabyte", "msi", "asrock"
        ],
        "enabled": True
    },
    "cameras": {
        "keywords": [
            "fotocamera", "camera", "mirrorless", "dslr", "canon",
            "nikon", "sony alpha", "gopro", "action cam"
        ],
        "enabled": True
    },
    "mice_keyboards": {
        "keywords": [
            "mouse", "tastiera", "keyboard", "mechanical keyboard",
            "gaming mouse", "logitech", "razer", "corsair"
        ],
        "enabled": True
    }
}

# Amazon department IDs for tech products
TECH_DEPARTMENT_IDS = [
    "460158031",  # Informatica (PC components, graphics cards, etc.)
    "412609031",  # Elettronica
    "412606031"   # Videogiochi
]


def get_all_keywords():
    """Get all keywords from enabled categories."""
    keywords = []
    for category, config in TRACKED_CATEGORIES.items():
        if config["enabled"]:
            keywords.extend(config["keywords"])
    return [k.lower() for k in keywords]


def is_tech_product(title):
    """
    Check if a product title matches any tracked tech category.
    
    Args:
        title (str): Product title to check
        
    Returns:
        bool: True if title contains any tracked keywords
    """
    if not title:
        return False
    
    title_lower = title.lower()
    keywords = get_all_keywords()
    
    return any(keyword in title_lower for keyword in keywords)


def get_matching_category(title):
    """
    Get the category that matches the product title.
    
    Args:
        title (str): Product title to check
        
    Returns:
        str or None: Category name if match found, None otherwise
    """
    if not title:
        return None
    
    title_lower = title.lower()
    
    for category, config in TRACKED_CATEGORIES.items():
        if config["enabled"]:
            for keyword in config["keywords"]:
                if keyword.lower() in title_lower:
                    return category
    
    return None
