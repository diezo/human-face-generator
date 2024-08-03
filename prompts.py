def ask():
    print("Please answer these prompts...")

    # Gender: List Options
    print("""
    (M) Male
    (F) Female
    
    (R) Random
    """)

    # Gender: Take Input
    gender: str = input("Gender: ").lower()

    # Age: List Options
    print("""
    (1) 12-18
    (2) 19-25
    (3) 26-35
    (4) 35-50
    (5) 50+

    (R) Random
    """)

    # Age: Take Input
    age: str = input("Age: ").lower()

    # Ethnicity: List Options
    print("""
    (A) Asian
    (B) Black
    (W) White
    (I) Indian
    (M) Middle Eastern
    (L) Latino Hispanic

    (R) Random
    """)

    # Ethnicity: Take Input
    ethnicity: str = input("Ethnicity: ").lower()

    # Return Values
    return gender, age, ethnicity
