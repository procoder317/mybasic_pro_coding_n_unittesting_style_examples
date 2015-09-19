'''
Created on August 15, 2015
@author: Kumar Sabyasachi Padhi

####One can have 5 basic assumptions in accord to Question, input & output####

1. all the sections must be seperated by commas for ex: "Raju, 3rd Block, BTL
layout, Bangalore - 456098"

2. below 3 and 4 assumptions are according to input and output results as
observed one has to be really strict with parsing string matching form like only
" Bangalore - 456098" and " PIN - 456098" form are considered to find the
postal code  and its case sensitive.

3. Its standard that postal code can only be with the place section like :
"Bangalore - 456098" and it distinctly one always something like
" Bangalore - 456098" only non other section should
contain it. As well as total length is considered as 21 chars

4. or it can only be with the pin section  like : "PIN - 567789" same assumption
for " PIN - 456098" as above. As well as total length is considered as 15 chars

5. assume it can be more restrictive but one can have a extra check where the
postal code is always 6 digits long as it is always for Banglore location.


########################################################################
approach to the problem

1. it would be more wiser to start parsing the entire string from right to left
if in every case the postal code always lies towards right end in the address
string in a single line

2. we use dictionary data structure to store the postal code  and corresponding
number of delivered mail counts because of its advantage of allowing us to store
only unique postal codes and its values as well as provide access in O(1) time .
Note: dictionary in here is same as hash tables

3. After it we track down the top three ranks in O(n) time

4. Finally we can say the overall running time is roughly O(n) in worst case
'''
import mimetypes as mtype


def write_outfile(ranks, outputfile_name="topthree.txt"):
    """
    (list, out file name(*.txt)) -> writes to out file(*.txt)
    takes the top 3 postal code list and writes the output to a text file

    its also assuming here its strictly that the ranks is a list of tuples
    (string, int)
    and the string in it is only digit types and int is always >= 0
    so I am not checking it in tests
    """
    try:
        #count variable represents position and ranks
        count = 0
        opfile = None
        assert(isinstance(ranks, list))
        assert(mtype.guess_type(outputfile_name)[0] == 'text/plain')
        opfile = open(outputfile_name, 'w')
        template = '{0:<3}{1:<11}{2:<8}{3:23}{4:1}'
        opfile.write(template.format('#', 'PINCOD', 'RANK',
                                     'No of Parcels Delivered', '\n'))
        for pin_code, no_delivery in ranks:
            count += 1
            opfile.write(template.format(str(count)+".", pin_code, str(count),
                                         str(no_delivery), '\n'))
    except IOError:
        return "IO failed"
    except AssertionError:
        return "type mismatch"
    finally:
        if opfile:
            opfile.close()


def ranksetter(ranklist, no_delivery, postalcode):
    """
    (list, int, string(only digits string))
    make sure that the ranklist is sorted while input if not code fails
    updates the max three ranks only and returns the ranklist.
    It works similar to insertion sort
    also assuming here its strictly that the ranklist is a list of tuples
    (string, int)
    and the string in it is only digit types and int is always >= 0
    so I am not checking it in tests
    example usage:
    ranksetter([('456098', 3), ('567789', 2), ('560089', 1)], 5, "234561")
    """
    try:
        assert(isinstance(ranklist, list))
        assert(isinstance(no_delivery, int))
        assert(isinstance(postalcode, str))
        assert(postalcode.isdigit())
        assert(len(ranklist) == 3)
        assert(len(postalcode) == 6)
        assert(no_delivery >= 0)
        check_list = [val[1] for val in ranklist]
        exp_list = check_list[:]
        exp_list.sort(reverse=True)
        assert(check_list == exp_list)
        count = 0
        found = False
        while count < 3:
            assert(isinstance(ranklist[count], tuple))
            assert(isinstance(ranklist[count][0], str))
            assert(isinstance(ranklist[count][1], int))
            assert(ranklist[count][1] >= 0)
            if ranklist[count][1] <= no_delivery:
                ranklist.insert(count, (postalcode, no_delivery))
                found = True
                break
            count += 1
        if found:
            ranklist.pop()
        return ranklist
    except AssertionError:
        return


def matcher_and_extractor(constraint_string, input_sub_string,
                          constraint_length):
    """
    (string, string, int) -> string
    takes 3 arguments 2 strings and a constraint length and checks for the match
    and extracts  and returns the postal_code
    example usage:
    matcher_and_extractor(" Bangalore - ", " Bangalore - 456098", 13)
    matcher_and_extractor(" PIN - ", " PIN - 456098", 7)
    """
    postal_code = None
    try:
        #parameters type checking
        assert(isinstance(constraint_string, str))
        assert(isinstance(input_sub_string, str))
        assert(isinstance(constraint_length, int))
        assert(constraint_length == 7 or constraint_length == 13)
        #Todo Note I am not sure of this length constraint I have a doubt
        #assuming 21 and 15 as lengths and length of the postal code is 6 digits
        assert(len(input_sub_string) == constraint_length + 8)
        #string matching test
        assert(constraint_string[:constraint_length]
               == input_sub_string[:constraint_length])
        #digit start next constraint just immediately after constraint match
        assert(input_sub_string[constraint_length].isdigit())
        # is the postal code what we think is digits only and note always we
        #consider it only 6 digit length
        postal_code = input_sub_string[constraint_length: constraint_length+6]
        assert(postal_code.isdigit())
        return postal_code
    except AssertionError:
        return


def toppostalcodes(input_filename):
    """
    (test_file name:"*.txt") -> (write out in a tabular format to a ".txt" file)
    and return None value
    takes the address list file as input and returns the top three rank holders
    info in a list in decreasing order
    """
    try:
        assert(mtype.guess_type(input_filename)[0] == 'text/plain')
        postalcodedict = {}
        ranker = [("NONE", 0), ("NONE", 0), ("NONE", 0)]
        for line in open(input_filename, 'r').readlines():
            addresslist = line.split(',')
            while addresslist:
                parsestring = addresslist.pop()
                codestr = None
                codestra = matcher_and_extractor(" Bangalore - ",
                                                 parsestring, 13)
                if codestra:
                    codestr = codestra
                else:
                    codestrb = matcher_and_extractor(" PIN - ", parsestring, 7)
                    if codestrb:
                        codestr = codestrb
                if codestr:
                    if postalcodedict.get(codestr) is None:
                        postalcodedict[codestr] = 1
                    else:
                        postalcodedict[codestr] += 1
                    break
        for p_code in postalcodedict:
            ranker = ranksetter(ranker, postalcodedict[p_code], p_code)
            assert(ranker is not None)
        print ranker
        return write_outfile(ranker)
    except AssertionError:
        return
    except IOError:
        return


if __name__ == '__main__':
    toppostalcodes('Input.txt')
