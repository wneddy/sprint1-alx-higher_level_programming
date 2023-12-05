#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    store = dir(hidden_4)
    for entity in store:
        if (entity[:2] == "__"):
            continue
        print(entity)
