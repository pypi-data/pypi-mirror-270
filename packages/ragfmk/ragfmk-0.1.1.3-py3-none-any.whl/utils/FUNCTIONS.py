import utils.CONST as C

def getCLIArgurment(arg, name):
    try:
        return arg[name]
    except:
        return C.NULLSTRING