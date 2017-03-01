print('Bite Error Rates for Direct Sequence Spread Spectrum CDMA system')

import numpy
from DSSS import DSSS

n_bits = 10000
# testing the code for one user and 10000 bits with SNR = infinite
EbN0_dB = numpy.inf
users = 1
ber = DSSS(EbN0_dB, users, n_bits)

print("Bit error rate for one user (in the presence of no other user and ", n_bits, "  transmitted bits with ", EbN0_dB," dB SNR) is ", ber)

# testing the code for 6 users and 10000 bits with SNR = 10
EbN0_dB = 10
users = 6
ber = DSSS(EbN0_dB, users, n_bits)
print("Bit error rate for all the six present users (for ", n_bits, "  transmitted bits with ", EbN0_dB," dB SNR) is ", ber, "respectively for each user")

# testing the code for 6 users and 10000 bits with SNR = 10
EbN0_dB = 10
users = 3
ber = DSSS(EbN0_dB, users, n_bits)
print("Bit error rate for all the three users (for ", n_bits, "  transmitted bits with ", EbN0_dB," dB SNR) is ", ber, "respectively for each user")


## Lets plot for infinite SNR, the error rate for first user and the average error
# rate for all users   
import matplotlib.pyplot as plt

users = numpy.array([1, 2, 3, 4, 5, 6])

EbN0_dB = numpy.inf
ber_user1_infsnr = numpy.zeros(len(users))
ber_average_infsnr = numpy.zeros(len(users))

for i in range(len(users)):
    ber = DSSS(EbN0_dB, users[i], n_bits)
    ber_user1_infsnr[i] = ber[0]
    ber_average_infsnr[i] = numpy.mean(ber)

## Lets plot for 10dB SNR, the error rate for first user and the average error
# rate for all users    
EbN0_dB = 10
ber_user1_10dBsnr = numpy.zeros(len(users))
ber_average_10dBsnr = numpy.zeros(len(users))

for i in range(len(users)):
    ber = DSSS(EbN0_dB, users[i], n_bits)
    ber_user1_10dBsnr[i] = ber[0]
    ber_average_10dBsnr[i] = numpy.mean(ber)
    
## Lets plot for 6dB SNR, the error rate for first user and the average error
# rate for all users    
EbN0_dB = 6
ber_user1_6dBsnr = numpy.zeros(len(users))
ber_average_6dBsnr = numpy.zeros(len(users))

for i in range(len(users)):
    ber = DSSS(EbN0_dB, users[i], n_bits)
    ber_user1_6dBsnr[i] = ber[0]
    ber_average_6dBsnr[i] = numpy.mean(ber)
    
# Lets plot this - Bit error rate for User 1 only in the presence of other users
ax = plt.subplot(111)
line1, = plt.plot(users, ber_user1_infsnr, lw=2, label = 'infinite SNR')
line2, = plt.plot(users, ber_user1_10dBsnr, lw=2, label = 'SNR = 10dB')
line3, = plt.plot(users, ber_user1_6dBsnr, lw=2, label = 'SNR = 6dB')
plt.yscale('log')
plt.grid(True)
plt.xlabel('No. of active users')
plt.ylabel('Bit error rate for user 1')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()

print('Bite Error Rates for Direct Sequence Spread Spectrum CDMA system')
print("transmitted bits = ", n_bits)
print('For infinite SNR, the bit error rate for user 1 is ', ber_user1_infsnr, 'in the presence of 0, 1, 2, 3, 4, and 5 other users respectively')
print('For 10dB SNR, the bit error rate for user 1 is ', ber_user1_10dBsnr, 'in the presence of 0, 1, 2, 3, 4, and 5 other users respectively')
print('For 6dB SNR, the bit error rate for user 1 is ', ber_user1_6dBsnr, 'in the presence of 0, 1, 2, 3, 4, and 5 other users respectively')

# Lets plot this - average bit error rate 
ax = plt.subplot(111)
line1, = plt.plot(users, ber_average_infsnr, lw=2, label = 'infinite SNR')
line2, = plt.plot(users, ber_average_10dBsnr, lw=2, label = 'SNR = 10dB')
line3, = plt.plot(users, ber_average_6dBsnr, lw=2, label = 'SNR = 6dB')
plt.yscale('log')
plt.grid(True)
plt.xlabel('No. of active users')
plt.ylabel('Average bit error rate for all users')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()

print('Bite Error Rates for Direct Sequence Spread Spectrum CDMA system')
print("transmitted bits = ", n_bits)
print('For infinite SNR, the average bit error rate is ', ber_average_infsnr, 'in the presence of 1, 2, 3, 4, 5, and 6 users respectively')
print('For 10dB SNR, the average bit error rate is ', ber_average_10dBsnr, 'in the presence of 1, 2, 3, 4, 5, and 6 users respectively')
print('For 6dB SNR, the average bit error rate is ', ber_average_6dBsnr, 'in the presence of 1, 2, 3, 4, 5, and 6 users respectively')

