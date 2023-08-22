import customtkinter as ctk
from PIL import Image, ImageTk, ImageDraw, ImageFont


class Text:
	def __init__(self, canvas):
		self.canvas = canvas
		self.text = ''
		self.font = 'Arial'
		self.size = 40 
		self.color = (255, 0, 0, 255)
		self.rotation = 0
		self.opacity = 255
		
	def modify_text(self):
		self.canvas.create_text_image(self)


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
		self_image_item = self.create_image(0, 0, image=self.image, anchor=ctk.NW)
		
		self.text_item = None
		
		self.drag_data = {'x': 0, 'y': 0, 'item': None}
	
	def create_text_image(self, text_obj):
		if self.text_item is None:
			self.text_item = self.create_image(self.winfo_reqwidth()//2, self.winfo_reqheight()//2, anchor=ctk.CENTER)
		self.font = ImageFont.truetype(text_obj.font.split()[0].lower(), size=text_obj.size)
		text_width, text_height = self.font.getsize(text_obj.text)
		img = Image.new('RGBA', (text_width, text_height), (0, 0, 0, 0))
		self.draw = ImageDraw.Draw(img, 'RGBA')
		self.draw.text((0, 0), text=text_obj.text, fill=text_obj.color, font=self.font)
		img = img.rotate(text_obj.rotation, expand=True, )
		self.text_item_image = ImageTk.PhotoImage(img)
		self.itemconfigure(self.text_item, image=self.text_item_image)
	
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
	def __init__(self, master, text_obj):
		super().__init__(master)
		
		self.text_obj = text_obj
		
		self.entry = ctk.CTkEntry(self, width=800, height=40, text_color='black',
		                          placeholder_text='Text Here', font=('Arial', 17, 'normal'))
		self.master.bind('<KeyPress-Return>', self.add_text)
		self.entry.grid(row=0, column=1)
		self.add_text_button = ctk.CTkButton(self, text='Add Text', font=('Arial', 17, 'bold'),
		                                     command=self.add_text)
		self.add_text_button.grid(row=0, column=0, padx=10, pady=10)
		
	def add_text(self, event=None):
		entry = self.entry.get()
		if entry != "":
			self.text_obj.text = entry
			self.text_obj.modify_text()
			self.master.focus_set()
			