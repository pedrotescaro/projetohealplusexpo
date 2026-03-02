import React, { useEffect } from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { StatusBar } from 'expo-status-bar';
import RootNavigator from './src/navigation/RootNavigator';
import { runMigrations } from './src/db/sqlite';

export default function App() {
  useEffect(() => {
    runMigrations();
  }, []);
  return (
    <>
      <StatusBar style="dark" />
      <NavigationContainer>
        <RootNavigator />
      </NavigationContainer>
    </>
  );
}
