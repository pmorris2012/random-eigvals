#!/bin/sh

#SBATCH --job-name=eigvals
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=20
#SBATCH --mem=4gb
#SBATCH --output=logs/eigvals_%j.log

#load modules
module load miniconda3-4.6.14-gcc-8.3.0-eenl5dj
source activate eigenvalues

# Execute the task
python3 generate_eigenvalues.py