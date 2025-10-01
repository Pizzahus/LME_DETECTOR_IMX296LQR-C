# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DETECTOR_7inch.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QDial, QFormLayout, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import src.resource_rc as resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 600)
        MainWindow.setMinimumSize(QSize(250, 0))
        MainWindow.setStyleSheet(u"background-color: rgb(38, 38, 38);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(1024, 600))
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.show_sidebar = QWidget(self.centralwidget)
        self.show_sidebar.setObjectName(u"show_sidebar")
        self.show_sidebar.setEnabled(True)
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
        self.verticalLayout_20 = QVBoxLayout(self.show_sidebar)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
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
        font = QFont()
        font.setFamilies([u"Kanit"])
        font.setPointSize(16)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_20.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 25, -1, -1)
        self.home_1 = QPushButton(self.show_sidebar)
        self.home_1.setObjectName(u"home_1")
        font1 = QFont()
        font1.setFamilies([u"Kanit"])
        font1.setBold(False)
        self.home_1.setFont(font1)
        self.home_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/assets/icon/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.home_1.setIcon(icon)
        self.home_1.setIconSize(QSize(40, 40))
        self.home_1.setCheckable(True)
        self.home_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.home_1)

        self.setting_1 = QPushButton(self.show_sidebar)
        self.setting_1.setObjectName(u"setting_1")
        font2 = QFont()
        font2.setFamilies([u"Kanit"])
        self.setting_1.setFont(font2)
        self.setting_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/assets/icon/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.setting_1.setIcon(icon1)
        self.setting_1.setIconSize(QSize(40, 40))
        self.setting_1.setCheckable(True)
        self.setting_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.setting_1)

        self.camera_setting_1 = QPushButton(self.show_sidebar)
        self.camera_setting_1.setObjectName(u"camera_setting_1")
        self.camera_setting_1.setFont(font2)
        self.camera_setting_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/assets/icon/camera.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.camera_setting_1.setIcon(icon2)
        self.camera_setting_1.setIconSize(QSize(40, 40))
        self.camera_setting_1.setCheckable(True)
        self.camera_setting_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.camera_setting_1)


        self.verticalLayout_20.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 297, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.restart_program_1 = QPushButton(self.show_sidebar)
        self.restart_program_1.setObjectName(u"restart_program_1")
        font3 = QFont()
        font3.setFamilies([u"Kanit"])
        font3.setStrikeOut(False)
        font3.setKerning(True)
        self.restart_program_1.setFont(font3)
        self.restart_program_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/assets/icon/restart.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.restart_program_1.setIcon(icon3)
        self.restart_program_1.setIconSize(QSize(40, 40))
#if QT_CONFIG(shortcut)
        self.restart_program_1.setShortcut(u"Ctrl+S")
#endif // QT_CONFIG(shortcut)

        self.verticalLayout_4.addWidget(self.restart_program_1)

        self.shutdown_1 = QPushButton(self.show_sidebar)
        self.shutdown_1.setObjectName(u"shutdown_1")
        self.shutdown_1.setFont(font3)
        self.shutdown_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/assets/icon/shutdown1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.shutdown_1.setIcon(icon4)
        self.shutdown_1.setIconSize(QSize(40, 40))
#if QT_CONFIG(shortcut)
        self.shutdown_1.setShortcut(u"Ctrl+S")
#endif // QT_CONFIG(shortcut)

        self.verticalLayout_4.addWidget(self.shutdown_1)


        self.verticalLayout_20.addLayout(self.verticalLayout_4)


        self.gridLayout_3.addWidget(self.show_sidebar, 0, 1, 1, 1)

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

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 25, -1, -1)
        self.home_2 = QPushButton(self.hide_sidebar)
        self.home_2.setObjectName(u"home_2")
        self.home_2.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home_2.sizePolicy().hasHeightForWidth())
        self.home_2.setSizePolicy(sizePolicy)
        self.home_2.setMinimumSize(QSize(0, 0))
        font4 = QFont()
        font4.setKerning(True)
        self.home_2.setFont(font4)
        self.home_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.home_2.setIcon(icon)
        self.home_2.setIconSize(QSize(40, 40))
        self.home_2.setCheckable(True)
        self.home_2.setChecked(True)
        self.home_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_2)

        self.setting_2 = QPushButton(self.hide_sidebar)
        self.setting_2.setObjectName(u"setting_2")
        self.setting_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setting_2.setIcon(icon1)
        self.setting_2.setIconSize(QSize(40, 40))
        self.setting_2.setCheckable(True)
        self.setting_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.setting_2)

        self.camera_setting_2 = QPushButton(self.hide_sidebar)
        self.camera_setting_2.setObjectName(u"camera_setting_2")
        self.camera_setting_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.camera_setting_2.setIcon(icon2)
        self.camera_setting_2.setIconSize(QSize(40, 40))
        self.camera_setting_2.setCheckable(True)
        self.camera_setting_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.camera_setting_2)


        self.verticalLayout_13.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 297, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer)

        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.restart_program_2 = QPushButton(self.hide_sidebar)
        self.restart_program_2.setObjectName(u"restart_program_2")
        self.restart_program_2.setFont(font3)
        self.restart_program_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.restart_program_2.setIcon(icon3)
        self.restart_program_2.setIconSize(QSize(40, 40))
#if QT_CONFIG(shortcut)
        self.restart_program_2.setShortcut(u"Ctrl+S")
#endif // QT_CONFIG(shortcut)

        self.verticalLayout_40.addWidget(self.restart_program_2)

        self.shutdown_2 = QPushButton(self.hide_sidebar)
        self.shutdown_2.setObjectName(u"shutdown_2")
        self.shutdown_2.setFont(font3)
        self.shutdown_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.shutdown_2.setIcon(icon4)
        self.shutdown_2.setIconSize(QSize(40, 40))
#if QT_CONFIG(shortcut)
        self.shutdown_2.setShortcut(u"Ctrl+S")
