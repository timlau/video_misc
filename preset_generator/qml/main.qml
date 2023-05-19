import QtQuick 6.0
import QtQuick.Controls.Fusion
import QtQuick.Layouts 6.0


ApplicationWindow {
    id: window
    width: 700
    height: 600
    visible: true
    title: qsTr("Shotcut Preset Generator")

    flags: Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint | Qt.CustomizeWindowHint | Qt.Dialog | Qt.WindowTitleHint


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


        Timer {
            id: timer_message
            interval: 5000
        }

        Rectangle {
            id: message
            width: 400
            height: 50
            anchors.centerIn: parent                
            color: "#ff0000"
            radius: 20
            property alias text: label.text
            opacity: timer_message.running ? 1.0 : 0.0
            Behavior on opacity { PropertyAnimation { duration: 1000 } }

            Label {
                id: label
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.verticalCenter: parent.verticalCenter
                color: "#ffffff"
            }
        }
        

        PresetType {
            id: preset
            anchors.top: parent.top
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

        function onMessage(msg) {
            message.text = msg
            timer_message.stop()
            timer_message.start()
        }
   }
}


/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
##^##*/
