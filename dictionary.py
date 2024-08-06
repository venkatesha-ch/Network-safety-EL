password = "106PETERSON1"
passfile='names.txt'

def hit(password,Pass):
    try:
        Pass = str(Pass.split('\n')[0])
        if(password != Pass):
            raise Exception('trying')
        else:
          print('Password Found: '+Pass)
          return True

    except:
        print('Trying: '+Pass)
        return False

        

f=open(passfile, 'r')
for i in f:
    if(hit(password,i)):
        f.close()
        break