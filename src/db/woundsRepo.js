import { getDb } from './sqlite';

export async function findAllWounds() {
  const db = getDb();
  return db.getAllAsync(`
    SELECT w.*, p.name as patientName
    FROM wounds w
    JOIN patients p ON p.id = w.patientId
    ORDER BY w.createdAt DESC
  `);
}

export async function findWoundsByPatient(patientId) {
  const db = getDb();
  return db.getAllAsync(
    `SELECT * FROM wounds WHERE patientId = ? ORDER BY createdAt DESC`,
    patientId
  );
}

export async function createWound(input) {
  const db = getDb();
  const now = new Date().toISOString();
  const id = input.id || String(Date.now());
  const { patientId, location, status, description } = input;
  await db.runAsync(
    `INSERT INTO wounds (id, patientId, location, status, description, createdAt, updatedAt) VALUES (?, ?, ?, ?, ?, ?, ?)`,
    id, patientId, location || '', status || 'active', description || '', now, now
  );
  return { ...input, id, createdAt: now, updatedAt: now };
}

export async function updateWound(id, updates) {
  const db = getDb();
  const now = new Date().toISOString();
  await db.runAsync(
    `UPDATE wounds SET location = COALESCE(?, location), status = COALESCE(?, status), description = COALESCE(?, description), updatedAt = ? WHERE id = ?`,
    updates.location ?? null, updates.status ?? null, updates.description ?? null, now, id
  );
}

export async function deleteWound(id) {
  const db = getDb();
  await db.runAsync(`DELETE FROM wounds WHERE id = ?`, id);
}
