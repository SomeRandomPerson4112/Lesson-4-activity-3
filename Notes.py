amount=int(input("enter amount to withdraw: "))
note1=amount//100
note2=(amount%100)//50
note3=((amount%100)%50)//10
print("notes 100 rupees: ",note1)
print("notes 50 rupees: ",note2)
print("notes 10 rupees: ",note3)