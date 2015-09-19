'''
Created on July 9, 2015
@author: Kumar Sabyasachi Padhi
'''
import mimetypes as mtype

def take(input_list=None, count=None):
    """
    (list, int) -> list
    Takes a list "input_list" and a number "count" 
    and returns the first n elements as list
    """
    try:
        assert isinstance(input_list, list)
        assert isinstance(count, int)
        assert(count > 0)
        assert(len(input_list) >= count)
        for value in input_list:
            assert isinstance(value, int)
        return input_list[:count]
    except:
        return []


def flatten(nested_list=None):
    """
    (list) -> list
    Takes a list of a lists 
    and returns all elements in the nested list as a  single list
    """
    try:
        assert isinstance(nested_list, list)
        final_list = []
        for inlist in nested_list:
            assert isinstance(inlist, list)
            for element in inlist:
                assert isinstance(element, int)
                final_list.append(element)
        return final_list
    except:
        return []


def indexer(input_filename=None):
    """
    (text file) -> dict(map of string, index list)
    read a text file, split them into words (seperated by spaces, tabs and newlines) 
    returning a map of word to line numbers
    """
    try:
        if mtype.guess_type(input_filename)[0] != 'text/plain':
            return {}
        ofile = open(input_filename,"r")
        count = 0
        mapdict = {}
        for inp_string in ofile.readlines():
            count += 1
            word = ''
            for char in inp_string:
                if char in (" ", "\t", "\n"):
                    indexer_helper(word, mapdict, count)
                    word = ''
                else:
                    word += char
            indexer_helper(word, mapdict, count)
        ofile.close()
        return mapdict
    except IOError:
        return {}
    except:
        return {}


def indexer_helper(word, mapdict, count):
    """
    (str, dict, int)
    Its a helper function for indexer
    takes the word map and count as input checks the word and inserts word into 
    map
    """
    if word != '':
        if mapdict.get(word, "not present") == "not present":
            mapdict[word] = [count]
        else:
            mapdict[word].append(count)


def compress(sorted_list=None):
    """
    (list) -> tuple in list
    converts a sorted list to a list of pairs,
    where each pair contains an element from the list and its count
    """
    try:
        assert isinstance(sorted_list, list)
        result = []
        curr_val = None
        count = 0
        for value in sorted_list:
            assert isinstance(value, int)
            if curr_val is None:
                curr_val = value
                count = 1
            elif curr_val != value:
                assert (curr_val < value)
                result.append((curr_val, count))
                curr_val = value
                count = 1
            else:
                count += 1
        result.append((curr_val, count))
        return result
    except:
        return []

if __name__ == '__main__':
    print take([2, 3, 6, 1, 5], 2)
    print flatten([[2, 3, 4], [5, 4], [23, 44, 56, 78]])
    print compress([-1, 0, 0, 0, 10, 23, 23, 14, 44, 44, 44, 54])
    print indexer("test.txt")
