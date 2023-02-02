#!/bin/python3
# -*- encoding: utf-8 -*-

def solve(weigh):
    i=2
    j = 1
    while i < 13:

        heavier = weigh([j], [i])
        if heavier == 'left':
            if i+1<13:
                heavier = weigh([j+1], [i+1])
                if heavier == 'right':
                    return(i, '-')
            elif i+1>=13:
                heavier = weigh([j], [1])
                if heavier == 'none':
                    return(i, '-')
            return (j, '+')

        elif heavier == 'right':
            if i+1<13:
                heavier = weigh([j+1],[i+1])
                if heavier == 'none':
                    return (j, '-')
            elif i+1>=13:
                heavier = weigh([i], [1])
                if heavier == 'none':
                    return(j, '-')

            return (i, '+')

        i += 2
        j += 2


    else:
        return (12, '-')