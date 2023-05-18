import QtQuick 6.0
import QtQuick.Controls 6.0

Row {
    id: input
    spacing: 20

    property alias text: label.text
    property alias input: field.text
    signal changed(string text)

    Label {
        id: label
        anchors.verticalCenter: parent.verticalCenter
        anchors.leftMargin: 10
        width: 55
        
    }
    TextField {
        id: field
        anchors.verticalCenter: parent.verticalCenter
        anchors.leftMargin: 10
        onTextEdited: input.changed(text)

    }
}