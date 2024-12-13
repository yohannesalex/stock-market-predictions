# Function to categorize articles
def categorize_article(headline):
    if any(keyword in headline.lower() for keyword in ['earnings', 'eps', 'announces']):
        return 'Financial Performance'
    elif any(keyword in headline.lower() for keyword in ['market', 'stocks', 'shares']):
        return 'Market Trends'
    elif any(keyword in headline.lower() for keyword in ['update', 'top', 'reports']):
        return 'General Updates'
    else:
        return 'Other'