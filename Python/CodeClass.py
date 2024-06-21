class ClassFunction():
    def Subfields():
        SubfieldsInAI=["Sub-fields in AI are:","Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for Sub_fieldsInAI in SubfieldsInAI:
            fields = Sub_fieldsInAI
            print(fields)
        #return fields
    def OddEven():
        num=int(input("Enter the Number:"))
        if(num%2==0):
            print( num,"is even number")
        else:
            print(num,"Number is odd number")
    def marriageEligible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if((gender=="male") and (age<25)):
            print("NOT ELIGIBLE")
    def percentage():
        sub1=int(input("Subject1:"))
        sub2=int(input("Subject2:"))
        sub3=int(input("Subject3:"))
        sub4=int(input("Subject4:"))
        sub5=int(input("Subject5:"))
        total=sub1+sub2+sub3+sub4+sub5
        Percentage=(total*100)/500
        print("total:",total)
        print("Percentage:",Percentage)
    def triangle():
        a_height=int(input("Height"))
        a_breadth=int(input("Breadth"))
        area_Triangle=(a_height*a_breadth)/2
        print("Area of Triangle:",area_Triangle)
        p_height1=int(input("Height1"))
        p_height2=int(input("Height2"))
        p_Breadth=int(input("Breadth"))
        perimeter=p_height1+p_height2+p_Breadth
        print("Perimeter of Triangle",perimeter)

                
           