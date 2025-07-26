# B859：cdist-如何估计反事实的分布特征？

介绍 `cdist` 命令的理论基础和应用。 
```stata
ssc install cdist, replace 
ssc install moremata, replace  // 需要利用该程序包提供的函数
net get cdist.pkg, replace //作者提供的辅助资料
```

`cdist` estimates counterfactual distributions using methods suggested by Chernozhukov et al. (2013). The unconditional (counterfactual) distributions are either obtained by distribution regression using `logit` models or by a linear quantile regression process (using `mm_qr()` from the `moremata` package).

For an alternative implementation of these (and related) methods see package [counterfactual](https://raw.githubusercontent.com/bmelly/Stata/main/) by Blaise Melly (type the following command:
```stata
net from https://raw.githubusercontent.com/bmelly/Stata/main/
```
the package also includes commands `cdeco` and `cdeco_jmp` to perform counterfactual decompositions).

## References

- Chernozhukov, Victor, Iván Fernández-Val, Blaise Melly. 2013. Inference on Counterfactual Distributions. Econometrica 81(6):2205–2268.
- Chernozhukov, Victor, Iván Fernández-Val, Blaise Melly. 2022. Fast algorithms for the quantile regression process. Empirical Economics 62(1):7–33.
- Juhn, Chinhui, Kevin M. Murphy, Brooks Pierce. 1993. Wage Inequality and the Rise in Returns to Skill. Journal of Political Economy 101(3):410-442.
- Portnoy, Stephen, Roger Koenker. 1997. The Gaussian hare and the Laplacian tortoise: computability of squared-error versus absolute-error estimators. Statistical Science 12(4):279-300.
