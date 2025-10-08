# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DETECTOR_7inch.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QStackedWidget, QTabWidget,
    QVBoxLayout, QWidget)
import src.resource_rc as resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 609)
        MainWindow.setMinimumSize(QSize(250, 0))
        MainWindow.setStyleSheet(u"background-color: rgb(38, 38, 38);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(1024, 600))
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout_12 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.hide_sidebar = QWidget(self.centralwidget)
        self.hide_sidebar.setObjectName(u"hide_sidebar")
        self.hide_sidebar.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(0, 150, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: rgb(0, 150, 255);\n"
"	font-size: 20px;\n"
"	color: white;\n"
"	text-align: left;\n"
"	height: 30px;\n"
"	border: none;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"	padding: 15px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: #f5fafe;\n"
"	color: rgb(0, 150, 255);\n"
"	font-weight: bold;\n"
"}")
        self.verticalLayout_13 = QVBoxLayout(self.hide_sidebar)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.profile_img2 = QLabel(self.hide_sidebar)
        self.profile_img2.setObjectName(u"profile_img2")
        self.profile_img2.setMinimumSize(QSize(60, 60))
        self.profile_img2.setMaximumSize(QSize(60, 60))
        self.profile_img2.setPixmap(QPixmap(u":/assets/images/polipharm.png"))
        self.profile_img2.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.profile_img2)


        self.verticalLayout_13.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.home_2 = QPushButton(self.hide_sidebar)
        self.home_2.setObjectName(u"home_2")
        self.home_2.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home_2.sizePolicy().hasHeightForWidth())
        self.home_2.setSizePolicy(sizePolicy)
        self.home_2.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setKerning(True)
        self.home_2.setFont(font)
        self.home_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/assets/icon/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.home_2.setIcon(icon)
        self.home_2.setIconSize(QSize(40, 40))
        self.home_2.setCheckable(True)
        self.home_2.setChecked(True)
        self.home_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.home_2)

        self.lme_setting_2 = QPushButton(self.hide_sidebar)
        self.lme_setting_2.setObjectName(u"lme_setting_2")
        self.lme_setting_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/assets/icon/testing.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.lme_setting_2.setIcon(icon1)
        self.lme_setting_2.setIconSize(QSize(40, 40))
        self.lme_setting_2.setCheckable(True)
        self.lme_setting_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.lme_setting_2)

        self.sys_setting_1 = QPushButton(self.hide_sidebar)
        self.sys_setting_1.setObjectName(u"sys_setting_1")
        self.sys_setting_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/assets/icon/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.sys_setting_1.setIcon(icon2)
        self.sys_setting_1.setIconSize(QSize(40, 40))
        self.sys_setting_1.setCheckable(True)
        self.sys_setting_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.sys_setting_1)


        self.verticalLayout_13.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 297, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.exit_program_2 = QPushButton(self.hide_sidebar)
        self.exit_program_2.setObjectName(u"exit_program_2")
        font1 = QFont()
        font1.setFamilies([u"Kanit"])
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.exit_program_2.setFont(font1)
        self.exit_program_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/assets/icon/exit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.exit_program_2.setIcon(icon3)
        self.exit_program_2.setIconSize(QSize(40, 40))
#if QT_CONFIG(shortcut)
        self.exit_program_2.setShortcut(u"Ctrl+S")
#endif // QT_CONFIG(shortcut)

        self.verticalLayout_4.addWidget(self.exit_program_2)

        self.restart_program_2 = QPushButton(self.hide_sidebar)
        self.restart_program_2.setObjectName(u"restart_program_2")
        self.restart_program_2.setFont(font1)
        self.restart_program_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/assets/icon/restart.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.restart_program_2.setIcon(icon4)
        self.restart_program_2.setIconSize(QSize(40, 40))
#if QT_CONFIG(shortcut)
        self.restart_program_2.setShortcut(u"Ctrl+S")
#endif // QT_CONFIG(shortcut)

        self.verticalLayout_4.addWidget(self.restart_program_2)

        self.shutdown_2 = QPushButton(self.hide_sidebar)
        self.shutdown_2.setObjectName(u"shutdown_2")
        self.shutdown_2.setFont(font1)
        self.shutdown_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/assets/icon/shutdown1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.shutdown_2.setIcon(icon5)
        self.shutdown_2.setIconSize(QSize(40, 40))
#if QT_CONFIG(shortcut)
        self.shutdown_2.setShortcut(u"Ctrl+S")
#endif // QT_CONFIG(shortcut)

        self.verticalLayout_4.addWidget(self.shutdown_2)


        self.verticalLayout_13.addLayout(self.verticalLayout_4)


        self.horizontalLayout_12.addWidget(self.hide_sidebar)

        self.show_sidebar = QWidget(self.centralwidget)
        self.show_sidebar.setObjectName(u"show_sidebar")
        self.show_sidebar.setEnabled(True)
        font2 = QFont()
        font2.setBold(False)
        self.show_sidebar.setFont(font2)
        self.show_sidebar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.show_sidebar.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(0, 150, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: rgb(0, 150, 255);\n"
"	font-size: 20px;\n"
"	color: white;\n"
"	text-align: left;\n"
"	height: 30px;\n"
"	border: none;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"	padding: 15px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: #f5fafe;\n"
"	color: rgb(0, 150, 255);\n"
"	font-weight: bold;\n"
"}")
        self.verticalLayout_15 = QVBoxLayout(self.show_sidebar)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, 0, -1)
        self.profile_img1 = QLabel(self.show_sidebar)
        self.profile_img1.setObjectName(u"profile_img1")
        self.profile_img1.setMinimumSize(QSize(60, 60))
        self.profile_img1.setMaximumSize(QSize(60, 60))
        self.profile_img1.setPixmap(QPixmap(u":/assets/images/polipharm.png"))
        self.profile_img1.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.profile_img1)

        self.label_3 = QLabel(self.show_sidebar)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setFamilies([u"Kanit"])
        font3.setPointSize(16)
        font3.setBold(True)
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_15.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 20, -1, -1)
        self.home_1 = QPushButton(self.show_sidebar)
        self.home_1.setObjectName(u"home_1")
        font4 = QFont()
        font4.setFamilies([u"Kanit"])
        font4.setBold(False)
        self.home_1.setFont(font4)
        self.home_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.home_1.setIcon(icon)
        self.home_1.setIconSize(QSize(40, 40))
        self.home_1.setCheckable(True)
        self.home_1.setChecked(True)
        self.home_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_1)

        self.lme_setting_1 = QPushButton(self.show_sidebar)
        self.lme_setting_1.setObjectName(u"lme_setting_1")
        font5 = QFont()
        font5.setFamilies([u"Kanit"])
        self.lme_setting_1.setFont(font5)
        self.lme_setting_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.lme_setting_1.setIcon(icon1)
        self.lme_setting_1.setIconSize(QSize(40, 40))
        self.lme_setting_1.setCheckable(True)
        self.lme_setting_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.lme_setting_1)

        self.sys_setting_2 = QPushButton(self.show_sidebar)
        self.sys_setting_2.setObjectName(u"sys_setting_2")
        self.sys_setting_2.setFont(font5)
        self.sys_setting_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.sys_setting_2.setIcon(icon2)
        self.sys_setting_2.setIconSize(QSize(40, 40))
        self.sys_setting_2.setCheckable(True)
        self.sys_setting_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.sys_setting_2)


        self.verticalLayout_15.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 297, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.exit_program_1 = QPushButton(self.show_sidebar)
        self.exit_program_1.setObjectName(u"exit_program_1")
        self.exit_program_1.setFont(font1)
        self.exit_program_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.exit_program_1.setIcon(icon3)
        self.exit_program_1.setIconSize(QSize(40, 40))
#if QT_CONFIG(shortcut)
        self.exit_program_1.setShortcut(u"Ctrl+S")
#endif // QT_CONFIG(shortcut)

        self.verticalLayout_3.addWidget(self.exit_program_1)

        self.restart_program_1 = QPushButton(self.show_sidebar)
        self.restart_program_1.setObjectName(u"restart_program_1")
        self.restart_program_1.setFont(font1)
        self.restart_program_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.restart_program_1.setIcon(icon4)
        self.restart_program_1.setIconSize(QSize(40, 40))
#if QT_CONFIG(shortcut)
        self.restart_program_1.setShortcut(u"Ctrl+S")
#endif // QT_CONFIG(shortcut)

        self.verticalLayout_3.addWidget(self.restart_program_1)

        self.shutdown_1 = QPushButton(self.show_sidebar)
        self.shutdown_1.setObjectName(u"shutdown_1")
        self.shutdown_1.setFont(font1)
        self.shutdown_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.shutdown_1.setIcon(icon5)
        self.shutdown_1.setIconSize(QSize(40, 40))
#if QT_CONFIG(shortcut)
        self.shutdown_1.setShortcut(u"Ctrl+S")
