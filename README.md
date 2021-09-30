# random-eigvals

```python3
import numpy as np
import matplotlib.pyplot as plt


n = 512
iterations = 100
histogram_bins = 1000


eigenvalues = np.zeros((iterations, n), dtype=np.complex64)
vectors = np.random.randn(n, n)

for i in range(iterations):
    eigenvalues[i], vectors = np.linalg.eig(vectors)
    
histogram = np.histogram2d(
    eigenvalues.real.reshape(-1),
    eigenvalues.imag.reshape(-1),
    bins=histogram_bins,
    range=[[-2, 2], [-2, 2]],
    density=True
)[0]

plt.imshow(histogram)
plt.show()
```

[![video](https://img.youtube.com/vi/yjz4Nx0u5mI/maxresdefault.jpg)](https://youtu.be/yjz4Nx0u5mI)
