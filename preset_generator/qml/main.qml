import QtQuick 6.0
import QtQuick.Window 6.0
import QtQuick.Controls 6.0
import QtQuick.Controls.Material 6.0

ApplicationWindow {
    id: window
    width: 700
    height: 600
    visible: true
    title: qsTr("Shotcut Preset Generator")

    flags: Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint | Qt.CustomizeWindowHint | Qt.Dialog | Qt.WindowTitleHint

    Material.theme: Material.Dark
    Material.accent: Material.Purple

    Rectangle {
        id: content
        height: 40
        color: "#000000"

        anchors {
            left: parent.left
            right: parent.right
            top: parent.top
            bottom: parent.bottom
            margins: 10
        }
        radius: 10

        PresetType {
            id: preset
        }

        VideoMode {
            id: video_mode
            anchors.top: preset.bottom
        }

        GridSize {
            id:grid_size
            anchors.top: video_mode.bottom
        }

        SlideConfig {
            id: slide
            anchors.top: grid_size.bottom
        }

        OutputDirectory {
            id: output
            anchors.bottom: button.top
            anchors.margins: 20

        }

        Row {
            id: button
            anchors.bottom: parent.bottom
            anchors.bottomMargin: 10
            anchors.horizontalCenter : parent.horizontalCenter 
            spacing: 30
            Button {
                text: "Genrate"
                onClicked: backend.generate()
            }
        }



    }

    Connections {
        target: backend

        property string preset
        property string output_dir
        property string video_width
        property string video_height
        property string video_fps
        property string grid_rows
        property string grid_cols
        property string grid_pad
        property string slide_size
        property string slide_duration


        function onRefresh(active) {
            console.info("Refresh: "+active)
            if(active == "slide") {
                slide.visible = true
            } else {
                slide.visible = false
            }
        }
   }
}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
##^##*/
