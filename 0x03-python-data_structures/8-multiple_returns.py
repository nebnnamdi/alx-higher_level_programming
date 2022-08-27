#!/usr/bin/python3
def multiple_returns(sentence):
    if (sentence == ''):
        t_res = (len(sentence), None)
    else:
        t_res = (len(sentence), sentence[0])
        return (t_res)
