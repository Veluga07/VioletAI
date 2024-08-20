# filter.py

def filter_content(text):
    banned_words = ['badword1', 'badword2']
    if any(word in text for word in banned_words):
        return 'Filtered content'
    return text
