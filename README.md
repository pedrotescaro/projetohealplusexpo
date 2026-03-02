# Heal+ Mobile App

Este é o aplicativo mobile do Heal+, desenvolvido em React Native com Expo. Ele espelha a experiência e arquitetura do projeto web Heal+.

## Instalação e Execução

### Pré-requisitos
- Node.js
- Expo CLI (`npm install -g expo-cli`)

### Scripts

1. Instalar dependências:
   ```bash
   npm install
   ```

2. Instalar dependências de navegação e AsyncStorage:
   ```bash
   npx expo install @react-navigation/native @react-navigation/native-stack @react-navigation/bottom-tabs react-native-screens react-native-safe-area-context @react-native-async-storage/async-storage expo-sqlite
   ```

3. Iniciar o projeto localmente:
   ```bash
   npx expo start
   ```

## Especificação do Formulário TIMERS
Para refletir os campos da anamnese do projeto Web:

- **Tissue (Tecido)**:
  - Avaliação do leito da ferida para identificar necrose, esfacelo, granulação ou epitelização.
  - Opções: Necrótico (escara), Esfacelo (fibrina), Granulação, Epitelização, etc.
- **Infection/Inflammation (Infecção/Inflamação)**:
  - Presença de sinais clínicos de infecção ou inflamação.
  - Sinais: Eritema, Calor, Edema, Dor localizada, Exsudato purulento.
- **Moisture (Umidade)**:
  - Nível de exsudato para manter o equilíbrio úmido adequado.
  - Opções: Seco, Leve, Moderado, Intenso.
- **Edges (Bordas)**:
  - Condição das bordas e área perilesional sugerindo avanço ou estagnação.
  - Opções: Maceradas, Aderidas/Planadas, Descoladas, Hiperqueratose.

Esses campos devem ser usados em `WoundFormScreen`.
