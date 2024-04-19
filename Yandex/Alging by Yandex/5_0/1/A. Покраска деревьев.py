P, V = map(int, input().split())
Q, M = map(int, input().split())

if P > Q:
    P, V, Q, M = Q, M, P, V

if P + V >= Q - M:
    print(max(P + V + 1, Q + M + 1) - min(P - V, Q - M))
else:
    print(V + V + 1 + M + M + 1)
