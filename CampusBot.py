import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from datetime import datetime

class CampusPortalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("University Central Student Portal")
        self.root.geometry("1050x700")
        
        # Collegiate Color Palette
        self.burgundy = "#6E0D25"
        self.dark_slate = "#1E2022"
        self.light_grey = "#F0F2F5"
        self.white = "#FFFFFF"
        self.accent_gold = "#D4AF37"
        
        self.root.configure(bg=self.light_grey)
        
        # Define shared font styles
        self.h1_font = ("Segoe UI", 22, "bold")
        self.h2_font = ("Segoe UI", 16, "bold")
        self.body_font = ("Segoe UI", 11)
        self.btn_font = ("Segoe UI", 11, "bold")

        # Set up the UI layout containers
        self.setup_ui_containers()
        self.setup_sidebar_navigation()
        
        # Initialize the different "pages"
        self.frames = {}
        for F in (DashboardPage, CourseDatabasePage, HelpdeskBotPage):
            page_name = F.__name__
            frame = F(parent=self.main_container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the default landing page
        self.show_frame("DashboardPage")

    def setup_ui_containers(self):
        # Master Sidebar on the left
        self.sidebar = tk.Frame(self.root, bg=self.dark_slate, width=250)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        self.sidebar.pack_propagate(False) # Force the sidebar to keep its width

        # Main Content Container on the right
        self.main_container = tk.Frame(self.root, bg=self.light_grey)
        self.main_container.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)
        self.main_container.grid_rowconfigure(0, weight=1)
        self.main_container.grid_columnconfigure(0, weight=1)

    def setup_sidebar_navigation(self):
        # University Logo / Branding
        brand_frame = tk.Frame(self.sidebar, bg=self.burgundy, pady=20)
        brand_frame.pack(fill=tk.X, side=tk.TOP)
        
        tk.Label(brand_frame, text="🎓", font=("Segoe UI", 36), bg=self.burgundy, fg=self.white).pack()
        tk.Label(brand_frame, text="STATE", font=self.h2_font, bg=self.burgundy, fg=self.white).pack()
        tk.Label(brand_frame, text="UNIVERSITY", font=("Segoe UI", 10, "bold"), bg=self.burgundy, fg=self.accent_gold).pack()

        # Navigation Buttons
        nav_frame = tk.Frame(self.sidebar, bg=self.dark_slate, pady=30)
        nav_frame.pack(fill=tk.BOTH, expand=True)

        btn_style = {"bg": self.dark_slate, "fg": self.white, "font": self.btn_font, "bd": 0, "pady": 12, "anchor": "w", "padx": 30, "activebackground": "#343A40", "activeforeground": self.white}

        tk.Button(nav_frame, text="📊 Student Dashboard", command=lambda: self.show_frame("DashboardPage"), **btn_style).pack(fill=tk.X, pady=5)
        tk.Button(nav_frame, text="📚 Course Records", command=lambda: self.show_frame("CourseDatabasePage"), **btn_style).pack(fill=tk.X, pady=5)
        tk.Button(nav_frame, text="🤖 Virtual Assistant", command=lambda: self.show_frame("HelpdeskBotPage"), **btn_style).pack(fill=tk.X, pady=5)

        # Logout at the bottom
        tk.Button(self.sidebar, text="🚪 Secure Logout", bg="#B22222", fg=self.white, font=self.btn_font, bd=0, pady=15, command=self.root.quit).pack(fill=tk.X, side=tk.BOTTOM)

    def show_frame(self, page_name):
        # Elevate the requested frame to the top of the stack
        frame = self.frames[page_name]
        frame.tkraise()

