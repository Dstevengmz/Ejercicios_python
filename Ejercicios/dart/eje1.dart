import 'dart:io';
List<String> nombres = [];
void main(){
  menu();
}
  void menu(){
  int opcion=0;
  do {
    print("menu listas ");
    print("1. leer nombres");
    print("2. consultar niombre");
    print("3. salir");
    print("ingrese opcion ");
    opcion= int.parse(stdin.readLineSync().toString());
    switch (opcion) {
      case 1: leernombre();
        break;
      case 2:
      consultarnombre();
      break;
      case 3:
      print("nos fuimos");
      break;

      default:
      print("opcion fuera de rango");

    }
    
  } while (opcion!=3);
}
  void leernombre() {
    print("ingrese el nombre de la persona para guardala en la lista:");
    String nombre =stdin.readLineSync().toString();
    nombres.add(nombre.toUpperCase());
  }
  void consultarnombre(){
    print("ingrese nombre para consultar en la lsita ");
    String nombre= stdin.readLineSync().toString();
    bool existe=false;
    for (var name in nombres) {
      if (name == nombre.toUpperCase()) {
        print("$name si existe en la lista ");
        existe=true;
        break;

      }
      
    }
    if(!existe){
      print("$nombre no existe en la lista");
    }
  }