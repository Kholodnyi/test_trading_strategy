import pickle
import matplotlib.pyplot as plt

with open ('data_file', 'rb') as fp: # File with a data generated by data_creator.ry should lay in the same dir
    list_of_rates = pickle.load(fp)
fp.close()

rates = len(list_of_rates)
depo_WAVES = 0
depo_BTC = 1
depo_WAVES = depo_BTC/float(list_of_rates[0][1]) # initial purchase
depo_BTC = 0
prev_rate = float(list_of_rates[0][1])

BTC_equivalent = []
WAVES_equivalent = []

for i in range(rates-1):
    current_rate = float(list_of_rates[i+1][1]) # defining an exchange rate
    if depo_BTC == 0:
        if current_rate >= 1.004 * prev_rate:
            depo_BTC = depo_WAVES * current_rate
            depo_WAVES = 0
            prev_rate = float(list_of_rates[i+1][1]) # updating an exchange rate with which we must compare current rate
        elif current_rate <= 0.99 * prev_rate:
            depo_BTC = depo_WAVES * current_rate
            depo_WAVES = 0
            prev_rate = float(list_of_rates[i+1][1]) # updating an exchange rate with which we must compare current rate
    elif depo_WAVES == 0:
        depo_WAVES = depo_BTC / current_rate
        depo_BTC = 0

    # creating a lists of minute-by-minute equivalent deposites of BTC and WAVES
    if depo_BTC == 0:
        BTC_equivalent.append(depo_WAVES * current_rate)
    else:
        BTC_equivalent.append(depo_BTC)
    if depo_WAVES == 0:
        WAVES_equivalent.append(depo_BTC / current_rate)
    else:
        WAVES_equivalent.append(depo_WAVES)

X = [] # list for X axis
for i in range(len(BTC_equivalent)):
    X.append(i / 1440) # 1440 minutes in a one day

# creating a polt by matplotlib
fig,axes = plt.subplots(nrows=2, ncols=1, figsize=(10,6), dpi=100)

axes[0].plot(X, BTC_equivalent)
axes[0].set_title('BTC deposit dynamics')

axes[1].plot(X, WAVES_equivalent)
axes[1].set_title('WAVES deposit dynamics')
plt.show()
