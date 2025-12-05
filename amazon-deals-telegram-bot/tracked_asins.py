"""
Configuration file for tracking specific ASINs (Amazon product IDs).
Add ASINs of products you want to track specifically.

The bot will:
1. Always include these ASINs if they have deals
2. Extract keywords from these products to find similar items
3. Prioritize these products when sending deals
"""

# Add your specific ASINs here
# Format: "ASIN": "Description (optional, for your reference)"
TRACKED_ASINS = {
    # Example ASINs - Replace with your own
    # "B0CSTJP37Y": "iPhone 15 Pro Max",
    # "B0CWV17BK2": "Samsung Galaxy S24 Ultra",
    # "B0D6Q8KYCW": "NVIDIA RTX 4070",
    # "B09SX4YZFG": "MacBook Air M2",
}

# If True, the bot will extract keywords from tracked ASINs and find similar products
# If False, only the exact ASINs will be tracked
FIND_SIMILAR_PRODUCTS = True

# Minimum similarity score (0-100) for products to be considered similar
# Higher = more strict, Lower = more variety
SIMILARITY_THRESHOLD = 30


def is_tracked_asin(asin):
    """Check if an ASIN is in the tracked list."""
    return asin in TRACKED_ASINS


def get_all_tracked_asins():
    """Get list of all tracked ASINs."""
    return list(TRACKED_ASINS.keys())


def extract_keywords_from_title(title):
    """
    Extract meaningful keywords from a product title.
    
    Args:
        title (str): Product title
        
    Returns:
        list: List of extracted keywords
    """
    if not title:
        return []
    
    # Common words to ignore (Italian and English)
    stop_words = {
        'di', 'da', 'in', 'con', 'per', 'su', 'a', 'e', 'il', 'la', 'i', 'le', 'lo', 'gli',
        'un', 'una', 'uno', 'del', 'della', 'dei', 'delle', 'al', 'alla', 'ai', 'alle',
        'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with',
        'colore', 'color', 'nuovo', 'new', 'originale', 'original', 'ufficiale', 'official'
    }
    
    # Split title into words and filter
    words = title.lower().replace(',', ' ').replace('(', ' ').replace(')', ' ').replace('[', ' ').replace(']', ' ').split()
    
    # Keep words that are:
    # - Not stop words
    # - At least 3 characters
    # - Not just numbers
    keywords = [
        word for word in words 
        if word not in stop_words 
        and len(word) >= 3 
        and not word.isdigit()
    ]
    
    return keywords


def calculate_similarity(title1, title2):
    """
    Calculate similarity between two product titles based on common keywords.
    
    Args:
        title1 (str): First product title
        title2 (str): Second product title
        
    Returns:
        int: Similarity score (0-100)
    """
    if not title1 or not title2:
        return 0
    
    keywords1 = set(extract_keywords_from_title(title1))
    keywords2 = set(extract_keywords_from_title(title2))
    
    if not keywords1 or not keywords2:
        return 0
    
    # Calculate Jaccard similarity
    intersection = len(keywords1.intersection(keywords2))
    union = len(keywords1.union(keywords2))
    
    if union == 0:
        return 0
    
    similarity = (intersection / union) * 100
    return int(similarity)


def is_similar_to_tracked(title, tracked_titles, threshold=SIMILARITY_THRESHOLD):
    """
    Check if a product is similar to any tracked products.
    
    Args:
        title (str): Product title to check
        tracked_titles (list): List of tracked product titles
        threshold (int): Minimum similarity score
        
    Returns:
        tuple: (is_similar: bool, best_match: str, score: int)
    """
    if not title or not tracked_titles:
        return False, None, 0
    
    best_score = 0
    best_match = None
    
    for tracked_title in tracked_titles:
        score = calculate_similarity(title, tracked_title)
        if score > best_score:
            best_score = score
            best_match = tracked_title
    
    is_similar = best_score >= threshold
    return is_similar, best_match, best_score
