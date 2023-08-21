import customtkinter as ctk
from PIL import Image, ImageTk


class LeftFrame(ctk.CTkCanvas):
	def __init__(self, master, file_name):
		super().__init__(master)
		self.configure(width=1350, height=700, )
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
		