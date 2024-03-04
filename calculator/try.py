class Calculator:
    def __init__(self):
        self.actions = {
            'add': lambda a,b: a+b, 
            'sub': lambda a,b: a-b,
            'mul': lambda a,b: a*b,
            'div': lambda a,b: a/b
        }


    def calculating(self, action , a, b):
        if action in self.actions:
            return self.actions[action](a,b)

        else:
            return None


action1= Calculator()
result = action1.calculating('mul', 10,2)
print(result)

    