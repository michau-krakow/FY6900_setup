from fygen import fygen
import time
import wave_definition as wave

fy = fygen.FYGen(serial_path='/dev/ttyUSB0', init_state=False) # do re-initialize gen - leave existing settings set manually!

current=fygen.CH1
voltage=fygen.CH2

# generate and save arbitrary waveforms
# fy.set_waveform(waveform_index=63, value_count=8192, values=wave.sine_harmonic_3())
# fy.set_waveform(waveform_index=64, value_count=8192, values=wave.sine_harmonic_3_5())

fy.set(channel=current, enable=True, wave='sin', freq_hz=50.0, volts=0.0123)
fy.set(channel=voltage, enable=True, wave='arb64', freq_hz=50, volts=1.5)

# while True:
#   fy.set(channel=current, phase_degrees=180)
#   time.sleep(5)
#   fy.set(channel=current, phase_degrees=0)
#   time.sleep(5)
