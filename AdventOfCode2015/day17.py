from functools import lru_cache

posode = [int(input()) for _ in range(20)]

najmanjse_st = 20
nacini_tedaj = 0

# @lru_cache(maxsize=None)
def nacini(kolicina, polozaj, uporabljeni):
    global nacini_tedaj
    global najmanjse_st

    if kolicina == 0:
        if uporabljeni > najmanjse_st:
            pass
        elif uporabljeni == najmanjse_st:
            nacini_tedaj += 1
        else:
            najmanjse_st = uporabljeni
            nacini_tedaj = 1

        return 1
    
    if kolicina < 0 or polozaj == 20:
        return 0

    return nacini(kolicina-posode[polozaj], polozaj+1, uporabljeni+1) + nacini(kolicina, polozaj+1,uporabljeni)


print(nacini(150, 0, 0))
print(nacini_tedaj, najmanjse_st)