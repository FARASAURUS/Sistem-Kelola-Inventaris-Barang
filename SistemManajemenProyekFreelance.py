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