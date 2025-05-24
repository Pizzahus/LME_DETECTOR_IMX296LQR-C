# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DETECTOR_7inch.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import QApplication, QFrame, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QMainWindow, QPushButton, QSizePolicy, QSlider, QSpacerItem, QStackedWidget, QVBoxLayout, QWidget
import ui.resource_rc as resource_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1012, 608)
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
        self.show_sidebar.setStyleSheet(
            u"QWidget {\n"
            "	background-color: rgb(0, 150, 255);\n"
            "	border-radius: 10px;\n"
            "}\n"
            "\n"
            "QPushButton {\n"
            "	background-color: rgb(0, 150, 255);\n"
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
            "}"
        )
        self.verticalLayout_41 = QVBoxLayout(self.show_sidebar)
        self.verticalLayout_41.setSpacing(20)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, 0, -1)
        self.profile_img1 = QLabel(self.show_sidebar)
        self.profile_img1.setObjectName(u"profile_img1")
        self.profile_img1.setMinimumSize(QSize(80, 80))
        self.profile_img1.setMaximumSize(QSize(80, 80))
        self.profile_img1.setPixmap(QPixmap(u":/assets/images/polipharm.png"))
        self.profile_img1.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.profile_img1)

        self.label_3 = QLabel(self.show_sidebar)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Kanit"])
        font.setPointSize(20)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.verticalLayout_41.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.home_1 = QPushButton(self.show_sidebar)
        self.home_1.setObjectName(u"home_1")
        font1 = QFont()
        font1.setFamilies([u"Kanit"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.home_1.setFont(font1)
        self.home_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/assets/icon/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.home_1.setIcon(icon)
        self.home_1.setIconSize(QSize(50, 50))
        self.home_1.setCheckable(True)
        self.home_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.home_1)

        self.setting_1 = QPushButton(self.show_sidebar)
        self.setting_1.setObjectName(u"setting_1")
        font2 = QFont()
        font2.setFamilies([u"Kanit"])
        font2.setPointSize(12)
        self.setting_1.setFont(font2)
        self.setting_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/assets/icon/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.setting_1.setIcon(icon1)
        self.setting_1.setIconSize(QSize(50, 50))
        self.setting_1.setCheckable(True)
        self.setting_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.setting_1)

        self.camera_setting_1 = QPushButton(self.show_sidebar)
        self.camera_setting_1.setObjectName(u"camera_setting_1")
        font3 = QFont()
        font3.setFamilies([u"Kanit"])
        font3.setPointSize(11)
        self.camera_setting_1.setFont(font3)
        self.camera_setting_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/assets/icon/camera.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.camera_setting_1.setIcon(icon2)
        self.camera_setting_1.setIconSize(QSize(50, 50))
        self.camera_setting_1.setCheckable(True)
        self.camera_setting_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.camera_setting_1)

        self.verticalLayout_41.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 297, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_41.addItem(self.verticalSpacer_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.restart_program_1 = QPushButton(self.show_sidebar)
        self.restart_program_1.setObjectName(u"restart_program_1")
        font4 = QFont()
        font4.setFamilies([u"Kanit"])
        font4.setPointSize(12)
        font4.setStrikeOut(False)
        font4.setKerning(True)
        self.restart_program_1.setFont(font4)
        self.restart_program_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/assets/icon/restart.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.restart_program_1.setIcon(icon3)
        self.restart_program_1.setIconSize(QSize(50, 50))
        # if QT_CONFIG(shortcut)
        self.restart_program_1.setShortcut(u"Ctrl+S")
        # endif // QT_CONFIG(shortcut)

        self.verticalLayout_4.addWidget(self.restart_program_1)

        self.verticalLayout_41.addLayout(self.verticalLayout_4)

        self.gridLayout_3.addWidget(self.show_sidebar, 0, 1, 1, 1)

        self.hide_sidebar = QWidget(self.centralwidget)
        self.hide_sidebar.setObjectName(u"hide_sidebar")
        self.hide_sidebar.setStyleSheet(
            u"QWidget {\n"
            "	background-color: rgb(0, 150, 255);\n"
            "	border-radius: 10px;\n"
            "}\n"
            "\n"
            "QPushButton{\n"
            "	background-color: rgb(0, 150, 255);\n"
            "	color: white;\n"
            "	height: 30px;\n"
            "	border: none;\n"
            "	border-radius: 10px;\n"
            "	padding: 15px;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "	background-color: #f5fafe;\n"
            "	color: rgb(0, 150, 255);\n"
            "	font-weight: bold;\n"
            "}"
        )
        self.verticalLayout_42 = QVBoxLayout(self.hide_sidebar)
        self.verticalLayout_42.setSpacing(20)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.profile_img2 = QLabel(self.hide_sidebar)
        self.profile_img2.setObjectName(u"profile_img2")
        self.profile_img2.setMinimumSize(QSize(80, 80))
        self.profile_img2.setMaximumSize(QSize(80, 80))
        self.profile_img2.setPixmap(QPixmap(u":/assets/images/polipharm.png"))
        self.profile_img2.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.profile_img2)

        self.verticalLayout_42.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.home_2 = QPushButton(self.hide_sidebar)
        self.home_2.setObjectName(u"home_2")
        self.home_2.setMinimumSize(QSize(5, 0))
        self.home_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.home_2.setIcon(icon)
        self.home_2.setIconSize(QSize(50, 50))
        self.home_2.setCheckable(True)
        self.home_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_2)

        self.setting_2 = QPushButton(self.hide_sidebar)
        self.setting_2.setObjectName(u"setting_2")
        self.setting_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setting_2.setIcon(icon1)
        self.setting_2.setIconSize(QSize(50, 50))
        self.setting_2.setCheckable(True)
        self.setting_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.setting_2)

        self.camera_setting_2 = QPushButton(self.hide_sidebar)
        self.camera_setting_2.setObjectName(u"camera_setting_2")
        self.camera_setting_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.camera_setting_2.setIcon(icon2)
        self.camera_setting_2.setIconSize(QSize(50, 50))
        self.camera_setting_2.setCheckable(True)
        self.camera_setting_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.camera_setting_2)

        self.verticalLayout_42.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 297, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_42.addItem(self.verticalSpacer)

        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.restart_program_2 = QPushButton(self.hide_sidebar)
        self.restart_program_2.setObjectName(u"restart_program_2")
        self.restart_program_2.setFont(font4)
        self.restart_program_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.restart_program_2.setIcon(icon3)
        self.restart_program_2.setIconSize(QSize(50, 50))
        # if QT_CONFIG(shortcut)
        self.restart_program_2.setShortcut(u"Ctrl+S")
        # endif // QT_CONFIG(shortcut)

        self.verticalLayout_40.addWidget(self.restart_program_2)

        self.verticalLayout_42.addLayout(self.verticalLayout_40)

        self.gridLayout_3.addWidget(self.hide_sidebar, 0, 0, 1, 1)

        self.screen_page = QWidget(self.centralwidget)
        self.screen_page.setObjectName(u"screen_page")
        self.verticalLayout_5 = QVBoxLayout(self.screen_page)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 0, 9, 0)
        self.widget = QWidget(self.screen_page)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 55))
        self.widget.setStyleSheet(u"background-color: rgb(100, 100, 100);\n" "color: rgb(255, 255, 255);\n" "border-radius: 8px;")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.frame_28 = QFrame(self.widget)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setEnabled(True)
        self.frame_28.setMinimumSize(QSize(0, 0))
        self.frame_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 75, 0)
        self.menu = QPushButton(self.frame_28)
        self.menu.setObjectName(u"menu")
        font5 = QFont()
        font5.setPointSize(9)
        self.menu.setFont(font5)
        self.menu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/assets/icon/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/assets/icon/menu_open.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.menu.setIcon(icon4)
        self.menu.setIconSize(QSize(40, 40))
        self.menu.setCheckable(True)
        self.menu.setAutoExclusive(True)

        self.horizontalLayout_6.addWidget(self.menu)

        self.horizontalLayout.addWidget(self.frame_28)

        self.horizontalSpacer_5 = QSpacerItem(92, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.title = QLabel(self.widget)
        self.title.setObjectName(u"title")
        font6 = QFont()
        font6.setFamilies([u"Kanit"])
        font6.setPointSize(22)
        font6.setBold(True)
        self.title.setFont(font6)
        self.title.setStyleSheet(u"")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.title)

        self.horizontalSpacer_4 = QSpacerItem(75, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.wifi_signal = QLabel(self.widget)
        self.wifi_signal.setObjectName(u"wifi_signal")
        self.wifi_signal.setMaximumSize(QSize(30, 30))
        self.wifi_signal.setPixmap(QPixmap(u":/assets/icon/no-wifi.png"))
        self.wifi_signal.setScaledContents(True)

        self.horizontalLayout.addWidget(self.wifi_signal)

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
        self.time_bar.setMaximumSize(QSize(100, 12))
        font8 = QFont()
        font8.setFamilies([u"Kanit"])
        font8.setPointSize(13)
        font8.setBold(False)
        self.time_bar.setFont(font8)
        self.time_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.datetime_group.addWidget(self.time_bar)

        self.date_bar = QLabel(self.datetime_group_2)
        self.date_bar.setObjectName(u"date_bar")
        self.date_bar.setMaximumSize(QSize(120, 12))
        self.date_bar.setFont(font8)
        self.date_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.datetime_group.addWidget(self.date_bar)

        self.horizontalLayout.addWidget(self.datetime_group_2)

        self.verticalLayout_5.addWidget(self.widget)

        self.stackedWidget = QStackedWidget(self.screen_page)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 70))
        self.stackedWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.stackedWidget.setStyleSheet(
            u"QWidget {\n"
            "	background-color: rgb(255, 255, 255);\n"
            "	color: rgb(255, 255, 255);\n"
            "}\n"
            "\n"
            "QGroupBox {\n"
            "	border: none;\n"
            "}\n"
            "\n"
            "#summary_weight_label_1, #summary_weight_label_2, #summary_average_label,  #summary_percent_label {\n"
            "	background-color: rgb(80, 80, 80);\n"
            "	border-top-left-radius: 15px;\n"
            "	border-top-right-radius: 15px;\n"
            "}"
        )
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
        self.detection_alert = QLabel(self.detection_frame_2)
        self.detection_alert.setObjectName(u"detection_alert")
        self.detection_alert.setMinimumSize(QSize(0, 50))
        self.detection_alert.setMaximumSize(QSize(16777215, 50))
        font9 = QFont()
        font9.setFamilies([u"Kanit"])
        font9.setPointSize(25)
        self.detection_alert.setFont(font9)
        self.detection_alert.setStyleSheet(u"background-color: rgb(0, 150, 255);\n" "border-radius: 15px;")
        self.detection_alert.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_15.addWidget(self.detection_alert)

        self.verticalLayout_14.addWidget(self.detection_frame_2)

        self.detection_frame = QFrame(self.detection_page)
        self.detection_frame.setObjectName(u"detection_frame")
        self.detection_frame.setStyleSheet(u"")
        self.detection_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.detection_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.detection_frame)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.webcam_monitor = QLabel(self.detection_frame)
        self.webcam_monitor.setObjectName(u"webcam_monitor")
        self.webcam_monitor.setMinimumSize(QSize(250, 250))
        self.webcam_monitor.setMaximumSize(QSize(16777215, 16777215))
        self.webcam_monitor.setStyleSheet(
            u"QLabel {\n" "	border: solid;\n" "	border-width: 2px;\n" "	border-color: rgb(111, 105, 37);\n" "	border-radius: 15px;\n" "	padding: 10px;\n" "	background-color: rgb(0, 0, 0);\n" "}\n" ""
        )
        self.webcam_monitor.setPixmap(QPixmap(u":/assets/icon/picture_default.png"))
        self.webcam_monitor.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.webcam_monitor)

        self.detection_widget = QWidget(self.detection_frame)
        self.detection_widget.setObjectName(u"detection_widget")
        self.detection_widget.setMinimumSize(QSize(300, 0))
        self.detection_widget.setMaximumSize(QSize(300, 16777215))
        self.detection_widget.setStyleSheet(u"QWidget {\n" "	background-color: rgb(220, 220, 220);\n" "	border-radius: 15px;\n" "}")
        self.verticalLayout_6 = QVBoxLayout(self.detection_widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, -1, 0)
        self.detection_view = QLabel(self.detection_widget)
        self.detection_view.setObjectName(u"detection_view")
        self.detection_view.setMinimumSize(QSize(200, 200))
        self.detection_view.setMaximumSize(QSize(16777215, 200))
        self.detection_view.setStyleSheet(
            u"QLabel {\n"
            "	border: solid;\n"
            "	border-width: 2px;\n"
            "	border-color: rgb(111, 105, 37);\n"
            "	border-radius: 15px;\n"
            "	background-color: rgb(255, 255, 255);\n"
            "	padding: 10px;\n"
            "}\n"
            ""
        )
        self.detection_view.setPixmap(QPixmap(u":/assets/icon/picture_default.png"))
        self.detection_view.setScaledContents(True)

        self.verticalLayout_6.addWidget(self.detection_view)

        self.widget_6 = QWidget(self.detection_widget)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMaximumSize(QSize(16777215, 140))
        self.gridLayout_4 = QGridLayout(self.widget_6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(12)
        self.gridLayout_4.setContentsMargins(20, 0, 20, -1)
        self.lot_label = QLabel(self.widget_6)
        self.lot_label.setObjectName(u"lot_label")
        self.lot_label.setMaximumSize(QSize(70, 16777215))
        self.lot_label.setFont(font)
        self.lot_label.setStyleSheet(u"color: rgb(61, 61, 61);")
        self.lot_label.setAlignment(Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.lot_label, 0, 0, 1, 1)

        self.lot_detected = QLabel(self.widget_6)
        self.lot_detected.setObjectName(u"lot_detected")
        self.lot_detected.setFont(font)
        self.lot_detected.setStyleSheet(u"color: rgb(61, 61, 61);")
        self.lot_detected.setAlignment(Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.lot_detected, 0, 1, 1, 1)

        self.mfg_label = QLabel(self.widget_6)
        self.mfg_label.setObjectName(u"mfg_label")
        self.mfg_label.setMaximumSize(QSize(70, 16777215))
        self.mfg_label.setFont(font)
        self.mfg_label.setStyleSheet(u"color: rgb(61, 61, 61);")
        self.mfg_label.setAlignment(Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.mfg_label, 1, 0, 1, 1)

        self.mfg_detected = QLabel(self.widget_6)
        self.mfg_detected.setObjectName(u"mfg_detected")
        self.mfg_detected.setFont(font)
        self.mfg_detected.setStyleSheet(u"color: rgb(61, 61, 61);")
        self.mfg_detected.setAlignment(Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.mfg_detected, 1, 1, 1, 1)

        self.exp_label = QLabel(self.widget_6)
        self.exp_label.setObjectName(u"exp_label")
        self.exp_label.setMaximumSize(QSize(70, 16777215))
        self.exp_label.setFont(font)
        self.exp_label.setStyleSheet(u"color: rgb(61, 61, 61);")
        self.exp_label.setAlignment(Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.exp_label, 2, 0, 1, 1)

        self.exp_detected = QLabel(self.widget_6)
        self.exp_detected.setObjectName(u"exp_detected")
        self.exp_detected.setFont(font)
        self.exp_detected.setStyleSheet(u"color: rgb(61, 61, 61);")
        self.exp_detected.setAlignment(Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.exp_detected, 2, 1, 1, 1)

        self.verticalLayout_6.addWidget(self.widget_6)

        self.widget_4 = QWidget(self.detection_widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(16777215, 60))
        self.widget_4.setStyleSheet(u"")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, -1, 0, -1)
        self.capture_test = QPushButton(self.widget_4)
        self.capture_test.setObjectName(u"capture_test")
        self.capture_test.setMinimumSize(QSize(0, 45))
        font10 = QFont()
        font10.setFamilies([u"Kanit"])
        font10.setPointSize(14)
        font10.setWeight(QFont.Medium)
        font10.setItalic(False)
        self.capture_test.setFont(font10)
        self.capture_test.setStyleSheet(
            u"QPushButton {\n" "	background-color: rgb(50, 50, 50);\n" "	border-radius: 10px;\n" "}\n" "QPushButton:pressed {\n" "	background-color: rgb(100, 100, 100);\n" "}"
        )
        self.capture_test.setIcon(icon2)
        self.capture_test.setIconSize(QSize(40, 40))

        self.horizontalLayout_7.addWidget(self.capture_test)

        self.start = QPushButton(self.widget_4)
        self.start.setObjectName(u"start")
        self.start.setMinimumSize(QSize(0, 45))
        self.start.setFont(font10)
        self.start.setStyleSheet(
            u"QPushButton {\n"
            "	background-color: rgb(200, 0, 0);\n"
            "	color: rgb(195, 195, 195);\n"
            "	text-align: center;\n"
            "	height: 30px;\n"
            "	border: none;\n"
            "	border-radius: 10px;\n"
            "	padding: 15px;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "	background-color: rgb(0, 170, 50);\n"
            "	color: white;\n"
            "}"
        )
        icon5 = QIcon()
        icon5.addFile(u":/assets/keyboard/record.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.start.setIcon(icon5)
        self.start.setIconSize(QSize(30, 30))
        self.start.setCheckable(True)
        self.start.setChecked(False)

        self.horizontalLayout_7.addWidget(self.start)

        self.verticalLayout_6.addWidget(self.widget_4)

        self.horizontalLayout_4.addWidget(self.detection_widget)

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
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(164, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_62.addItem(self.horizontalSpacer_2)

        self.process_img = QLabel(self.process_img_frame)
        self.process_img.setObjectName(u"process_img")
        self.process_img.setMinimumSize(QSize(350, 350))
        self.process_img.setMaximumSize(QSize(300, 300))
        self.process_img.setPixmap(QPixmap(u":/assets/gif/connecting.gif"))
        self.process_img.setScaledContents(True)
        self.process_img.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_62.addWidget(self.process_img)

        self.horizontalSpacer_3 = QSpacerItem(163, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_62.addItem(self.horizontalSpacer_3)

        self.verticalLayout_32.addWidget(self.process_img_frame)

        self.process_label_line_1 = QLabel(self.process_frame)
        self.process_label_line_1.setObjectName(u"process_label_line_1")
        self.process_label_line_1.setMinimumSize(QSize(0, 30))
        self.process_label_line_1.setMaximumSize(QSize(16777215, 30))
        self.process_label_line_1.setFont(font9)
        self.process_label_line_1.setStyleSheet(u"color: rgb(128, 128, 128);")
        self.process_label_line_1.setFrameShape(QFrame.Shape.NoFrame)
        self.process_label_line_1.setFrameShadow(QFrame.Shadow.Plain)
        self.process_label_line_1.setLineWidth(1)
        self.process_label_line_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_32.addWidget(self.process_label_line_1)

        self.process_label_line_2 = QLabel(self.process_frame)
        self.process_label_line_2.setObjectName(u"process_label_line_2")
        self.process_label_line_2.setMinimumSize(QSize(0, 30))
        self.process_label_line_2.setMaximumSize(QSize(16777215, 30))
        font11 = QFont()
        font11.setFamilies([u"Kanit"])
        font11.setPointSize(18)
        self.process_label_line_2.setFont(font11)
        self.process_label_line_2.setStyleSheet(u"color: rgb(128, 128, 128);")
        self.process_label_line_2.setFrameShape(QFrame.Shape.NoFrame)
        self.process_label_line_2.setFrameShadow(QFrame.Shadow.Plain)
        self.process_label_line_2.setLineWidth(1)
        self.process_label_line_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_32.addWidget(self.process_label_line_2)

        self.process_label_line_3 = QLabel(self.process_frame)
        self.process_label_line_3.setObjectName(u"process_label_line_3")
        self.process_label_line_3.setMinimumSize(QSize(0, 30))
        self.process_label_line_3.setMaximumSize(QSize(16777215, 30))
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
        self.numberTablets_title_groupBox_2 = QGroupBox(self.frame_4)
        self.numberTablets_title_groupBox_2.setObjectName(u"numberTablets_title_groupBox_2")
        self.numberTablets_title_groupBox_2.setMinimumSize(QSize(0, 70))
        self.numberTablets_title_groupBox_2.setMaximumSize(QSize(16777215, 70))
        self.horizontalLayout_60 = QHBoxLayout(self.numberTablets_title_groupBox_2)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(9, 0, 9, 0)
        self.numberTablets_input_title = QLabel(self.numberTablets_title_groupBox_2)
        self.numberTablets_input_title.setObjectName(u"numberTablets_input_title")
        self.numberTablets_input_title.setMinimumSize(QSize(0, 50))
        self.numberTablets_input_title.setMaximumSize(QSize(16777215, 50))
        self.numberTablets_input_title.setFont(font9)
        self.numberTablets_input_title.setStyleSheet(u"background-color: rgb(52, 157, 77);\n" "border-radius: 15px;")
        self.numberTablets_input_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_60.addWidget(self.numberTablets_input_title)

        self.verticalLayout_3.addWidget(self.numberTablets_title_groupBox_2)

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
        font13 = QFont()
        font13.setFamilies([u"Kanit"])
        font13.setPointSize(50)
        font13.setBold(True)
        self.val_input.setFont(font13)
        self.val_input.setStyleSheet(u"color: rgb(100, 100, 100);\n" "border: none;")
        self.val_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_38.addWidget(self.val_input)

        self.verticalLayout_3.addWidget(self.frame_9)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 250))
        self.frame_5.setMaximumSize(QSize(16777215, 250))
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
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
        # endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
        # endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
        # endif
        self.frame_6.setPalette(palette)
        self.frame_6.setStyleSheet(
            u"QPushButton {\n"
            "	width: 90px;\n"
            "	height: 70px;\n"
            "	background-color: rgb(50, 50, 50);\n"
            "	border-radius: 5px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    font-size: 40px;\n"
            "	background-color: rgb(100, 100, 100);\n"
            "}"
        )
        self.frame_6.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_6.setLineWidth(3)
        self.gridLayout = QGridLayout(self.frame_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.key_1 = QPushButton(self.frame_6)
        self.key_1.setObjectName(u"key_1")
        font14 = QFont()
        font14.setFamilies([u"Kanit"])
        font14.setPointSize(20)
        font14.setWeight(QFont.Medium)
        self.key_1.setFont(font14)

        self.gridLayout.addWidget(self.key_1, 0, 0, 1, 1)

        self.key_2 = QPushButton(self.frame_6)
        self.key_2.setObjectName(u"key_2")
        self.key_2.setFont(font14)

        self.gridLayout.addWidget(self.key_2, 0, 1, 1, 1)

        self.key_3 = QPushButton(self.frame_6)
        self.key_3.setObjectName(u"key_3")
        self.key_3.setFont(font14)

        self.gridLayout.addWidget(self.key_3, 0, 2, 1, 1)

        self.key_4 = QPushButton(self.frame_6)
        self.key_4.setObjectName(u"key_4")
        self.key_4.setFont(font14)

        self.gridLayout.addWidget(self.key_4, 1, 0, 1, 1)

        self.key_5 = QPushButton(self.frame_6)
        self.key_5.setObjectName(u"key_5")
        self.key_5.setFont(font14)

        self.gridLayout.addWidget(self.key_5, 1, 1, 1, 1)

        self.key_6 = QPushButton(self.frame_6)
        self.key_6.setObjectName(u"key_6")
        self.key_6.setFont(font14)

        self.gridLayout.addWidget(self.key_6, 1, 2, 1, 1)

        self.key_7 = QPushButton(self.frame_6)
        self.key_7.setObjectName(u"key_7")
        self.key_7.setFont(font14)

        self.gridLayout.addWidget(self.key_7, 2, 0, 1, 1)

        self.key_8 = QPushButton(self.frame_6)
        self.key_8.setObjectName(u"key_8")
        self.key_8.setFont(font14)

        self.gridLayout.addWidget(self.key_8, 2, 1, 1, 1)

        self.key_9 = QPushButton(self.frame_6)
        self.key_9.setObjectName(u"key_9")
        self.key_9.setFont(font14)

        self.gridLayout.addWidget(self.key_9, 2, 2, 1, 1)

        self.key_backslash = QPushButton(self.frame_6)
        self.key_backslash.setObjectName(u"key_backslash")
        self.key_backslash.setMinimumSize(QSize(0, 0))
        self.key_backslash.setMaximumSize(QSize(16777215, 150))
        self.key_backslash.setFont(font14)

        self.gridLayout.addWidget(self.key_backslash, 3, 0, 1, 1)

        self.key_0 = QPushButton(self.frame_6)
        self.key_0.setObjectName(u"key_0")
        self.key_0.setMinimumSize(QSize(0, 0))
        self.key_0.setMaximumSize(QSize(16777215, 150))
        self.key_0.setFont(font14)

        self.gridLayout.addWidget(self.key_0, 3, 1, 1, 1)

        self.key_backspace = QPushButton(self.frame_6)
        self.key_backspace.setObjectName(u"key_backspace")
        self.key_backspace.setMinimumSize(QSize(0, 0))
        self.key_backspace.setMaximumSize(QSize(16777215, 150))
        font15 = QFont()
        font15.setPointSize(20)
        self.key_backspace.setFont(font15)
        icon6 = QIcon()
        icon6.addFile(u":/assets/keyboard/backspace.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.key_backspace.setIcon(icon6)
        self.key_backspace.setIconSize(QSize(30, 30))

        self.gridLayout.addWidget(self.key_backspace, 3, 2, 1, 1)

        self.horizontalLayout_63.addWidget(self.frame_6)

        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"QPushButton {\n" "	background-color: rgb(50, 50, 50);\n" "	border-radius: 5px;\n" "}\n" "QPushButton:pressed {\n" "	background-color: rgb(100, 100, 100);\n" "}")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_8)
        self.verticalLayout_36.setSpacing(6)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.numberTablets_img = QLabel(self.frame_8)
        self.numberTablets_img.setObjectName(u"numberTablets_img")
        self.numberTablets_img.setPixmap(QPixmap(u":/assets/icon/characteristics.png"))
        self.numberTablets_img.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_36.addWidget(self.numberTablets_img)

        self.key_enter = QPushButton(self.frame_8)
        self.key_enter.setObjectName(u"key_enter")
        self.key_enter.setMinimumSize(QSize(0, 52))
        font16 = QFont()
        font16.setFamilies([u"Kanit"])
        font16.setPointSize(20)
        font16.setWeight(QFont.Medium)
        font16.setItalic(False)
        self.key_enter.setFont(font16)
        self.key_enter.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/assets/keyboard/enter.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.key_enter.setIcon(icon7)
        self.key_enter.setIconSize(QSize(30, 30))

        self.verticalLayout_36.addWidget(self.key_enter)

        self.key_cancel = QPushButton(self.frame_8)
        self.key_cancel.setObjectName(u"key_cancel")
        self.key_cancel.setMinimumSize(QSize(0, 52))
        self.key_cancel.setFont(font16)
        icon8 = QIcon()
        icon8.addFile(u":/assets/keyboard/cancel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.key_cancel.setIcon(icon8)
        self.key_cancel.setIconSize(QSize(30, 30))

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
        self.setting_title.setStyleSheet(u"background-color: rgb(52, 157, 77);\n" "border-radius: 15px;")
        self.setting_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_18.addWidget(self.setting_title)

        self.verticalLayout_37.addWidget(self.setting_title_frame)

        self.weighingSettings_Frame = QFrame(self.setting_frame)
        self.weighingSettings_Frame.setObjectName(u"weighingSettings_Frame")
        self.weighingSettings_Frame.setStyleSheet(u"QLabel {\n" "	color: rgb(60, 60, 60);\n" "	border: none;\n" "	margin: 0;\n" "}")
        self.weighingSettings_Frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.weighingSettings_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.weighingSettings_Frame)
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.webcam_setting_monitor = QLabel(self.weighingSettings_Frame)
        self.webcam_setting_monitor.setObjectName(u"webcam_setting_monitor")
        self.webcam_setting_monitor.setMinimumSize(QSize(250, 0))
        self.webcam_setting_monitor.setMaximumSize(QSize(16777215, 16777215))
        self.webcam_setting_monitor.setStyleSheet(
            u"QLabel {\n" "	border: solid;\n" "	border-width: 2px;\n" "	border-color: rgb(111, 105, 37);\n" "	border-radius: 15px;\n" "	padding: 10px;\n" "	background-color: rgb(0, 0, 0);\n" "}\n" ""
        )
        self.webcam_setting_monitor.setPixmap(QPixmap(u":/assets/icon/picture_default.png"))
        self.webcam_setting_monitor.setScaledContents(True)

        self.horizontalLayout_14.addWidget(self.webcam_setting_monitor)

        self.set_widget = QWidget(self.weighingSettings_Frame)
        self.set_widget.setObjectName(u"set_widget")
        self.set_widget.setMinimumSize(QSize(300, 0))
        self.set_widget.setMaximumSize(QSize(300, 16777215))
        self.set_widget.setStyleSheet(u"QWidget {\n" "	background-color: rgb(220, 220, 220);\n" "	border-radius: 15px;\n" "}")
        self.verticalLayout_8 = QVBoxLayout(self.set_widget)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, -1, 9, -1)
        self.webcam_setting_view = QLabel(self.set_widget)
        self.webcam_setting_view.setObjectName(u"webcam_setting_view")
        self.webcam_setting_view.setMinimumSize(QSize(200, 200))
        self.webcam_setting_view.setMaximumSize(QSize(16777215, 200))
        self.webcam_setting_view.setStyleSheet(
            u"QLabel {\n"
            "	border: solid;\n"
            "	border-width: 2px;\n"
            "	border-color: rgb(111, 105, 37);\n"
            "	border-radius: 15px;\n"
            "	background-color: rgb(255, 255, 255);\n"
            "	padding: 10px;\n"
            "}\n"
            ""
        )
        self.webcam_setting_view.setPixmap(QPixmap(u":/assets/icon/picture_default.png"))
        self.webcam_setting_view.setScaledContents(True)

        self.verticalLayout_8.addWidget(self.webcam_setting_view)

        self.widget_7 = QWidget(self.set_widget)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMaximumSize(QSize(16777215, 150))
        self.gridLayout_2 = QGridLayout(self.widget_7)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.lot_set_label = QLabel(self.widget_7)
        self.lot_set_label.setObjectName(u"lot_set_label")
        self.lot_set_label.setMaximumSize(QSize(70, 16777215))
        self.lot_set_label.setFont(font)
        self.lot_set_label.setStyleSheet(u"color: rgb(61, 61, 61);")
        self.lot_set_label.setAlignment(Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lot_set_label, 0, 0, 1, 1)

        self.lot_set = QLabel(self.widget_7)
        self.lot_set.setObjectName(u"lot_set")
        self.lot_set.setFont(font)
        self.lot_set.setStyleSheet(u"color: rgb(61, 61, 61);\n" "border: solid;\n" "border-width: 1px;\n" "border-color: rgb(111, 105, 37);\n" "border-radius: 10px;")
        self.lot_set.setAlignment(Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lot_set, 0, 1, 1, 1)

        self.mfg_set_label = QLabel(self.widget_7)
        self.mfg_set_label.setObjectName(u"mfg_set_label")
        self.mfg_set_label.setMinimumSize(QSize(50, 0))
        self.mfg_set_label.setMaximumSize(QSize(70, 16777215))
        self.mfg_set_label.setFont(font)
        self.mfg_set_label.setStyleSheet(u"color: rgb(61, 61, 61);")
        self.mfg_set_label.setAlignment(Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.mfg_set_label, 1, 0, 1, 1)

        self.mfg_set = QLabel(self.widget_7)
        self.mfg_set.setObjectName(u"mfg_set")
        self.mfg_set.setFont(font)
        self.mfg_set.setStyleSheet(u"color: rgb(61, 61, 61);\n" "border: solid;\n" "border-width: 1px;\n" "border-color: rgb(111, 105, 37);\n" "border-radius: 10px;")
        self.mfg_set.setAlignment(Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.mfg_set, 1, 1, 1, 1)

        self.exp_set_label = QLabel(self.widget_7)
        self.exp_set_label.setObjectName(u"exp_set_label")
        self.exp_set_label.setMaximumSize(QSize(70, 16777215))
        self.exp_set_label.setFont(font)
        self.exp_set_label.setStyleSheet(u"color: rgb(61, 61, 61);")
        self.exp_set_label.setAlignment(Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.exp_set_label, 2, 0, 1, 1)

        self.exp_set = QLabel(self.widget_7)
        self.exp_set.setObjectName(u"exp_set")
        self.exp_set.setFont(font)
        self.exp_set.setStyleSheet(u"color: rgb(61, 61, 61);\n" "border: solid;\n" "border-width: 1px;\n" "border-color: rgb(111, 105, 37);\n" "border-radius: 10px;")
        self.exp_set.setAlignment(Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.exp_set, 2, 1, 1, 1)

        self.verticalLayout_8.addWidget(self.widget_7)

        self.widget_3 = QWidget(self.set_widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(16777215, 60))
        self.widget_3.setStyleSheet(
            u"QPushButton {\n" "	background-color: rgb(50, 50, 50);\n" "	border-radius: 10px;\n" "}\n" "QPushButton:pressed {\n" "	background-color: rgb(100, 100, 100);\n" "}\n" ""
        )
        self.horizontalLayout_5 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.capture_set = QPushButton(self.widget_3)
        self.capture_set.setObjectName(u"capture_set")
        self.capture_set.setMinimumSize(QSize(0, 45))
        self.capture_set.setFont(font10)
        self.capture_set.setStyleSheet(u"")
        self.capture_set.setIcon(icon2)
        self.capture_set.setIconSize(QSize(40, 40))

        self.horizontalLayout_5.addWidget(self.capture_set)

        self.save_set = QPushButton(self.widget_3)
        self.save_set.setObjectName(u"save_set")
        self.save_set.setMinimumSize(QSize(0, 45))
        self.save_set.setFont(font10)
        self.save_set.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u":/assets/icon/save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.save_set.setIcon(icon9)
        self.save_set.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.save_set)

        self.verticalLayout_8.addWidget(self.widget_3)

        self.horizontalLayout_14.addWidget(self.set_widget)

        self.verticalLayout_37.addWidget(self.weighingSettings_Frame)

        self.verticalLayout_11.addWidget(self.setting_frame)

        self.stackedWidget.addWidget(self.lme_settings_page)
        self.camera_setting_page = QWidget()
        self.camera_setting_page.setObjectName(u"camera_setting_page")
        self.verticalLayout_7 = QVBoxLayout(self.camera_setting_page)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.camera_setting_frame = QFrame(self.camera_setting_page)
        self.camera_setting_frame.setObjectName(u"camera_setting_frame")
        self.camera_setting_frame.setMinimumSize(QSize(0, 70))
        self.camera_setting_frame.setMaximumSize(QSize(16777215, 70))
        self.camera_setting_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.camera_setting_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.camera_setting_frame)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.camera_setting_title = QLabel(self.camera_setting_frame)
        self.camera_setting_title.setObjectName(u"camera_setting_title")
        self.camera_setting_title.setMinimumSize(QSize(0, 50))
        self.camera_setting_title.setMaximumSize(QSize(16777215, 50))
        self.camera_setting_title.setFont(font9)
        self.camera_setting_title.setStyleSheet(u"background-color: rgb(52, 157, 77);\n" "border-radius: 15px;")
        self.camera_setting_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_29.addWidget(self.camera_setting_title)

        self.verticalLayout_7.addWidget(self.camera_setting_frame)

        self.camera_settings_Frame_2 = QFrame(self.camera_setting_page)
        self.camera_settings_Frame_2.setObjectName(u"camera_settings_Frame_2")
        self.camera_settings_Frame_2.setStyleSheet(u"QLabel {\n" "	color: rgb(60, 60, 60);\n" "	border: none;\n" "	margin: 0;\n" "}")
        self.camera_settings_Frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.camera_settings_Frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.camera_settings_Frame_2)
        self.horizontalLayout_30.setSpacing(10)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.camera_setting_monitor = QLabel(self.camera_settings_Frame_2)
        self.camera_setting_monitor.setObjectName(u"camera_setting_monitor")
        self.camera_setting_monitor.setMinimumSize(QSize(250, 0))
        self.camera_setting_monitor.setMaximumSize(QSize(16777215, 16777215))
        self.camera_setting_monitor.setStyleSheet(
            u"QLabel {\n" "	border: solid;\n" "	border-width: 2px;\n" "	border-color: rgb(111, 105, 37);\n" "	border-radius: 15px;\n" "	padding: 10px;\n" "	background-color: rgb(0, 0, 0);\n" "}\n" ""
        )
        self.camera_setting_monitor.setPixmap(QPixmap(u":/assets/icon/picture_default.png"))
        self.camera_setting_monitor.setScaledContents(True)

        self.horizontalLayout_30.addWidget(self.camera_setting_monitor)

        self.camera_setting_widget = QWidget(self.camera_settings_Frame_2)
        self.camera_setting_widget.setObjectName(u"camera_setting_widget")
        self.camera_setting_widget.setMinimumSize(QSize(350, 0))
        self.camera_setting_widget.setMaximumSize(QSize(400, 16777215))
        self.camera_setting_widget.setStyleSheet(u"QWidget {\n" "	background-color: rgb(220, 220, 220);\n" "	border-radius: 15px;\n" "}")
        self.verticalLayout_13 = QVBoxLayout(self.camera_setting_widget)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(12, 12, 12, 12)
        self.cameraZoomWidget = QWidget(self.camera_setting_widget)
        self.cameraZoomWidget.setObjectName(u"cameraZoomWidget")
        self.horizontalLayout_31 = QHBoxLayout(self.cameraZoomWidget)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.cameraZoomLabel = QLabel(self.cameraZoomWidget)
        self.cameraZoomLabel.setObjectName(u"cameraZoomLabel")
        self.cameraZoomLabel.setFont(font12)

        self.horizontalLayout_31.addWidget(self.cameraZoomLabel)

        self.cameraZoom = QSlider(self.cameraZoomWidget)
        self.cameraZoom.setObjectName(u"cameraZoom")
        self.cameraZoom.setMinimum(100)
        self.cameraZoom.setMaximum(500)
        self.cameraZoom.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_31.addWidget(self.cameraZoom)

        self.verticalLayout_13.addWidget(self.cameraZoomWidget)

        self.focusWidget = QWidget(self.camera_setting_widget)
        self.focusWidget.setObjectName(u"focusWidget")
        self.horizontalLayout_32 = QHBoxLayout(self.focusWidget)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.cameraFocusLabel = QLabel(self.focusWidget)
        self.cameraFocusLabel.setObjectName(u"cameraFocusLabel")
        self.cameraFocusLabel.setFont(font12)

        self.horizontalLayout_32.addWidget(self.cameraFocusLabel)

        self.cameraFocus = QSlider(self.focusWidget)
        self.cameraFocus.setObjectName(u"cameraFocus")
        self.cameraFocus.setMinimum(0)
        self.cameraFocus.setMaximum(255)
        self.cameraFocus.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_32.addWidget(self.cameraFocus)

        self.verticalLayout_13.addWidget(self.focusWidget)

        self.cameraAutoFocus = QPushButton(self.camera_setting_widget)
        self.cameraAutoFocus.setObjectName(u"cameraAutoFocus")
        self.cameraAutoFocus.setFont(font12)
        self.cameraAutoFocus.setStyleSheet(
            u"QPushButton {\n"
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
            "}"
        )
        self.cameraAutoFocus.setCheckable(True)
        self.cameraAutoFocus.setChecked(False)

        self.verticalLayout_13.addWidget(self.cameraAutoFocus)

        self.brightnessWidget = QWidget(self.camera_setting_widget)
        self.brightnessWidget.setObjectName(u"brightnessWidget")
        self.horizontalLayout_33 = QHBoxLayout(self.brightnessWidget)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.cameraBrightnessLabel = QLabel(self.brightnessWidget)
        self.cameraBrightnessLabel.setObjectName(u"cameraBrightnessLabel")
        self.cameraBrightnessLabel.setFont(font12)

        self.horizontalLayout_33.addWidget(self.cameraBrightnessLabel)

        self.cameraBrightness = QSlider(self.brightnessWidget)
        self.cameraBrightness.setObjectName(u"cameraBrightness")
        self.cameraBrightness.setMaximum(255)
        self.cameraBrightness.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_33.addWidget(self.cameraBrightness)

        self.verticalLayout_13.addWidget(self.brightnessWidget)

        self.contrastWidget = QWidget(self.camera_setting_widget)
        self.contrastWidget.setObjectName(u"contrastWidget")
        self.horizontalLayout_34 = QHBoxLayout(self.contrastWidget)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.cameraContrastLabel = QLabel(self.contrastWidget)
        self.cameraContrastLabel.setObjectName(u"cameraContrastLabel")
        self.cameraContrastLabel.setFont(font12)

        self.horizontalLayout_34.addWidget(self.cameraContrastLabel)

        self.cameraContrast = QSlider(self.contrastWidget)
        self.cameraContrast.setObjectName(u"cameraContrast")
        self.cameraContrast.setMaximum(255)
        self.cameraContrast.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_34.addWidget(self.cameraContrast)

        self.verticalLayout_13.addWidget(self.contrastWidget)

        self.exposureWidget = QWidget(self.camera_setting_widget)
        self.exposureWidget.setObjectName(u"exposureWidget")
        self.horizontalLayout_35 = QHBoxLayout(self.exposureWidget)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.cameraExposureLabel = QLabel(self.exposureWidget)
        self.cameraExposureLabel.setObjectName(u"cameraExposureLabel")
        self.cameraExposureLabel.setFont(font12)

        self.horizontalLayout_35.addWidget(self.cameraExposureLabel)

        self.cameraExposure = QSlider(self.exposureWidget)
        self.cameraExposure.setObjectName(u"cameraExposure")
        self.cameraExposure.setMaximum(255)
        self.cameraExposure.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_35.addWidget(self.cameraExposure)

        self.verticalLayout_13.addWidget(self.exposureWidget)

        self.sensorDelayWidget = QWidget(self.camera_setting_widget)
        self.sensorDelayWidget.setObjectName(u"sensorDelayWidget")
        self.horizontalLayout_36 = QHBoxLayout(self.sensorDelayWidget)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.sensorDelayLabel = QLabel(self.sensorDelayWidget)
        self.sensorDelayLabel.setObjectName(u"sensorDelayLabel")
        self.sensorDelayLabel.setFont(font12)

        self.horizontalLayout_36.addWidget(self.sensorDelayLabel)

        self.sensorDelay = QSlider(self.sensorDelayWidget)
        self.sensorDelay.setObjectName(u"sensorDelay")
        self.sensorDelay.setMaximum(3000)
        self.sensorDelay.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_36.addWidget(self.sensorDelay)

        self.verticalLayout_13.addWidget(self.sensorDelayWidget)

        self.save_camera_setting = QPushButton(self.camera_setting_widget)
        self.save_camera_setting.setObjectName(u"save_camera_setting")
        self.save_camera_setting.setMinimumSize(QSize(0, 45))
        self.save_camera_setting.setFont(font16)
        self.save_camera_setting.setStyleSheet(
            u"QPushButton {\n" "	background-color: rgb(50, 50, 50);\n" "	border-radius: 10px;\n" "}\n" "QPushButton:pressed {\n" "	background-color: rgb(100, 100, 100);\n" "}\n" ""
        )
        self.save_camera_setting.setIcon(icon9)
        self.save_camera_setting.setIconSize(QSize(30, 30))

        self.verticalLayout_13.addWidget(self.save_camera_setting)

        self.horizontalLayout_30.addWidget(self.camera_setting_widget)

        self.verticalLayout_7.addWidget(self.camera_settings_Frame_2)

        self.stackedWidget.addWidget(self.camera_setting_page)

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

        self.stackedWidget.setCurrentIndex(4)

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
        self.profile_img2.setText("")
        self.home_2.setText("")
        self.setting_2.setText("")
        self.camera_setting_2.setText("")
        self.restart_program_2.setText("")
        self.menu.setText("")
        self.title.setText(
            QCoreApplication.translate("MainWindow", u"\u0e23\u0e30\u0e1a\u0e1a\u0e15\u0e23\u0e27\u0e08\u0e2a\u0e2d\u0e1a\u0e01\u0e32\u0e23\u0e1e\u0e34\u0e21\u0e1e\u0e4c LOT,MFG,EXP", None)
        )
        self.wifi_signal.setText("")
        self.time_bar.setText(QCoreApplication.translate("MainWindow", u"HH:MM:SS", None))
        self.date_bar.setText(QCoreApplication.translate("MainWindow", u"DD/MM/YYYY", None))
        self.detection_alert.setText(QCoreApplication.translate("MainWindow", u"\u0e01\u0e33\u0e25\u0e31\u0e07\u0e23\u0e2d\u0e0a\u0e34\u0e49\u0e19\u0e07\u0e32\u0e19", None))
        self.webcam_monitor.setText("")
        self.detection_view.setText("")
        self.lot_label.setText(QCoreApplication.translate("MainWindow", u"LOT.", None))
        self.lot_detected.setText(QCoreApplication.translate("MainWindow", u"XXXXXX", None))
        self.mfg_label.setText(QCoreApplication.translate("MainWindow", u"MFG.", None))
        self.mfg_detected.setText(QCoreApplication.translate("MainWindow", u"XXXXXX", None))
        self.exp_label.setText(QCoreApplication.translate("MainWindow", u"EXP.", None))
        self.exp_detected.setText(QCoreApplication.translate("MainWindow", u"XXXXXX", None))
        self.capture_test.setText(QCoreApplication.translate("MainWindow", u" \u0e16\u0e48\u0e32\u0e22\u0e20\u0e32\u0e1e", None))
        self.start.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.process_img.setText("")
        self.process_label_line_1.setText(QCoreApplication.translate("MainWindow", u"PRINTING  INSPECTION SYSTEM", None))
        self.process_label_line_2.setText(QCoreApplication.translate("MainWindow", u"Created by Nattapon pondonko", None))
        self.process_label_line_3.setText(QCoreApplication.translate("MainWindow", u"Engineering Department", None))
        self.process_label_line_4.setText("")
        self.numberTablets_input_title.setText(QCoreApplication.translate("MainWindow", u"\u0e15\u0e31\u0e49\u0e07\u0e04\u0e48\u0e32 LOT, MFG, EXP", None))
        self.val_input.setText(QCoreApplication.translate("MainWindow", u"XXXX", None))
        self.key_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.key_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.key_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.key_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.key_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.key_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.key_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.key_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.key_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.key_backslash.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.key_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.key_backspace.setText("")
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
        self.capture_set.setText(QCoreApplication.translate("MainWindow", u" \u0e16\u0e48\u0e32\u0e22\u0e20\u0e32\u0e1e", None))
        self.save_set.setText(QCoreApplication.translate("MainWindow", u" \u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01", None))
        self.camera_setting_title.setText(
            QCoreApplication.translate(
                "MainWindow", u"\u0e15\u0e31\u0e49\u0e07\u0e04\u0e48\u0e32\u0e01\u0e25\u0e49\u0e2d\u0e07\u0e41\u0e25\u0e30\u0e40\u0e0b\u0e47\u0e19\u0e40\u0e0b\u0e2d\u0e23\u0e4c", None
            )
        )
        self.camera_setting_monitor.setText("")
        self.cameraZoomLabel.setText(QCoreApplication.translate("MainWindow", u"ZOOM", None))
        self.cameraFocusLabel.setText(QCoreApplication.translate("MainWindow", u"FOCUS", None))
        self.cameraAutoFocus.setText(QCoreApplication.translate("MainWindow", u"AUTO FOCUS", None))
        self.cameraBrightnessLabel.setText(QCoreApplication.translate("MainWindow", u"BRIGHTNESS", None))
        self.cameraContrastLabel.setText(QCoreApplication.translate("MainWindow", u"CONTRAST", None))
        self.cameraExposureLabel.setText(QCoreApplication.translate("MainWindow", u"EXPOSURE", None))
        self.sensorDelayLabel.setText(QCoreApplication.translate("MainWindow", u"SENSOR DELAY", None))
        self.save_camera_setting.setText(QCoreApplication.translate("MainWindow", u" \u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01", None))

    # retranslateUi
