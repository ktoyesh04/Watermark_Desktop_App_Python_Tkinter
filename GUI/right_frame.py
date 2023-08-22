import customtkinter as ctk
from PIL import Image
from tkinter import colorchooser


class ToolsFrame(ctk.CTkFrame):
	def __init__(self, master, text_obj):
		super().__init__(master)
		self.text_obj = text_obj
		
		self.rotation = Rotation(self)
		self.rotation.grid(row=2, column=0, pady=20)
	
		self.color = Color(self)
		self.color.grid(row=1, column=0, pady=20)
	
		self.size = Font(self)
		self.size.grid(row=0, column=0)
	
		
class Rotation(ctk.CTkFrame):
	def __init__(self, master):
		super().__init__(master)
		self.angle = ctk.IntVar(self, value=0, name='angle')
		
		name_label = ctk.CTkLabel(self, text='Rotation', font=('Arial', 17, 'bold'), )
		name_label.grid(row=0, column=0)
		
		self.rotation = ctk.CTkSlider(self, from_=0, to=359, command=self.on_slide, variable=self.angle
												, number_of_steps=360, hover=False, width=300, height=20)
		self.rotation.grid(row=1, column=0, columnspan=2)
		
		self.value_label = ctk.CTkLabel(self, text='0', font=('Arial', 17, 'bold'), )
		self.value_label.grid(row=0, column=1)
	
	def on_slide(self, angle):
		self.value_label.configure(text=f'%d'%(angle))
		self.master.text_obj.rotation = angle
		self.master.text_obj.modify_text()
		
	
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
	
	def select_color(self):
		def tk_rgb(r, g, b):
			return "#%02x%02x%02x" % (int(r * 255), int(g * 255), int(b * 255))
		current_color = self.master.text_obj.color[:3]
		rgb_color = colorchooser.askcolor(tk_rgb(*[val / 255 for val in current_color]))[0]
		self.master.text_obj.color = rgb_color + (255,)
		self.master.text_obj.modify_text()
	
	def on_slide(self, alpha):
		self.master.text_obj.color = self.master.text_obj.color[:3] + (int(alpha),)
		self.master.text_obj.modify_text()


class Font(ctk.CTkFrame):
	def __init__(self, master):
		super().__init__(master)
		
		self.size = ctk.IntVar(value=40, name='size')
		self.size_decrement_button = ctk.CTkButton(self, text='▼', width=20,
		                                           command=lambda: self.change_size(i=-1))
		self.size_decrement_button.grid(column=0, row=0)
		self.master.master.bind('<Down>', lambda e: self.change_size(i=-1))
		
		self.size_entry = ctk.CTkEntry(self, textvariable=self.size, width=38, height=15, corner_radius=3,
		                               state=ctk.DISABLED)
		self.size_entry.grid(column=1, row=0, padx=10)
		
		self.size_increment_button = ctk.CTkButton(self, text='▲', width=20,
		                                           command=lambda: self.change_size(i=1))
		self.size_increment_button.grid(column=2, row=0)
		self.master.master.bind('<Up>', lambda e: self.change_size(i=1))
	
	def change_size(self, i=0):
		old_val = self.size.get()
		new_val = old_val + i * 1
		self.size.set(new_val)
		self.master.text_obj.size = new_val
		self.master.text_obj.modify_text()
