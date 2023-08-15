import numpy as np
import matplotlib.pyplot as plt

def error(opt, best):
  error = ((opt - best) / opt) * 100
  error = np.abs(error)
  return error

#ATT48

att48opt = 33523.70850743559
att48hc = 49940.19250756425
att48wsa50 = 39860.023048799034 
att48wsa100 = 39344.1227124339
att48wsa250 = 37456.56419090763
att48wsa500 = 37539.83228051007

att48hcER = error(att48opt, att48hc)
att48wsa50ER = error(att48opt, att48wsa50)
att48wsa100ER = error(att48opt, att48wsa100)
att48wsa250ER = error(att48opt, att48wsa250)
att48wsa500ER = error(att48opt, att48wsa500)

att48labels = ['HC', 'WSA50', 'WSA100', 'WSA250', 'WSA500']
att48errors =[att48hcER, att48wsa50ER, att48wsa100ER, att48wsa250ER, att48wsa500ER]

plt.bar(att48labels, att48errors, color='r')
plt.xlabel('Algorithms')
plt.ylabel('Errors')
plt.title('Errors for ATT48')
plt.show()
print()

#BERLIN52

b52opt = 7544.365901904087
b52hc = 11862.987799855056
b52wsa50 = 9060.850180436964
b52wsa100 = 9265.6802451152
b52wsa250 = 8422.379316417833
b52wsa500 = 9169.262838073953

b52hcER = error(b52opt, b52hc)
b52wsa50ER = error(b52opt, b52wsa50)
b52wsa100ER = error(b52opt, b52wsa100)
b52wsa250ER = error(b52opt, b52wsa250)
b52wsa500ER = error(b52opt, b52wsa500)

b52labels = ['HC', 'WSA50', 'WSA100', 'WSA250', 'WSA500']
b52errors =[b52hcER, b52wsa50ER, b52wsa100ER, b52wsa250ER, b52wsa500ER]

plt.bar(b52labels, b52errors, color='b')
plt.xlabel('Algorithms')
plt.ylabel('Errors')
plt.title('Errors for B52')
plt.show()
print()

#PR76

pr76opt = 108159.4382741377
pr76hc = 235620.47723370924 
pr76wsa50 = 143901.25962546616
pr76wsa100 = 141528.63043108885
pr76wsa250 = 153407.00673691914
pr76wsa500 = 153287.43102982792

pr76hcER = error(pr76opt, pr76hc)
pr76wsa50ER = error(pr76opt, pr76wsa50)
pr76wsa100ER = error(pr76opt, pr76wsa100)
pr76wsa250ER = error(pr76opt, pr76wsa250)
pr76wsa500ER = error(pr76opt, pr76wsa500)

pr76labels = ['HC', 'WSA50', 'WSA100', 'WSA250', 'WSA500']
pr76errors =[pr76hcER, pr76wsa50ER, pr76wsa100ER, pr76wsa250ER, pr76wsa500ER]

plt.bar(pr76labels, pr76errors, color='g')
plt.xlabel('Algorithms')
plt.ylabel('Errors')
plt.title('Errors for PR76')
plt.show()
print()