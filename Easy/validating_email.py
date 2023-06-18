import re
import email.utils
n = int(input())
for _ in range(n):
    parser = email.utils.parseaddr(input())
    email_pattern = r"^[a-z][\w\-.]*@[a-z]+\.[a-z]{1,3}$"
    compare = re.search(email_pattern, parser[1], re.I)
    if compare:
        print(email.utils.formataddr(parser))
    