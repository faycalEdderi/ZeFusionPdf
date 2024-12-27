import os
from tkinter import Tk, Button, filedialog, Listbox, Scrollbar, messagebox
from PyPDF2 import PdfMerger

class FusionPDFApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fusion de PDF")

        self.pdf_files = []

        self.add_button = Button(self.root, text="Ajouter des PDF", command=self.add_pdf)
        self.add_button.pack(pady=10)

        self.listbox = Listbox(self.root, height=10, width=50, selectmode="single")
        self.listbox.pack(pady=10)

        self.scrollbar = Scrollbar(self.root, orient="vertical", command=self.listbox.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        self.merge_button = Button(self.root, text="Valider la Fusion", command=self.merge_pdf)
        self.merge_button.pack(pady=10)

        self.remove_button = Button(self.root, text="Supprimer le PDF", command=self.delete_pdf)
        self.remove_button.pack(pady=10)

        self.listbox.bind("<B1-Motion>", self.move_pdf)
        self.listbox.bind("<ButtonRelease-1>", self.end_moving)

        self.dragging_index = None

    def add_pdf(self):
        fichiers = filedialog.askopenfilenames(filetypes=[("Fichiers PDF", "*.pdf")])
        for fichier in fichiers:
            if fichier not in self.pdf_files:
                self.pdf_files.append(fichier)
                self.listbox.insert("end", os.path.basename(fichier))  # Afficher le nom du fichier

    def merge_pdf(self):
        if not self.pdf_files:
            messagebox.showwarning("Avertissement", "Aucun fichier PDF sélectionné !")
            return

        output_pdf = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Fichiers PDF", "*.pdf")])
        if not output_pdf:
            return

        try:
            merger = PdfMerger()
            for pdf in self.pdf_files:
                merger.append(pdf)
            merger.write(output_pdf)
            merger.close()

            messagebox.showinfo("Succès", f"Les fichiers PDF ont été fusionnés avec succès dans {output_pdf}")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur est survenue lors de la fusion : {e}")

    def delete_pdf(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("Avertissement", "Veuillez sélectionner un fichier à supprimer !")
            return

        index = selection[0]
        self.listbox.delete(index)
        del self.pdf_files[index]

    def move_pdf(self, event):
        index = self.listbox.nearest(event.y)

        if self.dragging_index is None:
            self.dragging_index = index
            self.listbox.selection_set(self.dragging_index)

    def end_moving(self, event):
        if self.dragging_index is not None:
            target_index = self.listbox.nearest(event.y)

            item = self.pdf_files.pop(self.dragging_index)
            self.pdf_files.insert(target_index, item)

            self.listbox.delete(0, "end")
            for pdf in self.pdf_files:
                self.listbox.insert("end", os.path.basename(pdf))

            self.dragging_index = None

root = Tk()
app = FusionPDFApp(root)
root.mainloop()
