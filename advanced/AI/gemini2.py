import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading
import time
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import os
import platform
import pyautogui

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
        self.running = False

    def setup_input_section(self):
        input_frame = ttk.Frame(self)
        input_frame.pack(pady=10)
        
        ttk.Label(input_frame, text="IP/Domain:").pack(side=tk.LEFT)
        self.ip_domain_entry = ttk.Entry(input_frame, width=50)
        self.ip_domain_entry.pack(side=tk.LEFT, padx=5)
        
        self.start_btn = ttk.Button(input_frame, text="Start Monitoring", command=self.start_monitoring)
        self.start_btn.pack(side=tk.LEFT, padx=5)

        self.stop_btn = ttk.Button(input_frame, text="Stop Monitoring", command=self.stop_monitoring)
        self.stop_btn.pack(side=tk.LEFT, padx=5)

        self.reset_btn = ttk.Button(input_frame, text="Reset", command=self.reset_monitoring)
        self.reset_btn.pack(side=tk.LEFT, padx=5)

        self.close_btn = ttk.Button(input_frame, text="Close", command=self.close_app)
        self.close_btn.pack(side=tk.LEFT, padx=5)

    def setup_timer_section(self):
        self.timer_label = ttk.Label(self, text="00:00")
        self.timer_label.pack()

    def setup_graph_section(self):
        self.graph_frame = ttk.Frame(self)
        self.graph_frame.pack(pady=10)
        
        self.fig, self.ax = plt.subplots(figsize=(6, 3))
        self.ax.set_facecolor('white')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.graph_frame)
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
        self.report_btn = ttk.Button(self, text="Capture & Save Screenshot", command=self.capture_gui_as_screenshot)
        self.report_btn.pack(pady=10)

    def start_monitoring(self):
        if not self.running:
            self.running = True
            self.monitoring_thread = threading.Thread(target=self.monitoring_logic)
            self.monitoring_thread.start()
            self.animate_graph()
            self.alerts_text.insert(tk.END, "Monitoring started.\n", "black")
            self.alerts_text.see(tk.END)
            self.start_timer()

    def stop_monitoring(self):
        if self.running:
            self.running = False
            self.alerts_text.insert(tk.END, "Monitoring stopped.\n", "black")
            self.alerts_text.see(tk.END)
            self.stop_timer()

    def reset_monitoring(self):
        self.ip_domain_entry.delete(0, tk.END)
        self.alerts_text.delete('1.0', tk.END)
        self.threats_text.delete('1.0', tk.END)
        self.running = False
        self.ax.clear()
        self.ax.set_facecolor('white')
        self.canvas.draw()
        self.stop_timer()

    def start_timer(self):
        self.start_time = time.time()
        self.update_timer()

    def update_timer(self):
        if self.running:
            current_time = time.time()
            elapsed_time = current_time - self.start_time
            mins, secs = divmod(int(elapsed_time), 60)
            time_str = '{:02d}:{:02d}'.format(mins, secs)
            self.timer_label.config(text=time_str)
            self.timer_label.after(1000, self.update_timer)

    def stop_timer(self):
        self.timer_label.config(text="00:00")

    def monitoring_logic(self):
        while self.running:
            # Add your monitoring logic here
            time.sleep(1)

            # Simulate alerts
            severity = np.random.choice(["Low", "Medium", "High"])
            color = {"Low": "blue", "Medium": "orange", "High": "red"}[severity]
            self.alerts_text.insert(tk.END, f"Simulated Alert: {severity} Severity\n", color)
            self.alerts_text.tag_config(color, foreground=color)
            self.alerts_text.see(tk.END)

            # Simulate threat detection
            detected = np.random.choice([True, False])
            if detected:
                severity = np.random.choice(["Low", "Medium", "High"])
                color = {"Low": "blue", "Medium": "orange", "High": "red"}[severity]
                self.threats_text.insert(tk.END, f"Detected Threat: {severity} Severity\n", color)
                self.threats_text.tag_config(color, foreground=color)
            else:
                self.threats_text.insert(tk.END, "No threats detected.\n", "black")
            self.threats_text.see(tk.END)

    def animate_graph(self):
        def animate(i):
            self.data_y = np.roll(self.data_y, -1)
            self.data_y[-1] = np.random.rand()
            self.ax.clear()
            self.ax.plot(self.data_x, self.data_y, 'o', color='blue')
            self.ax.set_facecolor('white')
            self.canvas.draw()
            if self.running:
                self.after(1000, animate, None)
        animate(None)

    def capture_gui_as_screenshot(self):
        x = self.winfo_rootx()
        y = self.winfo_rooty()
        x1 = x + self.winfo_width()
        y1 = y + self.winfo_height()
        screenshot_name = self.ip_domain_entry.get() + "_screenshot.png"
        pyautogui.screenshot(region=(x, y, x1, y1)).save(screenshot_name)

    def close_app(self):
        self.destroy()

if __name__ == "__main__":
    app = SecurityApp()
    app.mainloop()
