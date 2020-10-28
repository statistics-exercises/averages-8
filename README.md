# Method of moments for binomial random variable

The probability mass function for for the binomial random variable is the function of two parameters shown below:

![](https://render.githubusercontent.com/render/math?math=P(X=x)=\binom{k}{x}p^x(1-p)^{k-x})

Furthermore, as was explained in the video, we can thus derive the following expressions that relate the first and second moments of this distribution to the parameters in the above expression.

![](https://render.githubusercontent.com/render/math?math=\mathbb{E}(X)=kp\qquad\mathbb{E}(X^2)=kp(1-p)%2Bk^2p^2)

We can calculate estimates of the first and second moments of this distribution by sampling from the distribution multiple times and by computing the following two quantities.

![](https://render.githubusercontent.com/render/math?math=\overline{X}=\frac{1}{n}\sum_{i=1}^{n}X_i\qquad\widehat{\mu_2}=\frac{1}{n}\sum_{i=1}^{n}X_i^2)

As was discussed in the comprehension exercise we can thus use the method of moments to obtain the following estimators for the two parameters of the distribution:

![](https://render.githubusercontent.com/render/math?math=\widehat{p}=1%2B\overline{X}-\frac{\widehat{\mu_2}}{\overline{X}}\qquad\widehat{k}=\frac{\overline{X}}{\widehat{p}})

__With that in mind, the aim is for you to write a code to investigate how these two method of moments estimators for the parameters of a Binomial random variable depend on the number of samples they are computed from.__  To complete the exercise you will need to

1. Finish the function `binomial`. This function should take two parameters `k` and `p`. It should return a Binomial random variable from a distribution with parameters `k` and `p`. 
2. Set the first element of the list called `indices` equal to 1, the second element of the list called `indices` to 2 and so on.
3. Set the first element of the list called `p_estimator` equal to an estimate of the p parameter of the distribution that is calculated by generating 1 Binomial random variable with parameters `kval` and `pval`, the second element of the list `p_estimator` equal to an estimate of the p parameter of the distribution that is calculated by generating 2 Binomial random variables with parameters `kval` and `pval`, set the third element of the list called `p_estimator` equal to an estimate of the parameter of the distribution that is calculated by generating 3 Binomial random variables with parameters `kval` and `pval` and so on until you have computed an estimate of the p parameter of the distribution from 200 Binmomial  random variables. 
4. Set the first element of the list called `k_estimator` equal to an estimate of the k parameter of the distribution that is calculated by generating 1 Binomial random variable with parameters `kval` and `pval`, the second element of the list `k_estimator` equal to an estimate of the k parameter of the distribution that is calculated by generating 2 Binomial random variables with parameters `kval` and `pval`, set the third element of the list called `k_estimator` equal to an estimate of the parameter of the distribution that is calculated by generating 3 Binomial random variables with parameters `kval` and `pval` and so on until you have computed an estimate of the k parameter of the distribution from 200 Binmomial  random variables. 

When your code is complete a graph will be generated.  The red dots are the values of the method of moments estimator for the p parameter of the distribution you sampled from.  The black dashed line is then the true value of the parameter.  The blue dots are the values of the method of moments estimator for the k parameter of the distribution you sampled from.  The green dashed line is then the true value of the parameter.  
