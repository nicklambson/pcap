'''
try:
    raise Exception
except:
    print("c")
except BaseException:
    print("a")
except Exception:
    print("b")
'''

# error: default except: must be last

try:
    raise Exception
except BaseException:
    print("a")
except Exception:
    print("b")
except:
    print("c")

# a

try:
    raise Exception
except BaseException:
    print("a", end='')
else:
    print("b", end='')
finally:
    print("c")

# ac
