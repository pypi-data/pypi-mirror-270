import unittest

import numpy as np

from cuatro import CUATRO


def Rosenbrock(x):
    return (1 - x[0])**2 + 100*(x[1] - x[0]**2)**2


def sim(x):
    f1 = Rosenbrock
    return f1(x), []

conv_rad = 1e-02
N = 500
N_x = 2

optimum = 0

bounds = np.array([(-5.0, 5.0) for i in range(N_x)])
x0 = np.array([(b[0] + b[1])/2 for b in bounds])
x0_multiple = np.array([[0, 0.5], [0, -0.5]])
init_radius = np.max([(b[1] - b[0])/2 for b in bounds])
beta = 1e-3**(1/N)
N_min_s = N/10
tol= 1e-10


solvers = {
    'CUATRO_g': CUATRO(sampling='g', explore=None, method='global', N_min_samples=N_min_s, beta_red=beta, tolerance=tol, init_radius=init_radius),
    'CUATRO_l': CUATRO(sampling='g', explore=None, method='local', N_min_samples=N_min_s, beta_red=beta, tolerance=tol, init_radius=init_radius),
    'CUATRO_base': CUATRO(sampling='base', explore=None, N_min_samples=N_min_s, beta_red=beta, tolerance=tol, init_radius=init_radius),
    #'CUATRO_expl_expl': CUATRO_expl_expl, # TODO: expl expl might not be great
    'CUATRO_feas_samp': CUATRO(sampling='base', explore='feasible_sampling', N_min_samples=N_min_s, beta_red=beta, tolerance=tol, init_radius=init_radius),
    'CUATRO_sampl_region': CUATRO(sampling='base', explore='sampling_region', N_min_samples=N_min_s, beta_red=beta, tolerance=tol, init_radius=init_radius),
    'CUATRO_TIS': CUATRO(sampling='base', explore='TIS', N_min_samples=N_min_s, beta_red=beta, tolerance=tol, init_radius=init_radius),
    'CUATRO_TIP': CUATRO(sampling='base', explore='TIP', N_min_samples=N_min_s, beta_red=beta, tolerance=tol, init_radius=init_radius)
}


class TestConvergence_g(unittest.TestCase):
    def runTest(self):
        """
        see whether convergence is achieved for the given test function
        """  
        res = solvers['CUATRO_g'].run_optimiser(sim=sim, x0=x0, bounds=bounds, max_f_eval=N, rnd=0)
        self.assertTrue((abs(res['f_best_so_far'][-1] - optimum)**2 < conv_rad), f"CUATRO_g did not converge to {conv_rad} accuracy for a budget of {N}; best_f: {res['f_best_so_far'][-1]}, optimum: {optimum}")


class TestConvergence_base(unittest.TestCase):
    def runTest(self):
        """
        see whether convergence is achieved for the given test function
        """  
        res = solvers['CUATRO_base'].run_optimiser(sim=sim, x0=x0, bounds=bounds, max_f_eval=N, rnd=0)
        self.assertTrue((abs(res['f_best_so_far'][-1] - optimum)**2 < conv_rad), f"CUATRO_base did not converge to {conv_rad} accuracy for a budget of {N}; best_f: {res['f_best_so_far'][-1]}, optimum: {optimum}")


class TestConvergence_feas_samp(unittest.TestCase):
    def runTest(self):
        """
        see whether convergence is achieved for the given test function
        """  
        res = solvers['CUATRO_feas_samp'].run_optimiser(sim=sim, x0=x0, bounds=bounds, max_f_eval=N, rnd=0)
        self.assertTrue((abs(res['f_best_so_far'][-1] - optimum)**2 < conv_rad), f"CUATRO_feas_samp did not converge to {conv_rad} accuracy for a budget of {N}; best_f: {res['f_best_so_far'][-1]}, optimum: {optimum}")


class TestConvergence_sampl_region(unittest.TestCase):
    def runTest(self):
        """
        see whether convergence is achieved for the given test function
        """  
        res = solvers['CUATRO_sampl_region'].run_optimiser(sim=sim, x0=x0, bounds=bounds, max_f_eval=N, rnd=0)
        self.assertTrue((abs(res['f_best_so_far'][-1] - optimum)**2 < conv_rad), f"CUATRO_sampl_region did not converge to {conv_rad} accuracy for a budget of {N}; best_f: {res['f_best_so_far'][-1]}, optimum: {optimum}")


class TestConvergence_TIS(unittest.TestCase):
    def runTest(self):
        """
        see whether convergence is achieved for the given test function
        """  
        res = solvers['CUATRO_TIS'].run_optimiser(sim=sim, x0=x0, bounds=bounds, max_f_eval=N, rnd=0)
        self.assertTrue((abs(res['f_best_so_far'][-1] - optimum)**2 < conv_rad), f"CUATRO_TIS did not converge to {conv_rad} accuracy for a budget of {N}; best_f: {res['f_best_so_far'][-1]}, optimum: {optimum}")


class TestConvergence_TIP(unittest.TestCase):
    def runTest(self):
        """
        see whether convergence is achieved for the given test function
        """  
        res = solvers['CUATRO_TIP'].run_optimiser(sim=sim, x0=x0_multiple, bounds=bounds, max_f_eval=N, rnd=0)
        self.assertTrue((abs(res['f_best_so_far'][-1] - optimum)**2 < conv_rad), f"CUATRO_TIP did not converge to {conv_rad} accuracy for a budget of {N}; best_f: {res['f_best_so_far'][-1]}, optimum: {optimum}")


if __name__ == '__main__':
    unittest.main()



        