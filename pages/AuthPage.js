//
// Страница авторизации пользователей
//

import React, { useState } from 'react';
import { View, Text, SafeAreaView, StyleSheet, TextInput, TouchableOpacity, Dimensions } from 'react-native';
import { MaterialCommunityIcons } from '@expo/vector-icons';

// импорт констант из файла с конфигурациями
import { URL } from '../config';

// Экспортируемый экран авторизации
export const AuthScreen = ({ navigation }) => {

    const { width } = Dimensions.get('window');
    // сделаем так, что если ширина экрана меньше 400, то ширину блока будем делать 85%, иначе 34%
    const mainBlockWidth = width < 400 ? '85%' : '34%';

    // переменные состояний
    // message - переменная текста над полями авторизации
    const [message, setMessage] = useState('ВВЕДИТЕ ЛОГИН И ПАРОЛЬ');
    // login - переменная логина пользователя (по умолчанию отсутствует)
    const [login, setLogin] = useState('');
    // password - переменная пароля пользователя (по умолчанию отсутствует)
    const [password, setPassword] = useState('');
    // showChangePassword - переменная для отображения кнопки смены пароля
    const [showPassword, setShowPassword] = useState(false);

    // функция отправки данных на сервер для АВТОРИЗАЦИИ пользователей
    const sendDataToServerAuth = async () => {
        if (login != '' && password != '') {
            try {
                const response = await fetch(URL, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    // тело POST запроса
                    body: JSON.stringify({
                        login,
                        password,
                    }),
                });
                // Ждем ответа от сервера
                const data = await response.json();

                // Обработка ответа
                const { access, refresh } = data;

                // Сохранение access token в sessionStorage
                sessionStorage.setItem('accessToken', access);

                console.log('Access token сохранён:', access);
                console.log('Refresh token получен и хранится в куках автоматически');

                navigation.navigate("Home");

            } catch (error) {
                console.error('Ошибка при авторизации:', error);
            }
        } else {
            console.error('Ошибка заполнения, логин или пароль не заполнены');
        }

        // Сбрасываем значение для большей безопасности
        setLogin('');
        setPassword('');
    };

    return (
        <SafeAreaView style={styles.container}>
            <View style={[styles.mainBlock, { width: mainBlockWidth }]}>

                <Text style={styles.topText}>{message}</Text>

                <View style={styles.blockTextInput}>
                    {/* Поле ввода значения ЛОГИНА пользователя */}
                    <TextInput
                        style={styles.textInput}
                        placeholder="Логин или почта:"
                        autoFocus={true}
                        onChangeText={login => setLogin(login)}
                        value={login}
                    />
                </View>

                <View style={styles.blockTextInput}>
                    {/* Поле ввода значения ПАРОЛЯ пользователя*/}
                    <TextInput
                        secureTextEntry={!showPassword}
                        style={styles.textInput}
                        placeholder="Пароль:"
                        onChangeText={passw => setPassword(passw)}
                        value={password}
                    />

                    {/* Иконка - кнопка глаза, изменяющее состояние видимости пароля */}
                    <MaterialCommunityIcons
                        name={showPassword ? 'eye-off' : 'eye'}
                        size={28}
                        color="#aaa"
                        style={styles.icon}
                        onPress={() => setShowPassword(!showPassword)}
                    />
                </View>

                {/* Кнопка отправки данных на сервер для авторизации */}
                <TouchableOpacity style={styles.button.active} onPressOut={sendDataToServerAuth}>
                    <Text style={styles.buttonText}>Войти</Text>
                </TouchableOpacity>

                {/* Кнопка отправки данных на сервер для регистрации*/}
                <TouchableOpacity style={styles.button.inactive} onPressOut={() => {navigation.navigate("Reg");}}>
                    <Text style={styles.buttonText}>Регистрация</Text>
                </TouchableOpacity>
            </View>
        </SafeAreaView>
    );
};

// Конструктор стилей для экрана авторизации
const styles = StyleSheet.create({
    container: {
        alignItems: 'center',
        alignContent: 'center',
        justifyContent: 'center',
        flex: 1,

        backgroundColor: '#21292c',
    },

    mainBlock: {
        flex: 1,
        alignContent: 'center',
        justifyContent: 'center',
    },

    blockTextInput: {
        flexDirection: 'row',
        alignItems: 'center',
        justifyContent: 'center',
        backgroundColor: '#f3f3f3',

        borderWidth: .5,
    },

    textInput: {
        justifyContent: 'center',
        margin: 'auto',
        padding: '7%',
        backgroundColor: '#f3f3f3',
        color: 'black',
        width: '100%',

        fontFamily: "Arial"
    },

    icon: {
        marginRight: '5%',
    },

    button: {
        active:{
            width: '100%',
            height: '10%',
            backgroundColor: '#007bb7',
            
        },

        inactive: {
            width: '100%',
            height: '10%',
            backgroundColor: '#374e59',
            
        }

    },

    buttonText: {
        display: 'flex',
        justifyContent: 'center',
        textAlign: 'center',
        fontFamily: 'Arial',
        fontWeight: 'bold',
        margin: 'auto',

        color: '#e2e8e9',
        fontSize: '1.25rem',
    },

    topText:{
        textAlign: "center",
        justifyContent: "center",

        fontSize: '1.05rem',
        color: '#e2e8e9',
        margin: '5%',
        padding: "auto",
        fontFamily: 'Arial'
    }
});
