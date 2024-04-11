# promptable gramschmidt process

class GS:
    # initialize with vector space, field, inner product
    # each arg given as strings, parse to set variables in the class:
    def __init__(self, vector_space, field, inner_product):
        self.vector_space = vector_space
        self.field = field
        self.inner_product = inner_product
        self.vlist = []
        self.vzero = 0 * self.vlist[0]
        self.norms_squared = []
        self.ret = [self.vlist[0]]
    
    def parse_input():

