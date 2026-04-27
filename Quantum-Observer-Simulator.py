==========================================================
Project: Quantum Observer Simulator
Description: Interactive simulation of double-slit interference
and wavefunction collapse upon measurement.
License: MIT
==========================================================

import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact
import ipywidgets as widgets

def update_plot(observer_active, d, a):
# المعطيات الفيزيائية
L, k0 = 50.0, 3.0
lambda_dB = 2 * np.pi / k0
y = np.linspace(-30, 30, 2000)

# تنظيف الذاكرة وتجهيز الرسم
plt.close()
plt.figure(figsize=(10, 5))

if not observer_active:
# حالة التداخل (بدون مراقب)
beta = np.pi * d * y / (lambda_dB * L)
alpha = np.pi * a * y / (lambda_dB * L)
I = (np.cos(beta)2) * (np.sinc(alpha/np.pi) 2)
plt.plot(y, I, 'b-', label='Quantum Interference')
plt.title("Quantum Interference (Wave Pattern)")
else:
# حالة الرصد (انهيار الدالة الموجية) - مجموع شقين منفصلين
alpha1 = np.pi * a * (y - d/2) / (lambda_dB * L)
alpha2 = np.pi * a * (y + d/2) / (lambda_dB * L)
I = 0.5 * (np.sinc(alpha1/np.pi)2 + np.sinc(alpha2/np.pi) 2)
plt.plot(y, I, 'r-', label='Particle Distribution (Collapsed)')
plt.title("Quantum Measurement (Observer Active: Collapse)")

# إضافة العناوين العلمية للمحاور
plt.xlabel('Screen Position (y)')
plt.ylabel('Probability Density')

plt.ylim(0, 1.2)
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()

لوحة التحكم التفاعلية
interact(update_plot,
observer_active=False,
d=widgets.FloatSlider(value=6.0, min=1.0, max=10.0, step=0.5),
a=widgets.FloatSlider(value=1.0, min=0.5, max=3.0, step=0.1));