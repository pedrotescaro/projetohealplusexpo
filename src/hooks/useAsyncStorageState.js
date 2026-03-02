import { useEffect, useState } from 'react';
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
