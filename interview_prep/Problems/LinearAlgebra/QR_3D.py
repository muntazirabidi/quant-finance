import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

class Arrow3D(FancyArrowPatch):
    """A custom 3D arrow class for matplotlib."""
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)

def visualize_qr_3d(A):
    """Visualize QR decomposition for a 3x3 matrix."""
    # Compute QR decomposition
    Q, R = np.linalg.qr(A)
    
    # Create figure
    fig = plt.figure(figsize=(18, 6))
    
    # Plot original vectors (columns of A)
    ax1 = fig.add_subplot(131, projection='3d')
    ax1.set_title('Original Matrix A Columns')
    ax1.set_xlim([-2, 2])
    ax1.set_ylim([-2, 2])
    ax1.set_zlim([-2, 2])
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')
    
    # Draw coordinate axes
    ax1.plot([0, 2], [0, 0], [0, 0], 'k--', alpha=0.2)
    ax1.plot([0, 0], [0, 2], [0, 0], 'k--', alpha=0.2)
    ax1.plot([0, 0], [0, 0], [0, 2], 'k--', alpha=0.2)
    
    # Draw A columns as arrows
    for i in range(A.shape[1]):
        a = Arrow3D([0, A[0, i]], [0, A[1, i]], [0, A[2, i]], 
                   mutation_scale=20, lw=2, arrowstyle='-|>', color='r')
        ax1.add_artist(a)
        ax1.text(A[0, i], A[1, i], A[2, i], f'a{i+1}')
    
    # Plot orthogonal vectors (columns of Q)
    ax2 = fig.add_subplot(132, projection='3d')
    ax2.set_title('Orthogonal Matrix Q Columns')
    ax2.set_xlim([-2, 2])
    ax2.set_ylim([-2, 2])
    ax2.set_zlim([-2, 2])
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_zlabel('Z')
    
    # Draw coordinate axes
    ax2.plot([0, 2], [0, 0], [0, 0], 'k--', alpha=0.2)
    ax2.plot([0, 0], [0, 2], [0, 0], 'k--', alpha=0.2)
    ax2.plot([0, 0], [0, 0], [0, 2], 'k--', alpha=0.2)
    
    # Draw Q columns as arrows
    for i in range(Q.shape[1]):
        q = Arrow3D([0, Q[0, i]], [0, Q[1, i]], [0, Q[2, i]], 
                   mutation_scale=20, lw=2, arrowstyle='-|>', color='g')
        ax2.add_artist(q)
        ax2.text(Q[0, i], Q[1, i], Q[2, i], f'q{i+1}')
    
    # Visualize R as a heatmap
    ax3 = fig.add_subplot(133)
    ax3.set_title('Upper Triangular Matrix R')
    im = ax3.imshow(R, cmap='viridis')
    
    # Add color bar
    cbar = plt.colorbar(im, ax=ax3, orientation='vertical')
    cbar.set_label('Value')
    
    # Add text annotations with values
    for i in range(R.shape[0]):
        for j in range(R.shape[1]):
            text = ax3.text(j, i, f'{R[i, j]:.2f}',
                          ha="center", va="center", color="w" if abs(R[i, j]) > 0.5 else "k")
    
    plt.tight_layout()
    
    # Print the matrices
    print("Original Matrix A:")
    print(A)
    print("\nOrthogonal Matrix Q:")
    print(Q)
    print("\nUpper Triangular Matrix R:")
    print(R)
    print("\nVerification A = QR:")
    print(np.matmul(Q, R))
    
    return fig, Q, R

# Example usage with a 3x3 matrix
A = np.array([
    [2, 1, 0],
    [1, 1, 1],
    [0, 1, 2]
])
fig, Q, R = visualize_qr_3d(A)
plt.show()