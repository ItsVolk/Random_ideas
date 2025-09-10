from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QListWidgetItem, QVBoxLayout, QLabel, QDialog, QLineEdit, QDialogButtonBox, QFormLayout, QTextEdit
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt
from PyQt6 import uic
import sys
import json
import random

app = QApplication(sys.argv)
with open("messagebox.qss", "r") as f:
    app.setStyleSheet(f.read())

def load_data():
    with open(r"C:\Users\PC\OneDrive\Desktop\new_project\data\account.json", "r") as file:
        return json.load(file)
    
def ideas_data():
    with open(r"C:\Users\PC\OneDrive\Desktop\new_project\data\ideas.json", "r", encoding="utf-8") as file:
        return json.load(file)
    
def ideas_created_data():
    with open(r"C:\Users\PC\OneDrive\Desktop\new_project\data\ideas_created.json", "r", encoding="utf-8") as file:
        return json.load(file)
    
def favourite_data():
    with open(r"C:\Users\PC\OneDrive\Desktop\new_project\data\favourite.json", "r", encoding="utf-8") as file:
        return json.load(file)
    
def save_data(filename, data):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


class login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"C:\Users\PC\OneDrive\Desktop\new_project\ui\login.ui", self)
        self.submit_pushButton.clicked.connect(self.check)
        self.register_pushButton.clicked.connect(self.change_to_register)

    def check(self):
        username = self.username_lineEdit.text()
        email = self.email_lineEdit.text()
        password = self.password_lineEdit.text()

        if not email:
            QMessageBox.information(self, "!!!", "please fill in")
        elif not username:
            QMessageBox.information(self, "!!!", "please fill in")
        elif not password:
            QMessageBox.information(self, "!!!", "please fill in")
        else:
            data = load_data()
            for user in data:
                if user["username"] == username and user["email"] == email and user["password"] == password:
                    r_main.show()
                    r_main.change(username)
                    self.close()
                    QMessageBox.information(self, "=))", "Welcome Back")
                    return
                
            QMessageBox.information(self, "!!!", "Please try again")
                    
    def change_to_register(self):
        r_register.show()
        self.close()

class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"C:\Users\PC\OneDrive\Desktop\new_project\ui\register.ui", self)

        self.submitpushButton.clicked.connect(self.create_user)
        self.loginpushButton.clicked.connect(self.change_to_login)

    def create_user(self):
        username = self.usernamelineEdit.text()
        email = self.emaillineEdit.text()
        password = self.passwordlineEdit.text()
        confirm = self.confirmlineEdit.text()
        data = load_data()
        
        if not email:
            QMessageBox.information(self, "!!!", "please fill in")
        elif not username:
            QMessageBox.information(self, "!!!", "please fill in")
        elif not password:
            QMessageBox.information(self, "!!!", "please fill in")
        elif confirm != password:
            QMessageBox.information(self, "!!!", "password does not match")
        else:
            data.append({
            "username" : username,
            "email" : email,
            "password" : password
            })
            with open(r"C:\Users\PC\OneDrive\Desktop\new_project\data\account.json", "w") as file:
                json.dump(data, file, indent = 4)
            QMessageBox.information(self, "=))", "success")
            self.close()
            r_main.show()
            r_main.change(username)

    def change_to_login(self):
        r_login.show()
        self.close()


