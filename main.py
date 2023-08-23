import os.path
import customtkinter as ctk
from PIL import Image, ImageTk
from customtkinter import filedialog
from CTkMessagebox import CTkMessagebox

from left_frame import LeftFrame, TextFrame, Text
from right_frame import ToolsFrame

ctk.set_appearance_mode('light')
# ctk.set_default_color_theme("custom_theme.json")
ctk.set_default_color_theme('green')


class Main(ctk.CTk):
	def __init__(self):
		super().__init__()
		self.geometry("1520x760+0+10")
		self.resizable(True, False)
		self.title('WaterMark GUI')
		
		bg_image = ImageTk.PhotoImage(file=r'bg.png')
		bg_label = ctk.CTkLabel(self, image=bg_image, text='')
		bg_label.place(x=0, y=0)
		
		self.top_frame = TopFrame(self)
		self.top_frame.grid(row=0)
	
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
		
		self.cancel_button = ctk.CTkButton(master=self, text='Cancel', command=self.exit, font=('Arial', 17, 'bold'), )
		self.cancel_button.grid(row=0, column=1, pady=10)
		
		self.save_image_button = ctk.CTkButton(master=self, text='Save Image', font=('Arial', 17, 'bold'),
		                                       command=self.save_image, state=ctk.DISABLED)
		self.save_image_button.grid(row=0, column=2, padx=10, pady=10)
	
	def get_image(self):
		self.file_name = filedialog.askopenfilename(
			initialdir='./', title='Select an Image', filetypes=(('Image files', '*.png *.jpg *.jpeg *.gif *.bmp'),))
		if len(self.file_name) != 0:
			self.select_image_button.configure(state=ctk.DISABLED)
			self.save_image_button.configure(state=ctk.NORMAL)
			self.master.create_frames()
	
	def save_image(self):
		if not self.master.image_frame.any_changes():
			CTkMessagebox(title="Error", message="No changes", icon="cancel")
			return
		msg = CTkMessagebox(title="Save", message="Confirm to Save", icon="info", option_1="Cancel", option_2="Confirm")
		if msg.get() != 'Confirm':
			return
		save_file_dir = filedialog.asksaveasfile(mode='w', confirmoverwrite=True, initialdir=self.file_name,
		                                         initialfile='Modified Image', defaultextension='png',
		                                         filetypes=[("jpeg", ".jpeg"), ("png", ".png"), ("bitmap", "bmp"),
		                                                    ("gif", ".gif"), ("jpg", ".jpg")]).name
		if save_file_dir is not None:
			image = self.master.image_frame.combine()
			if os.path.splitext(save_file_dir)[1] == '.jpeg':
				image = image.convert('RGB')
			image.save(save_file_dir)
	
	def exit(self):
		msg = CTkMessagebox(title='Warning!', message='Do you want to exit?', icon='warning',
		                    option_1='Cancel', option_focus=1, option_2='Yes')
		if msg.get() == 'Yes':
			self.destroy()
			exit(0)


app = Main()
app.mainloop()
