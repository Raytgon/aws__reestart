myFruitList=["apple","mango","banana"]
print("\n" , myFruitList ,"\t" , type(myFruitList)," \n To access first element we use index ",myFruitList[0]," \n To access second element we use index ",myFruitList[1],
 " \n To access third element we use index ",myFruitList[2])
 
myFruitList[1]="orange"
print("\n",myFruitList)
animalList=("chikko","banana","papaya")
print("\n",animalList,"\t ",type(animalList),"\n To access first element of tuple ",animalList[0],"\n To access second element of tuple ",animalList[1],"\n To access third element of tuple ",animalList[2])


myDictionary={
    "isha":"Chiku",
    "sanyog":"saya",
    "mrudula":"chingu"
}
print("\n",myDictionary,"\t",type(myDictionary)," \n accessing by key ", myDictionary['isha'] ," \n accessing by key ",myDictionary['sanyog'],"\n accessing by key ",myDictionary['mrudula'])
print("\n",myDictionary.values())