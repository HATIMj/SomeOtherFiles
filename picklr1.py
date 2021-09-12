import pickle
#j=['koko','loko']
#m=open("jig.txt","wb")
#l=pickle.dump(j,m)
j=open("jig.txt","rb")
k=pickle.load(j)
print(k)