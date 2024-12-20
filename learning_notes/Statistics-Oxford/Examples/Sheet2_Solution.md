# Question 1

> A two-part question about statistical inference:

> What is the connection between Fisher's information and the asymptotic distribution of the maximum likelihood estimator?

> Assume the individuals in a sample of size $n = 1029$ are independent and that each individual has blood type M with probability $(1-\theta)^2$, type MN with probability $2\theta(1-\theta)$, and type N with probability $\theta^2$. For the following data (Rice, 2007) find the maximum likelihood estimate $\hat{\theta}$ and use the asymptotic distribution of the MLE to find an approximate 95% confidence interval for $\theta$.

> | Blood Type | Frequency |
> | ---------- | --------- |
> | M          | 342       |
> | MN         | 500       |
> | N          | 187       |

This question elegantly combines theoretical concepts of Fisher information with their practical application in genetic data analysis. It tests understanding of:

- The asymptotic theory of maximum likelihood estimation
- The role of Fisher information in determining estimation precision
- Practical computation of MLEs and confidence intervals
- Application to real genetic data following Hardy-Weinberg proportions

The problem requires both theoretical understanding and practical statistical computation skills. Note how the blood type frequencies follow a trinomial distribution with probabilities determined by a single parameter $\theta$, making this an interesting case study in constrained parameter estimation.
