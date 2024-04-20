G = {i+j*1j: c for j,r in enumerate(open('input.txt'))
               for i,c in enumerate(r.strip()) if c != '#'}

E = {p: [p+d for d in (1,-1,1j,-1j) if p+d in G] for p in G}


def collapse(p, n, d=1):
    while len(E[n]) == 2:
        p, n, d = n, [*{*E[n]}-{p}][0], d+1
    return n, d

E = {p: [collapse(p, n) for n in E[p]] for p in G}


def search(node, dist, best, stop=[*G][-1], seen=set()):
    if node == stop: return dist
    if node in seen: return best

    seen.add(node)
    best = max(search(n, d+dist, best) for n,d in E[node])
    seen.remove(node)

    return best

print(search([*G][0], 0, 0))
