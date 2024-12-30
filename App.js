//
// Основной файл разработки и запуска приложения
//

import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";
import React from "react";

import { HomeScreen } from "./pages/HomePage";
import { AuthScreen } from "./pages/AuthPage";
import { ProfileScreen } from "./pages/ProfilePage";
import { RegScreen } from "./pages/RegPage";

// создаем экземпляр объекта навигатора состояний
const Stack = createStackNavigator();

// экспорт основной функции приложения
export default function App() {
    return (
        <NavigationContainer>
            <Stack.Navigator
                initialRouteName="Home"
                screenOptions={{
                    headerStyle: {
                        backgroundColor: "#ffffff",
                    },
                }}
            >
                <Stack.Screen
                    name="Auth"
                    component={AuthScreen}
                    options={{
                        headerShown: false,
                    }}
                />

                <Stack.Screen
                    name="Reg"
                    component={RegScreen}
                    options={{
                        headerShown: false,
                    }}
                />

                <Stack.Screen
                    name="Home"
                    component={HomeScreen}
                    options={{
                        headerShown: false,
                    }}
                />

                <Stack.Screen
                    name="Profile"
                    component={ProfileScreen}
                />
            </Stack.Navigator>
        </NavigationContainer>
    );
}