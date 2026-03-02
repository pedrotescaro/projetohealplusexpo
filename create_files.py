import os

files = {
    "App.js": """import React, { useEffect } from 'react';
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
""",
    "src/theme/colors.js": """export const lightColors = {
  background: 'hsl(220, 93%, 95%)',
  foreground: 'hsl(222, 84%, 4.9%)',
  card: 'hsl(0, 0%, 100%)',
  cardForeground: 'hsl(222, 84%, 4.9%)',
  popover: 'hsl(0, 0%, 100%)',
  popoverForeground: 'hsl(222, 84%, 4.9%)',
  primary: 'hsl(217, 91%, 60%)',
  primaryForeground: 'hsl(210, 40%, 98%)',
  secondary: 'hsl(210, 40%, 96.1%)',
  secondaryForeground: 'hsl(222, 47%, 11.2%)',
  muted: 'hsl(210, 40%, 96.1%)',
  mutedForeground: 'hsl(215, 20%, 65.1%)',
  accent: 'hsl(210, 40%, 96.1%)',
  accentForeground: 'hsl(222, 47%, 11.2%)',
  destructive: 'hsl(0, 84.2%, 60.2%)',
  destructiveForeground: 'hsl(210, 40%, 98%)',
  border: 'hsl(214, 32%, 91.4%)',
  input: 'hsl(214, 32%, 91.4%)',
  ring: 'hsl(217, 91%, 60%)',
  textPrimary: 'hsl(222, 84%, 4.9%)',
  textSecondary: 'hsl(215, 20%, 65.1%)',
  textMuted: 'hsl(215, 20%, 65.1%)',
};

export const darkColors = { ...lightColors }; // placeholder for real dark ones if needed

export const colors = lightColors;
""",
    "src/theme/typography.js": """export const typography = {
  fontFamilyRegular: 'System',
  fontFamilyMedium: 'System',
  fontFamilyBold: 'System',
  h1: { fontSize: 28, lineHeight: 34, fontWeight: '700' },
  h2: { fontSize: 22, lineHeight: 28, fontWeight: '600' },
  h3: { fontSize: 18, lineHeight: 24, fontWeight: '600' },
  body: { fontSize: 14, lineHeight: 20, fontWeight: '400' },
  bodyBold: { fontSize: 14, lineHeight: 20, fontWeight: '600' },
  caption: { fontSize: 12, lineHeight: 16, fontWeight: '400' },
};
""",
    "src/theme/spacing.js": """export const spacing = {
  xs: 4,
  sm: 8,
  md: 12,
  lg: 16,
  xl: 24,
  xxl: 32,
};
""",
    "src/navigation/RootNavigator.js": """import React from 'react';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import AuthStack from './AuthStack';
import AppTabs from './AppTabs';

const Stack = createNativeStackNavigator();

export default function RootNavigator() {
  const isAuthenticated = true;
  return (
    <Stack.Navigator screenOptions={{ headerShown: false }}>
      {isAuthenticated ? (
        <Stack.Screen name="AppTabs" component={AppTabs} />
      ) : (
        <Stack.Screen name="AuthStack" component={AuthStack} />
      )}
    </Stack.Navigator>
  );
}
""",
    "src/navigation/AuthStack.js": """import React from 'react';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import LoginScreen from '../screens/auth/LoginScreen';
import RegisterScreen from '../screens/auth/RegisterScreen';

const Stack = createNativeStackNavigator();

export default function AuthStack() {
  return (
    <Stack.Navigator>
      <Stack.Screen name="Login" component={LoginScreen} options={{ title: 'Entrar no Heal+' }} />
      <Stack.Screen name="Register" component={RegisterScreen} options={{ title: 'Criar conta' }} />
    </Stack.Navigator>
  );
}
""",
    "src/navigation/AppTabs.js": """import React from 'react';
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
""",
    "src/navigation/PatientsStack.js": """import React from 'react';
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
""",
    "src/navigation/WoundsStack.js": """import React from 'react';
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
""",
    "src/components/layout/Screen.js": """import React from 'react';
import { SafeAreaView, View, StyleSheet } from 'react-native';
import { colors } from '../../theme/colors';
import { spacing } from '../../theme/spacing';

export default function Screen({ children, withPadding = true }) {
  return (
    <SafeAreaView style={styles.safeArea}>
      <View style={[styles.container, withPadding && styles.padded]}>
        {children}
      </View>
    </SafeAreaView>
  );
}
const styles = StyleSheet.create({
  safeArea: { flex: 1, backgroundColor: colors.background },
  container: { flex: 1 },
  padded: { paddingHorizontal: spacing.lg, paddingTop: spacing.lg },
});
""",
    "src/components/layout/TabBarIcon.js": """import React from 'react';
import { View } from 'react-native';

export default function TabBarIcon({ name, color, size }) {
  return (
    <View style={{ width: size, height: size, backgroundColor: color, borderRadius: size/2 }} />
  );
}
""",
    "src/components/ui/Text.js": """import React from 'react';
import { Text as RNText, StyleSheet } from 'react-native';
import { colors } from '../../theme/colors';
import { typography } from '../../theme/typography';

export default function Text({ variant = 'body', style, ...rest }) {
  const variantStyle = typography[variant] || typography.body;
  return (
    <RNText style={[styles.base, variantStyle, style]} {...rest} />
  );
}
const styles = StyleSheet.create({
  base: { color: colors.textPrimary },
});
""",
    "src/components/ui/Button.js": """import React from 'react';
import { TouchableOpacity, ActivityIndicator, StyleSheet } from 'react-native';
import Text from './Text';
import { colors } from '../../theme/colors';
import { spacing } from '../../theme/spacing';

export default function Button({ title, onPress, variant = 'primary', loading = false, disabled = false, style }) {
  const isPrimary = variant === 'primary';
  return (
    <TouchableOpacity
      onPress={onPress}
      disabled={disabled || loading}
      style={[
        styles.button,
        isPrimary ? styles.primary : styles.outlined,
        (disabled || loading) && styles.disabled,
        style,
      ]}
    >
      {loading ? (
        <ActivityIndicator color={isPrimary ? '#FFF' : colors.primary} />
      ) : (
        <Text variant="bodyBold" style={[styles.label, !isPrimary && { color: colors.primary }]}>
          {title}
        </Text>
      )}
    </TouchableOpacity>
  );
}
const styles = StyleSheet.create({
  button: { minHeight: 44, borderRadius: 8, paddingHorizontal: spacing.lg, alignItems: 'center', justifyContent: 'center', flexDirection: 'row' },
  primary: { backgroundColor: colors.primary },
  outlined: { backgroundColor: 'transparent', borderWidth: 1, borderColor: colors.primary },
  disabled: { opacity: 0.5 },
  label: { color: '#FFFFFF' },
});
""",
    "src/components/domain/PatientListItem.js": """import React from 'react';
import { TouchableOpacity, View, StyleSheet } from 'react-native';
import Text from '../ui/Text';
import { colors } from '../../theme/colors';
import { spacing } from '../../theme/spacing';

export default function PatientListItem({ patient, onPress }) {
  return (
    <TouchableOpacity onPress={onPress} style={styles.container}>
      <View style={styles.row}>
        <Text variant="h3" style={styles.name}>{patient.name}</Text>
        <Text variant="caption" style={styles.chip}>{patient.activeWoundsCount || 0} feridas ativas</Text>
      </View>
      <Text variant="body" style={styles.meta}>{patient.age} anos • {patient.gender}</Text>
    </TouchableOpacity>
  );
}
const styles = StyleSheet.create({
  container: { backgroundColor: colors.surface, padding: spacing.md, borderRadius: 10, marginBottom: spacing.sm, borderWidth: 1, borderColor: colors.border },
  row: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center' },
  name: { flex: 1, marginRight: spacing.sm },
  chip: { paddingHorizontal: spacing.sm, paddingVertical: spacing.xs, borderRadius: 999, backgroundColor: colors.primaryLight, color: colors.primaryDark },
  meta: { marginTop: spacing.xs, color: colors.textSecondary },
});
""",
    "src/db/sqlite.js": """import * as SQLite from 'expo-sqlite';

let dbInstance = null;
export function getDb() {
  if (!dbInstance) {
    dbInstance = SQLite.openDatabaseSync('healplus.db');
  }
  return dbInstance;
}

export function runMigrations() {
  const db = getDb();
  db.execSync(`
    CREATE TABLE IF NOT EXISTS patients (
      id TEXT PRIMARY KEY NOT NULL,
      name TEXT NOT NULL,
      gender TEXT,
      age INTEGER,
      createdAt TEXT NOT NULL,
      updatedAt TEXT NOT NULL,
      archivedAt TEXT
    );
    CREATE TABLE IF NOT EXISTS wounds (
      id TEXT PRIMARY KEY NOT NULL,
      patientId TEXT NOT NULL,
      status TEXT NOT NULL,
      location TEXT,
      description TEXT,
      createdAt TEXT NOT NULL,
      updatedAt TEXT NOT NULL,
      FOREIGN KEY (patientId) REFERENCES patients(id)
    );
    CREATE TABLE IF NOT EXISTS wound_evolutions (
      id TEXT PRIMARY KEY NOT NULL,
      woundId TEXT NOT NULL,
      note TEXT,
      photoUri TEXT,
      measurement TEXT,
      createdAt TEXT NOT NULL,
      FOREIGN KEY (woundId) REFERENCES wounds(id)
    );
    CREATE TABLE IF NOT EXISTS users (
      id TEXT PRIMARY KEY NOT NULL,
      name TEXT,
      email TEXT,
      role TEXT,
      createdAt TEXT NOT NULL
    );
  `);
}
""",
    "src/db/patientsRepo.js": """import { getDb } from './sqlite';

export async function findAllPatients() {
  const db = getDb();
  return db.getAllAsync(`
    SELECT p.*,
      (SELECT COUNT(*) FROM wounds w WHERE w.patientId = p.id AND w.status = 'active') AS activeWoundsCount
    FROM patients p
    WHERE p.archivedAt IS NULL
    ORDER BY p.createdAt DESC
  `);
}

export async function createPatient(patient) {
  const db = getDb();
  const now = new Date().toISOString();
  const id = patient.id || String(Date.now());
  await db.runAsync(
    `INSERT INTO patients (id, name, gender, age, createdAt, updatedAt) VALUES (?, ?, ?, ?, ?, ?)`,
    id, patient.name, patient.gender, patient.age, now, now
  );
  return { ...patient, id, createdAt: now, updatedAt: now };
}

export async function updatePatient(id, updates) {
  const db = getDb();
  const now = new Date().toISOString();
  const { name, gender, age } = updates;
  await db.runAsync(
    `UPDATE patients SET name = ?, gender = ?, age = ?, updatedAt = ? WHERE id = ?`,
    name, gender, age, now, id
  );
}

export async function archivePatient(id) {
  const db = getDb();
  const now = new Date().toISOString();
  await db.runAsync(`UPDATE patients SET archivedAt = ? WHERE id = ?`, now, id);
}
""",
    "src/db/woundsRepo.js": """import { getDb } from './sqlite';

export async function findAllWounds() {
  const db = getDb();
  return db.getAllAsync(`
    SELECT w.*, p.name as patientName
    FROM wounds w
    JOIN patients p ON p.id = w.patientId
    ORDER BY w.createdAt DESC
  `);
}

export async function findWoundsByPatient(patientId) {
  const db = getDb();
  return db.getAllAsync(
    `SELECT * FROM wounds WHERE patientId = ? ORDER BY createdAt DESC`,
    patientId
  );
}

export async function createWound(input) {
  const db = getDb();
  const now = new Date().toISOString();
  const id = input.id || String(Date.now());
  const { patientId, location, status, description } = input;
  await db.runAsync(
    `INSERT INTO wounds (id, patientId, location, status, description, createdAt, updatedAt) VALUES (?, ?, ?, ?, ?, ?, ?)`,
    id, patientId, location || '', status || 'active', description || '', now, now
  );
  return { ...input, id, createdAt: now, updatedAt: now };
}

export async function updateWound(id, updates) {
  const db = getDb();
  const now = new Date().toISOString();
  await db.runAsync(
    `UPDATE wounds SET location = COALESCE(?, location), status = COALESCE(?, status), description = COALESCE(?, description), updatedAt = ? WHERE id = ?`,
    updates.location ?? null, updates.status ?? null, updates.description ?? null, now, id
  );
}

export async function deleteWound(id) {
  const db = getDb();
  await db.runAsync(`DELETE FROM wounds WHERE id = ?`, id);
}
""",
    "src/hooks/usePatients.js": """import { useEffect, useState, useCallback } from 'react';
import { findAllPatients, createPatient, updatePatient, archivePatient } from '../db/patientsRepo';

export default function usePatients() {
  const [patients, setPatients] = useState([]);
  const [loading, setLoading] = useState(false);
  const reload = useCallback(async () => {
    setLoading(true);
    try {
      const data = await findAllPatients();
      setPatients(data);
    } finally {
      setLoading(false);
    }
  }, []);
  useEffect(() => { reload(); }, [reload]);
  const addPatient = async patientInput => {
    const created = await createPatient(patientInput);
    setPatients(prev => [created, ...prev]);
  };
  const editPatient = async (id, updates) => {
    await updatePatient(id, updates);
    setPatients(prev => prev.map(p => (p.id === id ? { ...p, ...updates } : p)));
  };
  const removePatient = async id => {
    await archivePatient(id);
    setPatients(prev => prev.filter(p => p.id !== id));
  };
  return { patients, loading, reload, addPatient, editPatient, removePatient };
}
""",
    "src/hooks/useWounds.js": """import { useState, useEffect, useCallback } from 'react';
import { findAllWounds, findWoundsByPatient, createWound, updateWound, deleteWound } from '../db/woundsRepo';

export default function useWounds({ patientId } = {}) {
  const [wounds, setWounds] = useState([]);
  const [loading, setLoading] = useState(false);
  const reload = useCallback(async () => {
    setLoading(true);
    try {
      const data = patientId ? await findWoundsByPatient(patientId) : await findAllWounds();
      setWounds(data);
    } finally {
      setLoading(false);
    }
  }, [patientId]);
  useEffect(() => { reload(); }, [reload]);
  const addWound = async input => {
    const created = await createWound(input);
    setWounds(prev => [created, ...prev]);
  };
  const editWound = async (id, updates) => {
    await updateWound(id, updates);
    setWounds(prev => prev.map(w => (w.id === id ? { ...w, ...updates } : w)));
  };
  const removeWound = async id => {
    await deleteWound(id);
    setWounds(prev => prev.filter(w => w.id !== id));
  };
  return { wounds, loading, reload, addWound, editWound, removeWound };
}
""",
    "src/hooks/useAsyncStorageState.js": """import { useEffect, useState } from 'react';
import AsyncStorage from '@react-native-async-storage/async-storage';

export default function useAsyncStorageState(key, initialValue) {
  const [value, setValue] = useState(initialValue);
  const [loaded, setLoaded] = useState(false);
  useEffect(() => {
    AsyncStorage.getItem(key)
      .then(stored => {
        if (stored != null) setValue(JSON.parse(stored));
      })
      .finally(() => setLoaded(true));
  }, [key]);
  const setPersistedValue = async newValue => {
    setValue(newValue);
    try {
      await AsyncStorage.setItem(key, JSON.stringify(newValue));
    } catch (e) {}
  };
  return [value, setPersistedValue, loaded];
}
""",
    "src/screens/patients/PatientsListScreen.js": """import React from 'react';
import { FlatList, RefreshControl } from 'react-native';
import Screen from '../../components/layout/Screen';
import Text from '../../components/ui/Text';
import Button from '../../components/ui/Button';
import PatientListItem from '../../components/domain/PatientListItem';
import usePatients from '../../hooks/usePatients';
import { spacing } from '../../theme/spacing';

export default function PatientsListScreen({ navigation }) {
  const { patients, loading, reload } = usePatients();
  return (
    <Screen>
      <Button title="Novo paciente" onPress={() => navigation.navigate('PatientForm')} style={{ marginBottom: spacing.md }} />
      <FlatList
        data={patients}
        keyExtractor={item => item.id.toString()}
        renderItem={({ item }) => (
          <PatientListItem
            patient={item}
            onPress={() => navigation.navigate('PatientDetail', { patientId: item.id })}
          />
        )}
        refreshControl={<RefreshControl refreshing={loading} onRefresh={reload} />}
        ListEmptyComponent={!loading ? <Text variant="body">Nenhum paciente cadastrado. Comece adicionando um novo.</Text> : null}
      />
    </Screen>
  );
}
""",
    "src/screens/wounds/WoundListScreen.js": """import React from 'react';
import { FlatList, RefreshControl } from 'react-native';
import Screen from '../../components/layout/Screen';
import Text from '../../components/ui/Text';
import Button from '../../components/ui/Button';
import useWounds from '../../hooks/useWounds';
import { spacing } from '../../theme/spacing';

function WoundListItem({ wound, onPress }) {
  return (
    <Button
      variant="outlined"
      onPress={onPress}
      style={{ marginBottom: spacing.sm, justifyContent: 'flex-start' }}
    >
      <Text variant="bodyBold">
        {wound.patientName} • {wound.location || 'Sem localização'}
      </Text>
    </Button>
  );
}

export default function WoundListScreen({ navigation }) {
  const { wounds, loading, reload } = useWounds();
  return (
    <Screen>
      <Button title="Nova avaliação" onPress={() => navigation.navigate('WoundForm')} style={{ marginBottom: spacing.md }} />
      <FlatList
        data={wounds}
        keyExtractor={item => item.id.toString()}
        renderItem={({ item }) => (
          <WoundListItem
            wound={item}
            onPress={() => navigation.navigate('WoundDetail', { woundId: item.id })}
          />
        )}
        refreshControl={<RefreshControl refreshing={loading} onRefresh={reload} />}
        ListEmptyComponent={!loading ? <Text variant="body">Nenhuma avaliação cadastrada. Comece criando uma nova.</Text> : null}
      />
    </Screen>
  );
}
""",
    "src/screens/dashboard/HomeScreen.js": "import React from 'react'; import Screen from '../../components/layout/Screen'; import Text from '../../components/ui/Text'; export default function HomeScreen() { return <Screen><Text variant='h1'>Dashboard Home</Text></Screen>; }",
    "src/screens/auth/LoginScreen.js": "import React from 'react'; import Screen from '../../components/layout/Screen'; import Text from '../../components/ui/Text'; export default function LoginScreen() { return <Screen><Text>Login</Text></Screen>; }",
    "src/screens/auth/RegisterScreen.js": "import React from 'react'; import Screen from '../../components/layout/Screen'; import Text from '../../components/ui/Text'; export default function RegisterScreen() { return <Screen><Text>Register</Text></Screen>; }",
    "src/screens/patients/PatientDetailScreen.js": "import React from 'react'; import Screen from '../../components/layout/Screen'; import Text from '../../components/ui/Text'; export default function PatientDetailScreen() { return <Screen><Text>Patient Detail</Text></Screen>; }",
    "src/screens/patients/PatientFormScreen.js": "import React from 'react'; import Screen from '../../components/layout/Screen'; import Text from '../../components/ui/Text'; export default function PatientFormScreen() { return <Screen><Text>Patient Form</Text></Screen>; }",
    "src/screens/wounds/WoundDetailScreen.js": "import React from 'react'; import Screen from '../../components/layout/Screen'; import Text from '../../components/ui/Text'; export default function WoundDetailScreen() { return <Screen><Text>Wound Detail</Text></Screen>; }",
    "src/screens/wounds/WoundFormScreen.js": "import React from 'react'; import Screen from '../../components/layout/Screen'; import Text from '../../components/ui/Text'; export default function WoundFormScreen() { return <Screen><Text>Wound Form</Text></Screen>; }",
    "src/screens/settings/SettingsScreen.js": "import React from 'react'; import Screen from '../../components/layout/Screen'; import Text from '../../components/ui/Text'; export default function SettingsScreen() { return <Screen><Text>Settings</Text></Screen>; }",
    "README.md": """# Heal+ Mobile App

Este é o aplicativo mobile do Heal+, desenvolvido em React Native com Expo. Ele espelha a experiência e arquitetura do projeto web Heal+.

## Instalação e Execução

### Pré-requisitos
- Node.js
- Expo CLI (`npm install -g expo-cli`)

### Scripts

1. Instalar dependências:
   ```bash
   npm install
   ```

2. Instalar dependências de navegação e AsyncStorage:
   ```bash
   npx expo install @react-navigation/native @react-navigation/native-stack @react-navigation/bottom-tabs react-native-screens react-native-safe-area-context @react-native-async-storage/async-storage expo-sqlite
   ```

3. Iniciar o projeto localmente:
   ```bash
   npx expo start
   ```

## Especificação do Formulário TIMERS
Para refletir os campos da anamnese do projeto Web:

- **Tissue (Tecido)**:
  - Avaliação do leito da ferida para identificar necrose, esfacelo, granulação ou epitelização.
  - Opções: Necrótico (escara), Esfacelo (fibrina), Granulação, Epitelização, etc.
- **Infection/Inflammation (Infecção/Inflamação)**:
  - Presença de sinais clínicos de infecção ou inflamação.
  - Sinais: Eritema, Calor, Edema, Dor localizada, Exsudato purulento.
- **Moisture (Umidade)**:
  - Nível de exsudato para manter o equilíbrio úmido adequado.
  - Opções: Seco, Leve, Moderado, Intenso.
- **Edges (Bordas)**:
  - Condição das bordas e área perilesional sugerindo avanço ou estagnação.
  - Opções: Maceradas, Aderidas/Planadas, Descoladas, Hiperqueratose.

Esses campos devem ser usados em `WoundFormScreen`.
""",
    "TIMERS_FORM.md": """# TIMERS Form Detailed Structure

### T - Tissue (Tecido)
Objetivo: Avaliar a viabilidade do tecido no leito da ferida.
- Necrótico (%)
- Esfacelo (%)
- Granulação (%)
- Epitelização (%)

### I - Infection / Inflammation (Infecção/Inflamação)
Objetivo: Identificar controle microbiano e sinais inflamatórios anormais.
- Sinais Clínicos: Dor, calor, rubor, edema, odor
- Características do Exsudato: Purulento, Seropurulento
- Avaliação: Presença de biofilme?

### M - Moisture (Umidade/Maceração)
Objetivo: Controlar o balanço hídrico na ferida.
- Nível de exsudato (Seco, Leve, Moderado, Alto)
- Tipo de exsudato (Seroso, Sanguinolento, etc.)

### E - Edges (Bordas)
Objetivo: Observar o avanço do epitélio e condições perilesionais.
- Maceração perilesional
- Bordas espessadas / Hiperqueratose
- Bordas soltas / Epíbole

### R - Repair (Reparo Tissular)
Objetivo: Avaliação adicional para terapias avançadas se estagnada.
*(Aplicações opcionais caso necessárias)*

### S - Social / Patient (Fatores do Paciente)
Objetivo: Questões sistêmicas e psicossociais atuando sobre a ferida.
- Dor e tratamento?
- Adesão do paciente?
"""
}

for path, content in files.items():
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Created {len(files)} files successfully.")
