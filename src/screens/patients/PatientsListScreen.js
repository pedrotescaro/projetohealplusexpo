import React from 'react';
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
