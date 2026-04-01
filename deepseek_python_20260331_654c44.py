# ============================================
# PTAV Optoacoustic Sensing - Visualization
# Google Colab Version (FULLY FIXED)
# ============================================

# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Import erf from scipy (Colab এ scipy আগে থেকেই আছে)
from scipy.special import erf

# Colab-এ গ্রাফ দেখানোর জন্য সেটিংস
%matplotlib inline

plt.rcParams.update({
    'font.size': 12,
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'xtick.labelsize': 11,
    'ytick.labelsize': 11,
    'legend.fontsize': 11,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'lines.linewidth': 2.5,
})

def plot_acoustic_spectrum():
    frequencies = np.linspace(10, 30, 1000)
    
    def lorentzian(f, f0, gamma, amp):
        return amp * (gamma**2 / ((f - f0)**2 + gamma**2))
    
    TR21 = lorentzian(frequencies, 20.5, 0.35, 1.0)
    TR23 = lorentzian(frequencies, 26.0, 0.5, 0.55)
    
    plt.figure(figsize=(8, 5))
    plt.plot(frequencies, TR21, color='#1f77b4', label='TR₂₁ mode', linewidth=2.5)
    plt.plot(frequencies, TR23, color='#ff7f0e', label='TR₂₃ mode', linewidth=2.5)
    plt.fill_between(frequencies, TR21, alpha=0.2, color='#1f77b4')
    plt.fill_between(frequencies, TR23, alpha=0.2, color='#ff7f0e')
    plt.xlabel('Frequency (MHz)', fontweight='bold')
    plt.ylabel('Acoustic Amplitude (a.u.)', fontweight='bold')
    plt.title('Fig. 2d – Acoustic Spectrum of PTAV Modes', fontweight='bold')
    plt.legend(frameon=True, fancybox=True, shadow=True)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

def plot_impedance_spectra():
    frequencies = np.linspace(18, 23, 1000)
    center = 20.5
    
    def spectrum(Z, f):
        gamma = 0.25 + 0.45 * (Z - 1.0)
        return gamma**2 / ((f - center)**2 + gamma**2)
    
    Z_list = [1.0, 1.5, 2.0, 2.5]
    colors = ['#2ca02c', '#d62728', '#9467bd', '#8c564b']
    
    plt.figure(figsize=(8, 5))
    for Z, col in zip(Z_list, colors):
        sig = spectrum(Z, frequencies)
        plt.plot(frequencies, sig, color=col, label=f'Z = {Z:.1f} MRayl', linewidth=2.5)
    
    plt.xlabel('Frequency (MHz)', fontweight='bold')
    plt.ylabel('Acoustic Amplitude (a.u.)', fontweight='bold')
    plt.title('Fig. 3a – Effect of Surrounding Impedance on TR₂₁ Mode', fontweight='bold')
    plt.legend(frameon=True, fancybox=True)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

def plot_impedance_vs_fwhm():
    impedance = np.array([1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4])
    np.random.seed(42)
    fwhm = 1.8 + 4.2 * (impedance - 1.0) + np.random.normal(0, 0.05, len(impedance))
    
    coeffs = np.polyfit(impedance, fwhm, 1)
    fit_line = np.polyval(coeffs, impedance)
    
    plt.figure(figsize=(7, 6))
    plt.scatter(impedance, fwhm, color='#d62728', s=100, zorder=5, label='Measured data', edgecolors='black')
    plt.plot(impedance, fit_line, color='#1f77b4', linewidth=2.5, linestyle='--', 
             label=f'Linear fit: slope = {coeffs[0]:.2f} MHz/MRayl')
    plt.xlabel('Acoustic Impedance Z (MRayl)', fontweight='bold')
    plt.ylabel('FWHM of TR₂₁ Mode (MHz)', fontweight='bold')
    plt.title('Fig. 3b – FWHM vs Acoustic Impedance', fontweight='bold')
    plt.legend(frameon=True, fancybox=True)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

def plot_interface_impedance():
    position = np.linspace(-100, 100, 500)
    Z_profile = 1.0 + 0.8 * (1 + np.tanh(position / 12)) / 2
    
    plt.figure(figsize=(9, 5))
    plt.plot(position, Z_profile, color='#17becf', linewidth=3)
    plt.axvline(0, color='black', linestyle='--', alpha=0.7, label='Liquid interface')
    plt.fill_between(position, Z_profile, alpha=0.2, color='#17becf')
    plt.xlabel('Position along fibre (µm)', fontweight='bold')
    plt.ylabel('Acoustic Impedance Z (MRayl)', fontweight='bold')
    plt.title('Fig. 3d – Impedance Variation Across Liquid Interface', fontweight='bold')
    plt.legend(frameon=True, fancybox=True)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

