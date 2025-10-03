import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.VirtualKeyboard 2.15

Rectangle {
    width: 600
    height: 400
    color: "#eeeeee"

    property TextField activeField: null   // ช่องที่ถูกเลือก
    
    Column {
        anchors.fill: parent
        spacing: 10
        padding: 10

        TextField {
            id: mainInput1
            width: parent.width
            height: 40
            font.pixelSize: 18
            placeholderText: "แตะเพื่อพิมพ์ที่นี่..."
            onActiveFocusChanged: if (activeFocus) activeField = this

            onAccepted: {
                Qt.inputMethod.hide()
                focus = false
            }
        }

        TextField {
            id: mainInput2
            width: parent.width
            height: 40
            font.pixelSize: 18
            placeholderText: "อีกช่องหนึ่ง..."
            onActiveFocusChanged: if (activeFocus) activeField = this

            onAccepted: {
                Qt.inputMethod.hide()
                focus = false
            }
        }

        Rectangle {
            width: parent.width
            height: 200
            color: "#cccccc"
            radius: 10

            Text {
                anchors.centerIn: parent
                text: "Main Content Area"
            }
        }
    }

    // ===== Virtual Keyboard =====
    InputPanel {
        id: inputPanel
        z: 10
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        visible: Qt.inputMethod.visible

        y: visible ? parent.height - height : parent.height
        Behavior on y { NumberAnimation { duration: 250; easing.type: Easing.InOutQuad } }

        // ===== Overlay ด้านบน keyboard =====
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
                color: "#222222"
                placeholderText: "พิมพ์ข้อความ..."
                
                // sync ข้อความกับ activeField
                text: activeField ? activeField.text : ""
                onTextChanged: if (activeField && activeField.text !== text) activeField.text = text

                // Enter → เคลียร์เฉพาะ overlayInput + ซ่อน keyboard
                onAccepted: {
                    text = ""              // เคลียร์แค่ mainInput2
                    Qt.inputMethod.hide()
                    if (activeField) activeField.focus = false
                }
            }
        }
    }
}
