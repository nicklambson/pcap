class Ex(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg + msg)
        self.args = (msg,)

try:
    print("attempting to raise exception")
    raise Ex("ex")
    print("still in the try block")
except Ex as e:
    print("running first Exception")
    print(e)
except Exception as e:
    print("running second Exception")
    print(e)

# ex

# but if self.args = msg
# then prints ('e', 'x')
# because it will interpret the msg as a multi-element tuple
# grabbing each character of the string

# this would print exex
# only if self.args is not reset to the singleton

# An exception can be initialized with a message.
# That message can be overridden with self.args.