#endif // QT_CONFIG(shortcut)

        self.verticalLayout_3.addWidget(self.shutdown_1)


        self.verticalLayout_15.addLayout(self.verticalLayout_3)


        self.horizontalLayout_12.addWidget(self.show_sidebar)

        self.screen_page = QWidget(self.centralwidget)
        self.screen_page.setObjectName(u"screen_page")
        self.verticalLayout_5 = QVBoxLayout(self.screen_page)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 0, 9, 0)
        self.widget = QWidget(self.screen_page)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 70))
        self.widget.setStyleSheet(u"background-color: rgb(100, 100, 100);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_28 = QFrame(self.widget)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setEnabled(True)
        self.frame_28.setMinimumSize(QSize(0, 0))
        self.frame_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 10, 0)
        self.menu = QPushButton(self.frame_28)
        self.menu.setObjectName(u"menu")
        font6 = QFont()
        font6.setPointSize(9)
        self.menu.setFont(font6)
        self.menu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/assets/icon/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6.addFile(u":/assets/icon/menu_open.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.menu.setIcon(icon6)
        self.menu.setIconSize(QSize(50, 50))
        self.menu.setCheckable(True)
        self.menu.setChecked(False)
        self.menu.setAutoRepeat(True)
        self.menu.setAutoExclusive(True)

        self.horizontalLayout_6.addWidget(self.menu)


        self.horizontalLayout.addWidget(self.frame_28)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.title = QLabel(self.widget)
        self.title.setObjectName(u"title")
        font7 = QFont()
        font7.setFamilies([u"Kanit"])
        font7.setPointSize(24)
        font7.setBold(True)
        self.title.setFont(font7)
        self.title.setStyleSheet(u"")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.title)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.datetime_group_2 = QGroupBox(self.widget)
        self.datetime_group_2.setObjectName(u"datetime_group_2")
        font8 = QFont()
        font8.setPointSize(11)
        self.datetime_group_2.setFont(font8)
        self.datetime_group_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.datetime_group = QVBoxLayout(self.datetime_group_2)
        self.datetime_group.setSpacing(0)
        self.datetime_group.setObjectName(u"datetime_group")
        self.datetime_group.setContentsMargins(0, 5, 0, 5)
        self.time_bar = QLabel(self.datetime_group_2)
        self.time_bar.setObjectName(u"time_bar")
        self.time_bar.setMaximumSize(QSize(140, 16))
        font9 = QFont()
        font9.setFamilies([u"Kanit"])
        font9.setPointSize(14)
        font9.setBold(False)
        self.time_bar.setFont(font9)
        self.time_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.datetime_group.addWidget(self.time_bar)

        self.date_bar = QLabel(self.datetime_group_2)
        self.date_bar.setObjectName(u"date_bar")
        self.date_bar.setMaximumSize(QSize(140, 16))
        self.date_bar.setFont(font9)
        self.date_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.datetime_group.addWidget(self.date_bar)


        self.horizontalLayout.addWidget(self.datetime_group_2)


        self.verticalLayout_5.addWidget(self.widget)

        self.stackedWidget = QStackedWidget(self.screen_page)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 70))
        self.stackedWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.stackedWidget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QGroupBox {\n"
"	border: none;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: none;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"	background: #E3F2FD;\n"
"	color: #1565C0;\n"
"	font-size: 16px;\n"
"	width: 150px;\n"
"	height: 40px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #42A5F5;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background-color: #90CAF9;\n"
"    color: #0D47A1;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: left;\n"
"}\n"
"")
        self.process_page = QWidget()
        self.process_page.setObjectName(u"process_page")
        self.horizontalLayout_61 = QHBoxLayout(self.process_page)
        self.horizontalLayout_61.setSpacing(0)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.process_main_frame = QFrame(self.process_page)
        self.process_main_frame.setObjectName(u"process_main_frame")
        self.process_main_frame.setStyleSheet(u"border: none;")
        self.process_main_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.process_main_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.process_main_frame)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.process_frame = QFrame(self.process_main_frame)
        self.process_frame.setObjectName(u"process_frame")
        self.process_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.process_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.process_frame)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.process_img_frame = QFrame(self.process_frame)
        self.process_img_frame.setObjectName(u"process_img_frame")
        self.process_img_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.process_img_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.process_img_frame)
        self.horizontalLayout_62.setSpacing(0)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 81, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(164, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_62.addItem(self.horizontalSpacer_2)

        self.process_img = QLabel(self.process_img_frame)
        self.process_img.setObjectName(u"process_img")
        self.process_img.setMinimumSize(QSize(350, 250))
        self.process_img.setMaximumSize(QSize(350, 250))
        self.process_img.setPixmap(QPixmap(u":/assets/gif/connecting.gif"))
        self.process_img.setScaledContents(True)
        self.process_img.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_62.addWidget(self.process_img)

        self.horizontalSpacer_3 = QSpacerItem(163, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_62.addItem(self.horizontalSpacer_3)


        self.verticalLayout_32.addWidget(self.process_img_frame)

        self.process_label_line_1 = QLabel(self.process_frame)
        self.process_label_line_1.setObjectName(u"process_label_line_1")
        self.process_label_line_1.setMinimumSize(QSize(0, 35))
        self.process_label_line_1.setMaximumSize(QSize(16777215, 35))
        font10 = QFont()
        font10.setFamilies([u"Kanit"])
        font10.setPointSize(27)
        self.process_label_line_1.setFont(font10)
        self.process_label_line_1.setStyleSheet(u"color: rgb(128, 128, 128);")
        self.process_label_line_1.setFrameShape(QFrame.Shape.NoFrame)
        self.process_label_line_1.setFrameShadow(QFrame.Shadow.Plain)
        self.process_label_line_1.setLineWidth(1)
        self.process_label_line_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_32.addWidget(self.process_label_line_1)

        self.process_label_line_2 = QLabel(self.process_frame)
        self.process_label_line_2.setObjectName(u"process_label_line_2")
        self.process_label_line_2.setMinimumSize(QSize(0, 35))
        self.process_label_line_2.setMaximumSize(QSize(16777215, 35))
        font11 = QFont()
        font11.setFamilies([u"Kanit"])
        font11.setPointSize(20)
        self.process_label_line_2.setFont(font11)
        self.process_label_line_2.setStyleSheet(u"color: rgb(128, 128, 128);")
        self.process_label_line_2.setFrameShape(QFrame.Shape.NoFrame)
        self.process_label_line_2.setFrameShadow(QFrame.Shadow.Plain)
        self.process_label_line_2.setLineWidth(1)
        self.process_label_line_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_32.addWidget(self.process_label_line_2)

        self.process_label_line_3 = QLabel(self.process_frame)
        self.process_label_line_3.setObjectName(u"process_label_line_3")
        self.process_label_line_3.setMinimumSize(QSize(0, 35))
        self.process_label_line_3.setMaximumSize(QSize(16777215, 35))
        self.process_label_line_3.setFont(font11)
        self.process_label_line_3.setStyleSheet(u"color: rgb(128, 128, 128);")
        self.process_label_line_3.setFrameShape(QFrame.Shape.NoFrame)
        self.process_label_line_3.setFrameShadow(QFrame.Shadow.Plain)
        self.process_label_line_3.setLineWidth(1)
        self.process_label_line_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_32.addWidget(self.process_label_line_3)

        self.process_label_line_4 = QLabel(self.process_frame)
        self.process_label_line_4.setObjectName(u"process_label_line_4")
        self.process_label_line_4.setMinimumSize(QSize(0, 30))
        self.process_label_line_4.setMaximumSize(QSize(16777215, 30))
        font12 = QFont()
        font12.setFamilies([u"Kanit"])
        font12.setPointSize(14)
        self.process_label_line_4.setFont(font12)
        self.process_label_line_4.setStyleSheet(u"color: rgb(128, 128, 128);")
        self.process_label_line_4.setFrameShape(QFrame.Shape.NoFrame)
        self.process_label_line_4.setFrameShadow(QFrame.Shadow.Plain)
        self.process_label_line_4.setLineWidth(1)
        self.process_label_line_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_32.addWidget(self.process_label_line_4)


        self.verticalLayout_33.addWidget(self.process_frame)


        self.horizontalLayout_61.addWidget(self.process_main_frame)

        self.stackedWidget.addWidget(self.process_page)
        self.detection_page = QWidget()
        self.detection_page.setObjectName(u"detection_page")
        self.verticalLayout_14 = QVBoxLayout(self.detection_page)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.detection_frame_2 = QFrame(self.detection_page)
        self.detection_frame_2.setObjectName(u"detection_frame_2")
        self.detection_frame_2.setMinimumSize(QSize(0, 70))
        self.detection_frame_2.setMaximumSize(QSize(16777215, 70))
        self.detection_frame_2.setStyleSheet(u"")
        self.detection_frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.detection_frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.detection_frame_2)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.detection_status = QLabel(self.detection_frame_2)
        self.detection_status.setObjectName(u"detection_status")
        self.detection_status.setMinimumSize(QSize(0, 50))
        self.detection_status.setMaximumSize(QSize(16777215, 50))
        font13 = QFont()
        font13.setFamilies([u"Kanit"])
        font13.setPointSize(24)
        self.detection_status.setFont(font13)
        self.detection_status.setStyleSheet(u"background-color: rgb(0, 150, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.detection_status.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_15.addWidget(self.detection_status)


        self.verticalLayout_14.addWidget(self.detection_frame_2)

        self.detection_frame = QFrame(self.detection_page)
        self.detection_frame.setObjectName(u"detection_frame")
        self.detection_frame.setStyleSheet(u"")
        self.detection_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.detection_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.detection_frame)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.widget_5 = QWidget(self.detection_frame)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_7 = QVBoxLayout(self.widget_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.detection_monitor = QLabel(self.widget_5)
        self.detection_monitor.setObjectName(u"detection_monitor")
        self.detection_monitor.setMinimumSize(QSize(250, 250))
        self.detection_monitor.setMaximumSize(QSize(16777215, 16777215))
        self.detection_monitor.setStyleSheet(u"QLabel {\n"
"	border: solid;\n"
"	border-width: 2px;\n"
"	border-color: rgb(111, 105, 37);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.detection_monitor.setPixmap(QPixmap(u":/assets/icon/picture_default.png"))
        self.detection_monitor.setScaledContents(True)

        self.verticalLayout_7.addWidget(self.detection_monitor)

        self.widget_10 = QWidget(self.widget_5)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, 5, -1, 5)
        self.widget_8 = QWidget(self.widget_10)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lot_label_2 = QLabel(self.widget_8)
        self.lot_label_2.setObjectName(u"lot_label_2")
        self.lot_label_2.setMinimumSize(QSize(45, 45))
        self.lot_label_2.setMaximumSize(QSize(45, 45))
        font14 = QFont()
        font14.setFamilies([u"Kanit"])
        font14.setPointSize(18)
        font14.setBold(True)
        self.lot_label_2.setFont(font14)
        self.lot_label_2.setStyleSheet(u"color: rgb(61, 61, 61);")
        self.lot_label_2.setPixmap(QPixmap(u":/assets/icon/ok.png"))
        self.lot_label_2.setScaledContents(True)
        self.lot_label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lot_label_2)

        self.count_ok = QLabel(self.widget_8)
        self.count_ok.setObjectName(u"count_ok")
        self.count_ok.setMaximumSize(QSize(16777215, 16777215))
        font15 = QFont()
        font15.setFamilies([u"Kanit"])
        font15.setPointSize(25)
        font15.setBold(True)
        self.count_ok.setFont(font15)
        self.count_ok.setStyleSheet(u"color: rgb(0, 170, 0);")
        self.count_ok.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.count_ok)


        self.horizontalLayout_21.addWidget(self.widget_8)

        self.widget_11 = QWidget(self.widget_10)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_20 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_20.setSpacing(10)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.lot_label_6 = QLabel(self.widget_11)
        self.lot_label_6.setObjectName(u"lot_label_6")
        self.lot_label_6.setMinimumSize(QSize(35, 35))
        self.lot_label_6.setMaximumSize(QSize(35, 35))
        self.lot_label_6.setFont(font14)
        self.lot_label_6.setStyleSheet(u"color: rgb(61, 61, 61);")
        self.lot_label_6.setPixmap(QPixmap(u":/assets/icon/ng.png"))
        self.lot_label_6.setScaledContents(True)
        self.lot_label_6.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_20.addWidget(self.lot_label_6)

        self.count_ng = QLabel(self.widget_11)
        self.count_ng.setObjectName(u"count_ng")
        self.count_ng.setMaximumSize(QSize(16777215, 16777215))
        self.count_ng.setFont(font15)
        self.count_ng.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.count_ng.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_20.addWidget(self.count_ng)


        self.horizontalLayout_21.addWidget(self.widget_11)

        self.widget_9 = QWidget(self.widget_10)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_19.setSpacing(10)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.lot_label_4 = QLabel(self.widget_9)
        self.lot_label_4.setObjectName(u"lot_label_4")
        self.lot_label_4.setMinimumSize(QSize(35, 35))
        self.lot_label_4.setMaximumSize(QSize(35, 35))
        self.lot_label_4.setFont(font14)
        self.lot_label_4.setStyleSheet(u"")
        self.lot_label_4.setPixmap(QPixmap(u":/assets/icon/all.png"))
        self.lot_label_4.setScaledContents(True)
        self.lot_label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_19.addWidget(self.lot_label_4)

        self.count_total = QLabel(self.widget_9)
        self.count_total.setObjectName(u"count_total")
        self.count_total.setMaximumSize(QSize(16777215, 16777215))
        self.count_total.setFont(font15)
        self.count_total.setStyleSheet(u"color: rgb(61, 61, 61);")
        self.count_total.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_19.addWidget(self.count_total)


        self.horizontalLayout_21.addWidget(self.widget_9)

        self.count_reset = QPushButton(self.widget_10)
        self.count_reset.setObjectName(u"count_reset")
        self.count_reset.setMinimumSize(QSize(0, 0))
        self.count_reset.setMaximumSize(QSize(45, 45))
        font16 = QFont()
        font16.setFamilies([u"Kanit"])
        font16.setPointSize(14)
        font16.setWeight(QFont.Medium)
        font16.setItalic(False)
        self.count_reset.setFont(font16)
        self.count_reset.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(50, 50, 50);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(100, 100, 100);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/assets/icon/reset.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.count_reset.setIcon(icon7)
        self.count_reset.setIconSize(QSize(30, 30))

        self.horizontalLayout_21.addWidget(self.count_reset)


        self.verticalLayout_7.addWidget(self.widget_10)


        self.horizontalLayout_22.addWidget(self.widget_5)

        self.detection_widget = QWidget(self.detection_frame)
        self.detection_widget.setObjectName(u"detection_widget")
        self.detection_widget.setMinimumSize(QSize(250, 0))
        self.detection_widget.setMaximumSize(QSize(300, 16777215))
        self.detection_widget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(220, 220, 220);\n"
