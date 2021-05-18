class Ex(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg + msg)
        #self.args = (msg,)

try:
    raise Ex('ex')
except Ex as e:
    print(e)
except Exception as e:
    print(e)

# Only the first matching exception branch is raised.
# In this case, Ex matches. So the first branch is executed but the second branch is not.
# The message was initialized to double itself,
# but then the arguments were reset to just a single message.

# Only one 'ex' will be printed.