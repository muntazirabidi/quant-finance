# Expected Number of Intersections of Brownian Paths

## 1. One-Dimensional Case

### 1.1 Problem Setup

Let $ B_1(t) $ and $ B_2(t) $ be two independent one-dimensional Brownian motions. Define the difference process:

$$ Z(t) = B_1(t) - B_2(t). $$

The paths intersect whenever \( Z(t) = 0 \). We aim to calculate the **expected number of zeros** of $ Z(t) $ in the interval $[0, T]$.

---

### 1.2 Properties of the Difference Process

1. $Z(t) $ is itself a Brownian motion:

   - $ Z(0) = 0 $
   - Variance of $ Z(t) $:
     $$ \text{Var}(Z(t)) = \text{Var}(B_1(t)) + \text{Var}(B_2(t)) = 2t. $$

2. Scaling relation:
   $$ Z(t) = \sqrt{2} B(t), $$
   where $B(t) $ is a standard Brownian motion.

---

### 1.3 Expected Number of Zeros

For a standard Brownian motion $ B(t) $, the expected number of zeros in $[0, T]$ is:

$$ \mathbb{E}[N(T)] = \frac{2}{\pi} \sqrt{T}. $$

For $ Z(t) = \sqrt{2} B(t) $, the scaling factor does not affect the zero-crossings, so:

$$ \mathbb{E}[N(T)] = \frac{2}{\pi} \sqrt{T}. $$

#### Derivation:

1. **Time Scaling of Brownian Motion**:
   The zero-crossing events of a Brownian motion are determined by its sample path properties, specifically the oscillatory nature of the path.

2. **Crossing Events as Poisson Process**:
   The expected number of zeros is proportional to the square root of the variance of the process. For standard Brownian motion, $\text{Var}(B(t)) = t $, and the crossing rate grows as $ \sqrt{t}$.

3. **Normalization Factor**:
   The factor $ \frac{2}{\pi} $ arises from the explicit calculation of the probability density of zeros based on the underlying Gaussian process and scaling constants.

For $Z(t) = \sqrt{2} B(t) $, the scaling factor $ \sqrt{2} $ does not affect the number of zeros, so:

$$ \mathbb{E}[N(T)] = \frac{2}{\pi} \sqrt{T}. $$

---

### 1.4 Adding Correlation

If $ B_1(t) $ and $ B_2(t) $ are correlated with coefficient $ \rho $, the variance of $ Z(t) $ becomes:

$$ \text{Var}(Z(t)) = 2(1 - \rho)t. $$

The expected number of zeros scales as:

$$ \mathbb{E}[N(T)] = \frac{2}{\pi} \sqrt{\frac{T}{1 - \rho}}. $$

---

## 2. Two-Dimensional Case

### 2.1 Problem Setup

Let $ \mathbf{B}\_1(t) = (X_1(t), Y_1(t))$ and $ \mathbf{B}\_2(t) = (X_2(t), Y_2(t)) $ be two independent 2D Brownian motions. The relative motion is:

$$ \mathbf{Z}(t) = \mathbf{B}\_1(t) - \mathbf{B}\_2(t). $$

The paths intersect whenever $ \mathbf{Z}(t) = \mathbf{0} $. We aim to calculate the **expected number of intersections** of the paths in $[0, T]$.

---

### 2.2 Distribution of Intersections

The relative motion $\mathbf{Z}(t) = (Z_X(t), Z_Y(t)) $ is a 2D Brownian motion with variance:

$$ \text{Var}(Z_X(t)) = \text{Var}(Z_Y(t)) = 2t. $$

The probability density for $ \mathbf{Z}(t) $ to be at the origin is given by the **Green's function**:

$$ G(\mathbf{0}, t) = \frac{1}{4\pi t}. $$

---

### 2.3 Expected Number of Intersections

The expected number of intersections is the integral of $ G(\mathbf{0}, t) $ over time:

$$ \mathbb{E}[N(T)] = \int_0^T G(\mathbf{0}, t) dt = \int_0^T \frac{1}{4\pi t} dt. $$

To handle the divergence as $ t \to 0 $, introduce a cutoff $ \epsilon > 0 $:

$$ \mathbb{E}[N(T)] = \frac{1}{4\pi} \int\_\epsilon^T \frac{1}{t} dt. $$

The integral evaluates to:

$$ \mathbb{E}[N(T)] \propto \frac{1}{4\pi} \log\left(\frac{T}{\epsilon}\right). $$

---

### 2.4 Incorporating Correlation

If the 2D Brownian motions are correlated with coefficient $ \rho $, the diffusivity is reduced by $ (1 - \rho^2) $. The probability density becomes:

$$ G(\mathbf{0}, t) = \frac{1}{4\pi (1 - \rho^2)t}. $$

The expected number of intersections scales as:

$$ \mathbb{E}[N(T)] \propto \frac{T}{\log(T)}(1 - \rho^2). $$

---

## 3. Summary of Results

### 1D Brownian Motion:

For two 1D Brownian motions:

$$ \mathbb{E}[N(T)] = \frac{2}{\pi} \sqrt{\frac{T}{1 - \rho}}. $$

### 2D Brownian Motion:

For two 2D Brownian motions:

$$ \mathbb{E}[N(T)] \propto \frac{T}{\log(T)}(1 - \rho^2). $$

The difference in scaling arises from the dimensionality, where 2D intersections are less frequent due to the extra spatial degree of freedom.
