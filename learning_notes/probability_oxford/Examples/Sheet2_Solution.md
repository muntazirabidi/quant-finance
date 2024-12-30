# Question 1: Joint Distribution in Polar Coordinates

Let $X$ and $Y$ be independent standard normal random variables. Define $R$ and $\Theta$ by the transformation:
$X = R\cos(\Theta)$
$Y = R\sin(\Theta)$

- (a) Find the joint distribution of $R$ and $\Theta$.

## Solution

Let's solve this step by step using the change of variables formula.

Since $X$ and $Y$ are independent standard normal variables, their joint probability density function (PDF) is:

$f_{X,Y}(x,y) = \frac{1}{2\pi} e^{-(x^2 + y^2)/2}$

To transform from $(x,y)$ to $(r,\theta)$, we need the Jacobian matrix. The partial derivatives are:

$\frac{\partial x}{\partial r} = \cos(\theta)$ &nbsp;&nbsp;&nbsp; $\frac{\partial x}{\partial \theta} = -r\sin(\theta)$

$\frac{\partial y}{\partial r} = \sin(\theta)$ &nbsp;&nbsp;&nbsp; $\frac{\partial y}{\partial \theta} = r\cos(\theta)$

The Jacobian determinant is:
$|J| = \begin{vmatrix} 
\cos(\theta) & -r\sin(\theta) \\
\sin(\theta) & r\cos(\theta)
\end{vmatrix}$

$|J| = r\cos^2(\theta) + r\sin^2(\theta) = r$

In polar coordinates:
$x^2 + y^2 = (r\cos(\theta))^2 + (r\sin(\theta))^2 = r^2(\cos^2(\theta) + \sin^2(\theta)) = r^2$

The joint PDF of $R$ and $\Theta$ is:

$f_{R,\Theta}(r,\theta) = f_{X,Y}(r\cos(\theta), r\sin(\theta)) \cdot |J|$

Substituting:

$f_{R,\Theta}(r,\theta) = \frac{1}{2\pi} e^{-r^2/2} \cdot r$

$f_{R,\Theta}(r,\theta) = \frac{r}{2\pi} e^{-r^2/2}$

where $r \geq 0$ and $0 \leq \theta < 2\pi$

Notice that the joint distribution can be factored:

$f_{R,\Theta}(r,\theta) = (r e^{-r^2/2}) \cdot (\frac{1}{2\pi})$

This factorization reveals that $R$ and $\Theta$ are independent random variables where:

1. $\Theta$ follows a uniform distribution over $[0, 2\pi)$:
   $f_{\Theta}(\theta) = \frac{1}{2\pi}$

2. $R$ follows a Rayleigh distribution:
   $f_R(r) = r e^{-r^2/2}$ for $r \geq 0$

This transformation from Cartesian to polar coordinates gives us an elegant result where the radius and angle are independent, despite starting with correlated Cartesian coordinates in the transformed space.
