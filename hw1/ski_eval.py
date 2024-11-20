import src.ski as ski


##########
# PART 1 #
##########
# TASK: Implement the below function `eval`.

def eval(e: ski.Expr) -> ski.Expr:
    # BEGIN_YOUR_CODE
    if isinstance(e, ski.App):
        e1 = eval(e.e1)
        e2 = eval(e.e2)
        if isinstance(e1, ski.I):
            return eval(e2)
        elif isinstance(e1, ski.App):
            e11 = eval(e1.e1)
            e12 = eval(e1.e2)
            if isinstance(e11, ski.K):
                return eval(e12)
            elif isinstance(e11, ski.App):
                e111 = eval(e11.e1)
                e112 = eval(e11.e2)
                if isinstance(e111, ski.S):
                    return eval(ski.App(eval(ski.App(e112, e2)), eval(ski.App(e12, e2))))
    return e
    # END_YOUR_CODE
