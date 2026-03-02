import React from 'react';
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
