import numpy as np
import functools
import multiprocessing
from time import perf_counter
from vbayesfa.lpa import lpa_model
from vbayesfa.finite_lpa import finite_lpa_model

def fit_mixture_model(x,
                      model_class = lpa_model,
                      n_workers = 4, 
                      restarts = 20, 
                      T = 20,
                      seed = 1234, 
                      tolerance = 1e-05, 
                      max_iter = 1000, 
                      min_iter = 10,
                      **prior_hpar):
    """
    Fit a mixture model using mean field variational Bayes.
    
    Parameters
    ----------
    x: data frame or array
        Observed data (data frame or matrix).  If a matrix then rows are variables and columns
        are observations; if a data frame then rows are observations and columns are variables.
    model_class: class, optional
        Class of mixture model to fit.
    n_workers: int, optional
        Number of workers in the pool for parallel processing; should be less than
        or equal to the number of available CPUs.
    restarts: int, optional
        Number of random restarts.
    T: integer, optional
        Truncation level of the variational approximation.
    seed: int, optional
        Random seed (determines starting conditions of each optimization).
    tolerance: float, optional
        Relative change in the ELBO at which the optimization should stop.
    max_iter: integer, optional
        Maximum number of iterations to run the optimization.
    min_iter: integer, optional
        Minimum number of iterations to run the optimization.
    prior_hpar:
        Prior hyperparameters (specified with keywords).
        
    Notes
    -----
    This creates multiple mixture model objects and fits them using parallel
    processing. See the documentation for the lpa_model object for more details.
    
    Output
    ------
    A dictionary with the following:
    
    final_elbo: list
        Final ELBO (evidence lower bound) values of each model.
    model_list: list
        Fitted model objects.
    best_model: mixture_model object
        Best fitted model (i.e. the one with the highest ELBO).
    fit_time: float
        Total time used to fit.
    """
    tic = perf_counter()

    model_list = []
    final_elbo = []
    
    with multiprocessing.Pool(n_workers) as pool:
        fun = functools.partial(__model_fit_wrapper__, x = x, T = T, model_class = model_class, tolerance = tolerance, max_iter = max_iter, min_iter = min_iter, **prior_hpar)
        
        # generate random seeds for each model based on the seed parameter
        seed_list = []
        rng = np.random.default_rng(seed)
        for i in range(restarts):
            seed_list += [rng.integers(low = 1000, high = 9999)]
        
        results = pool.map(fun, seed_list)
        for result in results:
            model_list += [result]
            final_elbo += [result.elbo_list[-1]]
        
    final_elbo = np.array(final_elbo)
    toc = perf_counter()
    
    return {'final_elbo': final_elbo, 'model_list': model_list, 'best_model': model_list[final_elbo.argmax()], 'fit_time': toc - tic}

def __model_fit_wrapper__(seed, x, T, model_class, tolerance, max_iter, min_iter, **prior_hpar):
    """
    Defines a mixture model and fits it to the data, returning the result.
    This function is only defined in order to get the parallelization to work.
    """
    new_model = model_class(x = x, T = T, seed = seed, **prior_hpar)
    new_model.fit(tolerance = tolerance, max_iter = max_iter, min_iter = min_iter)
    return new_model