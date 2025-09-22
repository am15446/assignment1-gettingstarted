### welcome_assignment_answers
### Input - All nine questions given in the assignment.
### Output - The right answer for the specific question.

def welcome_assignment_answers(question):
    #Students do not have to follow the skeleton for this assignment.
    #Another way to implement is using a "case" statements similar to C.
    if question.casefold() == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?".casefold():
        answer = "pcap"
    elif question.casefold() == "Are encoding and encryption the same? - Yes/No".casefold():
        answer = "No"
    elif question.casefold() == "Is it possible to decrypt a message without a key? - Yes/No".casefold():
        answer = "No"
    elif question.casefold() == "is it possible to decode a message without a key? - yes/no".casefold():
        answer = "Yes"
    elif question.casefold() == "Is a hashed message supposed to be un-hashed? - Yes/No".casefold():
        answer = "No"
    elif question.casefold() == "What is the SHA256 hashing value of your NYU email and use the answer in your code - ".casefold():
        answer = "76b20c54e4ea5ac0c549e87900c856cf6b4d7ee828fab10a6e82642dedae320e"
    elif question.casefold() == "Is MD5 a secured hashing algorithm? - Yes/No".casefold():
        answer = "No"
    elif question.casefold() == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number".casefold():
        answer = 5
    elif question.casefold() == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number".casefold():
        answer = 3
    ### you should understand why this else case should be included
    ### what happens if there is a typo in one of the questions?
    ### maybe put something here to flag an issue and catch errors
    else:
        raise Exception("This is not a valid question, maybe there is a typo")
    return(answer)
# Complete all the questions.


if __name__ == "__main__":
    #use this space to debug and verify that the program works
    debug_question = "are encoding and encryption the same? - Yes/No"
    print(welcome_assignment_answers(debug_question))


