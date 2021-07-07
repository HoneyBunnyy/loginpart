from PyQt5.QtWidgets import QMessageBox
import hashlib
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
from ui.sign_up import Ui_sign_up

class sign_up_processor(Ui_sign_up):

    def __init__(self):
        super.__init__()
        #将文本框数据传输到sign_up函数
        self.sign_up_pushButton.clicked.connect(self.sign_up)
        self.workid_lineEdit.returnPressed.connect(self.sign_up)
        self.name_lineEdit.returnPressed.connect(self.sign_up)
        self.password_lineEdit.returnPressed.connect(self.sign_up)
        self.check_password_lineEdit.returnPressed.connect(self.sign_up)
        self.verification()
        self.sign_up()

    # 验证注册模块中的工号/姓名/密码是否规范
    def verification(self):
        # 设置验证
        # 设置输入匹配规则，PB开头，后面加8位数字
        workid_reg = QRegExp("PB[0~9]{8}")
        workid_pValidator = QRegExpValidator(self)
        workid_pValidator.setRegExp(workid_reg)
        # 将匹配规则关联到输入框
        self.workid_lineEdit.setValidator(workid_pValidator)

        password_reg = QRegExp("[a-zA-z0-9]+$")
        password_pValidator = QRegExpValidator(self)
        password_pValidator.setRegExp(password_reg)
        self.password_lineEdit.setValidator(password_pValidator)
        self.check_password_lineEdit.setValidator(password_pValidator)



    #验证注册模块输入表单问题，相关数据库操作
    def sign_up(self):
        work_id = self.workid_lineEdit.text()
        work_name = self.name_label.text()
        work_password = self.password_lineEdit.text()
        check_password = self.check_password_lineEdit.text()
        if (work_id == "" or work_name == "" or work_password == "" or check_password == ""):
            print(QMessageBox.warning(self, "警告", "表单不可为空，请重新输入", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:  # 需要处理逻辑，1.账号已存在;2.密码不匹配;3.插入user表
            db = QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName('./db/worker.db')
            db.open()
            query = QSqlQuery()
            if (check_password != work_password):
                print(QMessageBox.warning(self, "警告", "两次输入密码不一致，请重新输入", QMessageBox.Yes, QMessageBox.Yes))
                return
            elif (check_password == work_password):
                # md5编码
                hl = hashlib.md5()
                hl.update(work_password.encode(encoding='utf-8'))
                md5password = hl.hexdigest()
                sql = "SELECT * FROM worker WHERE work_id='%s'" % (work_id)
                query.exec_(sql)
                if (query.next()):
                    print(QMessageBox.warning(self, "警告", "该账号已存在,请重新输入", QMessageBox.Yes, QMessageBox.Yes))
                    return
                else:
                    sql = "INSERT INTO worker VALUES ('%s','%s','%s')" % (
                        work_id, work_name, md5password)
                    db.exec_(sql)
                    db.commit()
                    print(QMessageBox.information(self, "提醒", "您已成功注册账号!", QMessageBox.Yes, QMessageBox.Yes))
                    self.student_signup_signal.emit(work_id)
                db.close()
                return

















