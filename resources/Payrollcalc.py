class Payrollcalc:
    name = ""
    basicSalary = 0
    benefits = 0
    grossSalary = 0
    paye = 0
    NHIF_deduct = 0
    nssf_deduct = 0
    taxable_income = 0
    netSalary = 0
    relief = 1408.00
    """before NHIF deduction"""
    gross_tax = 0


    def __init__(self, n, bas, ben):
        Payrollcalc.name = n
        Payrollcalc.basicSalary = bas
        Payrollcalc.benefits = ben
        Payrollcalc.get_gross_salary(self)
        Payrollcalc.get_nssf(self)
        Payrollcalc.get_paye(self)
        Payrollcalc.get_nhif(self)
        Payrollcalc.relief_calc(self)
        Payrollcalc.get_taxable_income(self)
        Payrollcalc.gross_tax_calc(self)
        Payrollcalc.get_netsalary_calc(self)


    def get_gross_salary(self):
        self.grossSalary = self.basicSalary + self.benefits

    def get_nssf(self):
        if self.grossSalary > 0 and self.grossSalary <= 6000:
            self.nssf_deduct = 6/100 * self.grossSalary
        elif self.grossSalary > 6000 and self.grossSalary <= 18000:
            self.nssf_deduct = (6/100 * 6000)+(6/100*self.grossSalary)
        elif self.grossSalary > 18000:
            self.nssf_deduct = 6/100*18000


    """"Do taxable income here"""
    def get_taxable_income(self):
        self.taxable_income = self.grossSalary - self.nssf_deduct


    def get_paye(self):
        if self.taxable_income <= 12298:
            self.paye = self.grossSalary * 0.1
        elif self.taxable_income < 23886:
            self.paye = (0.1*12298) + (0.15 * (self.taxable_income - 12298))
        elif self.taxable_income < 35473:
            self.paye = (0.1*12298) + (0.15 * 11587) + (0.2 *(self.taxable_income - 23885))
        elif self.taxable_income < 47060:
            self.paye = (0.1*12298) + (0.15 * 11587) + (0.2 * 11587) + (0.25 * (self.taxable_income - 35472))
        elif self.taxable_income >= 47060:
            self.paye = (0.1*12298) + (0.15 * 11587) + (0.2 * 11587) + (0.25 * 11587) + (0.3 *(self.taxable_income - 47059))

    def relief_calc(self):
        if self.grossSalary > 0:
            if self.paye > self.relief:
                self.after_relief = self.paye - self.relief

        else:
            self.relief = 0

    def gross_tax_calc(self):
        self.gross_tax = self.taxable_income - self.after_relief


    def get_nhif(self):

        if self.grossSalary <= 5999:
            self.NHIF_deduct = 150
        elif self.grossSalary >= 6000 and self.grossSalary <= 7999:
            self.NHIF_deduct = 300
        elif self.grossSalary >= 8000 and self.grossSalary <= 11999:
            self.NHIF_deduct = 400
        elif self.grossSalary >= 12000 and self.grossSalary <= 14999:
            self.NHIF_deduct = 500
        elif self.grossSalary >= 15000 and self.grossSalary <= 15999:
            self.NHIF_deduct = 600
        elif self.grossSalary >= 20000 and self.grossSalary <= 24999:
            self.NHIF_deduct = 750
        elif self.grossSalary >= 25000 and self.grossSalary <= 29999:
            self.NHIF_deduct = 850
        elif self.grossSalary >= 30000 and self.grossSalary <= 34999:
            self.NHIF_deduct = 900
        elif self.grossSalary >= 35000 and self.grossSalary <= 39999:
            self.NHIF_deduct = 950
        elif self.grossSalary >= 40000 and self.grossSalary <= 44999:
            self.NHIF_deduct = 1000
        elif self.grossSalary >= 45000 and self.grossSalary <= 49999:
            self.NHIF_deduct = 1100
        elif self.grossSalary >= 50000 and self.grossSalary <= 59999:
            self.NHIF_deduct = 1200
        elif self.grossSalary >= 60000 and self.grossSalary <= 69999:
            self.NHIF_deduct = 1300
        elif self.grossSalary >= 70000 and self.grossSalary <= 79999:
            self.NHIF_deduct = 1400
        elif self.grossSalary >= 80000 and self.grossSalary <= 89999:
            self.NHIF_deduct = 1500
        elif self.grossSalary >= 90000 and self.grossSalary <= 99999:
            self.NHIF_deduct = 1600
        else:
            self.NHIF_deduct = 1700



    def get_netsalary_calc(self):
        self.netSalary = self.gross_tax - self.NHIF_deduct