#endif // QT_CONFIG(shortcut)

        self.verticalLayout_40.addWidget(self.shutdown_2)


        self.verticalLayout_13.addLayout(self.verticalLayout_40)


        self.gridLayout_3.addWidget(self.hide_sidebar, 0, 0, 1, 1)

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
        font5 = QFont()
        font5.setPointSize(9)
        self.menu.setFont(font5)
        self.menu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/assets/icon/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/assets/icon/menu_open.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.menu.setIcon(icon5)
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
        font6 = QFont()
        font6.setFamilies([u"Kanit"])
        font6.setPointSize(24)
        font6.setBold(True)
        self.title.setFont(font6)
        self.title.setStyleSheet(u"")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.title)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.datetime_group_2 = QGroupBox(self.widget)
        self.datetime_group_2.setObjectName(u"datetime_group_2")
        font7 = QFont()
        font7.setPointSize(11)
        self.datetime_group_2.setFont(font7)
        self.datetime_group_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.datetime_group = QVBoxLayout(self.datetime_group_2)
        self.datetime_group.setSpacing(0)
        self.datetime_group.setObjectName(u"datetime_group")
        self.datetime_group.setContentsMargins(0, 5, 0, 5)
        self.time_bar = QLabel(self.datetime_group_2)
        self.time_bar.setObjectName(u"time_bar")
        self.time_bar.setMaximumSize(QSize(140, 16))
        font8 = QFont()
        font8.setFamilies([u"Kanit"])
        font8.setPointSize(14)
        font8.setBold(False)
        self.time_bar.setFont(font8)
        self.time_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.datetime_group.addWidget(self.time_bar)

        self.date_bar = QLabel(self.datetime_group_2)
        self.date_bar.setObjectName(u"date_bar")
        self.date_bar.setMaximumSize(QSize(140, 16))
        self.date_bar.setFont(font8)
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
"}")
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
        font9 = QFont()
        font9.setFamilies([u"Kanit"])
        font9.setPointSize(24)
        self.detection_status.setFont(font9)
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
        self.webcam_monitor = QLabel(self.widget_5)
        self.webcam_monitor.setObjectName(u"webcam_monitor")
        self.webcam_monitor.setMinimumSize(QSize(250, 250))
        self.webcam_monitor.setMaximumSize(QSize(16777215, 16777215))
        self.webcam_monitor.setStyleSheet(u"QLabel {\n"
"	border: solid;\n"
"	border-width: 2px;\n"
"	border-color: rgb(111, 105, 37);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.webcam_monitor.setPixmap(QPixmap(u":/assets/icon/picture_default.png"))
        self.webcam_monitor.setScaledContents(True)

        self.verticalLayout_7.addWidget(self.webcam_monitor)

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
        font10 = QFont()
        font10.setFamilies([u"Kanit"])
        font10.setPointSize(18)
        font10.setBold(True)
        self.lot_label_2.setFont(font10)
        self.lot_label_2.setStyleSheet(u"color: rgb(61, 61, 61);")
        self.lot_label_2.setPixmap(QPixmap(u":/assets/icon/ok.png"))
        self.lot_label_2.setScaledContents(True)
        self.lot_label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lot_label_2)

        self.count_ok = QLabel(self.widget_8)
        self.count_ok.setObjectName(u"count_ok")
        self.count_ok.setMaximumSize(QSize(16777215, 16777215))
        font11 = QFont()
        font11.setFamilies([u"Kanit"])
        font11.setPointSize(25)
        font11.setBold(True)
        self.count_ok.setFont(font11)
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
        self.lot_label_6.setFont(font10)
        self.lot_label_6.setStyleSheet(u"color: rgb(61, 61, 61);")
        self.lot_label_6.setPixmap(QPixmap(u":/assets/icon/ng.png"))
        self.lot_label_6.setScaledContents(True)
        self.lot_label_6.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_20.addWidget(self.lot_label_6)

        self.count_ng = QLabel(self.widget_11)
        self.count_ng.setObjectName(u"count_ng")
        self.count_ng.setMaximumSize(QSize(16777215, 16777215))
        self.count_ng.setFont(font11)
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
        self.lot_label_4.setFont(font10)
        self.lot_label_4.setStyleSheet(u"")
        self.lot_label_4.setPixmap(QPixmap(u":/assets/icon/all.png"))
        self.lot_label_4.setScaledContents(True)
        self.lot_label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_19.addWidget(self.lot_label_4)

        self.count_total = QLabel(self.widget_9)
        self.count_total.setObjectName(u"count_total")
        self.count_total.setMaximumSize(QSize(16777215, 16777215))
        self.count_total.setFont(font11)
        self.count_total.setStyleSheet(u"color: rgb(61, 61, 61);")
        self.count_total.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_19.addWidget(self.count_total)


        self.horizontalLayout_21.addWidget(self.widget_9)

        self.count_reset = QPushButton(self.widget_10)
        self.count_reset.setObjectName(u"count_reset")
        self.count_reset.setMinimumSize(QSize(0, 0))
        self.count_reset.setMaximumSize(QSize(45, 45))
        font12 = QFont()
        font12.setFamilies([u"Kanit"])
        font12.setPointSize(14)
        font12.setWeight(QFont.Medium)
        font12.setItalic(False)
        self.count_reset.setFont(font12)
        self.count_reset.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(50, 50, 50);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(100, 100, 100);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/assets/icon/reset.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.count_reset.setIcon(icon6)
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
        font13 = QFont()
        font13.setFamilies([u"Kanit"])
        font13.setPointSize(50)
        font13.setBold(True)
        self.detection_alert.setFont(font13)
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
        font14 = QFont()
        font14.setFamilies([u"Kanit"])
        font14.setPointSize(22)
        font14.setBold(True)
        self.lot_detected.setFont(font14)
        self.lot_detected.setStyleSheet(u"color: rgb(61, 61, 61);")
        self.lot_detected.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.lot_detected, 0, 1, 1, 1)

        self.exp_label = QLabel(self.widget_6)
        self.exp_label.setObjectName(u"exp_label")
        self.exp_label.setMaximumSize(QSize(85, 16777215))
        self.exp_label.setFont(font14)
        self.exp_label.setStyleSheet(u"color: rgb(61, 61, 61);")
        self.exp_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.exp_label, 2, 0, 1, 1)

        self.lot_label = QLabel(self.widget_6)
        self.lot_label.setObjectName(u"lot_label")
        self.lot_label.setMaximumSize(QSize(85, 16777215))
        self.lot_label.setFont(font14)
        self.lot_label.setStyleSheet(u"color: rgb(61, 61, 61);")
        self.lot_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.lot_label, 0, 0, 1, 1)

        self.mfg_label = QLabel(self.widget_6)
        self.mfg_label.setObjectName(u"mfg_label")
        self.mfg_label.setMaximumSize(QSize(85, 16777215))
        self.mfg_label.setFont(font14)
        self.mfg_label.setStyleSheet(u"color: rgb(61, 61, 61);")
        self.mfg_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.mfg_label, 1, 0, 1, 1)

        self.mfg_detected = QLabel(self.widget_6)
        self.mfg_detected.setObjectName(u"mfg_detected")
        self.mfg_detected.setFont(font14)
        self.mfg_detected.setStyleSheet(u"color: rgb(61, 61, 61);")
        self.mfg_detected.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.mfg_detected, 1, 1, 1, 1)

        self.exp_detected = QLabel(self.widget_6)
        self.exp_detected.setObjectName(u"exp_detected")
        self.exp_detected.setFont(font14)
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
        self.capture_test.setFont(font12)
        self.capture_test.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(50, 50, 50);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(100, 100, 100);\n"