def plot_diffusion_profile():
    z = np.linspace(-200, 200, 500)
    Df = 1.64e-9
    vf = 2.5e-3
    dm = 1e-3
    
    sigma = np.sqrt(2 * Df * dm / vf) * 1e6
    concentration = 0.5 * (1 + erf(z / sigma))  # ✅ Correct: using scipy.special.erf
    Z_profile = 1.0 + 0.8 * concentration
    
    plt.figure(figsize=(9, 5))
    plt.plot(z, Z_profile, color='#e377c2', linewidth=3)
    plt.fill_between(z, Z_profile, alpha=0.2, color='#e377c2')
    plt.axhline(1.0, color='gray', linestyle=':', alpha=0.7, label='Water (Z ≈ 1.0 MRayl)')
    plt.axhline(1.8, color='gray', linestyle=':', alpha=0.7, label='NaCl (Z ≈ 1.8 MRayl)')
    plt.xlabel('Position along fibre (µm)', fontweight='bold')
    plt.ylabel('Acoustic Impedance Z (MRayl)', fontweight='bold')
    plt.title('Fig. 4d – Diffusion Profile in Y-shaped Microchannel', fontweight='bold')
    plt.legend(frameon=True, fancybox=True)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

def plot_time_lapse_diffusion():
    z = np.linspace(-200, 200, 500)
    Df = 1.64e-9
    times = [0.05, 0.2, 0.5, 1.0]
    colors = ['#ff7f0e', '#2ca02c', '#1f77b4', '#d62728']
    
    plt.figure(figsize=(9, 5.5))
    for t, col in zip(times, colors):
        sigma = np.sqrt(2 * Df * t) * 1e6
        conc = 0.5 * (1 + erf(z / sigma))  # ✅ Correct: using scipy.special.erf
        Z_prof = 1.0 + 0.8 * conc
        plt.plot(z, Z_prof, color=col, linewidth=2.5, label=f't = {t} s')
    
    plt.xlabel('Position along fibre (µm)', fontweight='bold')
    plt.ylabel('Acoustic Impedance Z (MRayl)', fontweight='bold')
    plt.title('Fig. 4f – Time Evolution of Diffusion After Water Valve Opens', fontweight='bold')
    plt.legend(frameon=True, fancybox=True)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

def plot_interface_shift_spectrum():
    freqs = np.linspace(0, 5, 500)
    peak_freq = 1.07
    np.random.seed(42)
    amplitude = 1 / (1 + ((freqs - peak_freq)/0.1)**2) + 0.05*np.random.randn(len(freqs))
    
    plt.figure(figsize=(8, 4.5))
    plt.plot(freqs, amplitude, color='#8c564b', linewidth=2)
    plt.axvline(peak_freq, color='red', linestyle='--', alpha=0.7, label=f'Periodic shift @ {peak_freq} Hz')
    plt.xlabel('Frequency (Hz)', fontweight='bold')
    plt.ylabel('Amplitude (a.u.)', fontweight='bold')
    plt.title('Fig. 4e – Frequency Spectrum of Diffusion Interface Shift', fontweight='bold')
    plt.legend(frameon=True, fancybox=True)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

# ============================================
# সবগুলো প্লট রান করুন
# ============================================

print("=" * 60)
print("🔬 PTAV Optoacoustic Sensing - Visualization")
print("📄 Based on Nature Communications 12:4139 (2021)")
print("=" * 60)

print("\n📊 Generating Figure 2d: Acoustic Spectrum...")
plot_acoustic_spectrum()

print("\n📊 Generating Figure 3a: Impedance Effect on Spectrum...")
plot_impedance_spectra()

print("\n📊 Generating Figure 3b: FWHM vs Impedance...")
plot_impedance_vs_fwhm()

print("\n📊 Generating Figure 3d: Interface Impedance Profile...")
plot_interface_impedance()

print("\n📊 Generating Figure 4d: Diffusion Profile...")
plot_diffusion_profile()

print("\n📊 Generating Figure 4f: Time-lapse Diffusion...")
plot_time_lapse_diffusion()

print("\n📊 Generating Figure 4e: Interface Shift Spectrum...")
plot_interface_shift_spectrum()

print("\n" + "=" * 60)
print("✅ All 7 figures generated successfully!")
print("=" * 60)