def mad_libs():
    large_object = input("Give me a large object: ")
    large_objects_plural = input("Give me large objects (plural): ")
    adjective = input("Give me an adjective: ")
    body_part = input("Give me a body part: ")
    restaurant = input("Give me a restaurant: ")
    food_1 = input("Give me a food: ")
    food_2 = input("Give me another food: ")
    
    story = f"""
    I’ve had a very {adjective} day.
    This morning, I dropped a box of {large_objects_plural} on my {body_part}.
    Then, at lunch, I went to {restaurant} for their delicious {food_1},
    But the waiter brought me {food_2}, which I was not hungry for.
    Finally, on my way home, I was cut off by a van with a large {large_object} strapped to the roof.
    """
    
    print(story)

mad_libs()