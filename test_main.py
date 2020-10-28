import scipy.stats as st
import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_plot(self) : 
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        figdat = fighand.get_lines()[2].get_xydata()
        this_x2, this_y2 = zip(*figdat)
        self.assertTrue( len(this_x)==200, "the number of coordinates plotted on your graph is incorrect" )
        for i in range(len(this_y)) :
           self.assertTrue( np.abs(i + 1 - this_x[i])<1e-7, "the x-coordinates of the points in your graph are incorrect" )
           bar = np.sqrt(kval*pval*(1-pval)/(i+1))*st.norm.ppf( (0.99 + 1) / 2 )
           self.assertTrue( np.fabs( this_y[i]*this_y2[i] - kval*pval )<bar, "it looks like you have computed the estimators incorrectly" )
    
