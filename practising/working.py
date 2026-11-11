import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match=re.search(r"^([0-9](?:1[0-2])?):?([0-6][0-9])? ([A|P]M) to ([0-9](?:1[0-2])?):?([0-6][0-9])? ([A|P]M)",s)
    if not match.group(2)==None:
        if int(match.group(2))>=60 or int(match.group(5))>=60:
            raise ValueError
    elif match.group(6)=="PM":
        return f"{match.group(1)}:{match.group(2)} to {int(match.group(4))+12}:{match.group(5)}"
    elif match.group(6)=="AM":
        return f"{match.group(1)}:{match.group(2)} to {match.group(4)}:{match.group(5)}"


...


if __name__ == "__main__":
    main()
