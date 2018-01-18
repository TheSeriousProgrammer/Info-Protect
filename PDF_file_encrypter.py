import datetime
import pickle
class info_protect :
    def __init__(self,path,mode):
        self.path=path
        self.mode=mode
        self.base_str='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '
        self.password=str(input("Enter your password:"))
        self.key=[]
        for i in range(len(self.password)):
            x=self.base_str.find(self.password[i])
            self.key.append(x)            
        self.base_list=bytearray(range(256))*2
        self.in_pixels=bytearray(open(self.path,'rb').read())
        self.out_pixels=bytearray()
        self.venue=''
        self.date,self.time='',''

    def encrypt(self):
        for i in range(len(self.in_pixels)):
            self.out_pixels.append(self.base_list[self.in_pixels[i]+self.key[i%len(self.key)]])
        open(self.path[:len(self.path)-4]+'_output.pdf','wb').write(self.out_pixels)
        
    def decrypt(self):
        for i in range(len(self.in_pixels)):
            self.out_pixels.append(self.base_list[self.in_pixels[i]-self.key[i%len(self.key)]])
        open(self.path[:len(self.path)-4]+'_output.pdf','wb').write(self.out_pixels)

    def process(self):
        if self.mode=="Enc":
            self.encrypt()
        elif self.mode=="Dec":
            self.decrypt()
        self.venue=str(datetime.datetime.now())
        self.date,self.time=self.venue.split(' ')
        self.time=self.time.split(':')
        if int(self.time[0])>=12 :
            if int(self.time[0])==12:
                self.time=str(int(self.time[0]))+':'+self.time[1]+' PM'
            else:
                self.time=str(int(self.time[0])%12)+':'+self.time[1]+' PM'
        else:
            self.time=self.time[0]+':'+self.time[1]+' AM'
try:
    global file
    file1=open("pdflog.dat",'rb')
    file1.close()
    file1=open("pdflog.dat",'ab')
except IOError:
    file1=open("pdflog.dat",'ab')


while True :
    print('------------------------------------------------------------------------------------------------------------')
    choice=int(input("\n\n\nTo encrypt enter 1, to decrypt enter 2 , to view log enter 3 , to quit enter any other number :"))
    if choice==1 :
        try:
            enc_file=info_protect(input('\n Enter the path name of file :'),'Enc')
            enc_file.process()
            pickle.dump(enc_file,file1)
            
        except IOError :
            print('\nPlease enter a valid path name next time!!!')
            
        else:
            print("\nFile Successfully Encrypted!!")
            
    elif choice==2 :
        try:
            dec_file=info_protect(input('\n Enter the path name of file :'),'Dec')
            dec_file.process()
            pickle.dump(dec_file,file1)
        except IOError :
            print('\nPlease enter a valid path name next time!!!')
            
        else:
            print("\nFile Successfully Decrypted!!")
            
    elif choice==3 :
        try:
           file1.close()
           file1=open("pdflog.dat",'rb')
           a=1
           while True :
                   t=pickle.load(file1)
                   print('========================Entry %d=========================='%(a))
                   print('\nFile path:'+' '+t.path)
                   print('\nPassword :'+' '+"'"+t.key+"'")
                   print('\nProcess  :'+' '+t.mode+'ryption')
                   print('\nDate     :'+' '+t.date)
                   print('\nTime     :'+' '+t.time)
                   print()
                   print('==========================================================')
                   a+=1
        except EOFError :
           if a==1:
               print("No Records found")
           else:            
               print("\nThat's it---------")
    else :
        print("\nThanks for using me!!!!!!!!!")
        break
            
            
        
