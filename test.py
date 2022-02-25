#!/usr/bin/python3
def h_index(case):
    pappers = int(input("Insert number of pappers: "))
    references = map(int, input("Insert references each papper: ").split())
    
    h = 0
    r = ""
    citations = [0] * (pappers + 1)
    new_citations = 0
    for a in references:
        if a > h:
            try:
                citations[a] += 1
            except IndexError:
                citations[pappers] += 1
            if new_citations == citations[h]:
                h += 1
                new_citations = 0
            else:
                new_citations += 1
        r += ' ' + str(h)
    print(f"Case #{case}:{r}", flush=True)

    

cases = int(input("Insert test number: "))
for case in range(cases):
    h_index(case)
    