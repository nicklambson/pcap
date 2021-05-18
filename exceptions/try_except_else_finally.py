def f(x):
    try:
        x = x / x
    except:
        print("a", end='')
    else:
        print("b", end='')
    finally:
        print("c", end='')

f(1)
f(0)

# bcac

# else executes when there is no exception
# finally always executes