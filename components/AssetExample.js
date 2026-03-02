// 1. Adicionei o 'Button' na lista de imports
import { Text, View, StyleSheet, Image, Button } from 'react-native';

export default function AssetExample() {
  return (
    <View style={styles.container}>
      <Text style={styles.paragraph}>
        Local files and assets can be imported by dragging and dropping them into the editor
      </Text>
      
      {/* Agora o componente Button funcionará corretamente */}
      <Button 
        title="Pressione aqui" 
        onPress={() => console.log('Olá!')} 
      />

      <Image style={styles.logo} source={require('../assets/snack-icon.png')} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1, // Adicionei flex: 1 para centralizar na tela inteira
    alignItems: 'center',
    justifyContent: 'center',
    padding: 24,
    backgroundColor: '#ecf0f1',
  },
  paragraph: {
    margin: 24,
    marginTop: 0,
    fontSize: 14,
    fontWeight: 'bold',
    textAlign: 'center',
  },
  logo: {
    height: 128,
    width: 128,
    marginTop: 20, // Um pouco de margem para não grudar no botão
  }
});