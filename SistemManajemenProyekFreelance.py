import tkinter as tk
from tkinter import messagebox, filedialog
import csv

class Project:
    def init(self, project_id, nama, deskripsi, tanggal_mulai, tanggal_selesai):
        self.project_id = project_id
        self.nama = nama
        self.deskripsi = deskripsi
        self.tanggal_mulai = tanggal_mulai
        self.tanggal_selesai = tanggal_selesai

class ProjectManager:
    def init(self):
        self.projects = []

    def tambah_project(self, project):
        self.projects.append(project)

    def daftar_projects(self):
        return self.projects

    def perbarui_project(self, project_id, nama=None, deskripsi=None, tanggal_mulai=None, tanggal_selesai=None):
        for project in self.projects:
            if project.project_id == project_id:
                if nama:
                    project.nama = nama
                if deskripsi:
                    project.deskripsi = deskripsi
                if tanggal_mulai:
                    project.tanggal_mulai = tanggal_mulai
                if tanggal_selesai:
                    project.tanggal_selesai = tanggal_selesai
                return True
        return False

    def hapus_project(self, project_id):
        for project in self.projects:
            if project.project_id == project_id:
                self.projects.remove(project)
                return True
        return False

    def urutkan_projects_berdasarkan_nama(self):
        self.projects.sort(key=lambda project: project.nama)

    def cari_project_berdasarkan_id(self, project_id):
        for project in self.projects:
            if project.project_id == project_id:
                return project
        return None

