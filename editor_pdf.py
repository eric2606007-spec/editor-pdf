# ==========================================================
# 📄 PROYECTO: EDITOR DE PDFs
# Materia: Análisis y Diseño de Algoritmos
# Librería: PyPDF2
# ==========================================================
import PyPDF2

# ==========================================================
# 📚 TEMA 7: FUNCIONES
# Dividimos el programa en pequeñas tareas ordenadas.
# ==========================================================

def mostrar_menu():
    """Muestra en pantalla las opciones del editor."""
  # 📚 TEMA 3: Salida de datos (print)
    print("\n" + "="*40)
    print("      🛠️  EDITOR DE PDFs  🛠️")
    print("=" * 40)
    print("1. 📖 Ver cuántas páginas tiene un PDF")
    print("2. 🔗 Unir dos archivos PDF")
    print("3. ✂️  Extraer una página de un PDF")
    print("4. 🔄 Rotar las páginas de un PDF")
    print("5. ❌ Salir")
    print("=" * 40)

mostrar_menu()