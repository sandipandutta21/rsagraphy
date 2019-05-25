import random
from tkinter.filedialog import askopenfilename
from tkinter.ttk import *
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

key_window = Tk()
key_window.geometry ( '355x200' )
key_window.title ('Key Generation')

entry_p = Entry(key_window, width=5)
entry_q = Entry(key_window, width=5)

def primeerror():
	messagebox.showinfo('Error Occured!', 'Please Enter a Prime Number(e.g. 13, 17)')

def finish():
	messagebox.showinfo('Done!', 'Finished and Saved as efile.pem, dfile.pem and nfile.pem')

def coprime(a, b):
    while b != 0:
        a, b = b, a % b
    return a
    

def modInverse(a, m) : 

    a = a % m

    for x in range(1, m) : 

        if ((a * x) % m == 1) : 

            return x
    
def modinv(a, m):
	d = modInverse(a, m)
	return d	
	
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    n = p * q

    
    phi = (p-1) * (q-1)

    e = random.randrange(1, phi)
    print(e)

    g = coprime(e, phi)
  
    while g != 1:
        e = random.randrange(1, phi)
        g = coprime(e, phi)

    #Use Extended Euclid's Algorithm to generate the private key
    d = modinv(e, phi)
    publicKey = (e, n)
    privateKey = (d, n)

   #saving the values of n, d and e for further use	
    efile = open('efile.pem', 'w')
    efile.write('%d' %(int(e)))
    efile.close()
   
    dfile = open('dfile.pem', 'w')
    dfile.write('%d' %(int(d)))
    dfile.close()
   
    nfile = open('nfile.pem', 'w')
    nfile.write('%d' % (int(n)))
    nfile.close()

    print('Public key:', publicKey)
    print('Private key:', privateKey)
    return (publicKey, privateKey)
    #Return public and private keypair
    #Public key is (e, n) and private key is (d, n)
    #return ((e, n), (d, n))


def main():

    try:
        p = int(entry_p.get())
        q = int(entry_q.get())
        #print("Generating your public/private keypairs now . . .")
        public, private = generate_keypair(p, q)
        finish()
    
    except AttributeError:
        primeerroe()
    except ValueError:
        primeerror()

def quit():
	exit()

btn_key = Button( key_window, text = "Generate Key" , command = main)
btn_key.place( x=50, y=120 )
btn_exit = Button(key_window, text='Go Back', command = quit)
btn_exit.place( x=200, y=120 )
lbl_p = Label(key_window, text='Enter "p":')
lbl_p.place(x= 20,y=60)
lbl_q = Label(key_window, text='Enter "q":')
lbl_q.place(x= 180,y=60)
entry_p.place( x=100, y=60 )
entry_q.place(x=250, y=60)

key_window.mainloop()
