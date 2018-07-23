import unittest
import numpy as np
import apc

class TestIdentify(unittest.TestCase):

    def test_BZ_ln(self):
        model = apc.Model()
        model.data_from_df(apc.loss_BZ())
        model.fit('log_normal_response', 'APC')
        model.identify()
        self.assertTrue(np.allclose(
            model.para_table_adhoc['P>|z|'],
            np.array([
                0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 2.00274820e-79,
                8.23470360e-03, 6.99028376e-01, 2.52253326e-01, 9.44947585e-01,
                2.99779730e-01, 3.61984852e-01, 8.68870491e-01, 6.71030697e-01,
                7.17773089e-01, 6.64325362e-01, 6.54251805e-01, 7.06632657e-01,
                6.68992349e-01, 2.25311035e-01, 1.30553342e-02, 1.77350370e-02,
                7.07582982e-01, 6.85096418e-01, 2.92513328e-05, 8.56955875e-01,
                8.81192454e-01, 5.53721164e-01, 9.86966046e-08, 2.83296029e-01,
                1.87348807e-02, 3.18902324e-01,         np.nan, 0.00000000e+00,
                0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 1.55003598e-05,
                3.45473306e-01, 6.91540126e-01, 7.39439614e-01, 6.30783338e-01,
                        np.nan,         np.nan, 3.88858581e-01, 1.88538573e-01,
                1.04693286e-02, 5.98343270e-04, 2.97779338e-07, 6.30075991e-11,
                0.00000000e+00, 0.00000000e+00, 2.40947018e-07,         np.nan,
                np.nan, 2.07357673e-04, 5.60103297e-10, 1.11347145e-01,
                1.91918026e-02, 3.68315018e-08, 0.00000000e+00, 1.24363329e-05,
                8.13918274e-01, 3.74149721e-01,         np.nan
            ]),
            equal_nan=True)
                       )
        model.identify('sum_sum')
        self.assertTrue(np.allclose(
            model.para_table_adhoc['P>|z|'],
            np.array([
                0.00000000e+00, 5.58305092e-06, 2.67784602e-03, 2.00274820e-79,
                8.23470360e-03, 6.99028376e-01, 2.52253326e-01, 9.44947585e-01,
                2.99779730e-01, 3.61984852e-01, 8.68870491e-01, 6.71030697e-01,
                7.17773089e-01, 6.64325362e-01, 6.54251805e-01, 7.06632657e-01,
                6.68992349e-01, 2.25311035e-01, 1.30553342e-02, 1.77350370e-02,
                7.07582982e-01, 6.85096418e-01, 2.92513328e-05, 8.56955875e-01,
                8.81192454e-01, 5.53721164e-01, 9.86966046e-08, 2.83296029e-01,
                1.87348807e-02, 3.18902324e-01,         np.nan,         np.nan,
                0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
                0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
                0.00000000e+00,         np.nan,         np.nan, 7.17773089e-01,
                8.14615687e-01, 7.58653152e-01, 7.86916053e-01, 7.56048998e-01,
                8.44116015e-01, 7.27876096e-01, 5.16083943e-01, 3.88858581e-01,
                        np.nan,         np.nan, 6.85096418e-01, 7.42370529e-04,
                1.26530874e-06, 9.49610746e-09, 6.15689721e-11, 2.77536453e-07,
                2.00632262e-04, 4.79419824e-04, 2.07357673e-04
            ]),
            equal_nan=True)
                       )        
    
    def test_TA_odp(self):
        model = apc.Model()
        model.data_from_df(apc.loss_TA(), data_format='CL')
        model.fit('od_poisson_response', 'AC')
        model.identify()
        self.assertTrue(np.allclose(
           model.para_table_adhoc['P>|t|'],
           np.array([
                       np.nan, 1.26455388e-01, 5.40832482e-01, 1.35749045e-04,
               9.20260458e-01, 8.11965018e-03, 4.67631895e-01, 5.17889796e-01,
               5.58375527e-01, 2.35466770e-01, 1.08695074e-01, 1.67254401e-01,
               9.84463128e-01, 7.89979049e-01, 6.32105935e-01, 8.62556947e-01,
               7.99177515e-01, 3.19345261e-01, 9.21765023e-01,         np.nan,
               3.73716746e-08, 3.14639490e-06, 4.17156318e-05, 1.75658307e-02,
               1.15572711e-01, 1.52816095e-01, 3.68005022e-01, 1.48757062e-01,
                       np.nan,         np.nan, 3.48309028e-02, 1.05032288e-01,
               2.43482340e-01, 6.25449875e-01, 6.09484256e-01, 4.89009106e-01,
               2.96652660e-01, 7.09076601e-01,         np.nan
           ]),
           equal_nan=True)
                       )
        model.identify('sum_sum')
        self.assertTrue(np.allclose(
           model.para_table_adhoc['P>|t|'],
           np.array([
                       np.nan, 3.50394713e-09, 1.65458672e-02, 1.35749045e-04,
               9.20260458e-01, 8.11965018e-03, 4.67631895e-01, 5.17889796e-01,
               5.58375527e-01, 2.35466770e-01, 1.08695074e-01, 1.67254401e-01,
               9.84463128e-01, 7.89979049e-01, 6.32105935e-01, 8.62556947e-01,
               7.99177515e-01, 3.19345261e-01, 9.21765023e-01,         np.nan,
                       np.nan, 1.35749045e-04, 3.77783273e-06, 1.23527328e-08,
               1.98956984e-09, 1.80411397e-09, 9.87196547e-10, 4.59303884e-09,
               3.73716746e-08,         np.nan,         np.nan, 1.67254401e-01,
               6.66909338e-02, 3.10125845e-02, 3.21367951e-02, 3.87616664e-02,
               5.45918348e-02, 3.41998121e-02, 3.48309028e-02
           ]),
           equal_nan=True)
                       )

    def test_Belgian_gauss_rates(self):
        model = apc.Model()
        model.data_from_df(**apc.Belgian_lung_cancer())
        predictors = ['APC', 'AP', 'AC', 'PC', 'Ad', 'Pd', 'Cd',
                      'A', 'P', 'C', 't', 'tA', 'tP', 'tC', '1']
        for p in predictors:
            model.fit('gaussian_rates', p)
            model.identify('sum_sum')
            model.identify('detrend')

    def test_Belgian_bin_dose_response(self):
        data = apc.Belgian_lung_cancer()
        dose = (data['response']/data['rate'] * 10**5).astype(int)
        model = apc.Model()
        model.data_from_df(data['response'], dose=dose, data_format='AP')
        model.fit('binomial_dose_response', 'A')
        model.identify()
        self.assertTrue(np.allclose(
            model.para_table_adhoc['P>|z|'].values,
            np.array([
                0.00000000e+00, 0.00000000e+00, 1.33164723e-01, 3.32887753e-01,
                3.12519532e-01, 2.29233523e-01, 7.32087385e-01, 3.81022509e-01,
                8.33197044e-01, 5.17100474e-01, 2.22728929e-01,         np.nan,
                1.96085981e-02, 4.12480706e-03, 7.29829995e-07, 8.19528889e-11,
                3.29736238e-13, 8.88178420e-16, 4.44089210e-16, 2.22044605e-16,
                1.21335830e-10,         np.nan
            ]),
            equal_nan=True)
                       )
        model.identify('sum_sum')
        self.assertTrue(np.allclose(
            model.para_table_adhoc['P>|z|'].values,
            np.array([
                0.00000000e+00, 2.89687537e-11, 1.33164723e-01, 3.32887753e-01,
                3.12519532e-01, 2.29233523e-01, 7.32087385e-01, 3.81022509e-01,
                8.33197044e-01, 5.17100474e-01, 2.22728929e-01, 2.38534812e-04,
                9.72872606e-03, 6.49159614e-03, 1.50937017e-01, 7.32087385e-01,
                        np.nan,         np.nan, 3.81022509e-01, 3.20050892e-01,
                2.05498744e-01, 8.06553615e-02
            ]),
            equal_nan=True)
                       )
        
if __name__ == '__main__':
    unittest.main()