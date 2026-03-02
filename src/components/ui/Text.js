import React from 'react';
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