"	border-radius: 15px;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.detection_widget)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(12, -1, 12, 0)
        self.detection_view = QLabel(self.detection_widget)
        self.detection_view.setObjectName(u"detection_view")
        self.detection_view.setMinimumSize(QSize(120, 150))
        self.detection_view.setMaximumSize(QSize(16777215, 150))
        self.detection_view.setStyleSheet(u"QLabel {\n"
"	border: solid;\n"
"	border-width: 2px;\n"
"	border-color: rgb(111, 105, 37);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.detection_view.setPixmap(QPixmap(u":/assets/icon/picture_default.png"))
        self.detection_view.setScaledContents(True)

        self.verticalLayout_6.addWidget(self.detection_view)

        self.detection_alert = QLabel(self.detection_widget)
        self.detection_alert.setObjectName(u"detection_alert")
        self.detection_alert.setMinimumSize(QSize(0, 80))
        self.detection_alert.setMaximumSize(QSize(16777215, 80))
        font17 = QFont()
        font17.setFamilies([u"Kanit"])
        font17.setPointSize(50)
        font17.setBold(True)
        self.detection_alert.setFont(font17)
        self.detection_alert.setStyleSheet(u"background-color: rgb(148, 148, 148);\n"
"color: rgb(255, 255, 255);\n"
"margin-top: 10px;")
        self.detection_alert.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.detection_alert)

        self.widget_6 = QWidget(self.detection_widget)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMaximumSize(QSize(16777215, 100))
        self.gridLayout_4 = QGridLayout(self.widget_6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(8)
        self.gridLayout_4.setContentsMargins(0, 10, 0, 10)
        self.lot_detected = QLabel(self.widget_6)
        self.lot_detected.setObjectName(u"lot_detected")
        font18 = QFont()
        font18.setFamilies([u"Kanit"])
        font18.setPointSize(22)
        font18.setBold(True)
        self.lot_detected.setFont(font18)
        self.lot_detected.setStyleSheet(u"color: rgb(61, 61, 61);")
        self.lot_detected.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.lot_detected, 0, 1, 1, 1)

        self.label_29 = QLabel(self.widget_6)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(85, 16777215))
        self.label_29.setFont(font18)
        self.label_29.setStyleSheet(u"color: rgb(61, 61, 61);")
        self.label_29.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_29, 2, 0, 1, 1)

        self.label_27 = QLabel(self.widget_6)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(85, 16777215))
        self.label_27.setFont(font18)
        self.label_27.setStyleSheet(u"color: rgb(61, 61, 61);")
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_27, 0, 0, 1, 1)

        self.label_28 = QLabel(self.widget_6)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(85, 16777215))
        self.label_28.setFont(font18)
        self.label_28.setStyleSheet(u"color: rgb(61, 61, 61);")
        self.label_28.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_28, 1, 0, 1, 1)

        self.mfg_detected = QLabel(self.widget_6)
        self.mfg_detected.setObjectName(u"mfg_detected")
        self.mfg_detected.setFont(font18)
        self.mfg_detected.setStyleSheet(u"color: rgb(61, 61, 61);")
        self.mfg_detected.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.mfg_detected, 1, 1, 1, 1)

        self.exp_detected = QLabel(self.widget_6)
        self.exp_detected.setObjectName(u"exp_detected")
        self.exp_detected.setFont(font18)
        self.exp_detected.setStyleSheet(u"color: rgb(61, 61, 61);")
        self.exp_detected.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.exp_detected, 2, 1, 1, 1)


        self.verticalLayout_6.addWidget(self.widget_6)

        self.widget_4 = QWidget(self.detection_widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(16777215, 50))
        self.widget_4.setStyleSheet(u"")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.capture_test = QPushButton(self.widget_4)
        self.capture_test.setObjectName(u"capture_test")
        self.capture_test.setMinimumSize(QSize(110, 45))
        self.capture_test.setMaximumSize(QSize(16777215, 45))
        self.capture_test.setFont(font16)
        self.capture_test.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(50, 50, 50);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(100, 100, 100);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/assets/icon/camera.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.capture_test.setIcon(icon8)
        self.capture_test.setIconSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.capture_test)

        self.start = QPushButton(self.widget_4)
        self.start.setObjectName(u"start")
        self.start.setMinimumSize(QSize(0, 45))
        self.start.setMaximumSize(QSize(16777215, 45))
        font19 = QFont()
        font19.setFamilies([u"Kanit"])
        font19.setPointSize(12)
        font19.setWeight(QFont.Medium)
        font19.setItalic(False)
        self.start.setFont(font19)
        self.start.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 170, 50);\n"
"	color: white;\n"
"	text-align: center;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	padding: 15px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: rgb(200, 0, 0);\n"
"	color: white;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/assets/keyboard/record.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.start.setIcon(icon9)
        self.start.setIconSize(QSize(25, 25))
        self.start.setCheckable(True)
        self.start.setChecked(False)

        self.horizontalLayout_7.addWidget(self.start)


        self.verticalLayout_6.addWidget(self.widget_4)


        self.horizontalLayout_22.addWidget(self.detection_widget)


        self.verticalLayout_14.addWidget(self.detection_frame)

        self.stackedWidget.addWidget(self.detection_page)
        self.lme_settings_page = QWidget()
        self.lme_settings_page.setObjectName(u"lme_settings_page")
        self.verticalLayout_11 = QVBoxLayout(self.lme_settings_page)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.setting_frame = QFrame(self.lme_settings_page)
        self.setting_frame.setObjectName(u"setting_frame")
        self.setting_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.setting_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.setting_frame)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.setting_title_frame = QFrame(self.setting_frame)
        self.setting_title_frame.setObjectName(u"setting_title_frame")
        self.setting_title_frame.setMinimumSize(QSize(0, 70))
        self.setting_title_frame.setMaximumSize(QSize(16777215, 70))
        self.setting_title_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.setting_title_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.setting_title_frame)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.setting_title = QLabel(self.setting_title_frame)
        self.setting_title.setObjectName(u"setting_title")
        self.setting_title.setMinimumSize(QSize(0, 50))
        self.setting_title.setMaximumSize(QSize(16777215, 50))
        self.setting_title.setFont(font13)
        self.setting_title.setStyleSheet(u"background-color: rgb(52, 157, 77);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.setting_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_18.addWidget(self.setting_title)


        self.verticalLayout_37.addWidget(self.setting_title_frame)

        self.weighingSettings_Frame = QFrame(self.setting_frame)
        self.weighingSettings_Frame.setObjectName(u"weighingSettings_Frame")
        self.weighingSettings_Frame.setStyleSheet(u"QLabel {\n"
"	color: rgb(60, 60, 60);\n"
"	border: none;\n"
"	margin: 0;\n"
"}")
        self.weighingSettings_Frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.weighingSettings_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.weighingSettings_Frame)
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.lme_settings_monitor = QLabel(self.weighingSettings_Frame)
        self.lme_settings_monitor.setObjectName(u"lme_settings_monitor")
        self.lme_settings_monitor.setMinimumSize(QSize(250, 0))
        self.lme_settings_monitor.setMaximumSize(QSize(16777215, 16777215))
        self.lme_settings_monitor.setStyleSheet(u"QLabel {\n"
"	border: solid;\n"
"	border-width: 2px;\n"
"	border-color: rgb(111, 105, 37);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.lme_settings_monitor.setPixmap(QPixmap(u":/assets/icon/picture_default.png"))
        self.lme_settings_monitor.setScaledContents(True)

        self.horizontalLayout_14.addWidget(self.lme_settings_monitor)

        self.set_widget = QWidget(self.weighingSettings_Frame)
        self.set_widget.setObjectName(u"set_widget")
        self.set_widget.setMinimumSize(QSize(300, 0))
        self.set_widget.setMaximumSize(QSize(350, 16777215))
        self.set_widget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(220, 220, 220);\n"
"	border-radius: 15px;\n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.set_widget)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(12, 12, 12, 12)
        self.webcam_setting_view = QLabel(self.set_widget)
        self.webcam_setting_view.setObjectName(u"webcam_setting_view")
        self.webcam_setting_view.setMinimumSize(QSize(120, 150))
        self.webcam_setting_view.setMaximumSize(QSize(16777215, 16777215))
        self.webcam_setting_view.setStyleSheet(u"QLabel {\n"
"	border: solid;\n"
"	border-width: 2px;\n"
"	border-color: rgb(111, 105, 37);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.webcam_setting_view.setPixmap(QPixmap(u":/assets/icon/picture_default.png"))
        self.webcam_setting_view.setScaledContents(True)

        self.verticalLayout_8.addWidget(self.webcam_setting_view)

        self.widget_7 = QWidget(self.set_widget)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMaximumSize(QSize(16777215, 130))
        self.formLayout = QFormLayout(self.widget_7)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(-1, 5, -1, 5)
        self.label_24 = QLabel(self.widget_7)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(85, 16777215))
        self.label_24.setFont(font18)
        self.label_24.setStyleSheet(u"color: rgb(61, 61, 61);")
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_24)

        self.lot_set = QLineEdit(self.widget_7)
        self.lot_set.setObjectName(u"lot_set")
        font20 = QFont()
        font20.setPointSize(22)
        self.lot_set.setFont(font20)
        self.lot_set.setStyleSheet(u"background-color: white;\n"
"color: #868686;\n"
"border-radius: 8px;\n"
"text-align: center;")
        self.lot_set.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.lot_set.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lot_set.setClearButtonEnabled(False)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lot_set)

        self.label_25 = QLabel(self.widget_7)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(50, 0))
        self.label_25.setMaximumSize(QSize(85, 16777215))
        self.label_25.setFont(font18)
        self.label_25.setStyleSheet(u"color: rgb(61, 61, 61);")
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_25)

        self.mfg_set = QLineEdit(self.widget_7)
        self.mfg_set.setObjectName(u"mfg_set")
        self.mfg_set.setFont(font20)
        self.mfg_set.setStyleSheet(u"background-color: white;\n"
"color: #868686;\n"
"border-radius: 8px;\n"
"text-align: center;")
        self.mfg_set.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.mfg_set.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mfg_set.setClearButtonEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.mfg_set)

        self.label_26 = QLabel(self.widget_7)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(85, 16777215))
        self.label_26.setFont(font18)
        self.label_26.setStyleSheet(u"color: rgb(61, 61, 61);")
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_26)

        self.exp_set = QLineEdit(self.widget_7)
        self.exp_set.setObjectName(u"exp_set")
        self.exp_set.setFont(font20)
        self.exp_set.setStyleSheet(u"background-color: white;\n"
"color: #868686;\n"
"border-radius: 8px;\n"
"text-align: center;")
        self.exp_set.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.exp_set.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.exp_set.setClearButtonEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.exp_set)


        self.verticalLayout_8.addWidget(self.widget_7)

        self.save_images_detection = QPushButton(self.set_widget)
        self.save_images_detection.setObjectName(u"save_images_detection")
        self.save_images_detection.setMaximumSize(QSize(16777215, 45))
        font21 = QFont()
        font21.setFamilies([u"Kanit"])
        font21.setPointSize(12)
        self.save_images_detection.setFont(font21)
        self.save_images_detection.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(100, 100, 100);\n"
"	color: rgb(161, 161, 161);\n"
"	color: white;\n"
"	text-align: center;\n"
"	height: 30px;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	padding: 15px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: rgb(50, 50, 50);\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/assets/icon/save-images.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.save_images_detection.setIcon(icon10)
        self.save_images_detection.setIconSize(QSize(35, 35))
        self.save_images_detection.setCheckable(True)

        self.verticalLayout_8.addWidget(self.save_images_detection)

        self.widget_3 = QWidget(self.set_widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(16777215, 80))
        self.widget_3.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(50, 50, 50);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(100, 100, 100);\n"
