import io
import tkinter
import customtkinter as ctk
from customtkinter import filedialog
from CTkMessagebox import CTkMessagebox
from PIL import Image, ImageTk

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
		self.top_frame.get_image()
		
	def create_frames(self):
		
		self.image_frame = LeftFrame(self, self.top_frame.file_name)
		self.image_frame.grid(row=1, padx=10)
		
		self.text_frame = TextFrame(self)
		self.text_frame.grid(row=2, pady=10)
		
		self.tools_frame = ToolsFrame(self)
		self.tools_frame.grid(row=0, column=1, rowspan=3, pady=10, padx=10)
		

class TopFrame(ctk.CTkFrame):
	def __init__(self, master):
		super().__init__(master=master)
		self.configure()
		
		self.select_image_button = ctk.CTkButton(master=self, text='Select Image', font=('Arial', 17, 'bold'),
		                                         command=self.get_image)
		self.select_image_button.grid(row=0, column=0, padx=10, pady=10)
		
		self.cancel_button = ctk.CTkButton(master=self, text='Cancel', command=self.exit, font=('Arial', 17, 'bold'),)
		self.cancel_button.grid(row=0, column=1, pady=10)
		
		self.save_image_button = ctk.CTkButton(master=self, text='Save Image', font=('Arial', 17, 'bold'),
		                                         command=self.save_image)
		self.save_image_button.grid(row=0, column=2, padx=10, pady=10)
	
	def get_image(self):
		# file_name = filedialog.askopenfilename(
		# 	initialdir='./', title='Select an Image', filetypes=(('Image files', '*.png *.jpg *.jpeg *.gif *.bmp'),))
		self.file_name = r'./dummy1.png'
		if len(self.file_name) != 0:
			self.select_image_button.configure(state=ctk.DISABLED)
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


class LeftFrame(ctk.CTkCanvas):
	def __init__(self, master, file_name):
		super().__init__(master)
		self.configure(width=1350, height=700,)
		self.bind("<Button-1>", self.start_drag)
		self.bind("<B1-Motion>", self.drag)
		self.bind("<ButtonRelease-1>", self.release_drag)
		
		img = Image.open(file_name)
		img.thumbnail((self.winfo_reqwidth(), self.winfo_reqheight()))
		
		self.image = ImageTk.PhotoImage(img)
		self_image_item = self.create_image(0, 0, image=self.image,
		                                    anchor=ctk.NW)
		
		text = "Hello, Canvas!"
		self.text_x = self.winfo_reqwidth() // 2
		self.text_y = self.winfo_reqheight() // 2 + 100
		self.text_item = self.create_text(self.text_x, self.text_y, text=text, font=("Arial", 24), fill="black")
		self.drag_data = {'x': 0, 'y': 0, 'item': None}
		
	def start_drag(self, event):
		self.drag_data['item'] = self.text_item
		self.drag_data['x'] = event.x
		self.drag_data['y'] = event.y
		
	def drag(self, event):
		delta_x = event.x - self.drag_data['x']
		delta_y = event.y - self.drag_data['y']
		text_bbox = self.bbox(self.drag_data['item'])
		text_width = text_bbox[2] - text_bbox[0]
		text_height = text_bbox[3] - text_bbox[1]
		
		new_x = max(text_bbox[0] + delta_x, 0)
		new_y = max(text_bbox[1] + delta_y, 0)
		new_x = min(new_x, self.winfo_reqwidth() - text_width)
		new_y = min(new_y, self.winfo_reqheight() - text_height)
		
		self.move(self.drag_data['item'], new_x - text_bbox[0], new_y - text_bbox[1])
		self.drag_data['x'] = event.x
		self.drag_data['y'] = event.y
		
	def release_drag(self, event):
		self.drag_data['item'] = None


class TextFrame(ctk.CTkFrame):
	def __init__(self, master):
		super().__init__(master)
		
		self.configure()
		
		self.add_text_button = ctk.CTkButton(self, text='Add Text', font=('Arial', 17, 'bold'), )
		self.add_text_button.grid(row=0, column=0, padx=10, pady=10)
		
		self.entry = ctk.CTkEntry(self, width=800, height=40, text_color='black',
		                          font=('Arial', 17, 'normal'))
		self.entry.grid(row=0, column=1)
		
		
class ToolsFrame(ctk.CTkFrame):
	def __init__(self, master):
		super().__init__(master)
		self.configure(height=740, width=370,)
		
		class Rotation:
			def __init__(self, master):
				self.angle = ctk.IntVar(master, value=0, name='angle')
				
				label = ctk.CTkLabel(master, text='Rotation', font=('Arial', 17, 'bold'), )
				label.grid(row=2, column=0, padx=10)
				
				self.rotation = ctk.CTkSlider(master, from_=0, to=180, command=self.print, variable=self.angle,number_of_steps=180,
				                              hover=False, width=300, height=20)
				self.rotation.grid(row=2, column=1, columnspan=2)
				
			def print(self, angle):
				print(angle)

		Rotation(self)

app = Main()
app.mainloop()
