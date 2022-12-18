import json
import tkinter.filedialog as fd

class SaveAndLoad():
  def __init__(self, canvas):
    self.canvas = canvas
  
  def json_save(self):
    fileNameAndPath = fd.asksaveasfilename(filetypes=[("json", ".json")], defaultextension=".json")
    with open(fileNameAndPath ,'w') as f:
        for item in self.canvas.find_all():
            print(json.dumps({
                'type': self.canvas.type(item),
                'coords': self.canvas.coords(item),
                'options': {key:val[-1] for key,val in self.canvas.itemconfig(item).items()},
                'tags': self.canvas.gettags(item)
            }), file=f)

  def json_load(self):
    funcs = {
      'arc': self.canvas.create_arc,
      'line': self.canvas.create_line,
      'oval': self.canvas.create_oval,
      'polygon': self.canvas.create_polygon,
      'rectangle': self.canvas.create_rectangle,
      'text': self.canvas.create_text,
    }
    jsonFile = fd.askopenfilename(filetypes=[("Json File", '*.json')])
    if (jsonFile != ''):
      self.canvas.delete('all')
      with open(jsonFile) as f:
        for line in f:
            item = json.loads(line)
            if item['type'] in funcs:
                funcs[item['type']](item['coords'], **item['options'])
    else:
      pass