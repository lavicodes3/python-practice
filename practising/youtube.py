# converting urls into shorter and readable form ; practising regex

import re
def main():
    print(parse(input("HTML: ")))

def parse(s):
    if match := re.search(
        r'<iframe.*src="https?://(?:www\.)?youtube\.com/embed/([\w-]+)".*</iframe>',
        s,
        re.IGNORECASE,
    ):
        return f"https://youtu.be/{match.group(1)}"
    return None

if __name__ == "__main__":
    main()
