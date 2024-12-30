//
// Основная страница
// 
//

import React, { useState } from 'react';
import { SafeAreaView, View, Text, StyleSheet, Dimensions } from 'react-native';
import { Appbar, Menu, Provider } from 'react-native-paper';

// экспортируемый экран домашней страницы
export const HomeScreen = ({ navigation }) => {
    // Определяем размер иконки в зависимости от ширины экрана
    const { width } = Dimensions.get('window');
    // 24 для маленьких экранов, 30 для больших
    const iconSize = width < 400 ? 32 : 46;

    const [visible, setVisible] = useState(true);

    const openMenu = () => setVisible(true);
    const closeMenu = () => setVisible(false);

    // Логика выхода из аккаунта
    const logout = () => {
        localStorage.removeItem('authToken');
        localStorage.removeItem('expiresAt');
        navigation.navigate('Auth');
    };

    return (
        <Provider>
            <SafeAreaView style={styles.container}>
                <Appbar.Header>
                    <Appbar.Content title="" />
                    <Menu
                        visible={visible}
                        onDismiss={closeMenu}
                        anchor={<Appbar.Action size={iconSize} icon="account" onPress={openMenu} />}
                    >
                        <Menu.Item onPress={() => navigation.navigate("Profile")} title="Профиль" />
                        <Menu.Item onPress={logout} title="Выйти" />
                    </Menu>
                </Appbar.Header>

                <Text>Текст для проверки работоспособности</Text>
            </SafeAreaView>
        </Provider>
    );
};

const styles = StyleSheet.create({
    container: {},
    content: {},
});
