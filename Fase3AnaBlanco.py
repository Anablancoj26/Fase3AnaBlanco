import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry  # Requiere: pip install tkcalendar
from collections import deque


class AffiliationSystemApp:

  def __init__(self, root):
    self.root = root
    self.root.title("Login - Compensándote")
    self.root.geometry("400x300")
    self.root.resizable(False, False)

    # Data Structures
    self.stack_data = []  # Pila (LIFO)
    self.queue_data = deque()  # Cola (FIFO)
    self.list_data = []  # Lista

    self.create_login_widgets()

  def create_login_widgets(self):
    # Main Login Frame
    self.login_frame = ttk.Frame(self.root, padding="20")
    self.login_frame.pack(fill=tk.BOTH, expand=True)

    title_label = ttk.Label(
        self.login_frame,
        text="Compensándote - Login",
        font=("Arial", 14, "bold"),
    )
    title_label.pack(pady=10)

    pass_label = ttk.Label(self.login_frame, text="Password:")
    pass_label.pack(anchor=tk.W, pady=5)

    self.password_entry = ttk.Entry(self.login_frame, show="*")
    self.password_entry.pack(fill=tk.X, pady=5)

    btn_frame = ttk.Frame(self.login_frame)
    btn_frame.pack(fill=tk.X, pady=15)

    login_btn = ttk.Button(
        btn_frame, text="Ingresar", command=self.validate_login
    )
    login_btn.pack(side=tk.LEFT, padx=5, expand=True)

    about_btn = ttk.Button(
        btn_frame, text="Acerca de", command=self.show_about
    )
    about_btn.pack(side=tk.LEFT, padx=5, expand=True)

    exit_btn = ttk.Button(btn_frame, text="Salir", command=self.root.quit)
    exit_btn.pack(side=tk.LEFT, padx=5, expand=True)

  def show_about(self):
    messagebox.showinfo(
        "Acerca de",
        "Curso: Estructuras de Datos\nEstudiante: Ana Isabel Blanco"
        " Jaramillo\nRol: Technical Project Manager | Ingeniera de Sistemas\nGrupo"
        " Colaborativo: Fase 3",
    )

  def validate_login(self):
    password = self.password_entry.get()
    if password == "Caja":
      self.login_frame.destroy()
      self.open_main_dashboard()
    else:
      messagebox.showerror(
          "Error de Autenticación", "Contraseña incorrecta. Intente nuevamente."
      )

  def open_main_dashboard(self):
    self.root.title("Caja Compensándote – Control de Afiliados")
    self.root.geometry("1000x700")
    self.root.resizable(True, True)

    # Main Container
    main_frame = ttk.Frame(self.root, padding="10")
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Left Panel: Input Form
    form_frame = ttk.LabelFrame(
        main_frame, text="Formulario de Afiliación", padding="10"
    )
    form_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

    # Structure Selection
    ttk.Label(form_frame, text="Seleccionar Estructura:").grid(
        row=0, column=0, sticky=tk.W, pady=2
    )
    self.structure_combo = ttk.Combobox(
        form_frame, values=["Pila", "Cola", "Lista"], state="readonly"
    )
    self.structure_combo.grid(row=0, column=1, sticky=tk.EW, pady=2)
    self.structure_combo.current(0)

    # Identification Type
    ttk.Label(form_frame, text="Tipo ID:").grid(
        row=1, column=0, sticky=tk.W, pady=2
    )
    self.id_type_combo = ttk.Combobox(
        form_frame, values=["CC", "CE", "NUIP", "PAS"], state="readonly"
    )
    self.id_type_combo.grid(row=1, column=1, sticky=tk.EW, pady=2)
    self.id_type_combo.current(0)

    # Identification Number
    ttk.Label(form_frame, text="Número ID:").grid(
        row=2, column=0, sticky=tk.W, pady=2
    )
    self.id_number_entry = ttk.Entry(form_frame)
    self.id_number_entry.grid(row=2, column=1, sticky=tk.EW, pady=2)

    # Full Name
    ttk.Label(form_frame, text="Nombre Completo:").grid(
        row=3, column=0, sticky=tk.W, pady=2
    )
    self.name_entry = ttk.Entry(form_frame)
    self.name_entry.grid(row=3, column=1, sticky=tk.EW, pady=2)

    # Current Income
    ttk.Label(form_frame, text="Ingresos Actuales:").grid(
        row=4, column=0, sticky=tk.W, pady=2
    )
    self.income_entry = ttk.Entry(form_frame)
    self.income_entry.grid(row=4, column=1, sticky=tk.EW, pady=2)
    self.income_entry.bind(
        "<KeyRelease>", lambda e: self.calculate_fee_automatic()
    )

    # Employment Modality (Radiobuttons)
    ttk.Label(form_frame, text="Modalidad Empleo:").grid(
        row=5, column=0, sticky=tk.W, pady=2
    )
    mod_frame = ttk.Frame(form_frame)
    mod_frame.grid(row=5, column=1, sticky=tk.W, pady=2)
    self.mod_var = tk.StringVar(value="Empleado")
    ttk.Radiobutton(
        mod_frame,
        text="Empleado",
        variable=self.mod_var,
        value="Empleado",
        command=self.calculate_fee_automatic,
    ).pack(side=tk.LEFT, padx=2)
    ttk.Radiobutton(
        mod_frame,
        text="Independiente",
        variable=self.mod_var,
        value="Independiente",
        command=self.calculate_fee_automatic,
    ).pack(side=tk.LEFT, padx=2)

    # Desired Service
    ttk.Label(form_frame, text="Servicio Deseado:").grid(
        row=6, column=0, sticky=tk.W, pady=2
    )
    self.service_combo = ttk.Combobox(
        form_frame,
        values=[
            "Subsidio de desempleo",
            "Ingreso a parque",
            "Curso de formación",
            "Paquete de viaje",
            "Medicina preventiva",
        ],
        state="readonly",
    )
    self.service_combo.grid(row=6, column=1, sticky=tk.EW, pady=2)
    self.service_combo.current(0)
    self.service_combo.bind(
        "<<ComboboxSelected>>", lambda e: self.calculate_fee_automatic()
    )

    # Affiliation Fee (Non-editable)
    ttk.Label(form_frame, text="Tarifa Afiliación:").grid(
        row=7, column=0, sticky=tk.W, pady=2
    )
    self.fee_entry = ttk.Entry(form_frame, state="readonly")
    self.fee_entry.grid(row=7, column=1, sticky=tk.EW, pady=2)

    # Affiliation Date (DateEntry + Spinbox format)
    ttk.Label(form_frame, text="Fecha Afiliación:").grid(
        row=8, column=0, sticky=tk.W, pady=2
    )
    self.date_entry = DateEntry(
        form_frame, width=18, background="darkblue", foreground="white", date_pattern="dd/mm/yyyy"
    )
    self.date_entry.grid(row=8, column=1, sticky=tk.EW, pady=2)

    # Report Field (Non-editable)
    ttk.Label(form_frame, text="Reporte / Estado:").grid(
        row=9, column=0, sticky=tk.W, pady=2
    )
    self.report_entry = ttk.Entry(form_frame, state="readonly")
    self.report_entry.grid(row=9, column=1, sticky=tk.EW, pady=2)

    # Action Buttons Inside Form
    btn_action_frame = ttk.Frame(form_frame)
    btn_action_frame.grid(row=10, column=0, columnspan=2, pady=10)

    ttk.Button(
        btn_action_frame, text="Registrar", command=self.register_affiliate
    ).pack(side=tk.LEFT, padx=2)
    ttk.Button(
        btn_action_frame, text="Limpiar", command=self.clear_form
    ).pack(side=tk.LEFT, padx=2)
    ttk.Button(
        btn_action_frame, text="Reporte", command=self.generate_report
    ).pack(side=tk.LEFT, padx=2)
    ttk.Button(
        btn_action_frame, text="Eliminar", command=self.delete_record
    ).pack(side=tk.LEFT, padx=2)

    # Global Exit Button
    ttk.Button(
        form_frame, text="Salir", command=self.root.quit, bootstyle="danger"
    ).grid(row=11, column=0, columnspan=2, sticky=tk.EW, pady=5)

    # Right Panel: Treeview Display
    tree_frame = ttk.LabelFrame(
        main_frame, text="Registros en Estructuras", padding="10"
    )
    tree_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

    self.tree = ttk.Treeview(
        tree_frame,
        columns=(
            "Structure",
            "ID Type",
            "ID Number",
            "Name",
            "Income",
            "Modality",
            "Service",
            "Fee",
            "Date",
        ),
        show="headings",
    )
    for col in self.tree["columns"]:
      self.tree.heading(col, text=col)
      self.tree.column(col, width=90, anchor=tk.CENTER)

    scrollbar = ttk.Scrollbar(
        tree_frame, orient=tk.VERTICAL, command=self.tree.yview
    )
    self.tree.configure(yscrollcommand=scrollbar.set)
    self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

  def calculate_fee_automatic(self):
    try:
      income_text = self.income_entry.get().strip()
      if not income_text:
        return
      income = float(income_text)
      modality = self.mod_var.get()
      service = self.service_combo.get()

      base_fee = 0
      if modality == "Empleado":
        if 1000000 <= income <= 2000000:
          base_fee = 45000
        elif income <= 3000000:
          base_fee = 60000
        elif income <= 4000000:
          base_fee = 75000
        elif income <= 5000000:
          base_fee = 90000
        elif income > 5000000:
          base_fee = 150000
      else:  # Independiente
        if 1000000 <= income <= 2000000:
          base_fee = 10000
        elif income <= 3000000:
          base_fee = 20000
        elif income <= 4000000:
          base_fee = 30000
        elif income <= 5000000:
          base_fee = 40000
        elif income > 5000000:
          base_fee = 80000

      # Additional service fee
      if service == "Ingreso a parque":
        base_fee += 2500
      elif service == "Curso de formación":
        base_fee += 7500
      elif service == "Paquete de viaje":
        base_fee += 10000
      elif service == "Medicina preventiva":
        base_fee += income * 0.10

      self.fee_entry.configure(state="normal")
      self.fee_entry.delete(0, tk.END)
      self.fee_entry.insert(0, f"{base_fee:.2f}")
      self.fee_entry.configure(state="readonly")
    except ValueError:
      pass

  def register_affiliate(self):
    structure = self.structure_combo.get()
    id_type = self.id_type_combo.get()
    id_num = self.id_number_entry.get().strip()
    name = self.name_entry.get().strip()
    income = self.income_entry.get().strip()
    modality = self.mod_var.get()
    service = self.service_combo.get()
    fee = self.fee_entry.get().strip()
    date = self.date_entry.get()

    # Validations
    if not id_num or not name or not income:
      messagebox.showwarning(
          "Campos Vacíos", "Por favor diligencie todos los campos requeridos."
      )
      return

    if not id_num.isdigit():
      messagebox.showerror(
          "Error de Validación",
          "El número de identificación debe contener solo números.",
      )
      return

    if not all(c.isalpha() or c.isspace() for c in name):
      messagebox.showerror(
          "Error de Validación",
          "El nombre completo debe contener únicamente letras.",
      )
      return

    if not income.replace(".", "", 1).isdigit():
      messagebox.showerror(
          "Error de Validación",
          "Los ingresos actuales deben ser valores numéricos válidos.",
      )
      return

    record = (
        structure,
        id_type,
        id_num,
        name,
        float(income),
        modality,
        service,
        float(fee),
        date,
    )

    # Structure behavior implementation
    if structure == "Pila":
      self.stack_data.append(record)
    elif structure == "Cola":
      self.queue_data.append(record)
    elif structure == "Lista":
      self.list_data.append(record)

    # Insert into Treeview
    self.tree.insert("", tk.END, values=record)
    messagebox.showinfo("Éxito", "Afiliado registrado correctamente.")
    self.clear_form()

  def clear_form(self):
    self.id_number_entry.delete(0, tk.END)
    self.name_entry.delete(0, tk.END)
    self.income_entry.delete(0, tk.END)
    self.fee_entry.configure(state="normal")
    self.fee_entry.delete(0, tk.END)
    self.fee_entry.configure(state="readonly")
    self.report_entry.configure(state="normal")
    self.report_entry.delete(0, tk.END)
    self.report_entry.configure(state="readonly")

  def generate_report(self):
    structure = self.structure_combo.get()
    report_text = ""

    if structure == "Pila":
      total_fee = sum(item[7] for item in self.stack_data)
      report_text = f"Suma Tarifas Pila: ${total_fee:,.2f}"
    elif structure == "Cola":
      count_records = len(self.queue_data)
      report_text = f"Cantidad Registros Cola: {count_records}"
    elif structure == "Lista":
      if self.list_data:
        avg_income = sum(item[4] for item in self.list_data) / len(
            self.list_data
        )
        report_text = f"Promedio Ingresos Lista: ${avg_income:,.2f}"
      else:
        report_text = "Promedio Ingresos Lista: $0.00"

    self.report_entry.configure(state="normal")
    self.report_entry.delete(0, tk.END)
    self.report_entry.insert(0, report_text)
    self.report_entry.configure(state="readonly")

  def delete_record(self):
    structure = self.structure_combo.get()

    if structure == "Pila":
      if not self.stack_data:
        messagebox.showwarning("Aviso", "La Pila está vacía.")
        return
      if messagebox.askyesno(
          "Confirmar", "¿Desea desapilar el último registro?"
      ):
        self.stack_data.pop()
        # Refresh treeview for stack
        self.refresh_treeview()

    elif structure == "Cola":
      if not self.queue_data:
        messagebox.showwarning("Aviso", "La Cola está vacía.")
        return
      if messagebox.askyesno("Confirmar", "¿Desea desencolar el primer registro?"):
        self.queue_data.popleft()
        self.refresh_treeview()

    elif structure == "Lista":
      if not self.list_data:
        messagebox.showwarning("Aviso", "La Lista está vacía.")
        return
      target_id = self.id_number_entry.get().strip()
      if not target_id:
        messagebox.showwarning(
            "Aviso",
            "Digite el número de identificación del afiliado a eliminar en el"
            " campo Número ID.",
        )
        return

      found = False
      for idx, item in enumerate(self.list_data):
        if item[2] == target_id:
          found = True
          if messagebox.askyesno(
              "Confirmar",
              f"¿Desea eliminar al afiliado con ID {target_id}?",
          ):
            del self.list_data[idx]
            self.refresh_treeview()
            messagebox.showinfo("Éxito", "Registro eliminado de la lista.")
          break
      if not found:
        messagebox.showerror(
            "Error", "No se encontró un afiliado con ese número de ID en la lista."
        )

  def refresh_treeview(self):
    for row in self.tree.get_children():
      self.tree.delete(row)

    for item in self.stack_data:
      self.tree.insert("", tk.END, values=item)
    for item in self.queue_data:
      self.tree.insert("", tk.END, values=item)
    for item in self.list_data:
      self.tree.insert("", tk.END, values=item)


if __name__ == "__main__":
  root = tk.Tk()
  app = AffiliationSystemApp(root)
  root.mainloop()