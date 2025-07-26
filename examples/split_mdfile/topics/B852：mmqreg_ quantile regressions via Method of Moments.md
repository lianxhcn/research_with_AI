# B852：mmqreg: quantile regressions via Method of Moments

> Method of Moments Quantile Regression (MMQR) with fixed effects

`mmqreg` estimates quantile regressions using the method of moments as described in Machado and Santos Silva (2019, **JoE**), and expanding the methodology to allow for multiple fixed effects.

In contrast with `xtqreg`, `mmqreg` adds three features to the estimation of this type of models:
1. It allows the estimation of the Location-Scale quantile regressions when there are no fixed effects.
2. Using the command `hdfe` it allows the estimation of LS quantile regression absorbing multiple fix effects
3. It reports the estimation of various quantiles jointly, which facilitates testing of coefficients across quantiles, using **resampling methods** like Bootstrap. (see bootstrap), or based on analytical standard errors.

Also, in contrast with `xtqreg`, standard errors for quantiles, location, and scale effects, can be estimated adjusting for the degrees of freedom.

Furthermore, because this is a GMM estimator, `mmqreg` also provides 3 options for standard errors, the default which is the same as `xtqreg`, robust standard errors, and clustered standard errors.

- 参考资料
- Machado, J.A.F. and Santos Silva, J.M.C. (2019), Quantiles via Moments, Journal of Econometrics, 213(1), pp. 145-173.
- Rios-Avila, Fernando (2020), Extending Quantile regressions via Method of Moments using multiple fixed effects. MIMEO
 
## 安装
```stata
. ssc install hdfe, replace 
. ssc install ftools, replace 

. ssc install mmqreg, replace 
. net get mmqreg.pkg, replace  // 作者提供的范例数据
```
