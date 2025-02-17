import os

def create_project_structure(base_dir):
    structure = {
        "config": ["__init__.py", "settings.py", "symbols.py"],
        "data": ["__init__.py", "data_loader.py", "market_data.py"],
        "models": ["__init__.py", "garch.py", "risk_metrics.py", "volatility.py"],
        "analysis": ["__init__.py", "clustering.py", "regime.py"],
        "portfolio": ["__init__.py", "optimization.py", "risk_manager.py"],
        "visualization": ["__init__.py", "dashboard.py", "plots.py"],
        "utils": ["__init__.py", "helpers.py", "validation.py"],
    }
    
    os.makedirs(base_dir, exist_ok=True)
    
    # Create main files
    for filename in ["README.md", "requirements.txt"]:
        open(os.path.join(base_dir, filename), 'w').close()
    
    # Create subdirectories and files
    for subdir, files in structure.items():
        subdir_path = os.path.join(base_dir, subdir)
        os.makedirs(subdir_path, exist_ok=True)
        for file in files:
            open(os.path.join(subdir_path, file), 'w').close()

if __name__ == "__main__":
    create_project_structure("volatility_dashboard")
