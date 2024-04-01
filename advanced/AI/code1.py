"""
A simple GUI application using tkinter for an AI-Driven Security Monitoring system.
This application allows users to input a source IP/domain and the duration for monitoring.
It then simulates monitoring of the input IP/domain for the specified duration.
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import numpy as np
import threading
import time
import random
import os
from PIL import ImageGrab

class SecurityApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('AI-Driven Security Monitor')
        self.geometry('900x700')
        
        self.data_x = np.linspace(1, 60, 60)
        self.data_y = np.zeros(60)
        
        self.setup_input_section()
        self.setup_timer_section()
        self.setup_graph_section()
        self.setup_alerts_section()
        self.setup_threats_section()
        self.setup_report_section()

    def setup_input_section(self):
        input_frame = ttk.Frame(self)
        input_frame.pack(pady=10)
        
        ttk.Label(input_frame, text="IP/Domain:").pack(side=tk.LEFT)
        self.ip_domain_entry = ttk.Entry(input_frame, width=20)
        self.ip_domain_entry.pack(side=tk.LEFT, padx=5)
        
        ttk.Label(input_frame, text="Duration (s):").pack(side=tk.LEFT)
        self.duration_entry = ttk.Entry(input_frame, width=10)
        self.duration_entry.pack(side=tk.LEFT, padx=5)
        
        self.start_btn = ttk.Button(input_frame, text="Start Monitoring", command=self.start_monitoring)
        self.start_btn.pack(side=tk.LEFT, padx=5)

        self.reset_btn = ttk.Button(input_frame, text="Reset", command=self.reset_monitoring)
        self.reset_btn.pack(side=tk.LEFT, padx=5)

    def setup_timer_section(self):
        self.timer_label = ttk.Label(self, text="00:00")
        self.timer_label.pack()

    def setup_graph_section(self):
        plt.style.use('dark_background')
        fig, self.ax = plt.subplots(figsize=(6, 3))
        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.ax.set_facecolor('black')
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def setup_alerts_section(self):
        ttk.Label(self, text="Alerts / Notifications:").pack(pady=(10, 0))
        self.alerts_text = scrolledtext.ScrolledText(self, height=5)
        self.alerts_text.pack(pady=5)

    def setup_threats_section(self):
        ttk.Label(self, text="Detected Threats:").pack(pady=(10, 0))
        self.threats_text = scrolledtext.ScrolledText(self, height=5)
        self.threats_text.pack(pady=5)

    def setup_report_section(self):
        self.report_btn = ttk.Button(self, text="Capture & Save Report", command=self.capture_gui_as_pdf)
        self.report_btn.pack(pady=10)

    def start_monitoring(self):
        duration = int(self.duration_entry.get())
        self.monitoring_thread = threading.Thread(target=self.monitoring_logic, args=(duration,))
        self.monitoring_thread.start()
        self.animate_graph()

    def reset_monitoring(self):
        self.ip_domain_entry.delete(0, tk.END)
        self.duration_entry.delete(0, tk.END)
        self.alerts_text.delete('1.0', tk.END)
        self.threats_text.delete('1.0', tk.END)
        self.timer_label.config(text="00:00")
        self.data_y = np.zeros(60)
        self.ax.clear()
        self.ax.set_facecolor('black')
        self.canvas.draw()

    def monitoring_logic(self, duration):
        start_time = time.time()
        while time.time() - start_time < duration:
            time_remaining = duration - (time.time() - start_time)
            mins, secs = divmod(int(time_remaining), 60)
            time_str = '{:02d}:{:02d}'.format(mins, secs)
            self.timer_label.config(text=time_str)
            self.simulate_alerts()
            time.sleep(1)
        self.simulate_threat_detection()
        os.system('echo -e "\a"')  # Beep sound at the end (works on many Unix systems)

    def simulate_alerts(self):
        severity = np.random.choice(["Low", "Medium", "High"])
        color = {"Low": "blue", "Medium": "orange", "High": "red"}[severity]
        self.alerts_text.insert(tk.END, f"Simulated Alert: {severity} Severity\n", color)
        self.alerts_text.tag_config(color, foreground=color)
        self.alerts_text.see(tk.END)

    def simulate_threat_detection(self):
        detected = np.random.choice([True, False])
        if detected:
            severity = np.random.choice(["Low", "Medium", "High"])
            color = {"Low": "blue", "Medium": "orange", "High": "red"}[severity]
            self.threats_text.insert(tk.END, f"Detected Threat: {severity} Severity\n", color)
            self.threats_text.tag_config(color, foreground=color)
        else:
            self.threats_text.insert(tk.END, "No threats detected.\n")
        self.threats_text.see(tk.END)

    def capture_gui_as_pdf(self):
        x = self.winfo_rootx()
        y = self.winfo_rooty()
        x1 = x + self.winfo_width()
        y1 = y + self.winfo_height()
        ImageGrab.grab().crop((x, y, x1, y1)).save("scan_report.pdf", "PDF")

    def animate_graph(self):
        def animate(i):
            self.data_y = np.roll(self.data_y, -1)
            self.data_y[-1] = np.random.rand()
            colors = ['red', 'green', 'blue', 'yellow', 'purple', 'cyan']
            self.ax.clear()
            self.ax.plot(self.data_x, self.data_y, 'o', color=random.choice(colors))
            self.ax.set_facecolor('black')
            self.canvas.draw()
        self.anim = FuncAnimation(plt.gcf(), animate, interval=1000)

if __name__ == "__main__":
    app = SecurityApp()
    app.mainloop()
