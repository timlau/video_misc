import QtQuick
import QtQuick.Controls.Fusion
import QtQuick.Layouts


RowLayout {
    id: output_dir
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.leftMargin: 20
    anchors.rightMargin: 35
    anchors.topMargin: 20
    spacing: 20

    signal changed(string text)


    Label {
        id: label
        text: qsTr("Output")
        anchors.leftMargin: 10
        width: 55

    }

    TextField {
        id: field
        Layout.fillWidth: true
        Component.onCompleted: text = backend.output_dir
        onTextEdited: backend.output_dir = text

    }

}