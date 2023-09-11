class Multiplefunctions():
    def Subfields():
        subfeilds=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are:")
        for temp in subfeilds:
            print(temp)
    def oddeven():
        num=int(input("Enter the Number:"))
        if num%2==0:
            print("number is even")
            message='Even Number'
        else:
            print("number is odd")
            message='Odd Number'
        return message
    def mrgeligible():
        gender=input("your Gender:")
        age=int(input("your age:"))
        if gender=='female':
            if age<18:
                print("Not eligible")
            else:
                print("eligible")
        else:
            if age<21:
                print("Not eligible")
            else:
                print("eligible")
    def percentage():
        sub1=int(input("Subject1:"))
        sub2=int(input("Subject2:"))
        sub3=int(input("Subject3:"))
        sub4=int(input("Subject4:"))
        sub5=int(input("Subject5:"))
        total=(sub1+sub2+sub3+sub4+sub5)
        print("total:",total)
        percentage=total/5
        print("percentage:",percentage)
        percentage1="percentage:",percentage
        return percentage1
    def triangle():
        Height=int(input('Height:'))
        Breadth=int(input('breadth:'))
        Areaformula=(Height*Breadth)/2
        print('Area of Triangle:',Areaformula)
        height1=int(input('Height1:'))
        height2=int(input('Height2:'))
        Breadth=int(input('breadth:'))
        perimeterformula=height1+height2+Breadth
        print("Perimeter of Triangle:", perimeterformula)
        PerimeterofTriangle="Perimeter of Triangle:",perimeterformula
        return PerimeterofTriangle
        
        