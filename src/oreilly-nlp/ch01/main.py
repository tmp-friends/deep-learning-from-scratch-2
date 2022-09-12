import numpy as np
import forward_net

x = np.random.randn(10, 2)
model = forward_net.TwoLayerNet(2, 4, 3)
s = model.predict(x)

print(s)
