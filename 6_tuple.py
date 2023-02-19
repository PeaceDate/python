# Tuple - immutable list of objects (cannot be changed) - faster than list
# Tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.
# Tuples are used to write-protect data and are usually faster than list as it cannot change dynamically. It is defined within parentheses () where items are separated by commas. Tuples are immutable, and usually, they contain a heterogeneous sequence of elements that are accessed via unpacking (or indexing) or by attribute in case of namedtuples. Tuples can be thought of as immutable lists. Tuples are also used for cases where an immutable sequence of homogeneous data is needed (such as allowing storage in a set or dict instance).

if __name__ == '__main__':
    trash_can = ('Andrii', True, 0)

    print(trash_can) # ('Andrii', True, 0)
    print(trash_can[0]) # Andrii - first element
    print(trash_can[:2]) # ('Andrii', True) - first two elements


    # Unpacking - assign values to multiple variables

    name, is_awesome, count = trash_can

    print(name) # Andrii
    print(is_awesome) # True
    print(count) # 0

    # Unpacking with * - assign values to multiple variables

    name, *rest = trash_can

    print(name) # Andrii
    print(rest) # [True, 0]

    # Concatenation of tuples
    new_tuple = (21, 60)

    print(trash_can + new_tuple) # ('Andrii', True, 0, 21, 60)
