def negrito(f):
    def envelope():
        return "<b>" + f() + "</b>"
    return envelope

def italico(f):
    def envelope():
        return "<i>" + f() + "</i>"
    return envelope

@negrito
@italico
def alô():
    return 'Alô mundo'

print (alô())
