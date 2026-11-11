import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
from PIL import Image
from PIL.PngImagePlugin import PngInfo
import base64
MAXFILESIZE = 25 * 1024 * 1024
def hide_file():
     carrierpath: Path|None=None
     filecheck: Path|None=None
     carrierlabel=None
     window=tk.Toplevel()
     window.title("Hide a file")
     window.geometry("500x500")
     tk.Label(window, text ="Select a carrier PNG:").pack(pady=5)
     carrierlabel=tk.Label(window, text="No image selected")
     carrierlabel.pack(pady=5)
     def selcarrier():
         nonlocal carrierpath
         selectedcarrier=filedialog.askopenfilename(title="Select a carrier PNG",filetypes=[("PNG files","*.png")])
         if not selectedcarrier:
             messagebox.showerror("Error","No image selected.")
             return
         carrierpath=Path(selectedcarrier)
         if carrierpath:
             carrierpath=Path(carrierpath)
             if not carrierpath.is_file():
                 messagebox.showerror("Error","This picture does not exist.")
                 carrierlabel.config(text="No image selected")
                 return
             else:
                 if not carrierpath.suffix.lower()==".png":
                     messagebox.showerror("Error","This picture is not a PNG file.")
                     carrierlabel.config(text="No image selected")
                     return
                 try:
                     asdfghjk=Image.open(carrierpath)
                 except Exception:
                     messagebox.showerror("Error","Unable to open this image.")
                     carrierlabel.config(text="No image selected")
                     return
                 carrierpath=Path(carrierpath)
                 ducky=Image.open(carrierpath)
                 if not ducky.format=="PNG":
                     messagebox.showerror("Error","This picture is not a valid PNG file.")
                     carrierlabel.config(text="No image selected")
                     return
                 if "hiddenfile" in ducky.info or "hiddenfilename" in ducky.info:
                         messagebox.showerror("Error","This picture already has a hidden file.")
                         carrierlabel.config(text="No image selected")
                         return
                 carrierlabel.config(text=f"Selected: {carrierpath.name}")
     tk.Button(window, text="Select Carrier", command=selcarrier).pack(pady=5)
     filelabel=tk.Label(window, text="No file selected")
     filelabel.pack(pady=5)
     def selfile():
            nonlocal filecheck
            selected=filedialog.askopenfilename(title="Select a file to hide",filetypes=[("All files","*.*")])
            if not selected:
                messagebox.showerror("Error","No file selected.")
                return
            filecheck=Path(selected)
            if not filecheck.is_file():
                messagebox.showerror("Error","File does not exist.")
                filelabel.config(text="No file selected")
                return
            if filecheck.stat().st_size>MAXFILESIZE:
                messagebox.showerror("Error","File is too large to hide. Maximum size is 25MB.")
                filelabel.config(text="No file selected")
                return
            filelabel.config(text=f"Selected: {filecheck.name}")
     tk.Button(window, text="Select File to Hide", command=selfile).pack(pady=5)
     def hidefile():
         nonlocal carrierpath, filecheck
         if not carrierpath or not filecheck:
             messagebox.showerror("Error","Please select a carrier image and a file to hide.")
             return
         filebytes=filecheck.read_bytes()
         filename=filecheck.name
         encoded_file=base64.b64encode(filebytes).decode("ascii")
         metadata=PngInfo()
         metadata.add_itxt("hiddenfile",encoded_file)
         metadata.add_itxt("hiddenfilename",filename)
         image=Image.open(carrierpath)
         counter=1
         while True:
             output = carrierpath.parent/f"{carrierpath.stem}_pmfs_{counter:03}.png"
             if not output.exists():
                 break
             counter+=1
         image.save(output,"PNG",pnginfo=metadata)
         messagebox.showinfo("Success",f"File hidden in {output}.")
     tk.Button(window, text="Hide file", command=hidefile).pack(pady=15)
