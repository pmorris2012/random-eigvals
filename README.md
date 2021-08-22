# random-eigvals

```python3
import numpy as np

vecs = np.random.randn(512, 512)
for i in range(100):
    vals, vecs = np.linalg.eig(vecs)
```
