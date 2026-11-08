from collections import deque
import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry


class EstructuraDatosAfiliado:

  def __init__(
      self,
      structure_type,
      id_type,
      id_number,
      full_name,
      income,
      modality,
      service,
      fee,
      date,
  ):
    self.structure_type = structure_type
    self.id_type = id_type
    self.id_number = id_number
    self.full_name = full_name
    self.income = income
    self.modality = modality
    self.service = service
    self.fee = fee
    self.date = date

  def to_tuple(self):
    return (
        self.structure_type,
        self.id_type,
        self.id_number,
        self.full_name,
        self.income,
        self.modality,
        self.service,
        self.fee,
        self.date,
    )


class AffiliationSystemApp:

  def __init__(self, root):
    self.root = root
    self.root.title("Login - Compensándote")
    self.root.geometry("450x580")
    self.root.resizable(False, False)
    self.root.configure(bg="#0b1329")

    self.stack_data = []
    self.queue_data = deque()
    self.list_data = []

    self.create_login_widgets()

  def create_login_widgets(self):
    self.login_frame = tk.Frame(self.root, bg="#0b1329", padx=30, pady=20)
    self.login_frame.pack(fill=tk.BOTH, expand=True)

    tk.Label(
        self.login_frame,
        text="🏢 Compensándote",
        font=("Segoe UI", 20, "bold"),
        fg="#38bdf8",
        bg="#0b1329",
    ).pack(pady=(10, 5))
    tk.Label(
        self.login_frame,
        text="Family Compensation Fund — Affiliation Control",
        font=("Segoe UI", 9, "italic"),
        fg="#94a3b8",
        bg="#0b1329",
    ).pack(pady=(0, 15))

    info_frame = tk.Frame(self.login_frame, bg="#1e293b", padx=15, pady=12)
    info_frame.pack(fill=tk.X, pady=10)
    info_text = (
        "Application: Fase3AnaBlanco\nStudent: Ana Isabel Blanco Jaramillo\nRole:"
        " Technical Project Manager\nCourse: Data Structures - 301305"
    )
    tk.Label(
        info_frame,
        text=info_text,
        font=("Consolas", 10, "bold"),
        fg="#f8fafc",
        bg="#1e293b",
        justify=tk.LEFT,
    ).pack(anchor=tk.W)

    tk.Label(
        self.login_frame,
        text="Password",
        font=("Segoe UI", 11, "bold"),
        fg="#f8fafc",
        bg="#0b1329",
    ).pack(anchor=tk.W, pady=(15, 5))

    self.password_entry = tk.Entry(
        self.login_frame,
        show="*",
        font=("Segoe UI", 14),
        bg="#1e293b",
        fg="#ffffff",
        insertbackground="#ffffff",
        relief=tk.FLAT,
    )
    self.password_entry.pack(fill=tk.X, ipady=6, pady=5)

    tk.Label(
        self.login_frame,
        text="Password masked (* * *)",
        font=("Segoe UI", 8, "bold"),
        fg="#94a3b8",
        bg="#0b1329",
    ).pack(anchor=tk.W, pady=(0, 20))

    btn_frame = tk.Frame(self.login_frame, bg="#0b1329")
    btn_frame.pack(fill=tk.X, pady=10)

    # Función auxiliar para crear botones coloridos reales en Mac
    def create_custom_btn(parent, text, cmd, bg_color):
      btn = tk.Label(
          parent,
          text=text,
          bg=bg_color,
          fg="#ffffff",
          font=("Segoe UI", 10, "bold"),
          padx=12,
          pady=8,
          cursor="hand2",
          relief=tk.RAISED,
      )
      btn.bind("<Button-1>", lambda e: cmd())
      return btn

    create_custom_btn(btn_frame, "Ingresar", self.validate_login, "#0284c7").pack(
        side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 4)
    )
    create_custom_btn(btn_frame, "Acerca de", self.show_about, "#475569").pack(
        side=tk.LEFT, expand=True, fill=tk.X, padx=4
    )
    create_custom_btn(btn_frame, "Salir", self.root.quit, "#dc2626").pack(
        side=tk.RIGHT, expand=True, fill=tk.X, padx=(4, 0)
    )

    tk.Label(
        self.login_frame,
        text="UNAD — ECBTSI — Systems Engineering",
        font=("Segoe UI", 8),
        fg="#94a3b8",
        bg="#0b1329",
    ).pack(side=tk.BOTTOM, pady=10)

  def show_about(self):
    messagebox.showinfo(
        "Acerca de",
        "Curso: Estructuras de Datos (301305)\nEstudiante: Ana Isabel Blanco"
        " Jaramillo\nGrupo Colaborativo: Fase 3\nRol: Technical Project Manager"
        " | Ingeniera de Sistemas",
    )

  def validate_login(self):
    if self.password_entry.get() == "Caja":
      self.login_frame.destroy()
      self.open_main_dashboard()
    else:
      messagebox.showerror(
          "Error de Autenticación", "Contraseña incorrecta. Intente nuevamente."
      )

  def open_main_dashboard(self):
    self.root.title("Caja Compensándote – Control de Afiliados")
    self.root.geometry("1250x740")
    self.root.configure(bg="#0b1329")
    self.root.resizable(True, True)

    main_frame = tk.Frame(self.root, bg="#0b1329", padx=15, pady=15)
    main_frame.pack(fill=tk.BOTH, expand=True)

    form_card = tk.Frame(main_frame, bg="#1e293b", padx=20, pady=20)
    form_card.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))

    tk.Label(
        form_card,
        text="Formulario de Registro y Afiliación",
        font=("Segoe UI", 12, "bold"),
        fg="#38bdf8",
        bg="#1e293b",
    ).pack(anchor=tk.W, pady=(0, 15))

    fields_frame = tk.Frame(form_card, bg="#1e293b")
    fields_frame.pack(fill=tk.BOTH, expand=True)

    def add_label(text, r):
      tk.Label(
          fields_frame,
          text=text,
          font=("Segoe UI", 9, "bold"),
          fg="#f1f5f9",
          bg="#1e293b",
      ).grid(row=r, column=0, sticky=tk.W, pady=4)

    add_label("Ver estructura:", 0)
    self.structure_combo = ttk.Combobox(
        fields_frame,
        values=["Pila", "Cola", "Lista"],
        state="readonly",
        width=22,
    )
    self.structure_combo.grid(row=0, column=1, sticky=tk.EW, pady=4)
    self.structure_combo.current(0)
    self.structure_combo.bind(
        "<<ComboboxSelected>>", lambda e: self.refresh_treeview()
    )

    add_label("Tipo ID:", 1)
    self.id_type_combo = ttk.Combobox(
        fields_frame,
        values=["CC", "CE", "NUIP", "PAS"],
        state="readonly",
        width=22,
    )
    self.id_type_combo.grid(row=1, column=1, sticky=tk.EW, pady=4)
    self.id_type_combo.current(0)

    add_label("Número ID:", 2)
    self.id_number_entry = tk.Entry(
        fields_frame,
        font=("Segoe UI", 10),
        bg="#0b1329",
        fg="#ffffff",
        insertbackground="#ffffff",
        relief=tk.FLAT,
    )
    self.id_number_entry.grid(row=2, column=1, sticky=tk.EW, ipady=4, pady=4)

    add_label("Nombre Completo:", 3)
    self.name_entry = tk.Entry(
        fields_frame,
        font=("Segoe UI", 10),
        bg="#0b1329",
        fg="#ffffff",
        insertbackground="#ffffff",
        relief=tk.FLAT,
    )
    self.name_entry.grid(row=3, column=1, sticky=tk.EW, ipady=4, pady=4)

    add_label("Ingresos Actuales ($):", 4)
    self.income_entry = tk.Entry(
        fields_frame,
        font=("Segoe UI", 10),
        bg="#0b1329",
        fg="#ffffff",
        insertbackground="#ffffff",
        relief=tk.FLAT,
    )
    self.income_entry.grid(row=4, column=1, sticky=tk.EW, ipady=4, pady=4)
    self.income_entry.bind(
        "<KeyRelease>", lambda e: self.calculate_fee_automatic()
    )

    add_label("Modalidad de Empleo:", 5)
    mod_frame = tk.Frame(fields_frame, bg="#1e293b")
    mod_frame.grid(row=5, column=1, sticky=tk.W, pady=4)
    self.mod_var = tk.StringVar(value="Empleado")
    tk.Radiobutton(
        mod_frame,
        text="Empleado",
        variable=self.mod_var,
        value="Empleado",
        command=self.calculate_fee_automatic,
        bg="#1e293b",
        fg="#ffffff",
        selectcolor="#0b1329",
        activebackground="#1e293b",
        activeforeground="#ffffff",
    ).pack(side=tk.LEFT, padx=5)
    tk.Radiobutton(
        mod_frame,
        text="Independiente",
        variable=self.mod_var,
        value="Independiente",
        command=self.calculate_fee_automatic,
        bg="#1e293b",
        fg="#ffffff",
        selectcolor="#0b1329",
        activebackground="#1e293b",
        activeforeground="#ffffff",
    ).pack(side=tk.LEFT, padx=5)

    add_label("Servicio Deseado:", 6)
    self.service_combo = ttk.Combobox(
        fields_frame,
        values=[
            "Subsidio de desempleo",
            "Ingreso a parque",
            "Curso de formación",
            "Paquete de viaje",
            "Medicina preventiva",
        ],
        state="readonly",
        width=22,
    )
    self.service_combo.grid(row=6, column=1, sticky=tk.EW, pady=4)
    self.service_combo.current(0)
    self.service_combo.bind(
        "<<ComboboxSelected>>", lambda e: self.calculate_fee_automatic()
    )

    add_label("Tarifa Afiliación ($):", 7)
    self.fee_entry = tk.Entry(
        fields_frame,
        font=("Segoe UI", 10, "bold"),
        bg="#0b1329",
        fg="#38bdf8",
        insertbackground="#ffffff",
        relief=tk.FLAT,
    )
    self.fee_entry.grid(row=7, column=1, sticky=tk.EW, ipady=4, pady=4)
    self.fee_entry.config(state="disabled")

    add_label("Fecha Afiliación:", 8)
    self.date_entry = DateEntry(
        fields_frame,
        width=18,
        background="#0284c7",
        foreground="white",
        date_pattern="dd/mm/yyyy",
    )
    self.date_entry.grid(row=8, column=1, sticky=tk.EW, pady=4)

    add_label("Reporte / Estado:", 9)
    self.report_entry = tk.Entry(
        fields_frame,
        font=("Segoe UI", 10, "bold"),
        bg="#0b1329",
        fg="#4ade80",
        insertbackground="#ffffff",
        relief=tk.FLAT,
    )
    self.report_entry.grid(row=9, column=1, sticky=tk.EW, ipady=4, pady=4)
    self.report_entry.config(state="disabled")

    btn_action_frame = tk.Frame(form_card, bg="#1e293b")
    btn_action_frame.pack(fill=tk.X, pady=(15, 0))

    def create_dashboard_btn(parent, text, cmd, bg_color):
      btn = tk.Label(
          parent,
          text=text,
          bg=bg_color,
          fg="#ffffff",
          font=("Segoe UI", 9, "bold"),
          padx=8,
          pady=6,
          cursor="hand2",
          relief=tk.RAISED,
      )
      btn.bind("<Button-1>", lambda e: cmd())
      return btn

    # Colores intuitivos: Azul (Registrar), Rojo (Eliminar), Verde (Reporte), Naranja (Limpiar), Gris (Salir)
    create_dashboard_btn(
        btn_action_frame, "Registrar", self.register_affiliate, "#0284c7"
    ).pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)
    create_dashboard_btn(
        btn_action_frame, "Eliminar", self.delete_record, "#dc2626"
    ).pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)
    create_dashboard_btn(
        btn_action_frame, "Reporte", self.generate_report, "#0d9488"
    ).pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)
    create_dashboard_btn(
        btn_action_frame, "Limpiar", self.clear_form, "#d97706"
    ).pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)
    create_dashboard_btn(
        btn_action_frame, "Salir", self.root.quit, "#334155"
    ).pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)

    tree_card = tk.Frame(main_frame, bg="#1e293b", padx=15, pady=15)
    tree_card.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    tk.Label(
        tree_card,
        text="Registros en Estructura Seleccionada",
        font=("Segoe UI", 12, "bold"),
        fg="#38bdf8",
        bg="#1e293b",
    ).pack(anchor=tk.W, pady=(0, 10))

    tree_container = tk.Frame(tree_card, bg="#1e293b")
    tree_container.pack(fill=tk.BOTH, expand=True)

    self.tree = ttk.Treeview(
        tree_container,
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
      self.tree.column(col, width=95, anchor=tk.CENTER)

    scrollbar = ttk.Scrollbar(
        tree_container, orient=tk.VERTICAL, command=self.tree.yview
    )
    self.tree.configure(yscrollcommand=scrollbar.set)
    self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    self.refresh_treeview()

  def calculate_fee_automatic(self):
    try:
      income_text = self.income_entry.get().strip()
      if not income_text:
        self.set_fee("")
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
      else:
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

      if service == "Ingreso a parque":
        base_fee += 2500
      elif service == "Curso de formación":
        base_fee += 7500
      elif service == "Paquete de viaje":
        base_fee += 10000
      elif service == "Medicina preventiva":
        base_fee += income * 0.10

      self.set_fee(f"{base_fee:,.2f}")
    except ValueError:
      self.set_fee("")

  def set_fee(self, val):
    self.fee_entry.config(state="normal")
    self.fee_entry.delete(0, tk.END)
    self.fee_entry.insert(0, val)
    self.fee_entry.config(state="disabled")

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

    if not id_num or not name or not income or not fee:
      messagebox.showwarning(
          "Campos Vacíos", "Por favor diligencie todos los campos requeridos."
      )
      return

    if not id_num.isdigit():
      messagebox.showerror(
          "Error de Validación",
          "El número de identificación debe contener exclusivamente números.",
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

    affiliate_obj = EstructuraDatosAfiliado(
        structure,
        id_type,
        id_num,
        name,
        float(income),
        modality,
        service,
        fee,
        date,
    )
    record_tuple = affiliate_obj.to_tuple()

    if structure == "Pila":
      self.stack_data.append(record_tuple)
    elif structure == "Cola":
      self.queue_data.append(record_tuple)
    elif structure == "Lista":
      self.list_data.append(record_tuple)

    self.refresh_treeview()
    messagebox.showinfo("Éxito", "Afiliado registrado correctamente.")
    self.clear_form()

  def clear_form(self):
    self.id_number_entry.delete(0, tk.END)
    self.name_entry.delete(0, tk.END)
    self.income_entry.delete(0, tk.END)
    self.set_fee("")
    self.report_entry.config(state="normal")
    self.report_entry.delete(0, tk.END)
    self.report_entry.config(state="disabled")

  def generate_report(self):
    structure = self.structure_combo.get()
    report_text = ""

    if structure == "Pila":
      total_fee = sum(
          float(str(item[7]).replace(",", "")) for item in self.stack_data
      )
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

    self.report_entry.config(state="normal")
    self.report_entry.delete(0, tk.END)
    self.report_entry.insert(0, report_text)
    self.report_entry.config(state="disabled")

  def delete_record(self):
    structure = self.structure_combo.get()

    if structure == "Pila":
      if not self.stack_data:
        messagebox.showwarning("Aviso", "La Pila está vacía.")
        return
      if messagebox.askyesno(
          "Confirmar", "¿Desea desapilar el último registro de la Pila?"
      ):
        self.stack_data.pop()
        self.refresh_treeview()

    elif structure == "Cola":
      if not self.queue_data:
        messagebox.showwarning("Aviso", "La Cola está vacía.")
        return
      if messagebox.askyesno(
          "Confirmar", "¿Desea desencolar el primer registro de la Cola?"
      ):
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
            " campo 'Número ID'.",
        )
        return

      found = False
      for idx, item in enumerate(self.list_data):
        if item[2] == target_id:
          found = True
          if messagebox.askyesno(
              "Confirmar",
              f"¿Desea eliminar al afiliado con ID {target_id} de la lista?",
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

    selected_structure = self.structure_combo.get()
    if selected_structure == "Pila":
      for item in self.stack_data:
        self.tree.insert("", tk.END, values=item)
    elif selected_structure == "Cola":
      for item in self.queue_data:
        self.tree.insert("", tk.END, values=item)
    elif selected_structure == "Lista":
      for item in self.list_data:
        self.tree.insert("", tk.END, values=item)


if __name__ == "__main__":
  root = tk.Tk()
  app = AffiliationSystemApp(root)
  root.mainloop()