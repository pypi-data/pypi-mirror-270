import unittest
import numpy as np

from cuatro import CUATRO
from cuatro.test_functions.constraints.rosenbrock_constrained import rosenbrock_g1


def Rosenbrock(x):
    return (1 - x[0])**2 + 100*(x[1] - x[0]**2)**2


def sim(x):
    f1 = Rosenbrock
    g1 = rosenbrock_g1
    
    return f1(x), [g1(x)]


class TestCustomParams(unittest.TestCase):
    def runTest(self):
        """
        check whether parameters are successfully changed to some non-default values at initialization
        """
        
        # the non-default values
        setValues = {
                     'init_radius': 0.5,
                     'tolerance': 1e-09,
                     'beta_inc': 1.25,
                     'beta_red': 0.9,
                     'eta1': 0.3,
                     'eta2': 0.9,
                     'method': 'global',
                     'N_min_samples': 15,
                     'print_status': True,
                     'constr_handling': 'Regression',
                     'sampling': 'base',
                     'explore': 'feasible_sampling',
                     'sampling_trust_ratio': [0.2, 0.8],
                     'min_radius': 0.04,
                     'min_restart_radius': 2.2,
                     'conv_radius': 0.18,
                     'no_x0': 8,
                     'rescale_radius': True,
                     'solver_to_use': "MOSEK"
                     }
        
        
        solver_instance = CUATRO(
                                 init_radius = 0.5,
                                 tolerance = 1e-09,
                                 beta_inc = 1.25,
                                 beta_red = 0.9,
                                 eta1 = 0.3,
                                 eta2 = 0.9,
                                 method = 'global',
                                 N_min_samples = 15,
                                 print_status = True,
                                 constr_handling = 'Regression',
                                 sampling = 'base',
                                 explore = 'feasible_sampling',
                                 sampling_trust_ratio = [0.2, 0.8],
                                 min_radius = 0.04,
                                 min_restart_radius = 2.2,
                                 conv_radius = 0.18,
                                 no_x0 = 8,
                                 rescale_radius = True,
                                 solver_to_use = "MOSEK"
                                 )

        vars_to_check = solver_instance.__dict__
        
        for var, var_value in vars_to_check.items():                
            if var not in ['automatic_params', 'dim_red']: # TODO: implement testing for automatic_params, dim_red
               self.assertTrue((var_value == setValues[var]), f"{var} parameter was not set correctly, and has value {var_value} instead of {setValues[var]}")
            

class TestImplementations(unittest.TestCase):
    def runTest(self):
        """
        check correct CUATRO implementations (heuristics) were set
        """
        sampling_types = ['g', 'base']
        exploration_heuristics = [None, 'feasible_sampling', 'exploit_explore',\
             'sampling_region', 'TIS', 'TIP']
        
        x0 = np.array([-1.5,-1.5])

        for sampl in sampling_types:
            for expl in exploration_heuristics:
                solver_instance = CUATRO(sampling=sampl, explore=expl)

                if solver_instance.sampling == 'g':
                    try:
                        self.assertTrue(solver_instance.explore == None)
                    except:
                        ValueError(f"correct setting, {expl} can't be set as explore when sampling == g")

                if solver_instance.explore != None:
                    try:
                        self.assertTrue(solver_instance.sampling == 'base')

                    except:
                        ValueError(f"correct setting, g can't be set as sampling when explore == {expl}")


class TestTolerance(unittest.TestCase):
    def runTest(self):
        """
        check whether tolerance is used successfully as a termination criterion;
        set high value for tolerance,  and max_f_eval
        """
        x0 = np.array([-1.5,-1.5])

        tol = 1e-03
        max_eval = 1000

        solver_instance = CUATRO(tolerance=tol)
        results = solver_instance.run_optimiser(sim, x0=x0, max_f_eval=max_eval)

        self.assertTrue((results['N_eval'] < max_eval), "number of function evaluations is over the max allowed")
        self.assertTrue((results['TR'][-1] < tol), "radius was not smaller than tolerance")


class TestBudget(unittest.TestCase):
    def runTest(self):
        """
        check whether evaluation budget is used successfully as a termination criterion;low values for tolerance and max_f_eval
        """
        x0 = np.array([-1.5,-1.5])

        tol = 1e-10
        max_eval = 100
        
        # set N_min_samples to max_f_eval - 2 to force edge case where N_eval can't reach max_f_eval (need to have enough samples in trust region as well to work)
        solver_instance = CUATRO(tolerance=tol, N_min_samples=15)
        results = solver_instance.run_optimiser(sim, x0=x0, max_f_eval=max_eval)

        self.assertTrue(((results['N_eval'] == max_eval) or (results['N_eval'] == max_eval-1)), f"number of function evaluations was not equal to max allowed, it was {results['N_eval']}")
        self.assertTrue((results['TR'][-1] > tol), "radius was not bigger than tolerance")


class TestIterations(unittest.TestCase):
    def runTest(self):
        """
        check whether number of iterations is used successfully as a termination criterion;
        set high value for max_f_eval, low values for tolerance
        """
        x0 = np.array([-1.5,-1.5])

        tol = 1e-10
        max_eval = 10000

        solver_instance = CUATRO(tolerance=tol)
        results = solver_instance.run_optimiser(sim, x0=x0, max_f_eval=max_eval)

        self.assertTrue((results['N_eval'] < max_eval), "number of function evaluations was not smaller than max allowed")
        self.assertTrue((results['TR'][-1] > tol), "radius was not bigger than tolerance")


if __name__ == '__main__':
    unittest.main()
        








        

    
