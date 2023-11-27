from PyQt5.QtWidgets import QApplication, QLabel, QTextEdit, QPushButton
from PyQt5.QtWidgets import QWidget

class CVDisplay(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('CV Display')
        self.setGeometry(300, 300, 300, 200)

        label = QLabel('Cv', self)
        label.move(50, 50)

        textEdit = QTextEdit(self)
        textEdit.move(50, 100)
        textEdit.setText('''
        # Curriculum Vitae

        # Personal Information
        Name: Nguyen Phuong Nam
        Address: ML-20,vinhome greenbay me tri 
        Phone: 0968705050
        Email: [namnp2002@gmail.com]

        # Education
        Bachelor of Science in Information Technology, RMIT, 2020-present
        Data science - funix - in progress 
        High school of Education Scienc, 2017-2020
        # Work Experience
        HOUSE PRICING PREDICTION SEP 2021 - JAN 2022 
        INDIVIDUAL PROJECT. HCMC.
        - clean the retrieved data using the relevant imported library
        - analyses outcome using regression techniques
        - modeling the data
        - https://github.com/namtoptall/DataScience
        
        FRONT-END DEVELOPERS APR 2022 - OCT 2022
        WITH GROUP. HCMC.
        - Building the front-end of the website using Node.js
        - contribute the the deployment on Amazone Web Service

        SEPSIS PREDICTION FEB 2022 - APR 2022
        INDIVIDUAL PROJECT. HCMC .
        - Exploratory data cleaning
        - modeling the data using supervised learning techniques
        - evaluate the performance on dataset and predict set
        - https://github.com/namtoptall/predictting-sepsis
        
        BloomSage Apr 2023 - Present
        - craw data from websites
        - resize and clean the images folder
        - using deep learning techniques and libraries to build a classi¦cation model
        - build a recommended system based on the given dataset and the trained model
        - https://github.com/namtoptall/hoalacanhTes
        
        # Skills
        - Exploratory data cleaning
        - Programming: Python, Java, C++
        - Data modelling and evaluating
        - Fundalmental cloud computing
        - Fundamental Finance Analyst
        - TeamWork and Communication
        - PowerBi and SQL
        # References
        Available upon request.
        ''')

        button = QPushButton('Open CV', self)
        button.move(150, 150)
        button.clicked.connect(self.openCV)

    def openCV(self):
        print('Opening CV...')
