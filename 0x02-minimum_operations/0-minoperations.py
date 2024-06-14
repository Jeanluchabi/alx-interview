#!/usr/bin/python3
'''The minimum operations coding challenge.
'''


def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n H characters.
    '''
    if not isinstance(n, int):
        return 0
    ops_counting = 0
    clipb = 0
    done = 1
    # print('H', end='')
    while done < n:
        if clipb == 0:
            clipb = done
            done += clipb
            ops_count += 2
        elif n - done > 0 and (n - done) % done == 0:
            clipb = done
            done += clipb
            ops_count += 2
        elif clipb > 0:
            # paste
            done += clipb
            ops_counting += 1
    return ops_count

