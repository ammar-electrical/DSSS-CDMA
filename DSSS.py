def DSSS (EbN0_dB, users, n_bits):
    # input variables
    # users are number of users
    # n_bits are number of transmitted bits for each user
    # EbN0_dB is SNR in dB
    
    users = int(users)
    n_bits = int(n_bits)
    EbN0 = 10**(EbN0_dB/10)     # SNR conversion from dB to W/W
    
    import numpy
    import math
    numpy.set_printoptions(threshold=numpy.inf)
    
    # codes selected by me are as follows (direct sequence)
    # error rates also depend on the selected codes, the selected codes in this 
    # simulation are sub-optimal
    if users <= 6: # select following codes if number of users are less than 6
        code = numpy.array([[1, 0, 1, 1, 0, 0, 1, 0, 1, 0], 
                            [1, 1, 0, 1, 1, 0, 0, 1, 0, 0],
                            [0, 1, 1, 0, 0, 1, 0, 0, 1, 1], 
                            [0, 0, 1, 1, 1, 0, 0, 1, 0, 1],
                            [1, 0, 1, 0, 0, 1, 1, 0, 1, 0],
                            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]]) * 2 - 1
    else: # select following codes if the number of users are greater than 6
        code = numpy.random.randint(2, size=(users, users * 2))
    size_code = code.shape
    
    # bits are coded as follows
    bits = numpy.random.randint(2, size=(users, n_bits)) * 2 - 1
    
    # The transmitted signal is xt being transmitted after modulation
    xt = numpy.empty([users, size_code[1]*n_bits])
    for i in range(users):
        xt[i,:] = numpy.kron(bits[i,:], code[i,:])
        
    # the signals will be modulated now and passed through the channel. 
    # After demodulation, the received signals are as follows
    mu = 0; sigma = math.sqrt( 0.5*size_code[1]/EbN0 )
    noise = numpy.random.normal(mu, sigma, size = size_code[1]*n_bits)
    
    # coded signals are recieved as follows 
    x = numpy.sum(xt, axis=0) + noise
    
    y = numpy.empty_like(bits)
    for i in range(users):
        for k in range(n_bits):
            y[i,k] = numpy.sum( x[k*size_code[1]:k*size_code[1]+size_code[1]] * code[i] )
            if y[i,k] < 0:
                y[i,k] = -1
            else:
                y[i,k] = 1
    
    # coversion of bits from -1,1 to 0,1
    bits = (bits + 1)/2
    y = (y + 1)/2
    
    # calculation of Bit Error Rate for each receiver 
    ber = numpy.sum(numpy.absolute(bits - y) , axis = 1)/n_bits
    
    # return the bit error rate for each receiver
    return ber
    
