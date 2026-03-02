import React from 'react';
import { View } from 'react-native';

export default function TabBarIcon({ name, color, size }) {
  return (
    <View style={{ width: size, height: size, backgroundColor: color, borderRadius: size/2 }} />
  );
}