"}\n"
"")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.capture_set = QPushButton(self.widget_3)
        self.capture_set.setObjectName(u"capture_set")
        self.capture_set.setMinimumSize(QSize(0, 45))
        self.capture_set.setMaximumSize(QSize(16777215, 45))
        self.capture_set.setFont(font19)
        self.capture_set.setStyleSheet(u"")
        self.capture_set.setIcon(icon8)
        self.capture_set.setIconSize(QSize(40, 40))

        self.horizontalLayout_5.addWidget(self.capture_set)

        self.save_set = QPushButton(self.widget_3)
        self.save_set.setObjectName(u"save_set")
        self.save_set.setMinimumSize(QSize(0, 45))
        self.save_set.setMaximumSize(QSize(16777215, 45))
        self.save_set.setFont(font19)
        self.save_set.setStyleSheet(u"")
        icon11 = QIcon()
        icon11.addFile(u":/assets/icon/save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.save_set.setIcon(icon11)
        self.save_set.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.save_set)


        self.verticalLayout_8.addWidget(self.widget_3)


        self.horizontalLayout_14.addWidget(self.set_widget)


        self.verticalLayout_37.addWidget(self.weighingSettings_Frame)


        self.verticalLayout_11.addWidget(self.setting_frame)

        self.stackedWidget.addWidget(self.lme_settings_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.horizontalLayout_24 = QHBoxLayout(self.settings_page)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.tabWidget = QTabWidget(self.settings_page)
        self.tabWidget.setObjectName(u"tabWidget")
        font22 = QFont()
        font22.setPointSize(14)
        font22.setKerning(True)
        self.tabWidget.setFont(font22)
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabShape(QTabWidget.TabShape.Triangular)
        self.tabWidget.setIconSize(QSize(30, 30))
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideLeft)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.camera_settings_tab = QWidget()
        self.camera_settings_tab.setObjectName(u"camera_settings_tab")
        self.verticalLayout_24 = QVBoxLayout(self.camera_settings_tab)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame_15 = QFrame(self.camera_settings_tab)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"border: none")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_26.setSpacing(10)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_26 = QFrame(self.frame_15)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_26)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.camera_settings_monitor = QLabel(self.frame_26)
        self.camera_settings_monitor.setObjectName(u"camera_settings_monitor")
        self.camera_settings_monitor.setMinimumSize(QSize(250, 0))
        self.camera_settings_monitor.setMaximumSize(QSize(16777215, 16777215))
        self.camera_settings_monitor.setStyleSheet(u"QLabel {\n"
"	border: solid;\n"
"	border-width: 2px;\n"
"	border-color: rgb(111, 105, 37);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.camera_settings_monitor.setPixmap(QPixmap(u":/assets/icon/picture_default.png"))
        self.camera_settings_monitor.setScaledContents(True)

        self.verticalLayout_10.addWidget(self.camera_settings_monitor)

        self.camera_filter_1 = QPushButton(self.frame_26)
        self.camera_filter_1.setObjectName(u"camera_filter_1")
        self.camera_filter_1.setMinimumSize(QSize(0, 45))
        font23 = QFont()
        font23.setFamilies([u"Kanit"])
        font23.setPointSize(16)
        font23.setWeight(QFont.Medium)
        font23.setItalic(False)
        self.camera_filter_1.setFont(font23)
        self.camera_filter_1.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(120, 120, 120);\n"
"	color: white;\n"
"	text-align: center;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: rgb(60, 60, 60);\n"
"	color: white;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/assets/icon/effect.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.camera_filter_1.setIcon(icon12)
        self.camera_filter_1.setIconSize(QSize(30, 30))
        self.camera_filter_1.setCheckable(True)

        self.verticalLayout_10.addWidget(self.camera_filter_1)


        self.horizontalLayout_26.addWidget(self.frame_26)

        self.camera_setting_widget_2 = QWidget(self.frame_15)
        self.camera_setting_widget_2.setObjectName(u"camera_setting_widget_2")
        self.camera_setting_widget_2.setMinimumSize(QSize(380, 0))
        self.camera_setting_widget_2.setMaximumSize(QSize(400, 16777215))
        font24 = QFont()
        font24.setPointSize(13)
        self.camera_setting_widget_2.setFont(font24)
        self.camera_setting_widget_2.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(220, 220, 220);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel {\n"
"	color: #868686\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: none;\n"
"    height: 12px;\n"
"    background: #A4D3FF;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #2979FF;\n"
"    border: 2px solid #1565C0; /* \u0e02\u0e2d\u0e1a\u0e19\u0e49\u0e33\u0e40\u0e07\u0e34\u0e19\u0e40\u0e02\u0e49\u0e21 */\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    margin: -4px 0;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: #5393FF; /* \u0e2a\u0e35\u0e2d\u0e48\u0e2d\u0e19\u0e02\u0e36\u0e49\u0e19\u0e40\u0e21\u0e37\u0e48\u0e2d hover */\n"
"    border: 2px solid #1E88E5;\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: #77AAFF;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: #BDDFFF;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout_22 = QVBoxLayout(self.camera_setting_widget_2)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.brightnessWidget_16 = QWidget(self.camera_setting_widget_2)
        self.brightnessWidget_16.setObjectName(u"brightnessWidget_16")
        self.horizontalLayout_39 = QHBoxLayout(self.brightnessWidget_16)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.frame_24 = QFrame(self.brightnessWidget_16)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_24)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.label_74 = QLabel(self.frame_24)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setFont(font12)

        self.verticalLayout_36.addWidget(self.label_74)

        self.label_75 = QLabel(self.frame_24)
        self.label_75.setObjectName(u"label_75")
        font25 = QFont()
        font25.setFamilies([u"Kanit"])
        font25.setPointSize(10)
        self.label_75.setFont(font25)

        self.verticalLayout_36.addWidget(self.label_75)


        self.horizontalLayout_39.addWidget(self.frame_24)

        self.horizontalSpacer_5 = QSpacerItem(77, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_5)

        self.exposureTime = QLineEdit(self.brightnessWidget_16)
        self.exposureTime.setObjectName(u"exposureTime")
        self.exposureTime.setMaximumSize(QSize(100, 16777215))
        font26 = QFont()
        font26.setPointSize(14)
        self.exposureTime.setFont(font26)
        self.exposureTime.setStyleSheet(u"background-color: white;\n"
"color: #868686;\n"
"border-radius: 8px;\n"
"text-align: center;")
        self.exposureTime.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly)
        self.exposureTime.setMaxLength(100000)
        self.exposureTime.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.exposureTime.setClearButtonEnabled(False)

        self.horizontalLayout_39.addWidget(self.exposureTime)

        self.label_5 = QLabel(self.brightnessWidget_16)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font12)

        self.horizontalLayout_39.addWidget(self.label_5)


        self.verticalLayout_22.addWidget(self.brightnessWidget_16)

        self.brightnessWidget_17 = QWidget(self.camera_setting_widget_2)
        self.brightnessWidget_17.setObjectName(u"brightnessWidget_17")
        self.horizontalLayout_41 = QHBoxLayout(self.brightnessWidget_17)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.frame_25 = QFrame(self.brightnessWidget_17)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_25)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.label_76 = QLabel(self.frame_25)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setFont(font12)

        self.verticalLayout_38.addWidget(self.label_76)

        self.label_77 = QLabel(self.frame_25)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setFont(font25)

        self.verticalLayout_38.addWidget(self.label_77)


        self.horizontalLayout_41.addWidget(self.frame_25)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_6)

        self.delayShutter = QLineEdit(self.brightnessWidget_17)
        self.delayShutter.setObjectName(u"delayShutter")
        self.delayShutter.setMaximumSize(QSize(100, 16777215))
        self.delayShutter.setFont(font26)
        self.delayShutter.setStyleSheet(u"background-color: white;\n"
"color: #868686;\n"
"border-radius: 8px;\n"
"text-align: center;")
        self.delayShutter.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly)
        self.delayShutter.setMaxLength(1000)
        self.delayShutter.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.delayShutter.setClearButtonEnabled(False)

        self.horizontalLayout_41.addWidget(self.delayShutter)

        self.label_8 = QLabel(self.brightnessWidget_17)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font12)

        self.horizontalLayout_41.addWidget(self.label_8)


        self.verticalLayout_22.addWidget(self.brightnessWidget_17)

        self.brightnessWidget_18 = QWidget(self.camera_setting_widget_2)
        self.brightnessWidget_18.setObjectName(u"brightnessWidget_18")
        self.horizontalLayout_42 = QHBoxLayout(self.brightnessWidget_18)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(-1, 0, -1, 0)
        self.label_9 = QLabel(self.brightnessWidget_18)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font12)

        self.horizontalLayout_42.addWidget(self.label_9)

        self.cameraBrightness = QSlider(self.brightnessWidget_18)
        self.cameraBrightness.setObjectName(u"cameraBrightness")
        self.cameraBrightness.setMinimumSize(QSize(0, 50))
        self.cameraBrightness.setSizeIncrement(QSize(0, 0))
        self.cameraBrightness.setBaseSize(QSize(50, 50))
        self.cameraBrightness.setFont(font)
        self.cameraBrightness.setAcceptDrops(False)
        self.cameraBrightness.setStyleSheet(u"")
        self.cameraBrightness.setMaximum(255)
        self.cameraBrightness.setValue(0)
        self.cameraBrightness.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_42.addWidget(self.cameraBrightness)


        self.verticalLayout_22.addWidget(self.brightnessWidget_18)

        self.contrastWidget_2 = QWidget(self.camera_setting_widget_2)
        self.contrastWidget_2.setObjectName(u"contrastWidget_2")
        self.horizontalLayout_43 = QHBoxLayout(self.contrastWidget_2)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(-1, 0, -1, 0)
        self.label_10 = QLabel(self.contrastWidget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font12)

        self.horizontalLayout_43.addWidget(self.label_10)

        self.cameraContrast = QSlider(self.contrastWidget_2)
        self.cameraContrast.setObjectName(u"cameraContrast")
        self.cameraContrast.setMinimumSize(QSize(0, 50))
        self.cameraContrast.setMaximum(255)
        self.cameraContrast.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_43.addWidget(self.cameraContrast)


        self.verticalLayout_22.addWidget(self.contrastWidget_2)

        self.saturationWidget_2 = QWidget(self.camera_setting_widget_2)
        self.saturationWidget_2.setObjectName(u"saturationWidget_2")
        self.horizontalLayout_44 = QHBoxLayout(self.saturationWidget_2)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(-1, 0, -1, 0)
        self.label_11 = QLabel(self.saturationWidget_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font12)

        self.horizontalLayout_44.addWidget(self.label_11)

        self.cameraSaturation = QSlider(self.saturationWidget_2)
        self.cameraSaturation.setObjectName(u"cameraSaturation")
        self.cameraSaturation.setMinimumSize(QSize(0, 50))
        self.cameraSaturation.setMaximum(255)
        self.cameraSaturation.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_44.addWidget(self.cameraSaturation)


        self.verticalLayout_22.addWidget(self.saturationWidget_2)

        self.analogueGainWidget_2 = QWidget(self.camera_setting_widget_2)
        self.analogueGainWidget_2.setObjectName(u"analogueGainWidget_2")
        self.horizontalLayout_45 = QHBoxLayout(self.analogueGainWidget_2)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(-1, 0, -1, 0)
        self.label_12 = QLabel(self.analogueGainWidget_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font12)

        self.horizontalLayout_45.addWidget(self.label_12)

        self.cameraAnalogueGain = QSlider(self.analogueGainWidget_2)
        self.cameraAnalogueGain.setObjectName(u"cameraAnalogueGain")
        self.cameraAnalogueGain.setMinimumSize(QSize(0, 50))
        self.cameraAnalogueGain.setMaximum(255)
        self.cameraAnalogueGain.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_45.addWidget(self.cameraAnalogueGain)


        self.verticalLayout_22.addWidget(self.analogueGainWidget_2)

        self.SharpnessWidget_2 = QWidget(self.camera_setting_widget_2)
        self.SharpnessWidget_2.setObjectName(u"SharpnessWidget_2")
        self.horizontalLayout_46 = QHBoxLayout(self.SharpnessWidget_2)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(-1, 0, -1, 0)
        self.label_13 = QLabel(self.SharpnessWidget_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font12)

        self.horizontalLayout_46.addWidget(self.label_13)

        self.cameraSharpness = QSlider(self.SharpnessWidget_2)
        self.cameraSharpness.setObjectName(u"cameraSharpness")
        self.cameraSharpness.setMinimumSize(QSize(0, 50))
        self.cameraSharpness.setMaximum(255)
        self.cameraSharpness.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_46.addWidget(self.cameraSharpness)


        self.verticalLayout_22.addWidget(self.SharpnessWidget_2)


        self.horizontalLayout_26.addWidget(self.camera_setting_widget_2)


        self.verticalLayout_24.addWidget(self.frame_15)

        icon13 = QIcon()
        icon13.addFile(u":/assets/icon/camera.png", QSize(), QIcon.Mode.Active, QIcon.State.On)
        self.tabWidget.addTab(self.camera_settings_tab, icon13, "")
        self.sys_settings_tab = QWidget()
        self.sys_settings_tab.setObjectName(u"sys_settings_tab")
        self.horizontalLayout_27 = QHBoxLayout(self.sys_settings_tab)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.frame_16 = QFrame(self.sys_settings_tab)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"border: none")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_32.setSpacing(10)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_16)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_9)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.sys_settings_monitor = QLabel(self.frame_9)
        self.sys_settings_monitor.setObjectName(u"sys_settings_monitor")
        self.sys_settings_monitor.setMinimumSize(QSize(250, 0))
        self.sys_settings_monitor.setMaximumSize(QSize(16777215, 16777215))
        self.sys_settings_monitor.setStyleSheet(u"QLabel {\n"
"	border: solid;\n"
"	border-width: 2px;\n"
"	border-color: rgb(111, 105, 37);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.sys_settings_monitor.setPixmap(QPixmap(u":/assets/icon/picture_default.png"))
        self.sys_settings_monitor.setScaledContents(True)

        self.verticalLayout_18.addWidget(self.sys_settings_monitor)

        self.camera_filter_2 = QPushButton(self.frame_9)
        self.camera_filter_2.setObjectName(u"camera_filter_2")
        self.camera_filter_2.setMinimumSize(QSize(0, 45))
        self.camera_filter_2.setFont(font23)
        self.camera_filter_2.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(120, 120, 120);\n"
"	color: white;\n"
"	text-align: center;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: rgb(60, 60, 60);\n"
"	color: white;\n"
"}")
        self.camera_filter_2.setIcon(icon12)
        self.camera_filter_2.setIconSize(QSize(30, 30))
        self.camera_filter_2.setCheckable(True)

        self.verticalLayout_18.addWidget(self.camera_filter_2)


        self.horizontalLayout_32.addWidget(self.frame_9)

        self.camera_setting_widget_4 = QWidget(self.frame_16)
        self.camera_setting_widget_4.setObjectName(u"camera_setting_widget_4")
        self.camera_setting_widget_4.setMinimumSize(QSize(380, 0))
        self.camera_setting_widget_4.setMaximumSize(QSize(400, 16777215))
        self.camera_setting_widget_4.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(220, 220, 220);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel {\n"
"	color: #868686\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: none;\n"
"    height: 12px;\n"
"    background: #A4D3FF;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #2979FF;\n"
"    border: 2px solid #1565C0; /* \u0e02\u0e2d\u0e1a\u0e19\u0e49\u0e33\u0e40\u0e07\u0e34\u0e19\u0e40\u0e02\u0e49\u0e21 */\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    margin: -4px 0;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: #5393FF; /* \u0e2a\u0e35\u0e2d\u0e48\u0e2d\u0e19\u0e02\u0e36\u0e49\u0e19\u0e40\u0e21\u0e37\u0e48\u0e2d hover */\n"
"    border: 2px solid #1E88E5;\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: #77AAFF;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: #BDDFFF;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout_9 = QVBoxLayout(self.camera_setting_widget_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(15, -1, 9, -1)
        self.brightnessWidget_23 = QWidget(self.camera_setting_widget_4)
        self.brightnessWidget_23.setObjectName(u"brightnessWidget_23")
        self.brightnessWidget_23.setMaximumSize(QSize(16777215, 80))
        self.brightnessWidget_23.setStyleSheet(u"")
        self.horizontalLayout_48 = QHBoxLayout(self.brightnessWidget_23)
        self.horizontalLayout_48.setSpacing(5)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.brightnessWidget_23)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_22)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.label_72 = QLabel(self.frame_22)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setFont(font12)

        self.verticalLayout_34.addWidget(self.label_72)

        self.label_73 = QLabel(self.frame_22)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setFont(font25)

        self.verticalLayout_34.addWidget(self.label_73)


        self.horizontalLayout_48.addWidget(self.frame_22)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_48.addItem(self.horizontalSpacer_29)

        self.numberStickerBeforeDetection = QLineEdit(self.brightnessWidget_23)
        self.numberStickerBeforeDetection.setObjectName(u"numberStickerBeforeDetection")
        self.numberStickerBeforeDetection.setMaximumSize(QSize(60, 16777215))
        self.numberStickerBeforeDetection.setFont(font26)
        self.numberStickerBeforeDetection.setStyleSheet(u"background-color: white;\n"
"color: #868686;\n"
"border-radius: 6px;\n"
"border: 1px solid #808080;\n"
"text-align: center;")
        self.numberStickerBeforeDetection.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly)
        self.numberStickerBeforeDetection.setMaxLength(10)
        self.numberStickerBeforeDetection.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.numberStickerBeforeDetection.setClearButtonEnabled(False)

        self.horizontalLayout_48.addWidget(self.numberStickerBeforeDetection)

        self.label_57 = QLabel(self.brightnessWidget_23)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMinimumSize(QSize(50, 0))
        self.label_57.setMaximumSize(QSize(50, 16777215))
        self.label_57.setFont(font12)

        self.horizontalLayout_48.addWidget(self.label_57)


        self.verticalLayout_9.addWidget(self.brightnessWidget_23)

        self.brightnessWidget_22 = QWidget(self.camera_setting_widget_4)
        self.brightnessWidget_22.setObjectName(u"brightnessWidget_22")
        self.brightnessWidget_22.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_38 = QHBoxLayout(self.brightnessWidget_22)
        self.horizontalLayout_38.setSpacing(5)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.brightnessWidget_22)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_21)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_68 = QLabel(self.frame_21)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setFont(font12)

        self.verticalLayout_30.addWidget(self.label_68)

        self.label_69 = QLabel(self.frame_21)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setFont(font25)

        self.verticalLayout_30.addWidget(self.label_69)


        self.horizontalLayout_38.addWidget(self.frame_21)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_26)

        self.delayBeforeReject = QLineEdit(self.brightnessWidget_22)
        self.delayBeforeReject.setObjectName(u"delayBeforeReject")
        self.delayBeforeReject.setMaximumSize(QSize(60, 16777215))
        self.delayBeforeReject.setFont(font26)
        self.delayBeforeReject.setStyleSheet(u"background-color: white;\n"
"color: #868686;\n"
"border-radius: 6px;\n"
"border: 1px solid #808080;\n"
"text-align: center;")
        self.delayBeforeReject.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly)
        self.delayBeforeReject.setMaxLength(5000)
        self.delayBeforeReject.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.delayBeforeReject.setClearButtonEnabled(False)

        self.horizontalLayout_38.addWidget(self.delayBeforeReject)

        self.label_51 = QLabel(self.brightnessWidget_22)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMinimumSize(QSize(50, 0))
        self.label_51.setMaximumSize(QSize(50, 16777215))
        self.label_51.setFont(font12)

        self.horizontalLayout_38.addWidget(self.label_51)


        self.verticalLayout_9.addWidget(self.brightnessWidget_22)

        self.brightnessWidget_24 = QWidget(self.camera_setting_widget_4)
        self.brightnessWidget_24.setObjectName(u"brightnessWidget_24")
        self.brightnessWidget_24.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_47 = QHBoxLayout(self.brightnessWidget_24)
        self.horizontalLayout_47.setSpacing(5)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.brightnessWidget_24)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_20)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_66 = QLabel(self.frame_20)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setFont(font12)

        self.verticalLayout_29.addWidget(self.label_66)

        self.label_67 = QLabel(self.frame_20)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setFont(font25)

        self.verticalLayout_29.addWidget(self.label_67)


        self.horizontalLayout_47.addWidget(self.frame_20)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_27)

        self.rejectionPeriod = QLineEdit(self.brightnessWidget_24)
        self.rejectionPeriod.setObjectName(u"rejectionPeriod")
        self.rejectionPeriod.setMaximumSize(QSize(60, 16777215))
        self.rejectionPeriod.setFont(font26)
        self.rejectionPeriod.setStyleSheet(u"background-color: white;\n"
"color: #868686;\n"
"border-radius: 6px;\n"
"border: 1px solid #808080;\n"
"text-align: center;")
        self.rejectionPeriod.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly)
        self.rejectionPeriod.setMaxLength(1000)
        self.rejectionPeriod.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.rejectionPeriod.setClearButtonEnabled(False)

        self.horizontalLayout_47.addWidget(self.rejectionPeriod)

        self.label_53 = QLabel(self.brightnessWidget_24)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setMinimumSize(QSize(50, 0))
        self.label_53.setMaximumSize(QSize(50, 16777215))
        self.label_53.setFont(font12)

        self.horizontalLayout_47.addWidget(self.label_53)


        self.verticalLayout_9.addWidget(self.brightnessWidget_24)

        self.brightnessWidget_27 = QWidget(self.camera_setting_widget_4)
        self.brightnessWidget_27.setObjectName(u"brightnessWidget_27")
        self.horizontalLayout_40 = QHBoxLayout(self.brightnessWidget_27)
        self.horizontalLayout_40.setSpacing(5)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.brightnessWidget_27)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_19)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_64 = QLabel(self.frame_19)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setFont(font12)

        self.verticalLayout_25.addWidget(self.label_64)

        self.label_65 = QLabel(self.frame_19)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setFont(font25)

        self.verticalLayout_25.addWidget(self.label_65)


        self.horizontalLayout_40.addWidget(self.frame_19)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_25)

        self.frameRate = QLineEdit(self.brightnessWidget_27)
        self.frameRate.setObjectName(u"frameRate")
        self.frameRate.setMaximumSize(QSize(60, 16777215))
        self.frameRate.setFont(font26)
        self.frameRate.setStyleSheet(u"background-color: white;\n"
"color: #868686;\n"
"border-radius: 6px;\n"
"border: 1px solid #808080;\n"
"text-align: center;")
        self.frameRate.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly)
        self.frameRate.setMaxLength(100)
        self.frameRate.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frameRate.setClearButtonEnabled(False)

        self.horizontalLayout_40.addWidget(self.frameRate)

        self.label_49 = QLabel(self.brightnessWidget_27)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMinimumSize(QSize(50, 0))
        self.label_49.setMaximumSize(QSize(50, 16777215))
        self.label_49.setFont(font12)

        self.horizontalLayout_40.addWidget(self.label_49)


        self.verticalLayout_9.addWidget(self.brightnessWidget_27)

        self.brightnessWidget_25 = QWidget(self.camera_setting_widget_4)
        self.brightnessWidget_25.setObjectName(u"brightnessWidget_25")
        self.brightnessWidget_25.setMaximumSize(QSize(16777215, 80))
        self.brightnessWidget_25.setStyleSheet(u"")
        self.horizontalLayout_34 = QHBoxLayout(self.brightnessWidget_25)
        self.horizontalLayout_34.setSpacing(5)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.brightnessWidget_25)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_14)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_62 = QLabel(self.frame_14)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setFont(font12)

        self.verticalLayout_23.addWidget(self.label_62)

        self.label_63 = QLabel(self.frame_14)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setFont(font25)

        self.verticalLayout_23.addWidget(self.label_63)


        self.horizontalLayout_34.addWidget(self.frame_14)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_30)

        self.rotateImage = QLineEdit(self.brightnessWidget_25)
        self.rotateImage.setObjectName(u"rotateImage")
        self.rotateImage.setMaximumSize(QSize(60, 16777215))
        self.rotateImage.setFont(font26)
        self.rotateImage.setStyleSheet(u"background-color: white;\n"
"color: #868686;\n"
"border-radius: 6px;\n"
"border: 1px solid #808080;\n"
"text-align: center;")
        self.rotateImage.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly)
        self.rotateImage.setMaxLength(380)
        self.rotateImage.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.rotateImage.setClearButtonEnabled(False)

        self.horizontalLayout_34.addWidget(self.rotateImage)

        self.label_59 = QLabel(self.brightnessWidget_25)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMinimumSize(QSize(50, 0))
        self.label_59.setMaximumSize(QSize(50, 16777215))
        self.label_59.setFont(font12)

        self.horizontalLayout_34.addWidget(self.label_59)


        self.verticalLayout_9.addWidget(self.brightnessWidget_25)

        self.brightnessWidget_26 = QWidget(self.camera_setting_widget_4)
        self.brightnessWidget_26.setObjectName(u"brightnessWidget_26")
        self.horizontalLayout_35 = QHBoxLayout(self.brightnessWidget_26)
        self.horizontalLayout_35.setSpacing(5)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.brightnessWidget_26)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_11)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_60 = QLabel(self.frame_11)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font12)

        self.verticalLayout_20.addWidget(self.label_60)

        self.label_61 = QLabel(self.frame_11)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font25)

        self.verticalLayout_20.addWidget(self.label_61)


        self.horizontalLayout_35.addWidget(self.frame_11)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_28)

        self.detectionPercentage = QLineEdit(self.brightnessWidget_26)
        self.detectionPercentage.setObjectName(u"detectionPercentage")
        self.detectionPercentage.setMaximumSize(QSize(60, 16777215))
        self.detectionPercentage.setFont(font26)
        self.detectionPercentage.setStyleSheet(u"background-color: white;\n"
"color: #868686;\n"
"border-radius: 6px;\n"
"border: 1px solid #808080;\n"
"text-align: center;")
        self.detectionPercentage.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly)
        self.detectionPercentage.setMaxLength(100)
        self.detectionPercentage.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.detectionPercentage.setClearButtonEnabled(False)

        self.horizontalLayout_35.addWidget(self.detectionPercentage)

        self.label_55 = QLabel(self.brightnessWidget_26)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMinimumSize(QSize(50, 0))
        self.label_55.setMaximumSize(QSize(50, 16777215))
        self.label_55.setFont(font12)

        self.horizontalLayout_35.addWidget(self.label_55)


        self.verticalLayout_9.addWidget(self.brightnessWidget_26)

        self.brightnessWidget_28 = QWidget(self.camera_setting_widget_4)
        self.brightnessWidget_28.setObjectName(u"brightnessWidget_28")
        self.horizontalLayout_33 = QHBoxLayout(self.brightnessWidget_28)
        self.horizontalLayout_33.setSpacing(5)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.brightnessWidget_28)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_10)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_48 = QLabel(self.frame_10)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font12)

        self.verticalLayout_19.addWidget(self.label_48)

        self.label_47 = QLabel(self.frame_10)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font25)

        self.verticalLayout_19.addWidget(self.label_47)


        self.horizontalLayout_33.addWidget(self.frame_10)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_24)

        self.detection_resize_percent = QLineEdit(self.brightnessWidget_28)
        self.detection_resize_percent.setObjectName(u"detection_resize_percent")
        self.detection_resize_percent.setMaximumSize(QSize(60, 16777215))
        self.detection_resize_percent.setFont(font26)
        self.detection_resize_percent.setStyleSheet(u"background-color: white;\n"
"color: #868686;\n"
"border-radius: 6px;\n"
"border: 1px solid #808080;\n"
"text-align: center;")
        self.detection_resize_percent.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly)
        self.detection_resize_percent.setMaxLength(100)
        self.detection_resize_percent.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.detection_resize_percent.setClearButtonEnabled(False)

        self.horizontalLayout_33.addWidget(self.detection_resize_percent)

        self.label_46 = QLabel(self.brightnessWidget_28)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(50, 0))
        self.label_46.setMaximumSize(QSize(50, 16777215))
        self.label_46.setFont(font12)

        self.horizontalLayout_33.addWidget(self.label_46)


        self.verticalLayout_9.addWidget(self.brightnessWidget_28)

        self.frame_8 = QFrame(self.camera_setting_widget_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_25.setSpacing(5)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 9, 0)
        self.frame_23 = QFrame(self.frame_8)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_23)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.label_50 = QLabel(self.frame_23)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font12)

        self.verticalLayout_35.addWidget(self.label_50)

        self.label_52 = QLabel(self.frame_23)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font25)

        self.verticalLayout_35.addWidget(self.label_52)


        self.horizontalLayout_25.addWidget(self.frame_23)

        self.ocr_engine = QComboBox(self.frame_8)
        self.ocr_engine.addItem("")
        self.ocr_engine.addItem("")
        self.ocr_engine.setObjectName(u"ocr_engine")
        font27 = QFont()
        self.ocr_engine.setFont(font27)
        self.ocr_engine.setStyleSheet(u"QComboBox {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #cccccc;\n"
"    border-radius: 8px;\n"
"    padding: 6px 12px;\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    width: 28px;\n"
"}\n"
"")

        self.horizontalLayout_25.addWidget(self.ocr_engine)


        self.verticalLayout_9.addWidget(self.frame_8)


        self.horizontalLayout_32.addWidget(self.camera_setting_widget_4)


        self.horizontalLayout_27.addWidget(self.frame_16)

        icon14 = QIcon()
        icon14.addFile(u":/assets/icon/settings.png", QSize(), QIcon.Mode.Active, QIcon.State.On)
        self.tabWidget.addTab(self.sys_settings_tab, icon14, "")
        self.io_test = QWidget()
        self.io_test.setObjectName(u"io_test")
        self.verticalLayout_28 = QVBoxLayout(self.io_test)
        self.verticalLayout_28.setSpacing(15)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.frame_18 = QFrame(self.io_test)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"border: none")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_12 = QWidget(self.frame_18)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.widget_12.setAutoFillBackground(False)
        self.widget_12.setStyleSheet(u"background-color: #E8E8E8;\n"
"border-radius: 12px;")
        self.verticalLayout_21 = QVBoxLayout(self.widget_12)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label = QLabel(self.widget_12)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(16777215, 30))
        font28 = QFont()
        font28.setPointSize(15)
        font28.setBold(True)
        self.label.setFont(font28)
        self.label.setStyleSheet(u"color: #868686;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_21.addWidget(self.label)

        self.frame_12 = QFrame(self.widget_12)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"QLabel {\n"
"	border: none;\n"
"	border-radius:  45px;\n"
"}")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.cameraTriggerSignal = QLabel(self.frame_12)
        self.cameraTriggerSignal.setObjectName(u"cameraTriggerSignal")
        self.cameraTriggerSignal.setMinimumSize(QSize(90, 90))
        self.cameraTriggerSignal.setMaximumSize(QSize(90, 90))
        self.cameraTriggerSignal.setStyleSheet(u"background-color: red;")
        self.cameraTriggerSignal.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_28.addWidget(self.cameraTriggerSignal)


        self.verticalLayout_21.addWidget(self.frame_12)


        self.horizontalLayout_10.addWidget(self.widget_12)

        self.widget_13 = QWidget(self.frame_18)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.widget_13.setAutoFillBackground(False)
        self.widget_13.setStyleSheet(u"background-color: #E8E8E8;\n"
"border-radius: 12px;")
        self.verticalLayout_26 = QVBoxLayout(self.widget_13)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_4 = QLabel(self.widget_13)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 30))
        self.label_4.setMaximumSize(QSize(16777215, 30))
        self.label_4.setFont(font28)
        self.label_4.setStyleSheet(u"color: #868686;")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_4)

        self.frame_13 = QFrame(self.widget_13)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"QLabel {\n"
