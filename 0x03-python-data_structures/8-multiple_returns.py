#!/usr/bin/python3

def multiple_returns(sentence):
    len_sentence = len(sentence)
    if len_sentence < 1:
        sentence[0] = "None",
    return (len_sentence, sentence[0])
        
