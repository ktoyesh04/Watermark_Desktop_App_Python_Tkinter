import io
import tkinter
import customtkinter as ctk
from customtkinter import filedialog
from CTkMessagebox import CTkMessagebox
from PIL import Image, ImageTk

from GUI.left_frame import LeftFrame, TextFrame, Text
from GUI.right_frame import ToolsFrame

ctk.set_appearance_mode('light')
# ctk.set_default_color_theme("custom_theme.json")
ctk.set_default_color_theme('green')


class Main(ctk.CTk):
	def __init__(self):
		super().__init__()
		self.geometry("1520x760+0+10")
		self.resizable(True, False)
		self.title('WaterMark GUI')
		
		self.top_frame = TopFrame(self)
		self.top_frame.grid(row=0)
		# self.top_frame.get_image()
		
	def create_frames(self):
		
		self.image_frame = LeftFrame(self, self.top_frame.file_name)
		self.image_frame.grid(row=1, padx=10, pady=10)
		
		self.text_obj = Text(self.image_frame)
		
		self.text_frame = TextFrame(self, self.text_obj)
		self.text_frame.grid(row=2, pady=10)
		
		self.tools_frame = ToolsFrame(self, self.text_obj)
		self.tools_frame.grid(row=0, column=1, rowspan=3, pady=10, padx=10)
		

class TopFrame(ctk.CTkFrame):
	def __init__(self, master):
		super().__init__(master=master)
		
		self.select_image_button = ctk.CTkButton(master=self, text='Select Image', font=('Arial', 17, 'bold'),
		                                         command=self.get_image)
		self.select_image_button.grid(row=0, column=0, padx=10, pady=10)

		self.cancel_button = ctk.CTkButton(master=self, text='Cancel', command=self.exit, font=('Arial', 17, 'bold'),)
		self.cancel_button.grid(row=0, column=1, pady=10)

		self.save_image_button = ctk.CTkButton(master=self, text='Save Image', font=('Arial', 17, 'bold'),
		                                         command=self.save_image, state=ctk.DISABLED)
		self.save_image_button.grid(row=0, column=2, padx=10, pady=10)
	#
	def get_image(self):
		self.file_name = filedialog.askopenfilename(
			initialdir='./', title='Select an Image', filetypes=(('Image files', '*.png *.jpg *.jpeg *.gif *.bmp'),))
		# self.file_name = r'C:\Users\srivani\PycharmProjects\watermark_desktop_gui\dummy1.png'
		if len(self.file_name) != 0:
			self.select_image_button.configure(state=ctk.DISABLED)
			self.save_image_button.configure(state=ctk.NORMAL)
			self.master.create_frames()

	def save_image(self):
		save_file_location = filedialog.asksaveasfile(mode='w', initialdir=self.file_name, initialfile='Modified Image', defaultextension='.png',
		                         filetypes=(('Image files', '*.png *.jpg *.jpeg *.gif *.bmp'),))
		print(save_file_location.name)
		# with open(save_file_location.name, 'wb') as f:
		# 	self.master.image_frame.img.save(f)
		

	def exit(self):
		msg = CTkMessagebox(title='Warning!', message='Do you want to exit?', icon='warning',
		                    option_1='Cancel', option_focus=1, option_2='Yes')
		if msg.get() == 'Yes':
			self.destroy()
			exit(0)

app = Main()
app.mainloop()
