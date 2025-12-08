"""
Configuration file for tracking specific product types.
Add product IDs or keywords to filter deals to specific tech categories.
"""

# Tracked product categories with keywords
# The system will only show deals that match these keywords
TRACKED_CATEGORIES = {
    "smartphones": {
        "keywords": [
            # Brands
            "iphone", "samsung", "galaxy", "pixel", "xiaomi", "redmi", "poco",
            "oneplus", "oppo", "realme", "huawei", "honor", "motorola", "nokia",
            "vivo", "asus", "sony xperia", "lg", "zte", "tcl", "nothing phone",
            # General terms
            "smartphone", "cellulare", "telefono", "phone", "mobile",
            "android", "ios", "5g", "4g", "dual sim", "unlocked",
        ],
        "enabled": True
    },
    "laptops": {
        "keywords": [
            # Brands
            "macbook", "thinkpad", "dell", "hp", "lenovo", "asus", "acer",
            "msi", "razer", "alienware", "surface", "huawei matebook",
            "lg gram", "gigabyte", "framework", "system76",
            # Types
            "laptop", "notebook", "portatile", "ultrabook", "chromebook",
            "gaming laptop", "business laptop", "workstation",
            # General
            "computer portatile", "pc portatile", "laptop computer",
        ],
        "enabled": True
    },
    "graphics_cards": {
        "keywords": [
            # NVIDIA
            "nvidia", "geforce", "rtx", "gtx", "rtx 5090", "rtx 5080", "rtx 5070", "rtx 5060",
            "rtx 4090", "rtx 4080", "rtx 4070", "rtx 4060", "rtx 3090", "rtx 3080", "rtx 3070", "rtx 3060",
            "gtx 1660", "gtx 1650", "gtx 1080", "gtx 1070",
            # AMD
            "amd", "radeon", "rx 9000", "rx 8000", "rx 7900", "rx 7800", "rx 7700", "rx 7600",
            "rx 6900", "rx 6800", "rx 6700", "rx 6600", "rx 6500",
            # General
            "scheda video", "scheda grafica", "gpu", "graphics card", "video card",
            "vga", "graphic",
        ],
        "enabled": True
    },
    "processors": {
        "keywords": [
            # Intel
            "intel", "core i9", "core i7", "core i5", "core i3",
            "i9-14900", "i9-13900", "i7-14700", "i7-13700", "i5-14600", "i5-13600",
            "xeon", "pentium", "celeron",
            # AMD
            "amd", "ryzen", "ryzen 9", "ryzen 7", "ryzen 5", "ryzen 3",
            "9950x", "9900x", "7950x", "7900x", "7800x3d", "7700x", "7600x",
            "5950x", "5900x", "5800x3d", "5700x", "5600x",
            "threadripper", "epyc",
            # General
            "processore", "cpu", "processor", "central processing unit",
        ],
        "enabled": True
    },
    "monitors": {
        "keywords": [
            # Brands
            "lg", "samsung", "dell", "asus", "acer", "benq", "msi", "gigabyte",
            "hp", "viewsonic", "aoc", "philips", "lenovo", "razer",
            # Types
            "monitor", "schermo", "display", "gaming monitor", "professional monitor",
            # Specs
            "4k", "2k", "1440p", "1080p", "ultrawide", "curved", "flat",
            "144hz", "165hz", "240hz", "360hz", "ips", "va", "tn", "oled", "qled", "hdr",
            "freesync", "g-sync", "adaptive sync",
        ],
        "enabled": True
    },
    "tablets": {
        "keywords": [
            "tablet", "ipad", "galaxy tab", "surface", "kindle", "fire tablet",
            "android tablet", "windows tablet", "huawei", "lenovo tab",
            "xiaomi pad", "oppo pad", "realme pad",
        ],
        "enabled": True
    },
    "smartwatches": {
        "keywords": [
            "smartwatch", "apple watch", "galaxy watch", "fitbit", "garmin",
            "orologio smart", "wearable", "fitness tracker", "smart band",
            "huawei watch", "xiaomi watch", "amazfit", "fossil", "ticwatch",
        ],
        "enabled": True
    },
    "headphones": {
        "keywords": [
            # Brands
            "sony", "bose", "sennheiser", "jbl", "beats", "apple", "samsung",
            "anker", "soundcore", "jabra", "hyperx", "razer", "steelseries",
            "corsair", "logitech", "audio-technica", "beyerdynamic", "akg",
            # Types
            "cuffie", "auricolari", "headphones", "earbuds", "earphones",
            "airpods", "headset", "gaming headset",
            # Features
            "wireless", "bluetooth", "noise cancelling", "anc", "true wireless",
            "tws", "over-ear", "on-ear", "in-ear",
        ],
        "enabled": True
    },
    "consoles": {
        "keywords": [
            "playstation", "ps5", "ps4", "ps5 pro", "xbox", "xbox series",
            "nintendo switch", "switch", "switch 2", "steam deck", "rog ally",
            "console", "gaming console", "portable console",
        ],
        "enabled": True
    },
    "ssd_storage": {
        "keywords": [
            # Types
            "ssd", "nvme", "m.2", "sata", "hard disk", "hdd", "storage",
            "external drive", "portable ssd", "usb drive", "pendrive",
            # Brands
            "samsung", "crucial", "western digital", "wd", "kingston", "seagate",
            "sandisk", "corsair", "pny", "adata", "teamgroup", "sabrent",
            # Specs
            "1tb", "2tb", "4tb", "500gb", "256gb", "memoria", "storage",
        ],
        "enabled": True
    },
    "ram": {
        "keywords": [
            "ram", "memoria ram", "memory", "ddr5", "ddr4", "ddr3",
            "corsair", "kingston", "g.skill", "crucial", "teamgroup",
            "hyperx", "gskill", "vengeance", "trident", "ripjaws",
            "8gb", "16gb", "32gb", "64gb", "128gb",
        ],
        "enabled": True
    },
    "motherboards": {
        "keywords": [
            "scheda madre", "motherboard", "mainboard", "mobo",
            "asus", "msi", "gigabyte", "asrock", "evga", "biostar",
            "rog", "tuf", "prime", "strix", "aorus", "tomahawk",
            "b650", "x670", "z790", "b760", "h610",
        ],
        "enabled": True
    },
    "cameras": {
        "keywords": [
            "fotocamera", "camera", "mirrorless", "dslr", "reflex",
            "canon", "nikon", "sony", "fujifilm", "panasonic", "olympus",
            "gopro", "action cam", "dji", "insta360",
            "webcam", "web camera",
        ],
        "enabled": True
    },
    "mice_keyboards": {
        "keywords": [
            # Mouse
            "mouse", "gaming mouse", "wireless mouse", "ergonomic mouse",
            "logitech", "razer", "corsair", "steelseries", "glorious",
            "finalmouse", "zowie", "roccat", "hyperx",
            # Keyboard
            "tastiera", "keyboard", "gaming keyboard", "mechanical keyboard",
            "wireless keyboard", "keychron", "ducky", "varmilo", "gmmk",
            "cherry mx", "gateron", "kailh", "switches",
        ],
        "enabled": True
    },
    "pc_cases": {
        "keywords": [
            "case", "cabinet", "chassis", "tower", "case pc",
            "nzxt", "corsair", "lian li", "fractal", "phanteks",
            "cooler master", "thermaltake", "be quiet", "silverstone",
            "mid tower", "full tower", "mini itx", "micro atx", "atx",
        ],
        "enabled": True
    },
    "cooling": {
        "keywords": [
            "cooler", "ventola", "fan", "radiatore", "cooling",
            "liquid cooling", "aio", "air cooler", "water cooling",
            "noctua", "arctic", "be quiet", "cooler master", "deepcool",
            "corsair", "nzxt", "ekwb", "alphacool",
        ],
        "enabled": True
    },
    "power_supply": {
        "keywords": [
            "alimentatore", "power supply", "psu", "modular psu",
            "corsair", "seasonic", "evga", "thermaltake", "cooler master",
            "be quiet", "silverstone", "antec",
            "80+ gold", "80+ platinum", "80+ titanium", "80+ bronze",
            "650w", "750w", "850w", "1000w",
        ],
        "enabled": True
    },
    "accessories": {
        "keywords": [
            "usb", "cable", "cavo", "adapter", "adattatore", "hub",
            "usb-c", "thunderbolt", "hdmi", "displayport",
            "charger", "caricatore", "power bank", "battery",
            "stand", "supporto", "dock", "docking station",
            "mousepad", "tappetino", "desk mat",
        ],
        "enabled": True
    },
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
