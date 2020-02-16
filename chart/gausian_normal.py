import numpy as np
import scipy.stats as stats
import pylab as pl

import csv

with open('score.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))
    data = np.array(data).astype(np.float).transpose()[0]
    print(data)
    h = sorted([186, 176, 158, 180, 186, 168, 168, 164, 178, 170, 189, 195, 172,
        187, 180, 186, 185, 168, 179, 178, 183, 179, 170, 175, 186, 159,
        161, 178, 175, 185, 175, 162, 173, 172, 177, 175, 172, 177, 180])
    #plt.plot(data, [1,2,3,4,5,6])
    #h = sorted(data)
    #fit = stats.norm.pdf(h, np.mean(h), np.std(h))
    hmean = np.mean(h)
    hstd = np.std(h)
    pdf = stats.norm.pdf(h, hmean, hstd)
    
    pl.xlabel('Score')
    pl.ylabel('Density')
    #pl.plot(h,fit,'-o')
    pl.plot(h, pdf) # including h here is crucial  
    pl.show()  