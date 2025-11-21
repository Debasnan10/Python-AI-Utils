import re

def clean_text(s):
    s = s.lower().strip()
    s = re.sub(r'\s+', ' ', s)
    return s

if __name__ == '__main__':
    print(clean_text('  Hello   WORLD !!  '))