class App:
    def init(self, root):
        self.root = root
        self.root.title("Sistem Manajemen Proyek Freelance")
        self.root.configure(bg='#F0F0F0')  

        self.manager = ProjectManager()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Team 9 Sistem Manajemen Proyek Freelance", bg='#F0F0F0', fg='blue', font=("Arial", 16, "bold")).pack(pady=10)

        # Frame untuk input
        frame_input = tk.Frame(self.root, bg='#F0F0F0')  # Atur warna latar belakang frame
        frame_input.pack(pady=10)

        tk.Label(frame_input, text="ID Proyek", bg='#F0F0F0', fg='blue').grid(row=0, column=0, padx=5, pady=5)  # Atur warna latar belakang dan teks label
        self.entry_project_id = tk.Entry(frame_input, width=40)
        self.entry_project_id.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_input, text="Nama Proyek", bg='#F0F0F0', fg='blue').grid(row=1, column=0, padx=5, pady=5)  # Atur warna latar belakang dan teks label
        self.entry_nama = tk.Entry(frame_input, width=40)
        self.entry_nama.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_input, text="Deskripsi", bg='#F0F0F0', fg='blue').grid(row=2, column=0, padx=5, pady=5)  # Atur warna latar belakang dan teks label
        self.entry_deskripsi = tk.Entry(frame_input, width=40)
        self.entry_deskripsi.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame_input, text="Tanggal Mulai", bg='#F0F0F0', fg='blue').grid(row=3, column=0, padx=5, pady=5)  # Atur warna latar belakang dan teks label
        self.entry_tanggal_mulai = tk.Entry(frame_input, width=40)
        self.entry_tanggal_mulai.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(frame_input, text="Tanggal Selesai", bg='#F0F0F0', fg='blue').grid(row=4, column=0, padx=5, pady=5)  # Atur warna latar belakang dan teks label
        self.entry_tanggal_selesai = tk.Entry(frame_input, width=40)
        self.entry_tanggal_selesai.grid(row=4, column=1, padx=5, pady=5)

        # Frame untuk tombol
        frame_buttons = tk.Frame(self.root, bg='#F0F0F0')
        frame_buttons.pack(pady=10)

        button_width = 30  # Atur lebar tombol

        self.btn_tambah = tk.Button(frame_buttons, text="Tambah Proyek", command=self.tambah_project, bg='#4CAF50', fg='white', font=("Arial", 10, "bold"), width=button_width)
        self.btn_tambah.grid(row=0, column=0, padx=5, pady=5)

        self.btn_perbarui = tk.Button(frame_buttons, text="Perbarui Proyek", command=self.perbarui_project, bg='#FF9800', fg='black', font=("Arial", 10, "bold"), width=button_width)
        self.btn_perbarui.grid(row=1, column=0, padx=5, pady=5)

        self.btn_hapus = tk.Button(frame_buttons, text="Hapus Proyek", command=self.hapus_project, bg='#f44336', fg='white', font=("Arial", 10, "bold"), width=button_width)
        self.btn_hapus.grid(row=2, column=0, padx=5, pady=5)

        self.btn_cari = tk.Button(frame_buttons, text="Cari Proyek Berdasarkan ID", command=self.cari_project, bg='#9C27B0', fg='white', font=("Arial", 10, "bold"), width=button_width)
        self.btn_cari.grid(row=3, column=0, padx=5, pady=5)

        self.btn_daftar = tk.Button(frame_buttons, text="Daftar Proyek", command=self.daftar_projects, bg='#607D8B', fg='white', font=("Arial", 10, "bold"), width=button_width)
        self.btn_daftar.grid(row=4, column=0, padx=5, pady=5)

        self.btn_impor = tk.Button(frame_buttons, text="Impor CSV", command=self.import_csv, bg='#FFC107', fg='black', font=("Arial", 10, "bold"), width=button_width)
        self.btn_impor.grid(row=5, column=0, padx=5, pady=5)

        self.btn_urutkan = tk.Button(frame_buttons, text="Urutkan Proyek Berdasarkan Nama", command=self.urutkan_projects, bg='#2196F3', fg='white', font=("Arial", 10, "bold"), width=button_width)
        self.btn_urutkan.grid(row=6, column=0, padx=5, pady=5)

        # Frame untuk listbox
        frame_listbox = tk.Frame(self.root, bg='#F0F0F0')
        frame_listbox.pack(pady=10)

        self.scrollbar = tk.Scrollbar(frame_listbox, orient=tk.HORIZONTAL)
        self.scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        self.listbox = tk.Listbox(frame_listbox, width=80, bg='white', fg='black', font=("Arial", 10), xscrollcommand=self.scrollbar.set)  # Atur warna latar belakang dan teks listbox
        self.listbox.pack(padx=5, pady=5)

        self.scrollbar.config(command=self.listbox.xview)

    def tambah_project(self):
        project_id = self.entry_project_id.get()
        nama = self.entry_nama.get()
        deskripsi = self.entry_deskripsi.get()
        tanggal_mulai = self.entry_tanggal_mulai.get()
        tanggal_selesai = self.entry_tanggal_selesai.get()
        if project_id and nama and deskripsi and tanggal_mulai and tanggal_selesai:
            project = Project(project_id, nama, deskripsi, tanggal_mulai, tanggal_selesai)
            self.manager.tambah_project(project)
            self.clear_entries()
            messagebox.showinfo("Sukses", "Proyek berhasil ditambahkan.")
        else:
            messagebox.showwarning("Peringatan", "Semua kolom harus diisi.")
    def perbarui_project(self):
        project_id = self.entry_project_id.get()
        nama = self.entry_nama.get()
        deskripsi = self.entry_deskripsi.get()
        tanggal_mulai = self.entry_tanggal_mulai.get()
        tanggal_selesai = self.entry_tanggal_selesai.get()
        if self.manager.perbarui_project(project_id, nama, deskripsi, tanggal_mulai, tanggal_selesai):
            self.clear_entries()
            messagebox.showinfo("Sukses", "Proyek berhasil diperbarui.")
        else:
            messagebox.showwarning("Peringatan", "Proyek tidak ditemukan.")

    def hapus_project(self):
        project_id = self.entry_project_id.get()
        if self.manager.hapus_project(project_id):
            self.clear_entries()
            messagebox.showinfo("Sukses", "Proyek berhasil dihapus.")
        else:
            messagebox.showwarning("Peringatan", "Proyek tidak ditemukan.")

    def urutkan_projects(self):
        self.manager.urutkan_projects_berdasarkan_nama()
        messagebox.showinfo("Sukses", "Proyek diurutkan berdasarkan nama.")
        self.daftar_projects()

    def cari_project(self):
        project_id = self.entry_project_id.get()
        project = self.manager.cari_project_berdasarkan_id(project_id)
        if project:
            self.listbox.delete(0, tk.END)
            self.listbox.insert(tk.END, f'ID: {project.project_id}, Nama: {project.nama}, Deskripsi: {project.deskripsi}, Tanggal Mulai: {project.tanggal_mulai}, Tanggal Selesai: {project.tanggal_selesai}')
        else:
            messagebox.showwarning("Peringatan", "Proyek tidak ditemukan.")

    def daftar_projects(self):
        self.listbox.delete(0, tk.END)
        for project in self.manager.daftar_projects():
            self.listbox.insert(tk.END, f'ID: {project.project_id}, Nama: {project.nama}, Deskripsi: {project.deskripsi}, Tanggal Mulai: {project.tanggal_mulai}, Tanggal Selesai: {project.tanggal_selesai}')

    def import_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            try:
                with open(file_path, mode='r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        project = Project(row['ID Proyek'], row['Nama Proyek'], row['Deskripsi'], row['Tanggal Mulai'], row['Tanggal Selesai'])
                        self.manager.tambah_project(project)
                messagebox.showinfo("Sukses", "Proyek berhasil diimpor.")
                self.daftar_projects()  # Refresh daftar proyek setelah impor
            except Exception as e:
                messagebox.showerror("Error", f"Gagal mengimpor proyek: {str(e)}")

    def clear_entries(self):
        self.entry_project_id.delete(0, tk.END)
        self.entry_nama.delete(0, tk.END)
        self.entry_deskripsi.delete(0, tk.END)
        self.entry_tanggal_mulai.delete(0, tk.END)
        self.entry_tanggal_selesai.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
