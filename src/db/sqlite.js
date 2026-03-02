import * as SQLite from 'expo-sqlite';

let dbInstance = null;
export function getDb() {
  if (!dbInstance) {
    dbInstance = SQLite.openDatabaseSync('healplus.db');
  }
  return dbInstance;
}

export function runMigrations() {
  const db = getDb();
  db.execSync(`
    CREATE TABLE IF NOT EXISTS patients (
      id TEXT PRIMARY KEY NOT NULL,
      name TEXT NOT NULL,
      gender TEXT,
      age INTEGER,
      createdAt TEXT NOT NULL,
      updatedAt TEXT NOT NULL,
      archivedAt TEXT
    );
    CREATE TABLE IF NOT EXISTS wounds (
      id TEXT PRIMARY KEY NOT NULL,
      patientId TEXT NOT NULL,
      status TEXT NOT NULL,
      location TEXT,
      description TEXT,
      createdAt TEXT NOT NULL,
      updatedAt TEXT NOT NULL,
      FOREIGN KEY (patientId) REFERENCES patients(id)
    );
    CREATE TABLE IF NOT EXISTS wound_evolutions (
      id TEXT PRIMARY KEY NOT NULL,
      woundId TEXT NOT NULL,
      note TEXT,
      photoUri TEXT,
      measurement TEXT,
      createdAt TEXT NOT NULL,
      FOREIGN KEY (woundId) REFERENCES wounds(id)
    );
    CREATE TABLE IF NOT EXISTS users (
      id TEXT PRIMARY KEY NOT NULL,
      name TEXT,
      email TEXT,
      role TEXT,
      createdAt TEXT NOT NULL
    );
  `);
}
