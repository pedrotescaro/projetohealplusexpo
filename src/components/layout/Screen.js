import React from 'react';
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
