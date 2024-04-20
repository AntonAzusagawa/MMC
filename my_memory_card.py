from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
from random import randint, shuffle

class Question(): #Создание класса вопросов 1 прав и 3 неправ отв
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
    #Задаем строки пари создание обьекта для запоминания в свойства
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Бразильский', 'Испанский'))
question_list.append(Question('Какого цвета нету на флаге России', 'Зеленый', 'Красный', 'Синий', 'Белый'))
question_list.append(Question('Самое большое озеро мира', 'Каспийское море', 'Байкал', 'Виктория', 'Верхнее'))
question_list.append(Question('Первый человек побывавший на Луне', 'Нил Армстронг', 'Чарльз Дьюк', 'Джеймс Ирвин', 'Пит Конрад'))
question_list.append(Question('Самая высокая гора', 'Джомолунгма', 'Чогори', 'Чогори', 'Лхоцзе'))
question_list.append(Question('Первый президент США', 'Джордж Вашингтон', 'Людовик XVI', 'Дональд Трамп', 'Барак Обама'))
question_list.append(Question('International 10 и 12 выйграли', 'Team Spirit', 'Virtus Pro', 'Team Secret', 'NaVi'))
question_list.append(Question('Начало 2 Мировой Войны', '1939', '1941', '1932', '1945'))
#Инфертейс
app = QApplication([])

btn_OK = QPushButton('Ответить')
lb_Question = QLabel("Какой национальности не существует")
#Группа вариантов ответа
RadioGroupBox = QGroupBox('Варианты ответа')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
#Управление поведением переключателей
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout() #Вертик будут внутри горизонт
layout_ans3 = QVBoxLayout()
layout_ans4 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) #Два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) #Два ответа в второй столбец
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) #Столбцы в одной строке

RadioGroupBox.setLayout(layout_ans1) #Панель с вариантами ответа

AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('Прав ты или нет?') #Размешение надписи - верно/неверно
lb_Correct = QLabel('Ответ будет тут!') #Текст верного ответа

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment = Qt.AlignHCenter, stretch = 2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout() #Вопрос
layout_line2 = QHBoxLayout() #Варианты ответа или результат
layout_line3 = QHBoxLayout() #Кнопка ответить

layout_line1.addWidget(lb_Question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.hide()  #Скрытие панели с ответом, т к сначало должна быть видна панель с вопросом

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch = 2) #Увеличение размера кнопок
layout_line3.addStretch(1)

#Создание строки размещаем друг под другом
layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch = 2)
layout_card.addLayout(layout_line2, stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch = 1)
layout_card.addStretch(1)
layout_card.addSpacing(5) #Пробел между содержимым

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) #Сняли ограничения, чтобы можно было сбросить выбор радиокнопки
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) #Вернули ограничения, теперь только 1 кнопка сможет быть нажатой

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers) #Перемешивание списка из кнопок
    answers[0].setText(q.right_answer) #Первые элемент списка - верный ответ
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question) #Вопрос 
    lb_Correct.setText(q.right_answer) #Ответ
    show_question() #Показать панель вопросов

def show_correct(res): #Показать результат - установкаь текста в надписи и показ нужной панели
    lb_Result.setText(res)
    show_result()

def check_answer(): #Если выбран верный вариант ответа, -> показ панели ответов и проверка
    if answers[0].isChecked(): #Прав ответ
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n- Всего вопросов:', window.total, '\n-Правильных ответов:', window.score)
        print('Рейтинг:', (window.score/window.total*100),'%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!') #Неправ ответ
            print('Рейтинг:', (window.score/window.total*100),'%')

def next_question(): #смена вопроса из списка
    #переменная где укащан номер вопроса
    window.total += 1
    print('Статистика\n- Всего вопросов:', window.total, '\n-Правильных ответов:', window.score)
    cur_question = randint(0, len(question_list) -1)
    q = question_list[cur_question]
    ask(q) #Задали вопрос

def click_OK():
    if btn_OK.text() == "Ответить":
        check_answer() #Проверка ответа
    else:
        next_question() #След вопрос

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')

btn_OK.clicked.connect(click_OK) #Убрали тест, здесь нужна проверка ответа
window.total = 0
window.score = 0
next_question()
window.resize(400, 300)
window.show()
app.exec()



