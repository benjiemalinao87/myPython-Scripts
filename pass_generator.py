

import os,random,string

rPassword=""
length = 9
chars = string.ascii_letters + "!@#$%^&*()"
suffix = string.digits
random.seed = (os.urandom(1024))
rPassword = ''.join(random.choice(chars) for i in range(5)) + '@' + ''.join(random.choice(suffix) for j in range(3))

print ("Your RandomPassword ===>>> %s " % rPassword)