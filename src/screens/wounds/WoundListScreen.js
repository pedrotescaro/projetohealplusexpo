import React from 'react';
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
