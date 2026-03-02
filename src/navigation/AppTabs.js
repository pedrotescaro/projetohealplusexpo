import React from 'react';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import HomeScreen from '../screens/dashboard/HomeScreen';
import PatientsStack from './PatientsStack';
import WoundsStack from './WoundsStack';
import SettingsScreen from '../screens/settings/SettingsScreen';
import TabBarIcon from '../components/layout/TabBarIcon';
import { colors } from '../theme/colors';

const Tab = createBottomTabNavigator();

export default function AppTabs() {
  return (
    <Tab.Navigator
      screenOptions={{
        headerShown: false,
        tabBarActiveTintColor: colors.primary,
        tabBarInactiveTintColor: colors.textMuted,
      }}
    >
      <Tab.Screen name="HomeTab" component={HomeScreen} options={{ title: 'Início', tabBarIcon: ({ color, size }) => (<TabBarIcon name="home" color={color} size={size} />) }} />
      <Tab.Screen name="PatientsTab" component={PatientsStack} options={{ title: 'Pacientes', tabBarIcon: ({ color, size }) => (<TabBarIcon name="users" color={color} size={size} />) }} />
      <Tab.Screen name="WoundsTab" component={WoundsStack} options={{ title: 'Feridas', tabBarIcon: ({ color, size }) => (<TabBarIcon name="activity" color={color} size={size} />) }} />
      <Tab.Screen name="SettingsTab" component={SettingsScreen} options={{ title: 'Configurações', tabBarIcon: ({ color, size }) => (<TabBarIcon name="settings" color={color} size={size} />) }} />
    </Tab.Navigator>
  );
}
