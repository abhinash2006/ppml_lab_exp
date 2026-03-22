class Employee:
    def __init__(self, empid, name, basicpay):
        self.empid = empid
        self.name = name
        self.basicpay = basicpay
        self.ta = 0
        self.da = 0
        self.grosspay = 0
    def calc(self):
        self.ta = 0.10 * self.basicpay  
        self.da = 0.40 * self.basicpay
        self.grosspay = self.basicpay + self.ta + self.da
    def disp(self):
        print(f"Employee ID: {self.empid}")
        print(f"Name: {self.name}")
        print(f"Basic Pay: {self.basicpay}")
        print(f"TA (10%): {self.ta}")
        print(f"DA (40%): {self.da}")
        print(f"Gross Pay: {self.grosspay}")
emp = Employee(105, "anshuman", 50000)
emp.calc()
emp.disp()    