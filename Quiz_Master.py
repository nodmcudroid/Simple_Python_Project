import tkinter as tk
from tkinter import messagebox

# Expanded quiz dictionary (10 questions)
quiz_data = {
    "What is the capital of France?": ["Paris", "London", "Berlin", "Madrid", "Paris"],
    "Which planet is known as the Red Planet?": ["Earth", "Mars", "Jupiter", "Saturn", "Mars"],
    "Who wrote 'Romeo and Juliet'?": ["Shakespeare", "Hemingway", "Tolkien", "Dickens", "Shakespeare"],
    "What is the smallest prime number?": ["0", "1", "2", "3", "2"],
    "Which language is used to develop Android Apps?": ["Java", "Python", "C++", "HTML", "Java"],
    "What gas do plants absorb from the atmosphere?": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen", "Carbon Dioxide"],
    "Which is the largest mammal?": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus", "Blue Whale"],
    "How many continents are there?": ["5", "6", "7", "8", "7"],
    "What is H2O commonly known as?": ["Salt", "Water", "Hydrogen", "Acid", "Water"],
    "Who discovered gravity?": ["Einstein", "Newton", "Galileo", "Tesla", "Newton"]
}

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Master")
        self.root.geometry("700x500")
        self.root.config(bg="#1e1e2f")

        self.qn = 0
        self.score = 0
        self.questions = list(quiz_data.keys())

        # Header label
        self.header = tk.Label(root, text="🎓 Quiz Master", font=("Helvetica", 28, "bold"), fg="white", bg="#1e1e2f")
        self.header.pack(pady=20)

        # Frame for question and options
        self.frame = tk.Frame(root, bg="#2e2e44", bd=2, relief="groove", padx=20, pady=20)
        self.frame.pack(pady=10, fill="both", expand=True, padx=40)

        self.question_label = tk.Label(self.frame, text="", font=("Helvetica", 18, "bold"), fg="white", bg="#2e2e44", wraplength=600)
        self.question_label.pack(pady=20)

        self.var = tk.StringVar()

        self.options = []
        for i in range(4):
            rb = tk.Radiobutton(
                self.frame, text="", variable=self.var, value="", font=("Helvetica", 16),
                bg="#2e2e44", fg="white", selectcolor="#444466", activebackground="#444466",
                anchor="w", padx=20, pady=5
            )
            rb.pack(fill="x", pady=5)
            self.options.append(rb)

        # Button to go to the next question
        self.next_button = tk.Button(root, text="Next ➜", command=self.next_question,
                                     font=("Helvetica", 16, "bold"), bg="#00adb5", fg="white",
                                     activebackground="#00d1c1", relief="ridge", padx=20, pady=10)
        self.next_button.pack(pady=20)

        self.display_question()

    def display_question(self):
        if self.qn < len(self.questions):
            q = self.questions[self.qn]
            choices = quiz_data[q][:4]
            self.answer = quiz_data[q][4]

            self.question_label.config(text=f"Q{self.qn + 1}: {q}")
            self.var.set(None)

            for i in range(4):
                self.options[i].config(text=choices[i], value=choices[i])
        else:
            self.show_result()

    def next_question(self):
        selected = self.var.get()
        if selected == "":
            messagebox.showwarning("⚠️ Select an option", "Please select an answer before proceeding.")
            return

        if selected == self.answer:
            self.score += 1

        self.qn += 1
        self.display_question()

    def show_result(self):
        messagebox.showinfo("🎉 Quiz Completed", f"Your score: {self.score}/{len(self.questions)}")
        self.root.destroy()

# Start the app
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
