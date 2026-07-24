num = int(input())
for i in range(1, num + 1):
    comment = input()
    if comment.isspace() or len(comment) == 0:
        print(i, ': COMMENT SHOULD BE DELETED', sep='')
    else:
        print(i, ': ', comment, sep='')
        