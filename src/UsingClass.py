
import random
import time

# Class that generates password 3 times


class PwGenerator:
    password = ''

    def generator(self, length_of_password, chars):
        p = 0
        if p in range(3):
            for pwd in range(length_of_password):
                self.password += random.choice(chars)
            print(self.password)
        else:
            print("Password reset limit exceeded. Kindly wait till the counter hit the zero")

    def stopwatch(self, seconds):
        start = time.time()
        time.clock()
        elapsed = 0
        while elapsed < seconds:
            elapsed = time.time() - start
            print("Generating password in seconds"
                  "%2d" % (elapsed))
            time.sleep(1)



chars = 'abcdefgh!@%^*&ijklmn1234567opqrstuvwxyzABHCDEFGHIJKLMNO0912345678!%@^$' # string to be used for pwd creation
length_of_password = 10 #length of pwd string

pw = PwGenerator()
print("Kindly generate a password before the time expires")
pw.stopwatch(5)
pw.generator(length_of_password, chars)


