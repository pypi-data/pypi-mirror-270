import numpy as np
import scipy.fft as fft
import scipy.signal as signal

class Spectrum:

    frequencies = None
    amplitudes = None
    spl = None
    num_windows = 1

    def __init__(self, time_series_data: np.array, dt: float):
        self.time_series_data =  time_series_data
        self.num_steps = np.shape(self.time_series_data)[0]
        self.dt = dt
        self.time = np.linspace(0, self.num_steps*dt, self.num_steps)

    def cutoff_percent(self, percent: float):
        cutoff_index = int(self.num_steps*percent)
        self.time_series_data = self.time_series_data[cutoff_index:]
        self.time = self.time[cutoff_index:]
        self.num_steps = self.num_steps-cutoff_index

    def cutoff_indices(self, index_1: int, index_2: int):
        self.time_series_data = self.time_series_data[index_1:index_2]
        self.time = self.time[index_1:index_2]
        self.num_steps = index_2-index_1

    def use_windows(self, num_windows: int, print_info = True):
        split_ind = int(np.floor(np.shape(self.time)[0]/num_windows))
        self.num_windows = num_windows
        if print_info:
            print(" - using "+str(num_windows)+ " window(s) with "+str(split_ind)+" timesteps")

        data_windows = np.zeros((split_ind, num_windows))
        self.time = self.time[0:split_ind]
        self.num_steps = split_ind

        for i in range(num_windows):
            data_windows[:,i] = self.time_series_data[i*split_ind:(i+1)*split_ind]
        
        self.time_series_data = data_windows

    def apply_window_function(self, fft_window=None):
        if fft_window == None:
            fft_window=signal.windows.hann(self.time.shape[-1])

        if self.num_windows == 1:
            self.time_series_data = self.time_series_data*fft_window
        else:
            for i in range(self.num_windows):
                self.time_series_data[:,i] = self.time_series_data[:,i]*fft_window


    def do_FFT(self):
        self.amplitudes = fft.fft(self.time_series_data, axis= 0)
        self.frequencies = np.fft.fftfreq(self.num_steps, self.dt)


    def sound_pressure_level(self, P_ref = 2e-5):
        press_rms = np.abs(self.amplitudes/P_ref)
        self.spl = 20*np.log10(2/np.shape(press_rms)[0]*press_rms)
        return self.spl
    
    def average_spectra(self):
        self.amplitudes = np.mean(self.amplitudes, axis = 1)

        






        


