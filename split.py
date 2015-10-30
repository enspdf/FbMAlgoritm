import threading

manywords=0                   
conta=0                       
contb=0                      
contc=0                       
contd=0                       
conte=0                       
matrixa=[]                    
matrixb=[]                    
matrixc=[]                    
matrixd=[]                    
matrixe=[]                    


def worker(vector):           
        red=0
        for w in vector:      
                red+=1        
                print w      
        #print red {DEBUG}            

with open("dic.log","r") as words: 
        for word in words:         
                manywords+=1        
        split=manywords/5           

with open("dic.log","r") as wordsb: 
        for wordb in wordsb:        
                if conta!=split:    
                        conta+=1   
                        matrixa.append(wordb) 
                if contb!=split:
                        contb+=1
                        matrixb.append(wordb)
                if contc!=split:
                        contc+=1
                        matrixc.append(wordb)
                if contd!=split:
                        contd+=1
                        matrixd.append(wordb)
                if conte!=split:
                        conte+=1
                        matrixe.append(wordb)

# print manywords, split, conta, contb, contc, contd, conte {DEBUG}  

if True:
    t = threading.Thread(target=worker, args=(matrixa,))  
    t.start()
    t = threading.Thread(target=worker, args=(matrixb,))
    t.start()
    t = threading.Thread(target=worker, args=(matrixc,))
    t.start()
    t = threading.Thread(target=worker, args=(matrixd,))
    t.start()
    t = threading.Thread(target=worker, args=(matrixe,))
    t.start()
