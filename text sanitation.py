def sanitize(text):
    """returns a stripped and lowercased version of the text"""
    new_text=text.strip().lower()
    return new_text

def word_count(text):
    """returns the number of words in the text"""
    count=len(text.split())
    return count

def format_report(count):
    """returns a string with the count of words in the text"""
    return f'The text contains {count} words.'

def main():
    text="   Hello there, John! How are you today?   "
    sanitized_text = sanitize(text)
    count = word_count(sanitized_text)
    report = format_report(count)
    print(report)

if __name__ == '__main__':
    main()