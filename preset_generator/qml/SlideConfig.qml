import QtQuick 6.0
import QtQuick.Window 6.0
import QtQuick.Controls 6.0


Row {

    anchors.top: parent.top
    anchors.left: parent.left
    anchors.margins: 20
    spacing: 20

    CustomInput {
        id: size_input
        text: qsTr("Size")
        Component.onCompleted: input = backend.slide_size
        onChanged:  backend.alide_size = input
    }
    CustomInput {
        id: duration_input
        text: qsTr("Duration")
        Component.onCompleted: input = backend.slide_duration
        onChanged:  backend.slide_duration = input
    }

}
