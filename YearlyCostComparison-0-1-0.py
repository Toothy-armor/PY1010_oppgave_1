"""
Elbil vs Bensinbil

Sander S. Boge
"""
#%% Data
KmPerYear = 0 #Distance driven per year
InsurancePerDay = 8.38 # cost per day for both in kr

ElInsurancePerYear = 5000 #Electric car insurance in kr
ElKWhPerKm = 0.2 #
EnergyPrice = 2 # in kr
ElTollPrice = 0.1 # in kr/km 

GasInsurancePerYear = 7500 #Gas car insurance in kr
GasPricePerKm = 1 # in kr/km
GasTollPrice = 0.3 #Kr/km

#%%Functions
def CalcElPerKm(Powerdraw,PowerPrice, TollPrice):
    return(Powerdraw*PowerPrice + TollPrice)

def CalcGasPrice(GasPrice,TollPrice):
    return(GasPrice + TollPrice)

def CalcPerYearCost(Insurance,Km,DailyInsurance,PerKmCost):
    return(Km*PerKmCost + Insurance + DailyInsurance*365)
#%% Execution
ElPerKm = CalcElPerKm(ElKWhPerKm, EnergyPrice, ElTollPrice)
GasPerKm = CalcGasPrice(GasPricePerKm, GasTollPrice)
 
GasPerYear = CalcPerYearCost(GasInsurancePerYear, KmPerYear, InsurancePerDay, GasPerKm)
ElPerYear = CalcPerYearCost(ElInsurancePerYear, KmPerYear, InsurancePerDay, ElPerKm)
print(GasPerYear,"Kr is the price of a gas car per Year")
print(ElPerYear,"Kr is the price of an electric car per Year")
