import re

def mad_libs_generator():
    # Mad Libs template with placeholders
    template = "Once upon a time, in a {adjective1} {noun1}, there lived a {adjective2} {noun2}. {adverb}, they {verb} {adjective3} {noun3}."
    
    # Prompt user for words
    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    adjective2 = input("Enter another adjective: ")
    noun2 = input("Enter another noun: ")
    adverb = input("Enter an adverb: ")
    verb = input("Enter a verb: ")
    adjective3 = input("Enter one more adjective: ")
    noun3 = input("Enter one more noun: ")
    
    # Replace placeholders with user input
    mad_libs_story = template.format(adjective1=adjective1, noun1=noun1, adjective2=adjective2, noun2=noun2,
                                     adverb=adverb, verb=verb, adjective3=adjective3, noun3=noun3)
    
    # Print the generated Mad Libs story
    print("\nYour Mad Libs Story:\n")
    print(mad_libs_story)

# Call the function to generate Mad Libs
mad_libs_generator()
