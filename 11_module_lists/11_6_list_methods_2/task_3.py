number, comments = int(input()[1:]), []
for _ in range(number):
    comments.append(input())

for comment in comments:
    if '#' in comment:
        comment = comment[:comment.find('#')]
    comment = comment.rstrip()
    print(comment)
