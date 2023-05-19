import QtQuick
import QtQuick.Controls.Fusion
import QtQuick.Layouts



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
