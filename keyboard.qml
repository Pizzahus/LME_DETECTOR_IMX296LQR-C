import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.VirtualKeyboard 2.15

Rectangle {
    id: root
    width: parent ? parent.width : 1024
    height: parent ? parent.height / 2 : 300
    color: "transparent"

    // ช่อง input ปัจจุบันที่ sync จาก Python
    property var activeField: null

    InputPanel {
        id: inputPanel
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        visible: Qt.inputMethod.visible

        y: visible ? parent.height - height : parent.height
        Behavior on y { NumberAnimation { duration: 250; easing.type: Easing.InOutQuad } }

        Rectangle {
            width: parent.width
            height: 50
            color: "#222222"
            anchors.bottom: inputPanel.top

            TextField {
                id: overlayInput
                anchors.fill: parent
                anchors.margins: 5
                font.pixelSize: 20
                color: "white"
                placeholderText: "พิมพ์ข้อความ..."

                // sync กลับไปที่ activeField
                onTextChanged: if (root.activeField && root.activeField.text != text)
                                   root.activeField.text = text

                onAccepted: {
                    text = ""
                    Qt.inputMethod.hide()
                    if (root.activeField) root.activeField.focus = false
                }
            }
        }
    }

    // ฟังก์ชันเรียกจาก Python
    function setActiveField(field) {
        activeField = field
        if (field) {
            overlayInput.text = field.text
            overlayInput.forceActiveFocus()
        }
    }
}
