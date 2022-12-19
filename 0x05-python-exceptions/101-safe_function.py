#!/usr/bin/python3

#import sys


#def safe_function(fct, *args):
#    try:
#        result = fct(*ags)
#        return (result)
#    except:
#        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
#        return (None)

def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
    except Exception as i:
        sys.stderr.write("Exception: {}\n".format(i))
        result = None

    return (result)