"}")
        self.capture_test.setIcon(icon2)
        self.capture_test.setIconSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.capture_test)

        self.start = QPushButton(self.widget_4)
        self.start.setObjectName(u"start")
        self.start.setMinimumSize(QSize(0, 45))
        self.start.setMaximumSize(QSize(16777215, 45))
        font15 = QFont()
        font15.setFamilies([u"Kanit"])
        font15.setPointSize(12)
        font15.setWeight(QFont.Medium)
        font15.setItalic(False)
        self.start.setFont(font15)
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
        icon7 = QIcon()
        icon7.addFile(u":/assets/keyboard/record.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.start.setIcon(icon7)
        self.start.setIconSize(QSize(25, 25))
        self.start.setCheckable(True)
        self.start.setChecked(False)

        self.horizontalLayout_7.addWidget(self.start)


        self.verticalLayout_6.addWidget(self.widget_4)


        self.horizontalLayout_22.addWidget(self.detection_widget)


        self.verticalLayout_14.addWidget(self.detection_frame)

        self.stackedWidget.addWidget(self.detection_page)
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
        font16 = QFont()
        font16.setFamilies([u"Kanit"])
        font16.setPointSize(27)
        self.process_label_line_1.setFont(font16)
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
        font17 = QFont()
        font17.setFamilies([u"Kanit"])
        font17.setPointSize(20)
        self.process_label_line_2.setFont(font17)
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
        self.process_label_line_3.setFont(font17)
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
        font18 = QFont()
        font18.setFamilies([u"Kanit"])
        font18.setPointSize(14)
        self.process_label_line_4.setFont(font18)
        self.process_label_line_4.setStyleSheet(u"color: rgb(128, 128, 128);")
        self.process_label_line_4.setFrameShape(QFrame.Shape.NoFrame)
        self.process_label_line_4.setFrameShadow(QFrame.Shadow.Plain)
        self.process_label_line_4.setLineWidth(1)
        self.process_label_line_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_32.addWidget(self.process_label_line_4)


        self.verticalLayout_33.addWidget(self.process_frame)


        self.horizontalLayout_61.addWidget(self.process_main_frame)

        self.stackedWidget.addWidget(self.process_page)
        self.keyboard = QWidget()
        self.keyboard.setObjectName(u"keyboard")
        self.verticalLayout_34 = QVBoxLayout(self.keyboard)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.keyboard)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_35 = QVBoxLayout(self.widget_2)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.widget_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 300))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.keyboard_title_groupBox = QGroupBox(self.frame_4)
        self.keyboard_title_groupBox.setObjectName(u"keyboard_title_groupBox")
        self.keyboard_title_groupBox.setMinimumSize(QSize(0, 70))
        self.keyboard_title_groupBox.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_60 = QHBoxLayout(self.keyboard_title_groupBox)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(9, 0, 9, 0)
        self.keyboard_title = QLabel(self.keyboard_title_groupBox)
        self.keyboard_title.setObjectName(u"keyboard_title")
        self.keyboard_title.setMinimumSize(QSize(0, 50))
        self.keyboard_title.setMaximumSize(QSize(16777215, 65))
        font19 = QFont()
        font19.setFamilies([u"Kanit"])
        font19.setPointSize(30)
        self.keyboard_title.setFont(font19)
        self.keyboard_title.setStyleSheet(u"background-color: rgb(52, 157, 77);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.keyboard_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_60.addWidget(self.keyboard_title)


        self.verticalLayout_3.addWidget(self.keyboard_title_groupBox)

        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_9)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(-1, -1, -1, 20)
        self.val_input = QLabel(self.frame_9)
        self.val_input.setObjectName(u"val_input")
        font20 = QFont()
        font20.setFamilies([u"Kanit"])
        font20.setPointSize(80)
        font20.setBold(True)
        self.val_input.setFont(font20)
        self.val_input.setStyleSheet(u"color: rgb(100, 100, 100);\n"
"border: none;")
        self.val_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_38.addWidget(self.val_input)


        self.verticalLayout_3.addWidget(self.frame_9)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 270))
        self.frame_5.setMaximumSize(QSize(16777215, 270))
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush1 = QBrush(QColor(255, 255, 255, 128))
        brush1.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.frame_6.setPalette(palette)
        self.frame_6.setStyleSheet(u"QPushButton {\n"
"	width: 90px;\n"
"	height: 70px;\n"
"	background-color: rgb(50, 50, 50);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    font-size: 40px;\n"
"	background-color: rgb(100, 100, 100);\n"
"}")
        self.frame_6.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_6.setLineWidth(3)
        self.gridLayout = QGridLayout(self.frame_6)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.key_7 = QPushButton(self.frame_6)
        self.key_7.setObjectName(u"key_7")
        font21 = QFont()
        font21.setFamilies([u"Kanit"])
        font21.setPointSize(30)
        font21.setWeight(QFont.Medium)
        self.key_7.setFont(font21)

        self.gridLayout.addWidget(self.key_7, 2, 0, 1, 1)

        self.key_0 = QPushButton(self.frame_6)
        self.key_0.setObjectName(u"key_0")
        self.key_0.setMinimumSize(QSize(0, 0))
        self.key_0.setMaximumSize(QSize(16777215, 150))
        self.key_0.setFont(font21)

        self.gridLayout.addWidget(self.key_0, 3, 1, 1, 1)

        self.key_2 = QPushButton(self.frame_6)
        self.key_2.setObjectName(u"key_2")
        self.key_2.setFont(font21)

        self.gridLayout.addWidget(self.key_2, 0, 1, 1, 1)

        self.key_5 = QPushButton(self.frame_6)
        self.key_5.setObjectName(u"key_5")
        self.key_5.setFont(font21)

        self.gridLayout.addWidget(self.key_5, 1, 1, 1, 1)

        self.key_4 = QPushButton(self.frame_6)
        self.key_4.setObjectName(u"key_4")
        self.key_4.setFont(font21)

        self.gridLayout.addWidget(self.key_4, 1, 0, 1, 1)

        self.key_3 = QPushButton(self.frame_6)
        self.key_3.setObjectName(u"key_3")
        self.key_3.setFont(font21)

        self.gridLayout.addWidget(self.key_3, 0, 2, 1, 1)

        self.key_9 = QPushButton(self.frame_6)
        self.key_9.setObjectName(u"key_9")
        self.key_9.setFont(font21)

        self.gridLayout.addWidget(self.key_9, 2, 2, 1, 1)

        self.key_1 = QPushButton(self.frame_6)
        self.key_1.setObjectName(u"key_1")
        self.key_1.setFont(font21)

        self.gridLayout.addWidget(self.key_1, 0, 0, 1, 1)

        self.key_8 = QPushButton(self.frame_6)
        self.key_8.setObjectName(u"key_8")
        self.key_8.setFont(font21)

        self.gridLayout.addWidget(self.key_8, 2, 1, 1, 1)

        self.key_backspace = QPushButton(self.frame_6)
        self.key_backspace.setObjectName(u"key_backspace")
        self.key_backspace.setMinimumSize(QSize(0, 0))
        self.key_backspace.setMaximumSize(QSize(16777215, 150))
        font22 = QFont()
        font22.setPointSize(30)
        self.key_backspace.setFont(font22)
        icon8 = QIcon()
        icon8.addFile(u":/assets/keyboard/backspace.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.key_backspace.setIcon(icon8)
        self.key_backspace.setIconSize(QSize(40, 40))

        self.gridLayout.addWidget(self.key_backspace, 3, 2, 1, 1)

        self.key_backslash = QPushButton(self.frame_6)
        self.key_backslash.setObjectName(u"key_backslash")
        self.key_backslash.setMinimumSize(QSize(0, 0))
        self.key_backslash.setMaximumSize(QSize(16777215, 150))
        self.key_backslash.setFont(font21)

        self.gridLayout.addWidget(self.key_backslash, 3, 0, 1, 1)

        self.key_6 = QPushButton(self.frame_6)
        self.key_6.setObjectName(u"key_6")
        self.key_6.setFont(font21)

        self.gridLayout.addWidget(self.key_6, 1, 2, 1, 1)


        self.horizontalLayout_63.addWidget(self.frame_6)

        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(50, 50, 50);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(100, 100, 100);\n"
"}")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_8)
        self.verticalLayout_36.setSpacing(9)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(5, 0, -1, 8)
        self.numberTablets_img = QLabel(self.frame_8)
        self.numberTablets_img.setObjectName(u"numberTablets_img")
        self.numberTablets_img.setPixmap(QPixmap(u":/assets/icon/characteristics.png"))
        self.numberTablets_img.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_36.addWidget(self.numberTablets_img)

        self.key_enter = QPushButton(self.frame_8)
        self.key_enter.setObjectName(u"key_enter")
        self.key_enter.setMinimumSize(QSize(0, 40))
        self.key_enter.setMaximumSize(QSize(16777215, 55))
        font23 = QFont()
        font23.setFamilies([u"Kanit"])
        font23.setPointSize(30)
        font23.setWeight(QFont.Medium)
        font23.setItalic(False)
        self.key_enter.setFont(font23)
        self.key_enter.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u":/assets/keyboard/enter.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.key_enter.setIcon(icon9)
        self.key_enter.setIconSize(QSize(40, 40))

        self.verticalLayout_36.addWidget(self.key_enter)

        self.key_cancel = QPushButton(self.frame_8)
        self.key_cancel.setObjectName(u"key_cancel")
        self.key_cancel.setMinimumSize(QSize(0, 40))
        self.key_cancel.setMaximumSize(QSize(16777215, 55))
        self.key_cancel.setFont(font23)
        icon10 = QIcon()
        icon10.addFile(u":/assets/keyboard/cancel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.key_cancel.setIcon(icon10)
        self.key_cancel.setIconSize(QSize(40, 40))

        self.verticalLayout_36.addWidget(self.key_cancel)


        self.horizontalLayout_63.addWidget(self.frame_8)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.verticalLayout_35.addWidget(self.frame_4)


        self.verticalLayout_34.addWidget(self.widget_2)

        self.stackedWidget.addWidget(self.keyboard)
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
        self.setting_title.setFont(font9)
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
        self.webcam_setting_monitor = QLabel(self.weighingSettings_Frame)
        self.webcam_setting_monitor.setObjectName(u"webcam_setting_monitor")
        self.webcam_setting_monitor.setMinimumSize(QSize(250, 0))
        self.webcam_setting_monitor.setMaximumSize(QSize(16777215, 16777215))
        self.webcam_setting_monitor.setStyleSheet(u"QLabel {\n"
"	border: solid;\n"
"	border-width: 2px;\n"
"	border-color: rgb(111, 105, 37);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.webcam_setting_monitor.setPixmap(QPixmap(u":/assets/icon/picture_default.png"))
        self.webcam_setting_monitor.setScaledContents(True)

        self.horizontalLayout_14.addWidget(self.webcam_setting_monitor)

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
        self.webcam_setting_view.setMinimumSize(QSize(120, 120))
        self.webcam_setting_view.setMaximumSize(QSize(16777215, 1500))
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
        self.widget_7.setMaximumSize(QSize(16777215, 150))
        self.formLayout = QFormLayout(self.widget_7)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(4)
        self.formLayout.setContentsMargins(-1, 10, -1, 10)
        self.lot_set_label = QLabel(self.widget_7)
        self.lot_set_label.setObjectName(u"lot_set_label")
        self.lot_set_label.setMaximumSize(QSize(85, 16777215))
        self.lot_set_label.setFont(font14)
        self.lot_set_label.setStyleSheet(u"color: rgb(61, 61, 61);")
        self.lot_set_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lot_set_label)

        self.lot_set = QPushButton(self.widget_7)
        self.lot_set.setObjectName(u"lot_set")
        self.lot_set.setFont(font14)
        self.lot_set.setStyleSheet(u"color: rgb(61, 61, 61);\n"
"border: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(111, 105, 37);\n"
"border-radius: 10px;")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lot_set)

        self.mfg_set_label = QLabel(self.widget_7)
        self.mfg_set_label.setObjectName(u"mfg_set_label")
        self.mfg_set_label.setMinimumSize(QSize(50, 0))
        self.mfg_set_label.setMaximumSize(QSize(85, 16777215))
        self.mfg_set_label.setFont(font14)
        self.mfg_set_label.setStyleSheet(u"color: rgb(61, 61, 61);")
        self.mfg_set_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.mfg_set_label)

        self.mfg_set = QPushButton(self.widget_7)
        self.mfg_set.setObjectName(u"mfg_set")
        self.mfg_set.setFont(font14)
        self.mfg_set.setStyleSheet(u"color: rgb(61, 61, 61);\n"
"border: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(111, 105, 37);\n"
"border-radius: 10px;")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.mfg_set)

        self.exp_set_label = QLabel(self.widget_7)
        self.exp_set_label.setObjectName(u"exp_set_label")
        self.exp_set_label.setMaximumSize(QSize(85, 16777215))
        self.exp_set_label.setFont(font14)
        self.exp_set_label.setStyleSheet(u"color: rgb(61, 61, 61);")
        self.exp_set_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.exp_set_label)

        self.exp_set = QPushButton(self.widget_7)
        self.exp_set.setObjectName(u"exp_set")
        self.exp_set.setFont(font14)
        self.exp_set.setStyleSheet(u"color: rgb(61, 61, 61);\n"
"border: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(111, 105, 37);\n"
"border-radius: 10px;")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.exp_set)


        self.verticalLayout_8.addWidget(self.widget_7)

        self.save_images_detection = QPushButton(self.set_widget)
        self.save_images_detection.setObjectName(u"save_images_detection")
        self.save_images_detection.setMaximumSize(QSize(16777215, 50))
        font24 = QFont()
        font24.setFamilies([u"Kanit"])
        font24.setPointSize(12)
        self.save_images_detection.setFont(font24)
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
        icon11 = QIcon()
        icon11.addFile(u":/assets/icon/save-images.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.save_images_detection.setIcon(icon11)
        self.save_images_detection.setIconSize(QSize(40, 40))
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
        self.capture_set.setMinimumSize(QSize(0, 50))
        self.capture_set.setMaximumSize(QSize(16777215, 50))
        self.capture_set.setFont(font15)
        self.capture_set.setStyleSheet(u"")
        self.capture_set.setIcon(icon2)
        self.capture_set.setIconSize(QSize(40, 40))

        self.horizontalLayout_5.addWidget(self.capture_set)

        self.save_set = QPushButton(self.widget_3)
        self.save_set.setObjectName(u"save_set")
        self.save_set.setMinimumSize(QSize(0, 50))
        self.save_set.setMaximumSize(QSize(16777215, 50))
        self.save_set.setFont(font15)
        self.save_set.setStyleSheet(u"")
        icon12 = QIcon()
        icon12.addFile(u":/assets/icon/save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.save_set.setIcon(icon12)
        self.save_set.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.save_set)


        self.verticalLayout_8.addWidget(self.widget_3)


        self.horizontalLayout_14.addWidget(self.set_widget)


        self.verticalLayout_37.addWidget(self.weighingSettings_Frame)


        self.verticalLayout_11.addWidget(self.setting_frame)

        self.stackedWidget.addWidget(self.lme_settings_page)
        self.camera_setting_page = QWidget()
        self.camera_setting_page.setObjectName(u"camera_setting_page")
        self.verticalLayout_18 = QVBoxLayout(self.camera_setting_page)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.widget_20 = QWidget(self.camera_setting_page)
        self.widget_20.setObjectName(u"widget_20")
        self.horizontalLayout_17 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.cameraFocusWidget = QWidget(self.widget_20)
        self.cameraFocusWidget.setObjectName(u"cameraFocusWidget")
        self.cameraFocusWidget.setMinimumSize(QSize(150, 0))
        font25 = QFont()
        font25.setPointSize(12)
        self.cameraFocusWidget.setFont(font25)
        self.cameraFocusWidget.setStyleSheet(u"border: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(80, 80, 80);\n"
"border-radius: 15px;")
        self.verticalLayout_9 = QVBoxLayout(self.cameraFocusWidget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.cameraAutoFocus = QPushButton(self.cameraFocusWidget)
        self.cameraAutoFocus.setObjectName(u"cameraAutoFocus")
        self.cameraAutoFocus.setMinimumSize(QSize(0, 50))
        self.cameraAutoFocus.setMaximumSize(QSize(16777215, 50))
        self.cameraAutoFocus.setFont(font24)
        self.cameraAutoFocus.setStyleSheet(u"QPushButton {\n"
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
        self.cameraAutoFocus.setCheckable(True)
        self.cameraAutoFocus.setChecked(False)

        self.verticalLayout_9.addWidget(self.cameraAutoFocus)

        self.cameraFocusWidget2 = QWidget(self.cameraFocusWidget)
        self.cameraFocusWidget2.setObjectName(u"cameraFocusWidget2")
        self.cameraFocusWidget2.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_8 = QHBoxLayout(self.cameraFocusWidget2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.cameraFocusLabel = QLabel(self.cameraFocusWidget2)
        self.cameraFocusLabel.setObjectName(u"cameraFocusLabel")
        font26 = QFont()
        font26.setFamilies([u"Kanit"])
        font26.setPointSize(12)
        font26.setBold(False)
        self.cameraFocusLabel.setFont(font26)
        self.cameraFocusLabel.setStyleSheet(u"background-color: rgb(122, 122, 122);\n"
"border-radius: 10px;")
        self.cameraFocusLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.cameraFocusLabel)

        self.cameraFocusValue = QLabel(self.cameraFocusWidget2)
        self.cameraFocusValue.setObjectName(u"cameraFocusValue")
        self.cameraFocusValue.setFont(font26)
        self.cameraFocusValue.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(85, 170, 127);")
        self.cameraFocusValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.cameraFocusValue)


        self.verticalLayout_9.addWidget(self.cameraFocusWidget2)

        self.cameraFocus = QDial(self.cameraFocusWidget)
        self.cameraFocus.setObjectName(u"cameraFocus")
        self.cameraFocus.setMaximum(255)

        self.verticalLayout_9.addWidget(self.cameraFocus)


        self.horizontalLayout_17.addWidget(self.cameraFocusWidget)

        self.camera_monitor_widget = QWidget(self.widget_20)
        self.camera_monitor_widget.setObjectName(u"camera_monitor_widget")
        self.verticalLayout_19 = QVBoxLayout(self.camera_monitor_widget)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(10, 0, 10, 0)
        self.camera_setting_monitor = QLabel(self.camera_monitor_widget)
        self.camera_setting_monitor.setObjectName(u"camera_setting_monitor")
        self.camera_setting_monitor.setMinimumSize(QSize(250, 0))
        self.camera_setting_monitor.setMaximumSize(QSize(375, 250))
        self.camera_setting_monitor.setStyleSheet(u"QLabel {\n"
"	border: solid;\n"
"	border-width: 2px;\n"
"	border-color: rgb(111, 105, 37);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.camera_setting_monitor.setPixmap(QPixmap(u":/assets/icon/picture_default.png"))
        self.camera_setting_monitor.setScaledContents(True)

        self.verticalLayout_19.addWidget(self.camera_setting_monitor)


        self.horizontalLayout_17.addWidget(self.camera_monitor_widget)

        self.cameraZoomWidget = QWidget(self.widget_20)
        self.cameraZoomWidget.setObjectName(u"cameraZoomWidget")
        self.cameraZoomWidget.setMinimumSize(QSize(150, 0))
        self.cameraZoomWidget.setStyleSheet(u"border: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(80, 80, 80);\n"
"border-radius: 15px;")
        self.verticalLayout_17 = QVBoxLayout(self.cameraZoomWidget)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.save_camera_setting = QPushButton(self.cameraZoomWidget)
        self.save_camera_setting.setObjectName(u"save_camera_setting")
        self.save_camera_setting.setMinimumSize(QSize(0, 50))
        self.save_camera_setting.setMaximumSize(QSize(16777215, 50))
        font27 = QFont()
        font27.setFamilies([u"Kanit"])
        font27.setPointSize(18)
        font27.setWeight(QFont.Medium)
        font27.setItalic(False)
        self.save_camera_setting.setFont(font27)
        self.save_camera_setting.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(50, 50, 50);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(100, 100, 100);\n"
"}\n"
"")
        self.save_camera_setting.setIcon(icon12)
        self.save_camera_setting.setIconSize(QSize(25, 25))

        self.verticalLayout_17.addWidget(self.save_camera_setting)

        self.cameraZoomWidget2 = QWidget(self.cameraZoomWidget)
        self.cameraZoomWidget2.setObjectName(u"cameraZoomWidget2")
        self.cameraZoomWidget2.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_13 = QHBoxLayout(self.cameraZoomWidget2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.cameraZoomLabel = QLabel(self.cameraZoomWidget2)
        self.cameraZoomLabel.setObjectName(u"cameraZoomLabel")
        self.cameraZoomLabel.setFont(font26)
        self.cameraZoomLabel.setStyleSheet(u"background-color: rgb(122, 122, 122);\n"
"border-radius: 10px;")
        self.cameraZoomLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.cameraZoomLabel)

        self.cameraZoomValue = QLabel(self.cameraZoomWidget2)
        self.cameraZoomValue.setObjectName(u"cameraZoomValue")
        self.cameraZoomValue.setFont(font26)
        self.cameraZoomValue.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(85, 170, 127);")
        self.cameraZoomValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.cameraZoomValue)


        self.verticalLayout_17.addWidget(self.cameraZoomWidget2)

        self.cameraZoom = QDial(self.cameraZoomWidget)
        self.cameraZoom.setObjectName(u"cameraZoom")
        self.cameraZoom.setMinimum(100)
        self.cameraZoom.setMaximum(500)

        self.verticalLayout_17.addWidget(self.cameraZoom)


        self.horizontalLayout_17.addWidget(self.cameraZoomWidget)


        self.verticalLayout_18.addWidget(self.widget_20)

        self.widget_19 = QWidget(self.camera_setting_page)
        self.widget_19.setObjectName(u"widget_19")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_16.setSpacing(15)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.cameraBrightnessWidget = QWidget(self.widget_19)
        self.cameraBrightnessWidget.setObjectName(u"cameraBrightnessWidget")
        self.cameraBrightnessWidget.setStyleSheet(u"border: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(80, 80, 80);\n"
"border-radius: 15px;")
        self.verticalLayout_10 = QVBoxLayout(self.cameraBrightnessWidget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.cameraBrightnessWidget2 = QWidget(self.cameraBrightnessWidget)
        self.cameraBrightnessWidget2.setObjectName(u"cameraBrightnessWidget2")
        self.cameraBrightnessWidget2.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_9 = QHBoxLayout(self.cameraBrightnessWidget2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.cameraBrightnessLabel = QLabel(self.cameraBrightnessWidget2)
        self.cameraBrightnessLabel.setObjectName(u"cameraBrightnessLabel")
        self.cameraBrightnessLabel.setFont(font26)
        self.cameraBrightnessLabel.setStyleSheet(u"background-color: rgb(122, 122, 122);\n"
"border-radius: 10px;")
        self.cameraBrightnessLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.cameraBrightnessLabel)

        self.cameraBrightnessValue = QLabel(self.cameraBrightnessWidget2)
        self.cameraBrightnessValue.setObjectName(u"cameraBrightnessValue")
        self.cameraBrightnessValue.setFont(font26)
        self.cameraBrightnessValue.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(85, 170, 127);")
        self.cameraBrightnessValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.cameraBrightnessValue)


        self.verticalLayout_10.addWidget(self.cameraBrightnessWidget2)

        self.cameraBrightness = QDial(self.cameraBrightnessWidget)
        self.cameraBrightness.setObjectName(u"cameraBrightness")
        self.cameraBrightness.setMaximum(255)

        self.verticalLayout_10.addWidget(self.cameraBrightness)


        self.horizontalLayout_16.addWidget(self.cameraBrightnessWidget)

        self.cameraContrastWidget = QWidget(self.widget_19)
        self.cameraContrastWidget.setObjectName(u"cameraContrastWidget")
        self.cameraContrastWidget.setStyleSheet(u"border: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(80, 80, 80);\n"
"border-radius: 15px;")
        self.verticalLayout_12 = QVBoxLayout(self.cameraContrastWidget)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.cameraContrastWidget2 = QWidget(self.cameraContrastWidget)
        self.cameraContrastWidget2.setObjectName(u"cameraContrastWidget2")
        self.cameraContrastWidget2.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_10 = QHBoxLayout(self.cameraContrastWidget2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.cameraContrastLabel = QLabel(self.cameraContrastWidget2)
        self.cameraContrastLabel.setObjectName(u"cameraContrastLabel")
        self.cameraContrastLabel.setFont(font26)
        self.cameraContrastLabel.setStyleSheet(u"background-color: rgb(122, 122, 122);\n"
"border-radius: 10px;")
        self.cameraContrastLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.cameraContrastLabel)

        self.cameraContrastValue = QLabel(self.cameraContrastWidget2)
        self.cameraContrastValue.setObjectName(u"cameraContrastValue")
        self.cameraContrastValue.setFont(font26)
        self.cameraContrastValue.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(85, 170, 127);")
        self.cameraContrastValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.cameraContrastValue)


        self.verticalLayout_12.addWidget(self.cameraContrastWidget2)

        self.cameraContrast = QDial(self.cameraContrastWidget)
        self.cameraContrast.setObjectName(u"cameraContrast")
        self.cameraContrast.setMaximum(255)

        self.verticalLayout_12.addWidget(self.cameraContrast)


        self.horizontalLayout_16.addWidget(self.cameraContrastWidget)

        self.cameraExposureWidget = QWidget(self.widget_19)
        self.cameraExposureWidget.setObjectName(u"cameraExposureWidget")
        self.cameraExposureWidget.setStyleSheet(u"border: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(80, 80, 80);\n"
"border-radius: 15px;")
        self.verticalLayout_15 = QVBoxLayout(self.cameraExposureWidget)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.cameraExposureWidget2 = QWidget(self.cameraExposureWidget)
        self.cameraExposureWidget2.setObjectName(u"cameraExposureWidget2")
        self.cameraExposureWidget2.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_11 = QHBoxLayout(self.cameraExposureWidget2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.cameraExposureLabel = QLabel(self.cameraExposureWidget2)
        self.cameraExposureLabel.setObjectName(u"cameraExposureLabel")
        self.cameraExposureLabel.setFont(font26)
        self.cameraExposureLabel.setStyleSheet(u"background-color: rgb(122, 122, 122);\n"
"border-radius: 10px;")
        self.cameraExposureLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_11.addWidget(self.cameraExposureLabel)

        self.cameraExposureValue = QLabel(self.cameraExposureWidget2)
        self.cameraExposureValue.setObjectName(u"cameraExposureValue")
        self.cameraExposureValue.setFont(font26)
        self.cameraExposureValue.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(85, 170, 127);")
        self.cameraExposureValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_11.addWidget(self.cameraExposureValue)


        self.verticalLayout_15.addWidget(self.cameraExposureWidget2)

        self.cameraExposure = QDial(self.cameraExposureWidget)
        self.cameraExposure.setObjectName(u"cameraExposure")
        self.cameraExposure.setMaximum(255)

        self.verticalLayout_15.addWidget(self.cameraExposure)


        self.horizontalLayout_16.addWidget(self.cameraExposureWidget)

        self.sensorDelayWidget = QWidget(self.widget_19)
        self.sensorDelayWidget.setObjectName(u"sensorDelayWidget")
        self.sensorDelayWidget.setStyleSheet(u"border: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(80, 80, 80);\n"
"border-radius: 15px;")
        self.verticalLayout_16 = QVBoxLayout(self.sensorDelayWidget)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.sensorDelayWidget2 = QWidget(self.sensorDelayWidget)
        self.sensorDelayWidget2.setObjectName(u"sensorDelayWidget2")
        self.sensorDelayWidget2.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_12 = QHBoxLayout(self.sensorDelayWidget2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.sensorDelayWidgetLabel = QLabel(self.sensorDelayWidget2)
        self.sensorDelayWidgetLabel.setObjectName(u"sensorDelayWidgetLabel")
        self.sensorDelayWidgetLabel.setFont(font26)
        self.sensorDelayWidgetLabel.setStyleSheet(u"background-color: rgb(122, 122, 122);\n"
"border-radius: 10px;")
        self.sensorDelayWidgetLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_12.addWidget(self.sensorDelayWidgetLabel)

        self.sensorDelayValue = QLabel(self.sensorDelayWidget2)
        self.sensorDelayValue.setObjectName(u"sensorDelayValue")
        self.sensorDelayValue.setFont(font26)
        self.sensorDelayValue.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(85, 170, 127);")
        self.sensorDelayValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_12.addWidget(self.sensorDelayValue)


        self.verticalLayout_16.addWidget(self.sensorDelayWidget2)

        self.sensorDelay = QDial(self.sensorDelayWidget)
        self.sensorDelay.setObjectName(u"sensorDelay")
        self.sensorDelay.setMaximum(500)

        self.verticalLayout_16.addWidget(self.sensorDelay)


        self.horizontalLayout_16.addWidget(self.sensorDelayWidget)


        self.verticalLayout_18.addWidget(self.widget_19)

        self.stackedWidget.addWidget(self.camera_setting_page)
        self.shutdown_page = QWidget()
        self.shutdown_page.setObjectName(u"shutdown_page")
        self.verticalLayout_70 = QVBoxLayout(self.shutdown_page)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.shutdown_title = QLabel(self.shutdown_page)
        self.shutdown_title.setObjectName(u"shutdown_title")
        self.shutdown_title.setMaximumSize(QSize(16777215, 65))
        self.shutdown_title.setFont(font19)
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
        font28 = QFont()
        font28.setFamilies([u"Kanit"])
        font28.setPointSize(22)
        font28.setBold(True)
        font28.setStrikeOut(False)
        self.shutdown_warning_label.setFont(font28)
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
        self.confirm_shutdown.setFont(font23)
        self.confirm_shutdown.setStyleSheet(u"")
        self.confirm_shutdown.setIcon(icon9)
        self.confirm_shutdown.setIconSize(QSize(50, 50))

        self.horizontalLayout_92.addWidget(self.confirm_shutdown)

        self.cancel_shutdown = QPushButton(self.widget_18)
        self.cancel_shutdown.setObjectName(u"cancel_shutdown")
        self.cancel_shutdown.setMinimumSize(QSize(0, 52))
        self.cancel_shutdown.setFont(font23)
        self.cancel_shutdown.setIcon(icon10)
        self.cancel_shutdown.setIconSize(QSize(50, 50))

        self.horizontalLayout_92.addWidget(self.cancel_shutdown)


        self.verticalLayout_68.addWidget(self.widget_18)

        self.credit = QLabel(self.shutdown_widget)
        self.credit.setObjectName(u"credit")
        self.credit.setMaximumSize(QSize(16777215, 45))
        self.credit.setFont(font)
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
        self.version.setFont(font)
        self.version.setStyleSheet(u"color: rgb(91, 91, 91);")
        self.version.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_93.addWidget(self.version)


        self.verticalLayout_68.addWidget(self.widget_21)


        self.verticalLayout_70.addWidget(self.shutdown_widget)

        self.stackedWidget.addWidget(self.shutdown_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout_3.addWidget(self.screen_page, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menu.toggled.connect(self.show_sidebar.setVisible)
        self.menu.toggled.connect(self.hide_sidebar.setHidden)
        self.camera_setting_2.toggled.connect(self.camera_setting_1.setChecked)
        self.camera_setting_1.toggled.connect(self.camera_setting_2.setChecked)
        self.setting_1.toggled.connect(self.setting_2.setChecked)
        self.setting_2.toggled.connect(self.setting_1.setChecked)
        self.home_2.toggled.connect(self.home_1.setChecked)
        self.home_1.toggled.connect(self.home_2.setChecked)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.profile_img1.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"DETECTOR", None))
        self.home_1.setText(QCoreApplication.translate("MainWindow", u"  \u0e2b\u0e19\u0e49\u0e32\u0e2b\u0e25\u0e31\u0e01", None))
        self.setting_1.setText(QCoreApplication.translate("MainWindow", u" \u0e15\u0e31\u0e49\u0e07\u0e04\u0e48\u0e32", None))
        self.camera_setting_1.setText(QCoreApplication.translate("MainWindow", u" \u0e15\u0e31\u0e49\u0e07\u0e04\u0e48\u0e32\u0e01\u0e25\u0e49\u0e2d\u0e07", None))
        self.restart_program_1.setText(QCoreApplication.translate("MainWindow", u"  \u0e23\u0e35\u0e2a\u0e15\u0e32\u0e23\u0e4c\u0e17", None))
        self.shutdown_1.setText(QCoreApplication.translate("MainWindow", u"  \u0e1b\u0e34\u0e14\u0e40\u0e04\u0e23\u0e37\u0e48\u0e2d\u0e07", None))
        self.profile_img2.setText("")
        self.home_2.setText("")
        self.setting_2.setText("")
        self.camera_setting_2.setText("")
        self.restart_program_2.setText("")
        self.shutdown_2.setText("")
        self.menu.setText("")
        self.title.setText(QCoreApplication.translate("MainWindow", u"\u0e23\u0e30\u0e1a\u0e1a\u0e15\u0e23\u0e27\u0e08\u0e2a\u0e2d\u0e1a\u0e01\u0e32\u0e23\u0e1e\u0e34\u0e21\u0e1e\u0e4c", None))
        self.time_bar.setText(QCoreApplication.translate("MainWindow", u"HH:MM:SS", None))
        self.date_bar.setText(QCoreApplication.translate("MainWindow", u"DD/MM/YYYY", None))
        self.detection_status.setText(QCoreApplication.translate("MainWindow", u"\u0e01\u0e14\u0e1b\u0e38\u0e48\u0e21 START \u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e40\u0e23\u0e34\u0e48\u0e21\u0e17\u0e33\u0e07\u0e32\u0e19", None))
        self.webcam_monitor.setText("")
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
        self.exp_label.setText(QCoreApplication.translate("MainWindow", u"EXP.", None))
        self.lot_label.setText(QCoreApplication.translate("MainWindow", u"LOT.", None))
        self.mfg_label.setText(QCoreApplication.translate("MainWindow", u"MFG.", None))
        self.mfg_detected.setText(QCoreApplication.translate("MainWindow", u"XXXXXX", None))
        self.exp_detected.setText(QCoreApplication.translate("MainWindow", u"XXXXXX", None))
        self.capture_test.setText(QCoreApplication.translate("MainWindow", u"\u0e17\u0e14\u0e2a\u0e2d\u0e1a", None))
        self.start.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.process_img.setText("")
        self.process_label_line_1.setText(QCoreApplication.translate("MainWindow", u"PRINTING  INSPECTION SYSTEM", None))
        self.process_label_line_2.setText(QCoreApplication.translate("MainWindow", u"Created by Nattapon pondonko", None))
        self.process_label_line_3.setText(QCoreApplication.translate("MainWindow", u"Engineering Department", None))
        self.process_label_line_4.setText("")
        self.keyboard_title.setText(QCoreApplication.translate("MainWindow", u"\u0e15\u0e31\u0e49\u0e07\u0e04\u0e48\u0e32 LOT, MFG, EXP", None))
        self.val_input.setText(QCoreApplication.translate("MainWindow", u"XXXX", None))
        self.key_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.key_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.key_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.key_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.key_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.key_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.key_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.key_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.key_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.key_backspace.setText("")
        self.key_backslash.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.key_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.numberTablets_img.setText("")
        self.key_enter.setText(QCoreApplication.translate("MainWindow", u"  \u0e22\u0e37\u0e19\u0e22\u0e31\u0e19", None))
        self.key_cancel.setText(QCoreApplication.translate("MainWindow", u"  \u0e22\u0e01\u0e40\u0e25\u0e34\u0e01", None))
        self.setting_title.setText(QCoreApplication.translate("MainWindow", u"\u0e15\u0e31\u0e49\u0e07\u0e04\u0e48\u0e32 LOT, MFG, EXP", None))
        self.webcam_setting_monitor.setText("")
        self.webcam_setting_view.setText("")
        self.lot_set_label.setText(QCoreApplication.translate("MainWindow", u"LOT.", None))
        self.lot_set.setText(QCoreApplication.translate("MainWindow", u"XXXXXX", None))
        self.mfg_set_label.setText(QCoreApplication.translate("MainWindow", u"MFG.", None))
        self.mfg_set.setText(QCoreApplication.translate("MainWindow", u"XXXXXX", None))
        self.exp_set_label.setText(QCoreApplication.translate("MainWindow", u"EXP.", None))
        self.exp_set.setText(QCoreApplication.translate("MainWindow", u"XXXXXX", None))
        self.save_images_detection.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e1b\u0e34\u0e14\u0e43\u0e0a\u0e49\u0e07\u0e32\u0e19\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e20\u0e32\u0e1e\u0e17\u0e35\u0e48\u0e15\u0e23\u0e27\u0e08\u0e08\u0e31\u0e1a", None))
        self.capture_set.setText(QCoreApplication.translate("MainWindow", u" \u0e16\u0e48\u0e32\u0e22\u0e20\u0e32\u0e1e", None))
        self.save_set.setText(QCoreApplication.translate("MainWindow", u" \u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01", None))
        self.cameraAutoFocus.setText(QCoreApplication.translate("MainWindow", u"AUTO FOCUS", None))
        self.cameraFocusLabel.setText(QCoreApplication.translate("MainWindow", u"FOCUS", None))
        self.cameraFocusValue.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.camera_setting_monitor.setText("")
        self.save_camera_setting.setText(QCoreApplication.translate("MainWindow", u" \u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01", None))
        self.cameraZoomLabel.setText(QCoreApplication.translate("MainWindow", u"ZOOM", None))
        self.cameraZoomValue.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.cameraBrightnessLabel.setText(QCoreApplication.translate("MainWindow", u"BRIGHTNESS", None))
        self.cameraBrightnessValue.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.cameraContrastLabel.setText(QCoreApplication.translate("MainWindow", u"CONTRAST", None))
        self.cameraContrastValue.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.cameraExposureLabel.setText(QCoreApplication.translate("MainWindow", u"EXPOSURE", None))
        self.cameraExposureValue.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.sensorDelayWidgetLabel.setText(QCoreApplication.translate("MainWindow", u"DELAY", None))
        self.sensorDelayValue.setText(QCoreApplication.translate("MainWindow", u"0ms", None))
        self.shutdown_title.setText(QCoreApplication.translate("MainWindow", u"\u0e22\u0e37\u0e19\u0e22\u0e31\u0e19\u0e01\u0e32\u0e23\u0e1b\u0e34\u0e14\u0e40\u0e04\u0e23\u0e37\u0e48\u0e2d\u0e07", None))
        self.shutdown_warning_label.setText(QCoreApplication.translate("MainWindow", u"\u0e2b\u0e25\u0e31\u0e07\u0e08\u0e32\u0e01\u0e01\u0e14\u0e1b\u0e38\u0e48\u0e21 \u0e22\u0e37\u0e19\u0e22\u0e31\u0e19 \u0e43\u0e2b\u0e49\u0e23\u0e2d\u0e1b\u0e23\u0e30\u0e21\u0e32\u0e13 1 \u0e19\u0e32\u0e17\u0e35\u0e01\u0e48\u0e2d\u0e19\u0e16\u0e2d\u0e14\u0e1b\u0e25\u0e31\u0e4a\u0e01", None))
        self.confirm_shutdown.setText(QCoreApplication.translate("MainWindow", u"  \u0e22\u0e37\u0e19\u0e22\u0e31\u0e19", None))
        self.cancel_shutdown.setText(QCoreApplication.translate("MainWindow", u"  \u0e22\u0e01\u0e40\u0e25\u0e34\u0e01", None))
        self.credit.setText(QCoreApplication.translate("MainWindow", u"Created by Nattapon pondonko Engineering Department", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"Software version 1.0.0", None))
    # retranslateUi

