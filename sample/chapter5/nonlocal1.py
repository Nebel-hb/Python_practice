def dog():
    def cat():
        nonlocal pet
        pet = 'cat'

    pet = 'dog'
    cat()
    print(pet)


dog()
