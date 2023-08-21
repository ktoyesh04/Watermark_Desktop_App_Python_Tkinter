import customtkinter as ctk
from PIL import Image
from tkinter import colorchooser

class ToolsFrame(ctk.CTkFrame):
	def __init__(self, master, canvas):
		super().__init__(master)
		self.canvas = canvas
		
		self.rotation = Rotation(self)
		self.rotation.grid(row=2, column=0, pady=20)
	
		self.color = Color(self)
		self.color.grid(row=1, column=0, pady=20)
	
		
class Rotation(ctk.CTkFrame):
	def __init__(self, master):
		super().__init__(master)
		self.angle = ctk.IntVar(self, value=0, name='angle')
		
		name_label = ctk.CTkLabel(self, text='Rotation', font=('Arial', 17, 'bold'), )
		name_label.grid(row=0, column=0)
		
		self.rotation = ctk.CTkSlider(self, from_=0, to=180, command=self.on_slide, variable=self.angle
		                              , number_of_steps=180,
		                              hover=False, width=300, height=20)
		self.rotation.grid(row=1, column=0, columnspan=2)
		
		self.value_label = ctk.CTkLabel(self, text='0', font=('Arial', 17, 'bold'), )
		self.value_label.grid(row=0, column=1)
	
	def on_slide(self, angle):
		self.value_label.configure(text=f'%d'%(angle))
		self.master.canvas.itemconfig(self.master.canvas.text_item, angle=angle)
		
	
class Color(ctk.CTkFrame):
	def __init__(self, master):
		super().__init__(master)
		
		color_wheel = Image.open(r'C:\Users\srivani\PycharmProjects\watermark_desktop_gui\gui\color-wheel.png')
		img = ctk.CTkImage(color_wheel, size=(64, 64))
		self.select_color = ctk.CTkButton(self, text='', command=self.select_color, image=img)
		self.select_color.grid(row=0, column=0, padx=20, pady=20)
		
		self.alpha = ctk.IntVar(self, value=0, name='alpha')
		
		name_label = ctk.CTkLabel(self, text='Opacity', font=('Arial', 17, 'bold'), )
		name_label.grid(row=1, column=0)
		
		self.opacity = ctk.CTkSlider(self, from_=0, to=255, command=self.on_slide, variable=self.alpha
		                              , number_of_steps=255, hover=False, width=300, height=20)
		self.opacity.grid(row=2, column=0, columnspan=2)
		self.opacity.set(255)
		
		self.value_label = ctk.CTkLabel(self, text='255', font=('Arial', 17, 'bold'), )
		self.value_label.grid(row=1, column=1, columnspan=2)
	
	def select_color(self, alpha=255):
		def tk_rgb(r, g, b):
			return "#%02x%02x%02x" % (int(r * 255), int(g * 255), int(b * 255))
		
		current_fill = self.master.canvas.itemcget(self.master.canvas.text_item, "fill")
		rgb_color = colorchooser.askcolor(current_fill)[0]
		rgba_color = tk_rgb(*[val / 255 for val in rgb_color])
		self.master.canvas.itemconfig(self.master.canvas.text_item, fill=rgba_color)
	
	def on_slide(self, alpha):
		self.value_label.configure(text=f'%d' % (alpha))
		