class main(QMainWindow):
    def goto(self):
        self.stackedWidget.setCurrentIndex(0)

    def goto_1(self):
        self.stackedWidget.setCurrentIndex(1)

    def goto_2(self):
        self.stackedWidget.setCurrentIndex(2)

    def goto_3(self):
        self.stackedWidget.setCurrentIndex(3)

    def goto_4(self):
        self.stackedWidget.setCurrentIndex(4)

    def goto_5(self):
        self.stackedWidget.setCurrentIndex(5)

    def goto_register(self):
        r_register.show()
        r_login.close()

    def __init__(self):
        super().__init__()
        uic.loadUi(r"C:\Users\PC\OneDrive\Desktop\new_project\ui\main.ui", self)

        self.randomIdeas_btn.clicked.connect(self.goto_1)
        self.randomNum_btn.clicked.connect(self.goto_2)
        self.createIdeas_btn.clicked.connect(self.goto_4)
        self.favourite_btn.clicked.connect(self.goto_3)
        self.ic_btn.clicked.connect(self.goto_5)

        self.registerbtn.clicked.connect(self.goto_register)
        self.logout_btn.clicked.connect(self.logout)

        self.createbtn.clicked.connect(self.create_ideas)
        self.randombtn.clicked.connect(self.random_ideas)
        self.randomnum.clicked.connect(self.randomNums)
        self.savebtn.clicked.connect(self.save_to_fav)
        self.savetobtn.clicked.connect(self.save_to)

        self.favourite_btn.clicked.connect(self.show_fav)
        self.productfav_comboBox.currentTextChanged.connect(self.show_fav)
        self.ic_btn.clicked.connect(self.show_created_ideas)
        self.productIC_comboBox.currentTextChanged.connect(self.show_created_ideas)

        self.removefavbtn.clicked.connect(self.remove_item)
        self.deletebtn.clicked.connect(self.delete_item)
        self.deletenumbtn.clicked.connect(self.delete_num)
        self.deleteall.clicked.connect(self.clearHistory)

        self.result_textEdit.setReadOnly(True)
        self.hello.setReadOnly(True)

    def change(self, username=None):
        self.stackedWidget_2.setCurrentIndex(1)
        if username:
            self.hello.setText(f"Hello, {username}")
        else:
            data = load_data()
            if data:
                user = data[-1]["username"]
                self.hello.setText(f"Hello, {user}")

    def logout(self):
        reply = QMessageBox.question(
            self, "Remove?", f"Are you sure you want to logout?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            self.stackedWidget_2.setCurrentIndex(0)
            self.hello.clear()

    def random_ideas(self):
        tag = self.product_comboBox.currentText()
        ideas = ideas_data()

        if tag == "Product":
            all_ideas = [item for item in ideas]
            picked = random.choice(all_ideas)
            idea = picked["ideas"]
            in4 = picked["tag"]

            self.product_comboBox.setCurrentText(in4)
        else:
            filtered_ideas = [item for item in ideas if item["tag"] == tag]
            picked = random.choice(filtered_ideas)
            idea = picked["ideas"]

        self.result_textEdit.setPlainText(idea)
        
    def save_to_fav(self):
        idea = self.result_textEdit.toPlainText()
        tag = self.product_comboBox.currentText()
        fav = favourite_data()
        fav_idea = {
            "tag" : tag,
            "ideas" : idea
        }

        if not idea:
            QMessageBox.information(self, "!!!", "please fill in")
            return
        elif any(fav_idea["ideas"] == item["ideas"] for item in fav):
            QMessageBox.information(self, "!!!", "idea already saved")

            self.result_textEdit.clear()
            self.product_comboBox.setCurrentText("Product")
        else:
            fav.append(fav_idea)
            with open(r"C:\Users\PC\OneDrive\Desktop\new_project\data\favourite.json", "w", encoding="utf-8") as file:
                json.dump(fav, file, ensure_ascii=False, indent = 4)
            QMessageBox.information(self, "=))", "idea successfully shoved into your basement")

            self.result_textEdit.clear()
            self.product_comboBox.setCurrentText("Product")

        self.show_fav()

    def show_fav(self):
        fav_tag = self.productfav_comboBox.currentText()
        fav = favourite_data()

        if fav_tag == "Product":
            ideas_to_show = [item["ideas"] for item in fav]
        else:
            ideas_to_show = [item["ideas"] for item in fav if item["tag"] == fav_tag]

        if getattr(self, "current_fav_tag", None) != fav_tag:
            self.QLwidget.clear()

        existing_items = [self.QLwidget.item(i).text() for i in range(self.QLwidget.count())]
        
        for item in ideas_to_show:
            if item not in existing_items:
                self.QLwidget.addItem(item)
    
    def remove_item(self):
        item = self.QLwidget.currentItem()
        if not item: 
            QMessageBox.information(self, "!!!", "Choose an idea to remove")
            return
        text = item.text()
        reply = QMessageBox.question(
            self, "Remove?", f"Are you sure you want to remove '{text}' from favourite?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            fav = favourite_data()
            fav = [i for i in fav if i["ideas"] != text]
            save_data(r"C:\Users\PC\OneDrive\Desktop\new_project\data\favourite.json", fav)
            row = self.QLwidget.row(item)
            self.QLwidget.takeItem(row)

    def randomNums(self):
        mini = self.min_line.text()
        maxi = self.max_line.text()

        try:
            mini = int(mini)
            maxi = int(maxi)
        except ValueError:
            QMessageBox.information(self, "!!!", "Please fill in intergers")
            return
        
        if mini > maxi:
            QMessageBox.information(self, "!!!", "⚠️ Min must be less than Max")
            return
        
        rand_num = random.randint(mini, maxi)
        self.result_history.addItem(f"Random Number: {rand_num}")

    def delete_num(self):
        item = self.result_history.currentItem()
        if not item: 
            QMessageBox.information(self, "!!!", "Choose to remove")
            return
        text = item.text()
        reply = QMessageBox.question(
            self, "Remove?", f"Are you sure you want to remove '{text}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            row = self.result_history.row(item)
            self.result_history.takeItem(row)

    def create_ideas(self):
        fill_in = self.create_textEdit.toPlainText()
        tag = self.productCI_comboBox.currentText()

        ideas = ideas_created_data()

        new_idea = {
            "tag" : tag,
            "ideas" : fill_in
        }

        if not fill_in:
            QMessageBox.information(self, "!!!", "please fill in")
            return
        elif tag == "Product":
            QMessageBox.information(self, "!!!", "Choose a tag")
            return
        else:
            ideas.append(new_idea)
            with open(r"C:\Users\PC\OneDrive\Desktop\new_project\data\ideas_created.json", "w", encoding="utf-8") as file:
                json.dump(ideas, file, ensure_ascii=False, indent = 4)
            QMessageBox.information(self, "=))", "idea successfully created")
            
            self.show_created_ideas()
            self.create_textEdit.clear()
            self.productCI_comboBox.setCurrentText("Product")

    def save_to(self):
        new_idea = self.ic_widget.currentItem()
        if not new_idea: 
            QMessageBox.information(self, "!!!", "Choose an idea")
            return

        idea_text = new_idea.text()

        ideas = ideas_created_data()
        ori = ideas_data()

        if any(item["ideas"] == idea_text for item in ori):
            QMessageBox.information(self, "!!!", "idea already exists")
            return
        else: 
            matching_idea = next((item for item in ideas if item["ideas"] == idea_text), None)
            if not matching_idea:
                QMessageBox.information(self, "!!!", "Idea not found")
                return

            ori.append(matching_idea)

            with open(r"C:\Users\PC\OneDrive\Desktop\new_project\data\ideas.json", "w", encoding="utf-8") as file:
                json.dump(ori, file, ensure_ascii=False, indent = 4)

            QMessageBox.information(self, "!!!", "save idea to database")
            return

    def show_created_ideas(self):
        ic_tag = self.productIC_comboBox.currentText()
        ic = ideas_created_data()

        if ic_tag == "Product":
            ideas_to_show = [item["ideas"] for item in ic]
        else:
            ideas_to_show = [item["ideas"] for item in ic if item["tag"] == ic_tag]

        if getattr(self, "current_ic_tag", None) != ic_tag:
            self.ic_widget.clear()

        existing_items = [self.ic_widget.item(i).text() for i in range(self.ic_widget.count())]
        
        for item in ideas_to_show:
            if item not in existing_items:
                self.ic_widget.addItem(item)

    def delete_item(self):
        item = self.ic_widget.currentItem()
        if not item: 
            QMessageBox.information(self, "!!!", "Choose an idea to remove")
            return
        
        text = item.text()

        reply = QMessageBox.question(
            self, "Delete?", f"Are you sure you want to delete '{text}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            created = ideas_created_data()
            created = [i for i in created if i["ideas"] != text]
            save_data(r"C:\Users\PC\OneDrive\Desktop\new_project\data\ideas_created.json", created)
            row = self.ic_widget.row(item)
            self.ic_widget.takeItem(row)

    def clearHistory(self):
        self.result_history.clear()

r_login = login()
r_register = Register()
r_main = main()
r_main.showFullScreen()
sys.exit(app.exec())