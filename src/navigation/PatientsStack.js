import React from 'react';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import PatientsListScreen from '../screens/patients/PatientsListScreen';
import PatientDetailScreen from '../screens/patients/PatientDetailScreen';
import PatientFormScreen from '../screens/patients/PatientFormScreen';
import WoundFormScreen from '../screens/wounds/WoundFormScreen';

const Stack = createNativeStackNavigator();

export default function PatientsStack() {
  return (
    <Stack.Navigator>
      <Stack.Screen name="PatientsList" component={PatientsListScreen} options={{ title: 'Pacientes' }} />
      <Stack.Screen name="PatientDetail" component={PatientDetailScreen} options={{ title: 'Detalhes do paciente' }} />
      <Stack.Screen name="PatientForm" component={PatientFormScreen} options={{ title: 'Novo paciente' }} />
      <Stack.Screen name="WoundForm" component={WoundFormScreen} options={{ title: 'Nova ferida' }} />
    </Stack.Navigator>
  );
}
