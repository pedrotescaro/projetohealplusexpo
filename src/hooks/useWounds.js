import { useState, useEffect, useCallback } from 'react';
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
