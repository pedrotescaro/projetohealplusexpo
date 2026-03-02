import React from 'react';
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
