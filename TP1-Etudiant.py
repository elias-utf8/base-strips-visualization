import numpy as np
import matplotlib.pyplot as plt

def generate_signal(sequence, bit_duration=1):
    """
    Generate time vector and binary signal.

    Args:
        sequence (list): Binary sequence (e.g., [1, 0, 1, 1, 0, 0, 1, 1]).
        bit_duration (float): Duration of each bit in seconds.

    Returns:
        tuple: (time vector, binary signal)
    """
    time = np.arange(0, len(sequence) * bit_duration, bit_duration / 100)
    signal = np.repeat(sequence, 100)
    return time, signal

def nrz_l(sequence, bit_duration=1):
    """
    Encode a binary sequence using NRZ-L.

    Args:
        sequence (list): Binary sequence.
        bit_duration (float): Duration of each bit.

    Returns:
        tuple: (time vector, NRZ-L encoded signal)
    """
    time, signal = generate_signal(sequence, bit_duration)
    nrz_l_signal = np.array(signal)
    return time, nrz_l_signal

def nrz_i(sequence, bit_duration=1):
    """
    Encode a binary sequence using NRZ-I.

    Args:
        sequence (list): Binary sequence.
        bit_duration (float): Duration of each bit.

    Returns:
        tuple: (time vector, NRZ-I encoded signal)
    """
    time, signal = generate_signal(sequence, bit_duration)
    nrz_i_signal = np.zeros_like(signal)
    current_level = 0
    for i, bit in enumerate(sequence):
        if bit == 1:
            current_level = 1 - current_level  # Toggle the level
        nrz_i_signal[i * 100:(i + 1) * 100] = current_level
    return time, nrz_i_signal

def manchester(sequence, bit_duration=1):
    """
    Encode a binary sequence using Manchester coding.

    Args:
        sequence (list): Binary sequence.
        bit_duration (float): Duration of each bit.

    Returns:
        tuple: (time vector, Manchester encoded signal)
    """
    time = np.arange(0, len(sequence) * bit_duration, bit_duration / 100)
    signal = np.zeros_like(time)
    for i, bit in enumerate(sequence):
        midpoint = (i * 100 + (i + 1) * 100) // 2
        if bit == 1:
            signal[i * 100:midpoint] = 1
            signal[midpoint:(i + 1) * 100] = 0
        else:
            signal[i * 100:midpoint] = 0
            signal[midpoint:(i + 1) * 100] = 1
    return time, signal

# Binary sequence
binary_sequence = [1, 0, 1, 1, 0, 0, 1, 1]
bit_duration = 1

# Generate signals
time_generate_signal, signal_generate_signal= generate_signal(binary_sequence, bit_duration)
time_nrz_l, signal_nrz_l = nrz_l(binary_sequence, bit_duration)
time_nrz_i, signal_nrz_i = nrz_i(binary_sequence, bit_duration)
time_manchester, signal_manchester = manchester(binary_sequence, bit_duration)

# Plot the results
plt.figure(figsize=(12, 8))


# Plot generate_signal
"""
plt.subplot(4, 1, 1)
plt.plot(time_generate_signal, signal_generate_signal, label="generate_signal", drawstyle="steps-pre")
plt.title("Signal d'entrée")
plt.xlabel("Temps")
plt.ylabel("Amplitude")
plt.grid()
"""
# Plot NRZ-L
plt.subplot(4, 1, 1)
plt.plot(time_nrz_l, signal_nrz_l, label="generate_signal", drawstyle="steps-pre")
plt.title("Signal d'entrée")
plt.xlabel("Temps")
plt.ylabel("Amplitude")
plt.grid()

# Plot NRZ-I
plt.subplot(4, 1, 2)
plt.plot(time_nrz_i, signal_nrz_i, label="generate_signal", drawstyle="steps-pre")
plt.title("Signal d'entrée")
plt.xlabel("Temps")
plt.ylabel("Amplitude")
plt.grid()


# Plot Manchester
plt.subplot(4, 1, 3)
plt.plot(time_manchester, signal_manchester, label="generate_signal", drawstyle="steps-pre")
plt.title("Signal d'entrée")
plt.xlabel("Temps")
plt.ylabel("Amplitude")
plt.grid()


plt.tight_layout()
plt.show()
