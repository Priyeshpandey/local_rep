T = int(input())

for _ in range(T):
    X, Y, K, N = map(int, input().split())
    notebook = []
    for i in range(N):
        p, c = map(int, input().split())
        notebook.append((p, c))
    pages_required = X - Y
    book_found = False
    for book in notebook:
        pages, cost = book
        if pages >= pages_required and cost <= K:
            print('LuckyChef')
            book_found = True
            break
    if not book_found:
        print('UnluckyChef')
