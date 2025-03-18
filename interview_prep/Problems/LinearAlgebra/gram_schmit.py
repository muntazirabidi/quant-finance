import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from matplotlib.animation import FuncAnimation

def plot_vectors(ax, vectors, colors, alphas=None, labels=None):
    """Plot vectors as arrows starting from the origin."""
    if alphas is None:
        alphas = [1] * len(vectors)
    if labels is None:
        labels = [None] * len(vectors)
    
    arrows = []
    for v, c, a, l in zip(vectors, colors, alphas, labels):
        arrow = FancyArrowPatch((0, 0), v, color=c, alpha=a,
                               arrowstyle='-|>', mutation_scale=15)
        ax.add_patch(arrow)
        arrows.append(arrow)
        if l:
            ax.text(v[0], v[1], l, fontsize=12)
    return arrows

def animate_gram_schmidt(A):
    """Create an animation of the Gram-Schmidt process for a 2x2 matrix."""
    a1 = A[:, 0]  # First column of A
    a2 = A[:, 1]  # Second column of A
    
    # Step 1: Normalize a1 to get q1
    q1 = a1 / np.linalg.norm(a1)
    
    # Step 2: Calculate projection and orthogonalize
    projection = np.dot(a2, q1) * q1
    v2 = a2 - projection
    q2 = v2 / np.linalg.norm(v2)
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.grid(True)
    ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    ax.set_aspect('equal')
    
    # Title and text objects
    title = ax.set_title('Gram-Schmidt Orthogonalization', fontsize=14)
    info_text = ax.text(-2.8, -2.8, '', fontsize=12, bbox=dict(facecolor='white', alpha=0.7))
    
    # Initialize vectors (will be updated in animation)
    colors = ['r', 'b', 'g', 'y', 'm', 'purple']
    vectors = [a1, a2, np.zeros(2), np.zeros(2), np.zeros(2), np.zeros(2)]
    labels = ['$a_1$', '$a_2$', '', '', '', '']
    alphas = [1, 1, 0, 0, 0, 0]
    arrows = plot_vectors(ax, vectors, colors, alphas, labels)
    
    def animate(frame):
        if frame < 10:  # Show original vectors
            title.set_text('Original Column Vectors of Matrix A')
            info_text.set_text('Showing the original column vectors of matrix A.')
            # Everything stays the same
            
        elif frame < 20:  # Normalize first vector
            title.set_text('Step 1: Normalize First Vector')
            info_text.set_text('Normalizing $a_1$ to get $q_1$ (unit length)')
            
            # Interpolate between a1 and q1
            t = (frame - 10) / 10
            v = (1-t) * a1 + t * q1
            arrows[2].set_positions((0, 0), v)
            
            # Update display properties
            if frame == 10:  # First frame of this section
                arrows[2].set_alpha(0.8)
                labels[2] = '$q_1$'
                ax.text(q1[0], q1[1], labels[2], fontsize=12)
                arrows[2].set_color('g')
                
        elif frame < 30:  # Show projection
            title.set_text('Step 2a: Calculate Projection')
            info_text.set_text('Projecting $a_2$ onto $q_1$ to find component in that direction')
            
            # Show q1
            arrows[2].set_positions((0, 0), q1)
            arrows[2].set_alpha(0.8)
            
            # Show projection
            t = (frame - 20) / 10
            p = t * projection
            arrows[3].set_positions((0, 0), p)
            
            # Update display properties
            if frame == 20:  # First frame of this section
                arrows[3].set_alpha(0.8)
                labels[3] = 'proj'
                ax.text(projection[0], projection[1], labels[3], fontsize=12)
                arrows[3].set_color('y')
            
        elif frame < 40:  # Subtract projection
            title.set_text('Step 2b: Subtract Projection')
            info_text.set_text('Subtracting projection to get orthogonal vector $v_2$')
            
            # Show the subtraction visually
            arrows[3].set_positions((0, 0), projection)
            arrows[3].set_alpha(0.8)
            
            # Draw vector from projection to a2
            t = (frame - 30) / 10
            diff_vector = t * (a2 - projection)
            arrows[4].set_positions((projection), (projection + diff_vector))
            
            # Update display properties
            if frame == 30:  # First frame of this section
                arrows[4].set_alpha(0.8)
                labels[4] = '$v_2$'
                ax.text(v2[0], v2[1], labels[4], fontsize=12)
                arrows[4].set_color('m')
                
        elif frame < 50:  # Normalize second orthogonal vector
            title.set_text('Step 2c: Normalize Second Vector')
            info_text.set_text('Normalizing $v_2$ to get $q_2$ (unit length)')
            
            # Move v2 to origin and normalize
            arrows[4].set_positions((0, 0), v2)
            
            # Interpolate between v2 and q2
            t = (frame - 40) / 10
            v = (1-t) * v2 + t * q2
            arrows[5].set_positions((0, 0), v)
            
            # Update display properties
            if frame == 40:  # First frame of this section
                arrows[5].set_alpha(0.8)
                labels[5] = '$q_2$'
                ax.text(q2[0], q2[1], labels[5], fontsize=12)
                arrows[5].set_color('purple')
                
        else:  # Final orthonormal basis
            title.set_text('Final Orthonormal Basis (Q columns)')
            
            # Calculate R matrix for display
            r11 = np.dot(q1, a1)
            r12 = np.dot(q1, a2)
            r22 = np.dot(q2, a2)
            R = np.array([[r11, r12], [0, r22]])
            
            info_text.set_text(f'Q = [{q1[0]:.2f}, {q2[0]:.2f}; {q1[1]:.2f}, {q2[1]:.2f}]\n' +
                            f'R = [{r11:.2f}, {r12:.2f}; 0, {r22:.2f}]')
            
            # Show only the orthonormal basis
            arrows[0].set_alpha(0.2)  # Fade a1
            arrows[1].set_alpha(0.2)  # Fade a2
            arrows[3].set_alpha(0.2)  # Fade projection
            arrows[4].set_alpha(0.2)  # Fade v2
            
            arrows[2].set_alpha(1)  # Highlight q1
            arrows[5].set_alpha(1)  # Highlight q2
            
        return arrows + [title, info_text]
    
    anim = FuncAnimation(fig, animate, frames=60, interval=200, blit=False)
    plt.close()  # Prevent the static plot from displaying
    
    return anim

# Example usage
A = np.array([[2, 1], [1, 1]])
anim = animate_gram_schmidt(A)

# To save the animation (uncomment if needed)
# anim.save('gram_schmidt.gif', writer='pillow', fps=5)

# Display animation in some environments (e.g., Jupyter notebook)
# from IPython.display import HTML
# HTML(anim.to_jshtml())