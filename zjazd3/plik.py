with open("ścieżka") as f:
    print(f.read())



with open("ścieżka", w, encoding='utf-8') as f:
    f.write("text")