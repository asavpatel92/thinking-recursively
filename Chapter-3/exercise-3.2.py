#===============================================================================
# this function computes no of canonballs from the height of the layer. without using the explicit mathematical formula which is N(N + 1) (2N + 1) / 6 
#===============================================================================

def canonballCount(layers):
    if (layers == 1):
        return 1
    else:
        return (layers * layers) + canonballCount(layers-1)

if __name__ == '__main__':
    layers = int(raw_input("Enter the number of layers:"))
    print canonballCount(layers)