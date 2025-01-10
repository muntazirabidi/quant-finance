import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def create_streak_animation(n_flips=50):
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(12, 3))
    
    # Generate random flips
    flips = np.random.choice(['H', 'T'], size=n_flips)
    
    def animate(frame):
        ax.clear()
        # Show flips up to current frame
        current_flips = flips[:frame+1]
        # Color consecutive streaks
        colors = []
        current_streak = 1
        for i in range(len(current_flips)):
            if i > 0 and current_flips[i] == current_flips[i-1]:
                current_streak += 1
            else:
                current_streak = 1
            if current_streak >= 3:  # Highlight streaks of 3 or more
                colors.append('red')
            else:
                colors.append('blue')
                
        # Plot flips
        for i, (flip, color) in enumerate(zip(current_flips, colors)):
            ax.text(i, 0, flip, color=color, fontsize=14)
            
        ax.set_xlim(-1, n_flips)
        ax.set_ylim(-1, 1)
        ax.axis('off')
        
    return animation.FuncAnimation(fig, animate, frames=n_flips, interval=200)
  

def show_streak_windows():
    n_flips = 20  # Smaller number for clarity
    flips = np.random.choice(['H', 'T'], size=n_flips)
    
    fig, axes = plt.subplots(3, 1, figsize=(12, 6))
    
    # Show full sequence
    axes[0].text(0, 0, ' '.join(flips), fontsize=12)
    axes[0].set_title("Full Sequence")
    
    # Show overlapping windows of length 5
    for i in range(n_flips-4):
        window = flips[i:i+5]
        axes[1].text(i, 0, ' '.join(window), fontsize=12)
    axes[1].set_title("All Possible 5-Flip Windows")
    
    # Highlight successful streak windows
    for i in range(n_flips-4):
        window = flips[i:i+5]
        if len(set(window)) == 1:  # All same value
            axes[2].text(i, 0, ' '.join(window), fontsize=12, color='red')
        else:
            axes[2].text(i, 0, ' '.join(window), fontsize=12, alpha=0.3)
    axes[2].set_title("Successful Streak Windows Highlighted")
    
    for ax in axes:
        ax.axis('off')
    plt.tight_layout()
    
    
show_streak_windows()