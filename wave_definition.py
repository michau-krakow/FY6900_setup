import matplotlib.pyplot as plt
import numpy as np
import math

samples=8192

def _waveform_from_fun(fn):
  return [ fn(t) for t in range(samples) ]

# Scale array elements to fit [-1, 1] range
def normalize(wave):
  scale = 1 / np.maximum(np.amax(wave), -np.amin(wave))
  return [ wave[t] * scale for t in range(len(wave)) ]


def ramp(A=1):
  return _waveform_from_fun(lambda t: A * (t / samples - 1/2))

def triangle(A=1):
  half = samples / 2
  def tri(t):
    if t < half:
      return A * (t/half - 1/2)
    else:
      return A * (1 - (t-half)/half - 1/2)
  return _waveform_from_fun(tri)

def sine(A=1, freq=1, phase_deg=0):
  theta = math.pi * phase_deg / 180
  omega = 2.0 * math.pi * freq
  return _waveform_from_fun(lambda t: A * math.sin(omega * t/samples + theta))

def sine_harmonic_3():
  return normalize([ sum(x) for x in zip(
    sine(),
    sine(A=1/3, freq=3, phase_deg=45))
  ])

def sine_harmonic_3_5():
  return normalize([ sum(x) for x in zip(
    sine(),
    sine(A=1/3, freq=3, phase_deg=45),
    sine(A=1/5, freq=5, phase_deg=90))
  ])
