from hugetsu import (
    Metre,
    Ri,
    KiloGram
)

if __name__ == "__main__":
    m = Metre(10)
    r = Ri(20)
    k = KiloGram()
    print(m)
    print(f"{r.value()} [{r.name}]")
    print(r.si())
    print(m + r)
    print(r + m)
    print(k)
    k.value(20)
    print(k)
    try:
        print(m + k)
    except Exception as e:
        print(e)
    print(m.si() + k.si())
