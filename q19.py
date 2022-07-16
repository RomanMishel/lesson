def q18(a, b):
    try:
       c = a / b
       c = int(c)
       if c != 0:
           print(c)

    except Exception as e:
        print(e)


q18(10,0)