"	border: none;\n"
"	border-radius:  45px;\n"
"}")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.rejectTriggerSignal = QLabel(self.frame_13)
        self.rejectTriggerSignal.setObjectName(u"rejectTriggerSignal")
        self.rejectTriggerSignal.setMinimumSize(QSize(90, 90))
        self.rejectTriggerSignal.setMaximumSize(QSize(90, 90))
        self.rejectTriggerSignal.setStyleSheet(u"background-color: red;\n"
"")
        self.rejectTriggerSignal.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_29.addWidget(self.rejectTriggerSignal)


        self.verticalLayout_26.addWidget(self.frame_13)


        self.horizontalLayout_10.addWidget(self.widget_13)

        self.widget_14 = QWidget(self.frame_18)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.widget_14.setAutoFillBackground(False)
        self.widget_14.setStyleSheet(u"background-color: #E8E8E8;\n"
"border-radius: 12px;")
        self.verticalLayout_27 = QVBoxLayout(self.widget_14)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_6 = QLabel(self.widget_14)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 30))
        self.label_6.setMaximumSize(QSize(16777215, 30))
        self.label_6.setFont(font28)
        self.label_6.setStyleSheet(u"color: #868686;")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_6)

        self.frame_17 = QFrame(self.widget_14)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.testReject = QPushButton(self.frame_17)
        self.testReject.setObjectName(u"testReject")
        self.testReject.setMinimumSize(QSize(0, 90))
        self.testReject.setFont(font23)
        self.testReject.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(120, 120, 120);\n"
