import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Rectangle

def create_region_plot(x_value):
    """
    Create a plot showing the integration region for a specific value of x.
    
    Args:
        x_value (float): The value of x for which to show UV ≤ x
    """
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # Set up the plot
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel('U', fontsize=12)
    ax.set_ylabel('V', fontsize=12)
    ax.set_title(f'Integration Region for x = {x_value:.2f}', fontsize=14)
    
    # Create grid
    ax.grid(True, linestyle='--', alpha=0.3)
    
    # Create the hyperbola points UV = x
    u = np.linspace(x_value, 1, 1000)
    v = x_value / u
    
    # Mask points where v > 1
    mask = v <= 1
    u, v = u[mask], v[mask]
    
    # Plot the hyperbola
    ax.plot(u, v, 'r--', label='UV = x')
    
    # Fill the region where UV ≤ x
    u_fill = np.linspace(0, 1, 100)
    v_fill = np.minimum(1, x_value / u_fill)
    ax.fill_between(u_fill, 0, v_fill, alpha=0.3, color='blue', label='UV ≤ x')
    
    # Add legend
    ax.legend(fontsize=10)
    
    # Add text showing the integral value
    if x_value > 0:
        integral_value = x_value * (1 - np.log(x_value))
        ax.text(0.05, 0.95, f'F_X(x) = {integral_value:.3f}', 
                transform=ax.transAxes, fontsize=12, 
                bbox=dict(facecolor='white', alpha=0.8))
    
    return fig, ax

def create_animation():
    """
    Create an animation showing how the region changes with x.
    """
    fig, ax = plt.subplots(figsize=(10, 10))
    
    def update(frame):
        ax.clear()
        x_value = frame / 20  # This will give us x values from 0 to 1
        
        # Set up the plot
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_xlabel('U', fontsize=12)
        ax.set_ylabel('V', fontsize=12)
        ax.set_title(f'Integration Region for x = {x_value:.2f}', fontsize=14)
        ax.grid(True, linestyle='--', alpha=0.3)
        
        # Create the hyperbola points UV = x
        if x_value > 0:
            u = np.linspace(x_value, 1, 1000)
            v = x_value / u
            mask = v <= 1
            u, v = u[mask], v[mask]
            ax.plot(u, v, 'r--', label='UV = x')
        
        # Fill the region where UV ≤ x
        u_fill = np.linspace(0, 1, 100)
        v_fill = np.minimum(1, x_value / u_fill)
        ax.fill_between(u_fill, 0, v_fill, alpha=0.3, color='blue', label='UV ≤ x')
        
        # Add legend
        ax.legend(fontsize=10)
        
        # Add text showing the integral value
        if x_value > 0:
            integral_value = x_value * (1 - np.log(x_value))
            ax.text(0.05, 0.95, f'F_X(x) = {integral_value:.3f}', 
                    transform=ax.transAxes, fontsize=12,
                    bbox=dict(facecolor='white', alpha=0.8))
        
        return ax,
    
    ani = FuncAnimation(fig, update, frames=21, interval=500, blit=True)
    return ani

# Create static plots for specific x values
def create_multiple_plots():
    """
    Create multiple plots showing the region for different x values.
    """
    x_values = [0.2, 0.4, 0.6, 0.8]
    fig, axes = plt.subplots(2, 2, figsize=(15, 15))
    
    for ax, x_value in zip(axes.flat, x_values):
        # Create the hyperbola points UV = x
        u = np.linspace(x_value, 1, 1000)
        v = x_value / u
        mask = v <= 1
        u, v = u[mask], v[mask]
        
        # Set up the plot
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_xlabel('U', fontsize=12)
        ax.set_ylabel('V', fontsize=12)
        ax.set_title(f'x = {x_value:.2f}', fontsize=14)
        ax.grid(True, linestyle='--', alpha=0.3)
        
        # Plot the hyperbola
        ax.plot(u, v, 'r--', label='UV = x')
        
        # Fill the region where UV ≤ x
        u_fill = np.linspace(0, 1, 100)
        v_fill = np.minimum(1, x_value / u_fill)
        ax.fill_between(u_fill, 0, v_fill, alpha=0.3, color='blue', label='UV ≤ x')
        
        # Add legend
        ax.legend(fontsize=10)
        
        # Add text showing the integral value
        integral_value = x_value * (1 - np.log(x_value))
        ax.text(0.05, 0.95, f'F_X(x) = {integral_value:.3f}', 
                transform=ax.transAxes, fontsize=12,
                bbox=dict(facecolor='white', alpha=0.8))
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Create static plots
    create_multiple_plots()
    
    # Create a single plot for x = 0.5
    fig, ax = create_region_plot(0.5)
    plt.show()
    
    # Create animation
    ani = create_animation()
    plt.show()