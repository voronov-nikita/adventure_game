// 
// По какой-то причине встроенные уведомления не работали, 
// поэтому было принято решения написать модуль собственного вида.
// Принцип остается такой же, за исключением того, что теперь необходимо импортировать блок AlertBox
// 

import { View, TouchableOpacity, Text, StyleSheet } from "react-native";

// Компонент для отображения уведомлений
export const AlertBox = ({ message, onDismiss }) => {
    if (!message) return null;

    return (
        <View style={styles.alertBox}>
            <Text style={styles.alertText}>{message}</Text>
            <TouchableOpacity onPress={onDismiss}>
                <Text style={styles.alertDismiss}>Закрыть</Text>
            </TouchableOpacity>
        </View>
    );
};

const styles = StyleSheet.create({
    alertBox: {
        position: 'absolute',
        top: 0,
        width: '100%',
        backgroundColor: 'red',
        padding: 10,
        zIndex: 1,
    },
    alertText: {
        color: 'white',
        textAlign: 'center',
        fontSize: 16,
    },
    alertDismiss: {
        color: 'yellow',
        textAlign: 'center',
        fontSize: 14,
        marginTop: 5,
    }
})