from barter import summarize_article

url=input()
# s, t = getPost(url)
s, t = summarize_article(url, max_length=1024)

print(t)
print()
print(s)