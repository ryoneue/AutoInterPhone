from ulab import numpy as np
from ulab import scipy
signal = scipy.signal

# サンプルデータの生成（例えば、サイン波）
fs = 1024*2*2*2  # サンプリング周波数
t = np.linspace(0, 1, fs)
f = 5  # 信号の周波数
x = np.sin(2 * np.pi * f * t)

# FFTの実行
X = np.fft.fft(x)

# 結果の表示
print("FFT結果:", X)
print(X[0].shape)
