import tkinter as tk
from tkinter import filedialog
from tkinter.messagebox import showinfo
from deep_translator import GoogleTranslator
import codecs

#Functions we use
def openFileDialog():
    global fileToTranslatePath
    fileToTranslatePath = filedialog.askopenfilename(title = "Select Text File To Translate", filetypes=[("My Text Files", ".txt .csv")], multiple = "false")
    var_fileToTranslate.set(fileToTranslatePath)
    
def exportFileDialog():
    global exportPath 
    exportPath = filedialog.askdirectory()
    var_ExportFolder.set(exportPath)

def translateFile():
    text_file = open(var_ExportFolder.get() + "/data.txt", "w", encoding="utf-8")
    file1 = codecs.open(var_fileToTranslate.get(), mode='r', encoding="utf-8")
    Lines = file1.readlines()
    for line in Lines:
        translated = GoogleTranslator(source='auto', target='ja').translate(line)
        text_file.write(translated + "\n")
        print(translated)
    text_file.close()



root = tk.Tk()
root.title('Mass Translate Files')

root.attributes('-alpha', 1)
root.resizable(True, True)

#Input Boxes
global var_fileToTranslate 
var_fileToTranslate =  tk.StringVar()
global var_ExportFolder 
var_ExportFolder = tk.StringVar()

name_label = tk.Label(root, text = 'File Path for File to be Translated', font=('calibre',10, 'bold'))
name_entry = tk.Entry(root, textvariable = var_fileToTranslate, font=('calibre',10,'normal'))
  
export_label = tk.Label(root, text = 'Export Path', font=('calibre',10, 'bold'))
export_entry = tk.Entry(root, textvariable = var_ExportFolder, font=('calibre',10,'normal'))


#Button Boxes
text_to_translate_Button = tk.Button(
   root, 
   text="File to Translate", 
   command=openFileDialog
)

export_path_Button = tk.Button(
   root, 
   text="Export Path", 
   command=exportFileDialog
)

translate_file_Button = tk.Button(
   root, 
   text="Translate File", 
   command=translateFile
)


  

name_label.pack(ipadx=5, ipady=5, expand=True)
name_entry.pack(ipadx=5, ipady=5, expand=True)
export_label.pack(ipadx=5, ipady=5, expand=True)
export_entry.pack(ipadx=5, ipady=5, expand=True)
text_to_translate_Button.pack(ipadx=5, ipady=5, expand=True)
export_path_Button.pack(ipadx=5, ipady=5, expand=True)
translate_file_Button.pack(ipadx=5, ipady=5, expand=True)

root.mainloop()