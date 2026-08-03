text = input().lower().split()
count_articles = text.count('a') + text.count('an') + text.count('the')
print(f"Общее количество артиклей: {count_articles}")
