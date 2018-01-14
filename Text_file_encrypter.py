import datetime

class info_protect :

    def __init__(self,pathname,mode):
        self.pathname=pathname
        self.mode=mode
        self.base_str="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        self.base_str*=2
        self.instr=open(self.pathname,'r').read()
        self.outstr=''
        self.key=str(input("\n Enter your desired password:"))
        self.temp=[]
        self.venue=''
        self.date,self.time='',''

    def encrypt(self):        
        for i in self.key:
            self.temp.append(self.base_str.find(i))
        print(self.temp)
        for i in range(len(self.instr)) :
             if self.instr[i] in self.base_str:
                 index=self.base_str.find(self.instr[i])            
                 val=self.temp[i%len(self.temp)]
                 new_chr=self.base_str[index+val]            
             else:
                 new_chr=self.instr[i]
             self.outstr+=new_chr   
        open(self.pathname,'w').write(self.outstr)

    def decrypt(self):        
        for i in self.key:
            self.temp.append(self.base_str.find(i))
        for i in range(len(self.instr)) :
         if self.instr[i] in self.base_str :
            index=self.base_str.find(self.instr[i])
            val=self.temp[i%len(self.temp)]
            new_chr=self.base_str[index-val]
         else:
            new_chr=self.instr[i]
         self.outstr+=new_chr   
        open(self.pathname,'w').write(self.outstr)

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
#------------------------------------Main_code---------------------------------------

#Checking for the presence for usage_log
import pickle

try:
    global file
    file1=open("log.dat",'rb')
    file1.close()
    file1=open("log.dat",'ab')
except IOError:
    file1=open("log.dat",'ab')


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
           file1=open("log.dat",'rb')
           a=1
           while True :
                   t=pickle.load(file1)
                   print('========================Entry %d=========================='%(a))
                   print('\nFile path:'+' '+t.pathname)
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
        
                
               


















                
        
        