def extractfile():
    imagepath: Path|None=None
    window=tk.Toplevel()
    window.title("Extract")
    window.geometry("500x500")
    tk.Label(window, text="Select an image:").pack(pady=5)
    imagelabel=tk.Label(window, text="No image selected")
    imagelabel.pack(pady=5)
    def selimage():
        nonlocal imagepath
        selected=filedialog.askopenfilename(title="Select an image",filetypes=[("PNG files", "*.png")])
        if not selected:
            messagebox.showerror("Error", "No image selected.")
            return
        imagepath=Path(selected)
        if not imagepath.is_file():
                messagebox.showerror("Error", "Image does not exist.")
                imagelabel.config(text="No image selected")
                imagepath=None
                return
        if not imagepath.suffix.lower()== ".png":
            messagebox.showerror("Error", "This is not a PNG file.")
            imagelabel.config(text="No image selected")
            imagepath2=Path(selected)
            imagepath=None
            return
        try:
            ggomg=Image.open(imagepath)
        except Exception:
            messagebox.showerror("Error", "Unable to open this image.")
            imagelabel.config(text="No image selected")
            imagepath=None
            return
        image=Image.open(imagepath)
        if not image.format=="PNG":
            messagebox.showerror("Error", "This picture is not a valid PNG file.")
            imagelabel.config(text="No image selected")
            imagepath=None
            return
        imagelabel.config(text=f"Selected: {imagepath.name}")

    tk.Button(window, text="Select Image", command=selimage).pack(pady=5)

    def extract():
        if imagepath is None:
            messagebox.showerror("Error", "Please select an image.")
            return
        try:
            image=Image.open(imagepath)
            metadata=image.info
            if "hiddenfile" not in metadata or "hiddenfilename" not in metadata:
                messagebox.showerror("Error", "No hidden file found in the image.")
                return
            filebytes=base64.b64decode(metadata["hiddenfile"], validate=True)
            filename=Path(metadata["hiddenfilename"]).name
            if not filename:
                raise ValueError
        except Exception:
            messagebox.showerror("Error", "The hidden file data is invalid.")
            return

        output=imagepath.parent/filename
        if output.exists():
            counter=1
            while True:
                candidate=output.with_name(f"{output.stem}_{counter:03}{output.suffix}")
                if not candidate.exists():
                    output=candidate
                    break
                counter+=1
        try:
            output.write_bytes(filebytes)
        except Exception as error:
            messagebox.showerror("Error", f"Unable to extract the file: {error}")
            return
        messagebox.showinfo("Success", f"Hidden file extracted to {output}.")

    tk.Button(window, text="Extract file", command=extract).pack(pady=15)
def deletefile():
    imagepath: Path|None=None
    window=tk.Toplevel()
    window.title("Delete")
    window.geometry("500x500")
    tk.Label(window, text="Select an image:").pack(pady=5)
    imagelabel=tk.Label(window, text="No image selected")
    imagelabel.pack(pady=5)
    def selimage():
        nonlocal imagepath
        selected=filedialog.askopenfilename(title="Select an image",filetypes=[("PNG files", "*.png")])
        if not selected:
            messagebox.showerror("Error", "No image selected.")
            return
        imagepath=Path(selected)
        if not imagepath.is_file():
                messagebox.showerror("Error", "Image does not exist.")
                imagelabel.config(text="No image selected")
                imagepath=None
                return
        if not imagepath.suffix.lower()==".png":
            messagebox.showerror("Error", "This is not a PNG file.")
            imagelabel.config(text="No image selected")
            imagepath=None
            return
        try:
            duck8844=Image.open(imagepath)
        except Exception:
            messagebox.showerror("Error", "Unable to open this image.")
            imagelabel.config(text="No image selected")
            imagepath=None
            return
        image=Image.open(imagepath)
        if not image.format=="PNG":
            messagebox.showerror("Error", "This picture is not a valid PNG file.")
            imagelabel.config(text="No image selected")
            imagepath=None
            return
        imagelabel.config(text=f"Selected: {imagepath.name}")

    tk.Button(window, text="Select Image", command=selimage).pack(pady=5)
    def delete():
        if imagepath is None:
            messagebox.showerror("Error", "Please select an image.")
            return
        try:
            image=Image.open(imagepath)
            metadata=image.info
            if "hiddenfile" not in metadata or "hiddenfilename" not in metadata:
                messagebox.showerror("Error", "No hidden file found in the image.")
                return
            delmetadata=PngInfo()
            counter=1
            while True:
                remoutput=imagepath.parent/f"{imagepath.stem}_nohidden_{counter:03}.png"
                if not remoutput.exists():
                    break
                counter+=1
            image.save(remoutput, "PNG", pnginfo=delmetadata)
            messagebox.showinfo("Success", f"Hidden file removed. The new image is saved as {remoutput}.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while deleting the hidden file: {e}")
    tk.Button(window, text="Delete", command=delete).pack(pady=15)
def main():
        root=tk.Tk()
        root.title("PMFS")
        root.geometry("500x500")
        hidefile5=tk.Button(root,text="Hide a file",command=hide_file)
        hidefile5.pack(pady=5)
        extractfile5=tk.Button(root,text="Extract a hidden file",command=extractfile)
        extractfile5.pack(pady=5)
        deletefile5=tk.Button(root,text="Delete a hidden file",command=deletefile)
        deletefile5.pack(pady=5)

        root.mainloop()

if __name__ == "__main__":
    main()