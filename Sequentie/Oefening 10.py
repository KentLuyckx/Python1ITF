fixed_costs = float (83.6)
night_costs = float (0.035)  # € per kWh
day_costs = float (0.068)  # € per kWh
vat = float (1.21)  # 21%
usage_day = int(input("Power consumption during the day (in kWh): "))
usage_night = int(input("Power consumption during the night (in kWh): "))

print("Invoice")
print("*****")
print("Fixed Costs: €", fixed_costs)
print("Daily consumption: €", usage_day * day_costs)
print("Night consumption: €", usage_night * night_costs)
print("Total excluding VAT: €", fixed_costs + (usage_day * day_costs) + (usage_night * night_costs))
print("Total including VAT: €", (fixed_costs + (usage_day * day_costs) + (usage_night * night_costs)) * vat)