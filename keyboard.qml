// keyboard.qml (แก้ไขแล้ว)

import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.VirtualKeyboard 2.15

Rectangle {
    id: root
    width: parent ? parent.width : 1024
    height: parent ? parent.height / 2 : 300
    color: "transparent"

    signal reqHideKeyboard()
    property var activeField: null

    opacity: activeField !== null ? 1 : 0
    enabled: activeField !== null

    // 👇 MouseArea ครอบทั้งพื้นที่เพื่อตรวจจับ "outside click"
    MouseArea {
        anchors.fill: parent
        propagateComposedEvents: true  // ให้ event ผ่านไปยัง child ได้

        onClicked: {
            // ถ้าคลิกไม่ได้เกิดบน overlayInput หรือ InputPanel → ถือว่า "outside"
            // แต่เราไม่สามารถเช็คตรงๆ ได้ใน QML ง่ายๆ → ใช้ trick: ถ้า focus ไม่ได้อยู่ที่ overlayInput
            // หรือใช้ flag ว่าคลิกเกิดที่ child หรือไม่ → วิธีง่ายกว่า: ใช้ preventStealing + onReleased

            // ✅ วิธีที่เชื่อถือได้: ถ้า activeField ยังมีอยู่ และคลิกที่พื้นหลัง → ซ่อน
            if (root.activeField) {
                root.reqHideKeyboard()
            }
        }

        // 👇 ป้องกันไม่ให้ MouseArea ขโมย event จาก child (เช่น TextField)
        onPressed: (mouse) => {
            mouse.accepted = true
        }
    }

    InputPanel {
        id: inputPanel
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        visible: activeField !== null

        y: visible ? parent.height - height : parent.height
        Behavior on y { NumberAnimation { duration: 250; easing.type: Easing.InOutQuad } }

        Rectangle {
            width: parent.width
            height: 70
            color: "#222222"
            anchors.bottom: inputPanel.top

            TextField {
                id: overlayInput
                anchors.fill: parent
                anchors.margins: 10
                font.pixelSize: 25
                color: "#222222"
                placeholderText: "ป้อนข้อมูล..."
                readOnly: false

                onTextChanged: {
                    if (root.activeField) {
                        root.activeField.setText(text)
                    }
                }

                Keys.onReturnPressed: {
                    root.reqHideKeyboard()
                }
            }
        }
    }

    // กำหนด field ที่จะทำการใช้งาน keyboard
    function setActiveField(field) {
        activeField = field
        if (field) {
            overlayInput.text = field.text
            overlayInput.inputMethodHints = field.inputMethodHints
            root.opacity = 1
            root.enabled = true
            overlayInput.forceActiveFocus()
        }
    }

    // function hideKeyboard() {
    //     activeField = null
    //     overlayInput.text = ""
    //     root.opacity = 0
    //     root.enabled = false
    // }
}