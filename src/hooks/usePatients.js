import { useEffect, useState, useCallback } from 'react';
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