# ==========================================
# MODULE 1: DASHBOARD PAGE
# ==========================================
class DashboardPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=controller.light_grey)
        
        # Header
        header = tk.Frame(self, bg=controller.white, pady=20, padx=30)
        header.pack(fill=tk.X)
        tk.Label(header, text="Student Dashboard", font=controller.h1_font, bg=controller.white, fg=controller.burgundy).pack(side=tk.LEFT)
        
        self.time_label = tk.Label(header, font=("Segoe UI", 12, "bold"), bg=controller.white, fg="#555555")
        self.time_label.pack(side=tk.RIGHT)
        self.update_time()

        # Content Grid
        content = tk.Frame(self, bg=controller.light_grey, padx=30, pady=30)
        content.pack(fill=tk.BOTH, expand=True)

        # Card 1: Announcements
        card1 = tk.Frame(content, bg=controller.white, padx=20, pady=20, highlightbackground="#DDDDDD", highlightthickness=1)
        card1.pack(fill=tk.X, pady=(0, 20))
        tk.Label(card1, text="📢 Campus Announcements", font=controller.h2_font, bg=controller.white).pack(anchor="w", pady=(0, 10))
        tk.Label(card1, text="• Fall Semester registration opens next Monday.\n• Library hours extended to 2 AM during finals week.\n• Flu shots available at the campus clinic all week.", font=controller.body_font, bg=controller.white, justify="left").pack(anchor="w")

        # Card 2: Quick Stats
        card2 = tk.Frame(content, bg=controller.white, padx=20, pady=20, highlightbackground="#DDDDDD", highlightthickness=1)
        card2.pack(fill=tk.X)
        tk.Label(card2, text="📈 Academic Overview", font=controller.h2_font, bg=controller.white).pack(anchor="w", pady=(0, 10))
        tk.Label(card2, text="Current Major: Computer Science\nCredits Completed: 84 / 120\nCumulative GPA: 3.8", font=controller.body_font, bg=controller.white, justify="left").pack(anchor="w")

    def update_time(self):
        now = datetime.now().strftime("%B %d, %Y | %I:%M %p")
        self.time_label.config(text=now)
        self.after(60000, self.update_time) # Update every minute

# ==========================================
# MODULE 2: COURSE DATABASE (DATA TABLE)
# ==========================================
class CourseDatabasePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=controller.light_grey)
        
        # Header
        header = tk.Frame(self, bg=controller.white, pady=20, padx=30)
        header.pack(fill=tk.X)
        tk.Label(header, text="Course Records & Grades", font=controller.h1_font, bg=controller.white, fg=controller.burgundy).pack(side=tk.LEFT)

        # Main Table Area
        table_frame = tk.Frame(self, bg=controller.light_grey, padx=30, pady=30)
        table_frame.pack(fill=tk.BOTH, expand=True)

        # Setup Treeview (Advanced Table)
        columns = ("code", "title", "credits", "grade")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)
        
        # Define Headings
        self.tree.heading("code", text="Course Code")
        self.tree.heading("title", text="Course Title")
        self.tree.heading("credits", text="Credits")
        self.tree.heading("grade", text="Final Grade")
        
        # Define Columns
        self.tree.column("code", width=120, anchor=tk.CENTER)
        self.tree.column("title", width=350, anchor=tk.W)
        self.tree.column("credits", width=80, anchor=tk.CENTER)
        self.tree.column("grade", width=100, anchor=tk.CENTER)

        # Insert Mock Data
        mock_data = [
            ("CS 101", "Introduction to Programming", 4, "A"),
            ("ENG 105", "Freshman Composition", 3, "A-"),
            ("MAT 202", "Calculus II", 4, "B+"),
            ("PHY 110", "Physics for Engineers", 4, "B"),
            ("CS 210", "Data Structures", 3, "A"),
            ("HIS 102", "World History", 3, "A"),
            ("CS 330", "Operating Systems", 3, "In Progress")
        ]
        for item in mock_data:
            self.tree.insert("", tk.END, values=item)

        # Add scrollbar to table
        scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# ==========================================
