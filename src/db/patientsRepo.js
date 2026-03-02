import { getDb } from './sqlite';

export async function findAllPatients() {
  const db = getDb();
  return db.getAllAsync(`
    SELECT p.*,
      (SELECT COUNT(*) FROM wounds w WHERE w.patientId = p.id AND w.status = 'active') AS activeWoundsCount
    FROM patients p
    WHERE p.archivedAt IS NULL
    ORDER BY p.createdAt DESC
  `);
}

export async function createPatient(patient) {
  const db = getDb();
  const now = new Date().toISOString();
  const id = patient.id || String(Date.now());
  await db.runAsync(
    `INSERT INTO patients (id, name, gender, age, createdAt, updatedAt) VALUES (?, ?, ?, ?, ?, ?)`,
    id, patient.name, patient.gender, patient.age, now, now
  );
  return { ...patient, id, createdAt: now, updatedAt: now };
}

export async function updatePatient(id, updates) {
  const db = getDb();
  const now = new Date().toISOString();
  const { name, gender, age } = updates;
  await db.runAsync(
    `UPDATE patients SET name = ?, gender = ?, age = ?, updatedAt = ? WHERE id = ?`,
    name, gender, age, now, id
  );
}

export async function archivePatient(id) {
  const db = getDb();
  const now = new Date().toISOString();
  await db.runAsync(`UPDATE patients SET archivedAt = ? WHERE id = ?`, now, id);
}
