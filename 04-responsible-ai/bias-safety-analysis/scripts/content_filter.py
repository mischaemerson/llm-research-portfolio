import re

# Simple offensive word filter
def filter_text(text):
    blacklist = ["offensiveword1", "offensiveword2", "offensiveword3"]
    pattern = re.compile("|".join(blacklist), re.IGNORECASE)
    if pattern.search(text):
        return False
    return True

# Test example
example = "This is a clean sentence."
print(filter_text(example))