# MODULE 3: VIRTUAL FAQ ASSISTANT
# ==========================================
class HelpdeskBotPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=controller.light_grey)
        self.controller = controller
        
        # Header
        header = tk.Frame(self, bg=controller.white, pady=20, padx=30)
        header.pack(fill=tk.X)
        tk.Label(header, text="Virtual Campus Assistant", font=controller.h1_font, bg=controller.white, fg=controller.burgundy).pack(side=tk.LEFT)

        # Layout Container for Chat and Buttons
        content = tk.Frame(self, bg=controller.light_grey, padx=30, pady=30)
        content.pack(fill=tk.BOTH, expand=True)

        # Chat Window (Left Side)
        chat_frame = tk.Frame(content, bg=controller.white, highlightbackground="#DDDDDD", highlightthickness=1)
        chat_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 20))
        
        self.chat_display = scrolledtext.ScrolledText(chat_frame, font=("Segoe UI", 11), bg=controller.white, fg="#333333", wrap=tk.WORD, bd=0, padx=20, pady=20)
        self.chat_display.insert(tk.END, "🤖 Assistant: Hello! I am your State University AI Guide.\n\nPlease click a topic on the right to get instant answers regarding campus life, IT support, or financial aid.")
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.pack(fill=tk.BOTH, expand=True)

        # Control Panel (Right Side)
        control_frame = tk.Frame(content, bg=controller.light_grey, width=250)
        control_frame.pack(side=tk.RIGHT, fill=tk.Y)
        
        tk.Label(control_frame, text="Select Inquiry Topic:", font=controller.h2_font, bg=controller.light_grey).pack(anchor="w", pady=(0, 15))

        btn_style = {"bg": controller.burgundy, "fg": controller.white, "font": ("Segoe UI", 11, "bold"), "bd": 0, "pady": 10, "activebackground": "#8A1C38", "activeforeground": controller.white}

        tk.Button(control_frame, text="💡 Password Reset", command=lambda: self.bot_reply("IT"), **btn_style).pack(fill=tk.X, pady=8)
        tk.Button(control_frame, text="💰 Tuition Deadlines", command=lambda: self.bot_reply("FINANCE"), **btn_style).pack(fill=tk.X, pady=8)
        tk.Button(control_frame, text="🚌 Campus Shuttle Schedule", command=lambda: self.bot_reply("TRANSIT"), **btn_style).pack(fill=tk.X, pady=8)
        tk.Button(control_frame, text="🩺 Health Center Appts", command=lambda: self.bot_reply("HEALTH"), **btn_style).pack(fill=tk.X, pady=8)
        
        tk.Button(control_frame, text="🧹 Clear Chat", command=self.clear_chat, bg="#888888", fg="white", font=("Segoe UI", 10), bd=0, pady=5).pack(fill=tk.X, side=tk.BOTTOM)

    def bot_reply(self, topic):
        self.chat_display.config(state=tk.NORMAL)
        
        if topic == "IT":
            msg = "\n\n👤 You: How do I reset my portal password?\n🤖 Assistant: To reset your university password, visit my.state.edu/password. You will need access to your secondary email address or phone number for 2-Factor Authentication."
        elif topic == "FINANCE":
            msg = "\n\n👤 You: When is tuition due?\n🤖 Assistant: Fall tuition is due on August 15th. Spring tuition is due on January 10th. If you need a payment plan, please visit the Bursar's Office online."
        elif topic == "TRANSIT":
            msg = "\n\n👤 You: When does the shuttle run?\n🤖 Assistant: The Red Line Shuttle runs every 15 minutes from 7:00 AM to 10:00 PM between the Main Library and the North Dormitories."
        elif topic == "HEALTH":
            msg = "\n\n👤 You: How do I see a doctor?\n🤖 Assistant: The Student Health Clinic is open Mon-Fri, 8 AM - 5 PM. Walk-ins are welcome for emergencies, but you can book a routine appointment via your student portal."
            
        self.chat_display.insert(tk.END, msg)
        self.chat_display.see(tk.END)
        self.chat_display.config(state=tk.DISABLED)
        
    def clear_chat(self):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.delete('1.0', tk.END)
        self.chat_display.insert(tk.END, "🤖 Assistant: Chat cleared. How else can I help you today?")
        self.chat_display.config(state=tk.DISABLED)

# --- Application Execution ---
if __name__ == "__main__":
    root = tk.Tk()
    app = CampusPortalApp(root)
    root.mainloop()