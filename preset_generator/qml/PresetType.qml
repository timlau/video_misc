import QtQuick 6.0
import QtQuick.Controls 6.0


Item {

    // property alias selected: row_input.input
    id: preset_type
    anchors.top: parent.top
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.margins: 20
    height: 30
    

    ComboBox {
        id: preset_combo
        implicitWidth: 400
        implicitHeight: 35
        anchors.horizontalCenter: preset_type.horizontalCenter
        textRole: "key"
        valueRole: "value"
        Component.onCompleted: currentIndex = indexOfValue(backend.preset)
        model: ListModel {
            ListElement { key: "Crop Rectangle: Grid"; value: "grid" }
            ListElement { key: "Crop Rectangle: Corner Slide"; value: "slide" }
        }

        onActivated:  backend.preset = currentValue
    
    }    


}
