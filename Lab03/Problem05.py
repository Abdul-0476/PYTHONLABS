def should_ali_watch():
    ali = {"Inception", "Life of Pi", "The Dark Knight", "A Separation"}
    you = {"The Dark Knight", "12 Angry Men", "Inception", "LOR:TT"}
    mohammed = {"LOR:TT", "Seven Samurai", "Inception", "The Matrix"}

    return len(ali & you) > len(ali & mohammed)

print("Ali should watch Oppenheimer:", should_ali_watch())
