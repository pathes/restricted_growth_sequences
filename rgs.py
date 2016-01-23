#!/usr/bin/env python

import sys

def next_rgs(seq, n, k):
    """Gets next restricted-growth sequence with values in {0..k}"""
    # b[i] = max(seq[i - 1], b[0], ..., b[i - 1]) = max(seq[i - 1], b[i - 1])
    # All restricted growth sequences start with 0
    b = [0]
    result = seq[:]
    for i in range(1, n):
        b.append(max(seq[i - 1], b[i - 1]))
    # Find the earliest index when previous and next sequence are diverging
    for j in range(n - 1, 0, -1):
        if seq[j] + 1 > k:
            continue
        if seq[j] > b[j]:
            continue
        break
    # Create components of new result
    # prefix - maximal common prefix of original and new sequence
    prefix = seq[:j]
    # incremented - the value at j-th place that was incremented
    incremented = seq[j] + 1
    # suffix_length - how many nonzero numbers should we put at the end
    #                 of new sequence to make it restricted-growing
    #                 and to have all numbers 0..(k-1) in it.
    suffix_length = k - max(b[j], incremented)
    zeroes = [0] * (n - j - suffix_length - 1)
    suffix = list(range(k - suffix_length + 1, k + 1))
    # Construct new sequence
    result = prefix + [incremented] + zeroes + suffix
    return result


def restricted_growth_sequences(n):
    """Generates all restricted-growth sequences of size n"""
    # k - biggest value that should be contained in subsequence
    for k in range(n):
        # initially seq = [0, 0, ... 0, 1, 2, ..., k-1, k]
        seq = [0] * (n - k) + list(range(1, k+1))
        # final = [0, 1, 2, ..., k-1, k, ..., k]
        final = list(range(k)) + [k] * (n - k)
        while seq != final:
            yield seq
            seq = next_rgs(seq, n, k)
        yield final


def main():
    if len(sys.argv) < 2:
        print('Usage: ./rgs.py [n]')
        return
    for rgs in restricted_growth_sequences(int(sys.argv[1])):
        print(rgs)


if __name__ == '__main__':
    main()
