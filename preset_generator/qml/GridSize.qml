import QtQuick
import QtQuick.Controls.Fusion


Row {

    property alias grid_rows: row_input.input
    property alias grid_cols: col_input.input
    property alias grid_pad : pad_input.input

    anchors.top: parent.top
    anchors.left: parent.left
    anchors.margins: 20
    spacing: 20

    CustomInput {
        id: row_input
        text: qsTr("Rows")
        Component.onCompleted: input = backend.grid_rows
        onChanged:  backend.grid_rows = input

    }

    CustomInput {
        id: col_input
        text: qsTr("Columns")
        Component.onCompleted: input = backend.grid_cols
        onChanged:  backend.grid_cols = input
    }

    CustomInput {
        id: pad_input
        text: qsTr("Padding")
        Component.onCompleted: input = backend.grid_pad
        onChanged:  backend.grid_pad = input
        
    
    }

}
