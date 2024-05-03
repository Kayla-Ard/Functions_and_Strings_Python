# Product Review Analysis
# Task 1: Keyword Highlighter
# Write a program that searches through a series of product reviews for keywords such as "good", "excellent", "bad", "poor", and "average".
# Print out each review with the keywords in uppercase so they stand out.

python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!","I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]
keywords = ["good", "excellent", "bad", "poor", "average"]
reviews = " ".join(python_reviews)

for word in keywords:
    reviews = reviews.replace(word, word.upper())
    reviews = reviews.replace(word.title(), word.upper())
print(reviews)    



# Product Review Analysis
# Task 2: Sentiment Tally
# Develop a function that tallies the number of positive and negative words in each review.
# Use a predefined list of positive and negative words to check against. The function should return the count of positive and negative words for each review.

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!","I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]

def pos_and_neg_count():
    number_of_positive = 0
    number_of_negative = 0
    for sentence in python_reviews:
        for word in sentence.split():
            word = word.replace(".", "")
            if word.lower() in positive_words:
                number_of_positive += 1

    print(f" The number of positives are {number_of_positive}.")
    
    for sentence in python_reviews:
        for word in sentence.split():
            word = word.replace(".", "")
            if word.lower() in negative_words:
                number_of_negative += 1
                
    print(f" The number of negatives are {number_of_negative}.")
    
pos_and_neg_count()



# Task 3: Review Summary
# Implement a script that takes the first 30 characters of a review and appends "…" to create a summary.
# Ensure that the summary does not cut off in the middle of a word.

python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!","I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]
reviews = " ".join(python_reviews)
new_reviews = reviews.replace("'", "")
sliced_review = new_reviews[:31] + "..."
print(sliced_review)




# User Input Data Processor
# Task 1: Input Length Validator Write a script that checks the length of the user's first name and last name.
# Both should be at least 2 characters long. If not, print an error message.

print("Let's get you info!")
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
while True:
    
    if len(first_name) >= 2:
        print("First name recorded successfully!")
        if len(last_name) >= 2:
            print("Last name recorded successfully!")
            break
        else:
            print("Last name must be at least 2 characters long!")
            last_name = input("Please enter your last name: ")
    else:
        print("First name must be at least 2 characters long!")
        first_name = input("Please enter your first name: ")
        
print(f"Your name has been recorded as {first_name} {last_name}! Thank you!")