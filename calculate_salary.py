# Recalculating for a gross salary of 10,000 PLN per month.

gross_salary_10000 = 10000

# Social security contribution (13.71%)
social_security_10000 = gross_salary_10000 * 0.1371

# Health insurance contribution (9%)
health_insurance_10000 = gross_salary_10000 * 0.09

# Income tax (17%) applied to the remaining after social security deduction
tax_base_10000 = gross_salary_10000 - social_security_10000
income_tax_10000 = tax_base_10000 * 0.17
print(income_tax_10000)

# Net salary after all deductions
net_salary_10000 = gross_salary_10000 - (social_security_10000 + health_insurance_10000 + income_tax_10000)
net_salary_10000
print (net_salary_10000)