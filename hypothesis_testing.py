def reject(pvalue, alpha_levels=[.05,.01,.005]):

	assert pvalue >= 0.
	assert pvalue <= 1.

	print('The probability of null hypothesis is {}% so we'.format(100*pvalue))
	
	for critical in alpha_levels:
	    if critical > pvalue:
	        print('reject null hypothesis at {}% confidence interval.'.format(100*(1-critical)))
	    else:
	        print('do not reject null hypothesis at {}% confidence interval.'.format(100*(1-critical)))
