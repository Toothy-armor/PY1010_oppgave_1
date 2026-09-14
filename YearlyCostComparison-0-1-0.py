"""
Elbil vs Bensinbil

Sander S. Boge
"""
#%% Data
KmPerYear = 10000 #Distance driven per year
InsurancePerDay = 8.38 # cost per day for both in kr

ElInsurancePerYear = 5000 #Electric car insurance in kr
ElKWhPerKm = 0.2 #
EnergyPrice = 2 # in kr
ElTollPrice = 0.1 # in kr/km 

GasInsurancePerYear = 7500 #Gas car insurance in kr
GasPricePerKm = 1 # in kr/km
GasTollPrice = 0.3 #Kr/km

#%% Execution
ElPerKm = ElKWhPerKm*EnergyPrice + ElTollPrice
GasPerKm = GasPricePerKm + GasTollPrice
 
GasPerYear = KmPerYear*GasPerKm + GasInsurancePerYear + InsurancePerDay*365
ElPerYear = KmPerYear*ElPerKm + ElInsurancePerYear + InsurancePerDay*365

#%%print costs
print(GasPerYear,"Kr is the price of a gas car per Year")
print(ElPerYear,"Kr is the price of an electric car per Year")
