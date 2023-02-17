#!/bin/python3i

from collections import deque
import copy


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''

    with open(dictionary_file, 'r') as f:
        test = f.read()
    dictionary = test.splitlines()

    if start_word == end_word:
        return [start_word]

    stack = []
    stack.append(start_word)
    queue = deque()
    queue.append(stack)

    while len(queue) != 0:
        cur_stack = queue.popleft()
        dict_copy = dictionary.copy()
        for word in dict_copy:
            if _adjacent(word, cur_stack[-1]):
                if word == end_word:
                    cur_stack.append(word)
                    return cur_stack
                stack_copy = copy.copy(cur_stack)
                stack_copy.append(word)
                queue.append(stack_copy)
                dictionary = [x for x in dictionary if (x != word)]
    return None


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''

    if ladder == []:
        return False
    for i in range(len(ladder) - 1):
        if _adjacent(ladder[i], ladder[i + 1]):
            pass
        else:
            return False
    return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    if len(word1) != len(word2):
        return False
    checker = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            checker += 1
    return checker == 1
