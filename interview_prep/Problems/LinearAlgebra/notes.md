
# Determinants, Eigenvalues, and Eigenvectors

### Determinants: The Area/Volume Transformer

**Intuitive Understanding:**
The determinant tells us how a matrix transformation affects area (in 2D) or volume (in higher dimensions):
- Determinant = 2: transformation doubles area/volume
- Determinant = 0.5: transformation shrinks area/volume by half
- Determinant = 0: transformation collapses space (creates dependence)
- Negative determinant: transformation flips orientation

**Calculation Methods:**
- For 2×2 matrix [a b; c d]: det = ad - bc
- For larger matrices: cofactor expansion or row reduction

### Eigenvalues & Eigenvectors: The "Special Directions"

**Intuitive Understanding:**
- Eigenvectors are special vectors that maintain their direction when transformed by a matrix, only being stretched or shrunk
- Eigenvalues tell us the scaling factor applied to these special vectors
- If Av = λv, then v is an eigenvector with eigenvalue λ

**Geometric Meaning:**
- Eigenvectors represent invariant directions under transformation
- Eigenvalues represent scaling along these directions
- The complete set provides a coordinate system for understanding the transformation

## Quick Tricks for Interview Problems

### Determinant Shortcuts

1. **Triangular Matrix Trick:** If the matrix is triangular (upper or lower), the determinant equals the product of diagonal entries.

2. **Row/Column Operations:**
   - Swapping rows/columns: flips the sign of determinant
   - Multiplying a row/column by scalar k: multiplies determinant by k
   - Adding a multiple of one row to another: preserves determinant

3. **Zero Patterns:** A row or column of zeros means determinant = 0

4. **Special Cases:**
   - Identity matrix: determinant = 1
   - Block diagonal: determinant = product of block determinants

### Eigenvalue Shortcuts

1. **Trace-Determinant Method (for 2×2):**
   - Sum of eigenvalues = trace (diagonal sum)
   - Product of eigenvalues = determinant
   - Create quadratic: λ² - (trace)λ + determinant = 0

2. **Special Matrix Types:**
   - Diagonal/triangular matrices: eigenvalues = diagonal entries
   - Symmetric matrices: all eigenvalues are real
   - Orthogonal matrices: all eigenvalues have magnitude 1
   - Projection matrices: eigenvalues are only 0 or 1
   - Nilpotent matrices: all eigenvalues = 0

3. **Integer Matrices Trick:** For matrices with integer entries, rational eigenvalues must be divisors of the determinant

4. **Similarity Invariance:** Similar matrices (P⁻¹AP) have identical eigenvalues

### Eigenvector Computation

1. **Standard Method:** After finding eigenvalue λ, solve (A - λI)v = 0

2. **Symmetric Matrix Advantage:** Eigenvectors of different eigenvalues are perpendicular to each other

3. **Repeated Eigenvalues Alert:** May have fewer independent eigenvectors than the matrix dimension

4. **Algebraic vs Geometric Multiplicity:** The difference indicates "defectiveness"

## Interview Problem-Solving Strategy

### Step 1: Analyze the Matrix Structure
- Identify special properties: symmetric, triangular, orthogonal, etc.
- Note pattern of entries that might indicate shortcuts

### Step 2: Calculate Key Information
- For 2×2 and 3×3 matrices: calculate trace and determinant
- For 2×2: use the trace-determinant shortcut for eigenvalues

### Step 3: Find Eigenvalues
- Set up characteristic polynomial: det(A - λI) = 0
- Solve for λ (factoring when possible)
- Check results with trace/determinant properties

### Step 4: Find Eigenvectors
- For each eigenvalue λ, set up (A - λI)v = 0
- Solve the resulting system of equations
- Express the general solution in parametric form when needed

### Step 5: Verify Results
- Confirm Av = λv for each eigenpair
- Check that eigenvalue count matches expectations

## Worked Example

For the matrix A = [4 2; 1 3]:

1. **Quick Analysis:**
   - Trace = 4 + 3 = 7
   - Determinant = 4×3 - 2×1 = 12 - 2 = 10

2. **Eigenvalues:**
   - Characteristic equation: λ² - 7λ + 10 = 0
   - Factored form: (λ - 5)(λ - 2) = 0
   - Therefore: λ₁ = 5, λ₂ = 2

3. **Eigenvectors:**
   - For λ₁ = 5:
     - Set up [4-5 2; 1 3-5][x; y] = [0; 0]
     - Gives [-1 2; 1 -2][x; y] = [0; 0]
     - This means x = 2y
     - Eigenvector v₁ = [2; 1] (or any multiple)
   
   - For λ₂ = 2:
     - Set up [4-2 2; 1 3-2][x; y] = [0; 0]
     - Gives [2 2; 1 1][x; y] = [0; 0]
     - This means x = -y
     - Eigenvector v₂ = [-1; 1] (or any multiple)

4. **Verification:**
   - A[2; 1] = [4×2 + 2×1; 1×2 + 3×1] = [10; 5] = 5[2; 1] ✓
   - A[-1; 1] = [4×(-1) + 2×1; 1×(-1) + 3×1] = [-2; 2] = 2[-1; 1] ✓

## Applications to Highlight

During an interview, mentioning these applications demonstrates deeper understanding:

1. **Diagonalization:** Finding P such that P⁻¹AP is diagonal simplifies matrix powers

2. **Principal Component Analysis:** Eigenvectors of covariance matrices identify main data variation directions

3. **Markov Chains:** The eigenvector with eigenvalue 1 represents the steady-state distribution

4. **Differential Equations:** Eigenvalues determine stability of solutions

5. **Google's PageRank:** The primary eigenvector of the web graph represents page importance

## Common Interview Questions

1. "What does it mean if a matrix has a zero eigenvalue?"
   - The transformation collapses space in some direction
   - The matrix is singular (non-invertible)
   - The nullspace is non-trivial

2. "What's the relationship between eigenvectors of A and A⁻¹?"
   - Same eigenvectors, but eigenvalues are reciprocals (1/λ)

3. "What happens to eigenvalues when you multiply a matrix by a scalar?"
   - All eigenvalues get multiplied by that scalar

4. "How do eigenvalues relate to the trace and determinant?"
   - Sum of eigenvalues = trace
   - Product of eigenvalues = determinant

5. "What can you say about eigenvalues of a rotation matrix?"
   - For 2D rotation matrices, eigenvalues are complex conjugates with magnitude 1

Remember: In an interview, clearly explaining your approach often matters as much as getting the final answer right. Don't just apply formulas—demonstrate understanding of the underlying concepts.