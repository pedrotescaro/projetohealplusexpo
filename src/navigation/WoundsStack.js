import React from 'react';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import WoundListScreen from '../screens/wounds/WoundListScreen';
import WoundDetailScreen from '../screens/wounds/WoundDetailScreen';
import WoundFormScreen from '../screens/wounds/WoundFormScreen';

const Stack = createNativeStackNavigator();

export default function WoundsStack() {
  return (
    <Stack.Navigator>
      <Stack.Screen name="WoundList" component={WoundListScreen} options={{ title: 'Feridas' }} />
      <Stack.Screen name="WoundDetail" component={WoundDetailScreen} options={{ title: 'Detalhes da ferida' }} />
      <Stack.Screen name="WoundForm" component={WoundFormScreen} options={{ title: 'Nova ferida' }} />
    </Stack.Navigator>
  );
}
