from PyQt5.QtWidgets import QMessageBox
import hashlib
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
from ui.sign_in import Ui_sign_in

class sign_in_processor(Ui_sign_in):
    def __init__(self):
        super.__init__()
        self.verification()


    # 验证登录模块中的工号/密码是否规范
    def verification(self):
        # 设置验证
        reg = QRegExp("PB[0~9]{8}")
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg)
        #验证工号是否规范
        self.workid_lineEdit.setValidator(pValidator)

        reg = QRegExp("[a-zA-z0-9]+$")
        pValidator.setRegExp(reg)
        #验证密码是否规范
        self.work_password_lineEdit.setValidator(pValidator)

    # 验证注册模块输入表单问题，相关数据库操作
    def sign_in(self):
        work_id = self.lineEdit1.text()
        work_password = self.lineEdit2.text()
        if (work_id == "" or work_password == ""):
            print(QMessageBox.warning(self, "警告", "工号和密码不可为空!", QMessageBox.Yes, QMessageBox.Yes))
            return
        # 打开数据库连接
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('./db/worker.db')
        db.open()
        query = QSqlQuery()
        sql = "SELECT * FROM Worker WHERE work_id='%s'" % (work_id)
        query.exec_(sql)
        db.close()

        hl = hashlib.md5()
        hl.update(work_password.encode(encoding='utf-8'))
        if (not query.next()):
            print(QMessageBox.information(self, "提示", "该账号不存在!", QMessageBox.Yes, QMessageBox.Yes))
        else:
            if (work_id == query.value(0) and hl.hexdigest() == query.value(2)):
                self.is_student_signal.emit(work_id)
            else:
                print(QMessageBox.information(self, "提示", "密码错误!", QMessageBox.Yes, QMessageBox.Yes))
        return

