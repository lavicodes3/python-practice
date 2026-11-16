class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def show(self):
        print(f"{self.real}i + {self.img}j")

    def add(self,self2):# or directly self + num2  if replaced method add to __add__
        newReal=self.real+self2.real
        newImg=self.img+self2.img
        return Complex(newReal,newImg)

num1 = Complex(1,2)
num2 = Complex(4,5)
num3 = num1.add(num2) 
num1.show()
num2.show()
num3.show()