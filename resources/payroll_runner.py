from Payrollcalc import Payrollcalc

sal = Payrollcalc('Joe', 55000, 0)

print('Name: ', sal.name)
print('Gross Salary: KSH', sal.grossSalary)
print('Gross Taxable income: KSH ', sal.taxable_income)
print('NSSF DEDUCTION: KSH', round(sal.nssf_deduct, 2))
print('PAYE: KSH', round(sal.paye, 2))
print('Personal Relief: KSH', sal.relief)
print('NHIF: KSH', sal.NHIF_deduct)
print('Net Salary: KSH', round(sal.netSalary, 2))