"	color: white;\n"
"	text-align: center;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: rgb(60, 60, 60);\n"
"	color: white;\n"
"}")
        self.testReject.setIcon(icon12)
        self.testReject.setIconSize(QSize(30, 30))
        self.testReject.setCheckable(True)

        self.horizontalLayout_30.addWidget(self.testReject)


        self.verticalLayout_27.addWidget(self.frame_17)


        self.horizontalLayout_10.addWidget(self.widget_14)


        self.verticalLayout_28.addWidget(self.frame_18)

        self.frame_3 = QFrame(self.io_test)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"color: #808080;\n"
"border: none;")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QFrame {\n"
"	border: 1px solid #808080;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
" border: none;\n"
"}")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_4)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_35 = QLabel(self.frame_4)
        self.label_35.setObjectName(u"label_35")
        font29 = QFont()
        font29.setPointSize(16)
        font29.setBold(True)
        self.label_35.setFont(font29)
        self.label_35.setStyleSheet(u"background-color: #808080;\n"
"border-radius: 12px;\n"
"color: white;\n"
"padding: 8px;")
        self.label_35.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_35)

        self.cpu_usage = QLabel(self.frame_4)
        self.cpu_usage.setObjectName(u"cpu_usage")
        self.cpu_usage.setFont(font26)

        self.verticalLayout_12.addWidget(self.cpu_usage)

        self.ram_usage = QLabel(self.frame_4)
        self.ram_usage.setObjectName(u"ram_usage")
        self.ram_usage.setFont(font26)

        self.verticalLayout_12.addWidget(self.ram_usage)

        self.disk_usage = QLabel(self.frame_4)
        self.disk_usage.setObjectName(u"disk_usage")
        self.disk_usage.setFont(font26)

        self.verticalLayout_12.addWidget(self.disk_usage)

        self.cpu_temp = QLabel(self.frame_4)
        self.cpu_temp.setObjectName(u"cpu_temp")
        self.cpu_temp.setFont(font26)

        self.verticalLayout_12.addWidget(self.cpu_temp)


        self.horizontalLayout_11.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QFrame {\n"
"	border: 1px solid #808080;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
" border: none;\n"
"}")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_39 = QLabel(self.frame_5)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font29)
        self.label_39.setStyleSheet(u"background-color: #808080;\n"
"border-radius: 12px;\n"
"color: white;\n"
"padding: 8px;")
        self.label_39.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_39)

        self.eth0 = QLabel(self.frame_5)
        self.eth0.setObjectName(u"eth0")
        self.eth0.setFont(font26)

        self.verticalLayout_16.addWidget(self.eth0)

        self.eth1 = QLabel(self.frame_5)
        self.eth1.setObjectName(u"eth1")
        self.eth1.setFont(font26)

        self.verticalLayout_16.addWidget(self.eth1)

        self.wlan0 = QLabel(self.frame_5)
        self.wlan0.setObjectName(u"wlan0")
        self.wlan0.setFont(font26)

        self.verticalLayout_16.addWidget(self.wlan0)

        self.label_43 = QLabel(self.frame_5)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font26)

        self.verticalLayout_16.addWidget(self.label_43)


        self.horizontalLayout_11.addWidget(self.frame_5)


        self.verticalLayout_28.addWidget(self.frame_3)

        icon15 = QIcon()
        icon15.addFile(u":/assets/icon/characteristics.png", QSize(), QIcon.Mode.Active, QIcon.State.On)
        self.tabWidget.addTab(self.io_test, icon15, "")
        self.credit_tab = QWidget()
        self.credit_tab.setObjectName(u"credit_tab")
        self.credit_tab.setStyleSheet(u"QFrame {\n"
" 	border:  1px solid #808080;\n"
"	border-radius: 18px;\n"
"}\n"
"\n"
"QLabel {\n"
" border: none;\n"
"}")
        self.verticalLayout_17 = QVBoxLayout(self.credit_tab)
        self.verticalLayout_17.setSpacing(10)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(-1, 10, -1, -1)
        self.widget_2 = QWidget(self.credit_tab)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_17 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_17.setSpacing(10)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.widget_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(9, 9, 9, 9)
        self.label_32 = QLabel(self.frame)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(350, 150))
        self.label_32.setPixmap(QPixmap(u":/assets/images/Tesseract_OCR_logo_(Google).png"))
        self.label_32.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_32)


        self.horizontalLayout_17.addWidget(self.frame)

        self.frame_7 = QFrame(self.widget_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 20, 0)
        self.label_36 = QLabel(self.frame_7)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMaximumSize(QSize(350, 200))
        self.label_36.setPixmap(QPixmap(u":/assets/images/logo_EasyOCR-3386444.png"))
        self.label_36.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.label_36)


        self.horizontalLayout_17.addWidget(self.frame_7)


        self.verticalLayout_17.addWidget(self.widget_2)

        self.widget_15 = QWidget(self.credit_tab)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_23.setSpacing(10)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.widget_15)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.label_31 = QLabel(self.frame_2)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMaximumSize(QSize(230, 16777215))
        self.label_31.setPixmap(QPixmap(u":/assets/images/flaticon.png"))
        self.label_31.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.label_31)


        self.horizontalLayout_23.addWidget(self.frame_2)

        self.frame_6 = QFrame(self.widget_15)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_34 = QLabel(self.frame_6)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(175, 175))
        self.label_34.setPixmap(QPixmap(u":/assets/images/qt-logo-png_seeklogo-340086.png"))
        self.label_34.setScaledContents(True)
        self.label_34.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_34)


        self.horizontalLayout_23.addWidget(self.frame_6)


        self.verticalLayout_17.addWidget(self.widget_15)

        icon16 = QIcon()
        icon16.addFile(u":/assets/icon/info.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget.addTab(self.credit_tab, icon16, "")

        self.horizontalLayout_24.addWidget(self.tabWidget)

        self.stackedWidget.addWidget(self.settings_page)
        self.shutdown_page = QWidget()
        self.shutdown_page.setObjectName(u"shutdown_page")
        self.verticalLayout_70 = QVBoxLayout(self.shutdown_page)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.shutdown_title = QLabel(self.shutdown_page)
        self.shutdown_title.setObjectName(u"shutdown_title")
        self.shutdown_title.setMaximumSize(QSize(16777215, 65))
        font30 = QFont()
        font30.setFamilies([u"Kanit"])
        font30.setPointSize(30)
        self.shutdown_title.setFont(font30)
        self.shutdown_title.setStyleSheet(u"background-color: rgb(52, 157, 77);\n"
"border-radius: 15px;")
        self.shutdown_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_70.addWidget(self.shutdown_title)

        self.shutdown_widget = QWidget(self.shutdown_page)
        self.shutdown_widget.setObjectName(u"shutdown_widget")
        self.shutdown_widget.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(50, 50, 50);\n"
"	border-radius: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	padding: 8px;\n"
"}")
        self.verticalLayout_68 = QVBoxLayout(self.shutdown_widget)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.widget_17 = QWidget(self.shutdown_widget)
        self.widget_17.setObjectName(u"widget_17")
        self.verticalLayout_69 = QVBoxLayout(self.widget_17)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(-1, 10, -1, -1)
        self.shutdown_warning_label = QLabel(self.widget_17)
        self.shutdown_warning_label.setObjectName(u"shutdown_warning_label")
        self.shutdown_warning_label.setMaximumSize(QSize(16777215, 16777215))
        font31 = QFont()
        font31.setFamilies([u"Kanit"])
        font31.setPointSize(22)
        font31.setBold(True)
        font31.setStrikeOut(False)
        self.shutdown_warning_label.setFont(font31)
        self.shutdown_warning_label.setStyleSheet(u"color: rgb(91, 91, 91);")
        self.shutdown_warning_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.shutdown_warning_label.setWordWrap(True)

        self.verticalLayout_69.addWidget(self.shutdown_warning_label)


        self.verticalLayout_68.addWidget(self.widget_17)

        self.widget_18 = QWidget(self.shutdown_widget)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setMaximumSize(QSize(16777215, 150))
        self.horizontalLayout_92 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_92.setSpacing(20)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.horizontalLayout_92.setContentsMargins(20, -1, 20, -1)
        self.confirm_shutdown = QPushButton(self.widget_18)
        self.confirm_shutdown.setObjectName(u"confirm_shutdown")
        self.confirm_shutdown.setMinimumSize(QSize(0, 52))
        font32 = QFont()
        font32.setFamilies([u"Kanit"])
        font32.setPointSize(30)
        font32.setWeight(QFont.Medium)
        font32.setItalic(False)
        self.confirm_shutdown.setFont(font32)
        self.confirm_shutdown.setStyleSheet(u"")
        icon17 = QIcon()
        icon17.addFile(u":/assets/keyboard/enter.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.confirm_shutdown.setIcon(icon17)
        self.confirm_shutdown.setIconSize(QSize(50, 50))

        self.horizontalLayout_92.addWidget(self.confirm_shutdown)

        self.cancel_shutdown = QPushButton(self.widget_18)
        self.cancel_shutdown.setObjectName(u"cancel_shutdown")
        self.cancel_shutdown.setMinimumSize(QSize(0, 52))
        self.cancel_shutdown.setFont(font32)
        icon18 = QIcon()
        icon18.addFile(u":/assets/keyboard/cancel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cancel_shutdown.setIcon(icon18)
        self.cancel_shutdown.setIconSize(QSize(50, 50))

        self.horizontalLayout_92.addWidget(self.cancel_shutdown)


        self.verticalLayout_68.addWidget(self.widget_18)

        self.credit = QLabel(self.shutdown_widget)
        self.credit.setObjectName(u"credit")
        self.credit.setMaximumSize(QSize(16777215, 45))
        self.credit.setFont(font3)
        self.credit.setStyleSheet(u"color: rgb(91, 91, 91);")
        self.credit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_68.addWidget(self.credit)

        self.widget_21 = QWidget(self.shutdown_widget)
        self.widget_21.setObjectName(u"widget_21")
        self.widget_21.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_93 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.version = QLabel(self.widget_21)
        self.version.setObjectName(u"version")
        self.version.setMaximumSize(QSize(16777215, 50))
        self.version.setFont(font3)
        self.version.setStyleSheet(u"color: rgb(91, 91, 91);")
        self.version.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_93.addWidget(self.version)


        self.verticalLayout_68.addWidget(self.widget_21)


        self.verticalLayout_70.addWidget(self.shutdown_widget)

        self.stackedWidget.addWidget(self.shutdown_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_12.addWidget(self.screen_page)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menu.toggled.connect(self.show_sidebar.setVisible)
        self.menu.toggled.connect(self.hide_sidebar.setHidden)
        self.lme_setting_1.toggled.connect(self.lme_setting_2.setChecked)
        self.lme_setting_2.toggled.connect(self.lme_setting_1.setChecked)
        self.home_2.toggled.connect(self.home_1.setChecked)
        self.home_1.toggled.connect(self.home_2.setChecked)
        self.sys_setting_1.toggled.connect(self.sys_setting_2.setChecked)
        self.sys_setting_2.toggled.connect(self.sys_setting_1.setChecked)
        self.camera_filter_1.toggled.connect(self.camera_filter_2.setChecked)
        self.camera_filter_2.toggled.connect(self.camera_filter_1.setChecked)

        self.stackedWidget.setCurrentIndex(3)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.profile_img2.setText("")
        self.home_2.setText("")
        self.lme_setting_2.setText("")
        self.sys_setting_1.setText("")
        self.exit_program_2.setText("")
        self.restart_program_2.setText("")
        self.shutdown_2.setText("")
        self.profile_img1.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"DETECTOR", None))
        self.home_1.setText(QCoreApplication.translate("MainWindow", u"  \u0e2b\u0e19\u0e49\u0e32\u0e2b\u0e25\u0e31\u0e01", None))
        self.lme_setting_1.setText(QCoreApplication.translate("MainWindow", u"  \u0e41\u0e21\u0e48\u0e41\u0e1a\u0e1a", None))
        self.sys_setting_2.setText(QCoreApplication.translate("MainWindow", u"  \u0e15\u0e31\u0e49\u0e07\u0e04\u0e48\u0e32", None))
        self.exit_program_1.setText(QCoreApplication.translate("MainWindow", u"  \u0e1b\u0e34\u0e14\u0e42\u0e1b\u0e23\u0e41\u0e01\u0e23\u0e21", None))
        self.restart_program_1.setText(QCoreApplication.translate("MainWindow", u"  \u0e23\u0e35\u0e2a\u0e15\u0e32\u0e23\u0e4c\u0e17", None))
        self.shutdown_1.setText(QCoreApplication.translate("MainWindow", u"  \u0e1b\u0e34\u0e14\u0e40\u0e04\u0e23\u0e37\u0e48\u0e2d\u0e07", None))
        self.menu.setText("")
        self.title.setText(QCoreApplication.translate("MainWindow", u"\u0e23\u0e30\u0e1a\u0e1a\u0e15\u0e23\u0e27\u0e08\u0e2a\u0e2d\u0e1a\u0e01\u0e32\u0e23\u0e1e\u0e34\u0e21\u0e1e\u0e4c", None))
        self.time_bar.setText(QCoreApplication.translate("MainWindow", u"HH:MM:SS", None))
        self.date_bar.setText(QCoreApplication.translate("MainWindow", u"DD/MM/YYYY", None))
        self.process_img.setText("")
        self.process_label_line_1.setText(QCoreApplication.translate("MainWindow", u"PRINTING  INSPECTION SYSTEM", None))
        self.process_label_line_2.setText(QCoreApplication.translate("MainWindow", u"Created by Nattapon pondonko", None))
        self.process_label_line_3.setText(QCoreApplication.translate("MainWindow", u"Engineering Department", None))
        self.process_label_line_4.setText("")
        self.detection_status.setText(QCoreApplication.translate("MainWindow", u"\u0e01\u0e14\u0e1b\u0e38\u0e48\u0e21 START \u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e40\u0e23\u0e34\u0e48\u0e21\u0e17\u0e33\u0e07\u0e32\u0e19", None))
        self.detection_monitor.setText("")
        self.lot_label_2.setText("")
        self.count_ok.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lot_label_6.setText("")
        self.count_ng.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lot_label_4.setText("")
        self.count_total.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.count_reset.setText("")
        self.detection_view.setText("")
        self.detection_alert.setText(QCoreApplication.translate("MainWindow", u"Wait", None))
        self.lot_detected.setText(QCoreApplication.translate("MainWindow", u"XXXXXX", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"EXP.", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"LOT.", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"MFG.", None))
        self.mfg_detected.setText(QCoreApplication.translate("MainWindow", u"XXXXXX", None))
        self.exp_detected.setText(QCoreApplication.translate("MainWindow", u"XXXXXX", None))
        self.capture_test.setText(QCoreApplication.translate("MainWindow", u"\u0e17\u0e14\u0e2a\u0e2d\u0e1a", None))
        self.start.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.setting_title.setText(QCoreApplication.translate("MainWindow", u"\u0e15\u0e31\u0e49\u0e07\u0e04\u0e48\u0e32 LOT, MFG, EXP", None))
        self.lme_settings_monitor.setText("")
        self.webcam_setting_view.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"LOT.", None))
        self.lot_set.setText("")
        self.lot_set.setPlaceholderText(QCoreApplication.translate("MainWindow", u"XXXXXX", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"MFG.", None))
        self.mfg_set.setText("")
        self.mfg_set.setPlaceholderText(QCoreApplication.translate("MainWindow", u"XXXXXX", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"EXP.", None))
        self.exp_set.setText("")
        self.exp_set.setPlaceholderText(QCoreApplication.translate("MainWindow", u"XXXXXX", None))
        self.save_images_detection.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e1b\u0e34\u0e14\u0e43\u0e0a\u0e49\u0e07\u0e32\u0e19\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e20\u0e32\u0e1e\u0e17\u0e35\u0e48\u0e15\u0e23\u0e27\u0e08\u0e08\u0e31\u0e1a", None))
        self.capture_set.setText(QCoreApplication.translate("MainWindow", u" \u0e16\u0e48\u0e32\u0e22\u0e20\u0e32\u0e1e", None))
        self.save_set.setText(QCoreApplication.translate("MainWindow", u" \u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01", None))
        self.camera_settings_monitor.setText("")
        self.camera_filter_1.setText(QCoreApplication.translate("MainWindow", u"\u0e14\u0e39\u0e41\u0e1a\u0e1a filter \u0e01\u0e48\u0e2d\u0e19 detect", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e27\u0e25\u0e32\u0e0a\u0e31\u0e15\u0e40\u0e15\u0e2d\u0e23\u0e4c", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"\u0e23\u0e30\u0e22\u0e30\u0e40\u0e27\u0e25\u0e32\u0e40\u0e1b\u0e34\u0e14\u0e0a\u0e31\u0e15\u0e40\u0e15\u0e2d\u0e23\u0e4c", None))
        self.exposureTime.setText(QCoreApplication.translate("MainWindow", u"100000", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"us", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"\u0e2b\u0e19\u0e48\u0e27\u0e07\u0e40\u0e27\u0e25\u0e32\u0e01\u0e48\u0e2d\u0e19\u0e16\u0e48\u0e32\u0e22\u0e20\u0e32\u0e1e", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"\u0e2b\u0e19\u0e48\u0e27\u0e07\u0e40\u0e27\u0e25\u0e32\u0e43\u0e2b\u0e49\u0e20\u0e32\u0e1e\u0e19\u0e34\u0e48\u0e07\u0e01\u0e48\u0e2d\u0e19\u0e16\u0e48\u0e32\u0e22", None))
        self.delayShutter.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"ms", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0e04\u0e27\u0e32\u0e21\u0e2a\u0e27\u0e48\u0e32\u0e07", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Contrast", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0e04\u0e27\u0e32\u0e21\u0e2d\u0e34\u0e48\u0e21\u0e2a\u0e35", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Gain", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0e04\u0e27\u0e32\u0e21\u0e04\u0e21", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.camera_settings_tab), QCoreApplication.translate("MainWindow", u"\u0e15\u0e31\u0e49\u0e07\u0e04\u0e48\u0e32\u0e01\u0e25\u0e49\u0e2d\u0e07", None))
        self.sys_settings_monitor.setText("")
        self.camera_filter_2.setText(QCoreApplication.translate("MainWindow", u" filter \u0e01\u0e48\u0e2d\u0e19 detect", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"\u0e08\u0e33\u0e19\u0e27\u0e19\u0e2a\u0e15\u0e34\u0e4a\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"\u0e08\u0e33\u0e19\u0e27\u0e19\u0e2a\u0e15\u0e34\u0e4a\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c\u0e01\u0e48\u0e2d\u0e19\u0e15\u0e23\u0e27\u0e08\u0e2a\u0e2d\u0e1a", None))
        self.numberStickerBeforeDetection.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"\u0e41\u0e1c\u0e48\u0e19", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"\u0e2b\u0e19\u0e48\u0e27\u0e07\u0e40\u0e27\u0e25\u0e32\u0e01\u0e48\u0e2d\u0e19\u0e23\u0e35\u0e40\u0e08\u0e04", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"\u0e2b\u0e19\u0e48\u0e27\u0e07\u0e40\u0e27\u0e25\u0e32\u0e01\u0e48\u0e2d\u0e19\u0e40\u0e1b\u0e34\u0e14\u0e01\u0e23\u0e30\u0e1a\u0e2d\u0e01\u0e25\u0e21", None))
        self.delayBeforeReject.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"ms", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"\u0e23\u0e30\u0e22\u0e30\u0e40\u0e27\u0e25\u0e32\u0e23\u0e35\u0e40\u0e08\u0e04", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"\u0e23\u0e30\u0e22\u0e30\u0e40\u0e27\u0e25\u0e32\u0e40\u0e1b\u0e34\u0e14\u0e01\u0e23\u0e30\u0e1a\u0e2d\u0e01\u0e25\u0e21", None))
        self.rejectionPeriod.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"ms", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e1f\u0e23\u0e21\u0e40\u0e23\u0e17", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"\u0e2d\u0e31\u0e15\u0e23\u0e32\u0e40\u0e1f\u0e21\u0e40\u0e23\u0e17", None))
        self.frameRate.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"fps", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"\u0e2b\u0e21\u0e38\u0e19\u0e20\u0e32\u0e1e", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"\u0e2b\u0e21\u0e38\u0e19\u0e20\u0e32\u0e1e\u0e01\u0e48\u0e2d\u0e19\u0e15\u0e23\u0e27\u0e08\u0e2a\u0e2d\u0e1a", None))
        self.rotateImage.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"\u0e2d\u0e07\u0e28\u0e32", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"\u0e01\u0e32\u0e23\u0e15\u0e23\u0e27\u0e08\u0e2a\u0e2d\u0e1a", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e1b\u0e2d\u0e23\u0e4c\u0e40\u0e0b\u0e47\u0e19\u0e15\u0e4c\u0e01\u0e32\u0e23\u0e15\u0e23\u0e27\u0e08\u0e2a\u0e2d\u0e1a", None))
        self.detectionPercentage.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"\u0e1b\u0e23\u0e31\u0e1a\u0e40\u0e2a\u0e01\u0e25", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"\u0e1b\u0e23\u0e31\u0e1a\u0e40\u0e2a\u0e01\u0e25\u0e20\u0e32\u0e1e\u0e01\u0e48\u0e2d\u0e19\u0e01\u0e32\u0e23\u0e15\u0e23\u0e27\u0e08\u0e2a\u0e2d\u0e1a", None))
        self.detection_resize_percent.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e04\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e21\u0e37\u0e2d\u0e15\u0e23\u0e27\u0e08\u0e2a\u0e2d\u0e1a", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"[easyocr \u0e0a\u0e49\u0e32,\u0e41\u0e21\u0e48\u0e19\u0e22\u0e33], [tesseract \u0e40\u0e23\u0e47\u0e27]", None))
        self.ocr_engine.setItemText(0, QCoreApplication.translate("MainWindow", u"easyocr", None))
        self.ocr_engine.setItemText(1, QCoreApplication.translate("MainWindow", u"tesseract", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sys_settings_tab), QCoreApplication.translate("MainWindow", u"\u0e15\u0e31\u0e49\u0e07\u0e04\u0e48\u0e32\u0e23\u0e30\u0e1a\u0e1a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e19 \u0e17\u0e23\u0e34\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c \u0e01\u0e25\u0e49\u0e2d\u0e07", None))
        self.cameraTriggerSignal.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e19 \u0e17\u0e23\u0e34\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c \u0e23\u0e35\u0e40\u0e08\u0e04", None))
        self.rejectTriggerSignal.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0e23\u0e35\u0e40\u0e08\u0e04", None))
        self.testReject.setText(QCoreApplication.translate("MainWindow", u"\u0e17\u0e14\u0e2a\u0e2d\u0e1a", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e23\u0e30\u0e1a\u0e1a", None))
        self.cpu_usage.setText(QCoreApplication.translate("MainWindow", u"CPU: 10.6% @ 1700Mhz", None))
        self.ram_usage.setText(QCoreApplication.translate("MainWindow", u"RAM: 1045.25/16218MB", None))
        self.disk_usage.setText(QCoreApplication.translate("MainWindow", u"DISK: 9.25/58GB", None))
        self.cpu_temp.setText(QCoreApplication.translate("MainWindow", u"TEMP: 43.5C", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e01\u0e32\u0e23\u0e40\u0e0a\u0e37\u0e48\u0e2d\u0e21\u0e15\u0e48\u0e2d", None))
        self.eth0.setText(QCoreApplication.translate("MainWindow", u"eth0: 192.168.175.138", None))
        self.eth1.setText(QCoreApplication.translate("MainWindow", u"eth1: N/A", None))
        self.wlan0.setText(QCoreApplication.translate("MainWindow", u"wlan0: 192.168.175.138", None))
        self.label_43.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.io_test), QCoreApplication.translate("MainWindow", u"\u0e2e\u0e32\u0e23\u0e4c\u0e14\u0e41\u0e27\u0e23\u0e4c", None))
        self.label_32.setText("")
        self.label_36.setText("")
        self.label_31.setText("")
        self.label_34.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.credit_tab), QCoreApplication.translate("MainWindow", u"Credit", None))
        self.shutdown_title.setText(QCoreApplication.translate("MainWindow", u"\u0e22\u0e37\u0e19\u0e22\u0e31\u0e19\u0e01\u0e32\u0e23\u0e1b\u0e34\u0e14\u0e40\u0e04\u0e23\u0e37\u0e48\u0e2d\u0e07", None))
        self.shutdown_warning_label.setText(QCoreApplication.translate("MainWindow", u"\u0e2b\u0e25\u0e31\u0e07\u0e08\u0e32\u0e01\u0e01\u0e14\u0e1b\u0e38\u0e48\u0e21 \u0e22\u0e37\u0e19\u0e22\u0e31\u0e19 \u0e43\u0e2b\u0e49\u0e23\u0e2d\u0e1b\u0e23\u0e30\u0e21\u0e32\u0e13 1 \u0e19\u0e32\u0e17\u0e35\u0e01\u0e48\u0e2d\u0e19\u0e16\u0e2d\u0e14\u0e1b\u0e25\u0e31\u0e4a\u0e01", None))
        self.confirm_shutdown.setText(QCoreApplication.translate("MainWindow", u"  \u0e22\u0e37\u0e19\u0e22\u0e31\u0e19", None))
        self.cancel_shutdown.setText(QCoreApplication.translate("MainWindow", u"  \u0e22\u0e01\u0e40\u0e25\u0e34\u0e01", None))
        self.credit.setText(QCoreApplication.translate("MainWindow", u"Created by Nattapon pondonko Engineering Department", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"Software version 1.0.0", None))
    # retranslateUi

