import QtQuick 6.0
import QtQuick.Window 6.0
import QtQuick.Controls 6.0


Row {

    property alias video_width: width_input.input
    property alias video_height: height_input.input
    property alias video_fps: fps_input.input

    anchors.top: parent.top
    anchors.left: parent.left
    anchors.margins: 20
    spacing: 20

    CustomInput {
        id: width_input
        text: qsTr("Width")
        Component.onCompleted: input = backend.video_width
        onChanged:  backend.video_width = input
    }
    CustomInput {
        id: height_input
        text: qsTr("Height")
        Component.onCompleted: input = backend.video_height
        onChanged:  backend.video_height = input
    }
    CustomInput {
        id: fps_input
        text: qsTr("FPS")
        Component.onCompleted: input = backend.video_fps
        onChanged:  backend.video_fps = input
        
    
    }

}
