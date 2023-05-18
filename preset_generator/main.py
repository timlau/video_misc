#!/usr/bin/python3

import os
import sys
from turtle import width
from typing import Protocol

from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtCore import QtMsgType, qInstallMessageHandler

from ui.backend import Backend


def qt_message_handler(mode, context, message):
    if mode == QtMsgType.QtInfoMsg:
        mode = "Info"
    elif mode == QtMsgType.QtWarningMsg:
        mode = "Warning"
    elif mode == QtMsgType.QtCriticalMsg:
        mode = "critical"
    elif mode == QtMsgType.QtFatalMsg:
        mode = "fatal"
    else:
        mode = "Debug"
    print(f"{mode}: {message}")


if __name__ == "__main__":
    qInstallMessageHandler(qt_message_handler)
    # directory where this file is located
    workdir = os.path.dirname(os.path.abspath(__file__))

    # Define our backend object, which we pass to QML.
    backend = Backend()

    # Qt application setup
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)

    # register backend to QML engine
    engine.rootContext().setContextProperty("backend", backend)

    engine.load(os.path.join(workdir, "qml/main.qml"))

    if not engine.rootObjects():
        sys.exit(-1)

    # reefresh the UI based on default preset
    backend.refresh.emit(backend.data.preset)
    # run the application
    sys.exit(app.exec())
