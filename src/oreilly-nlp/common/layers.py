import numpy as np

import sys
sys.path.append('/src/oreilly-nlp')
from common.functions import softmax, cross_entropy_error

class MatMul:
    def __init__(self, W):
        self.params = [W]
        self.grads = [np.zeors_like(W)]
        self.x = None

    def forward(self, x):
        W, = self.params
        out = np.dot(x, W)

        self.x = x

        return out

    def backward(self, dout):
        W, = self.params
        dx = np.dot(dout, W.T)

        dW = np.dot(self.x.T, dout)
        self.grads[0][...] = dW

        return dx

class Sigmoid:
    def __init__(self):
        self.params, self.grads = [], []
        self.out = None

    def forward(self, x):
        out = 1 / (1 + np.exp(-x))

        self.out = out

        return out

    def backward(self, dout):
        # dout → dy
        # Sigmoid関数の微分はdy/dx = y(1-y)
        dx = dout * self.out * (1 - self.out)

        return dx

class Affine:
    def __init__(self, W, b):
        self.params = [W, b]
        self.grads = [np.zeros_like(W), np.zeros_like(b)]
        self.out = None

    def forward(self, x):
        W, b = self.params
        out = np.dot(x, W) + b

        self.x = x

        return out

    def backward(self, dout):
        W, b = self.params
        dx = np.dot(dout, W.T)

        dW = np.dot(self.x.T, dout)
        db = np.sum(dout, axis=0)
        self.grads[0][...] = dW
        self.grads[1][...] = db

        return dx

class SoftmaxWithLoss:
    def __init__(self):
        self.params, self.grads = [], []
        self.y = None # softmaxの出力
        self.t = None # 教師ラベル

    def forward(self, x, t):
        self.t = t
        self.y = softmax(x)

        # 教師ラベルがone-hotベクトルの場合、正解のindexに変換
        if self.t.size == self.y.size:
            self.t = self.t.argmax(axis=1)

        loss = cross_entropy_error(self.y, self.t)

        return loss

    def backward(self, dout=1):
        batch_size = self.t.shape[0]

        dx = self.y.copy()
        dx[np.arange(batch_size), self.t] -= 1
        dx *= dout
        dx = dx / batch_size

        return dx
