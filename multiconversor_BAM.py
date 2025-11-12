import re

# -------------------------------------------------------------
# CLASE PRINCIPAL DEL PROGRAMA
# -------------------------------------------------------------
class Conversor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.historial = []  # Variable no primitiva (lista)
        self.tasas = {       # Variable no primitiva (diccionario)
            "dolar_mxn": 18.6,
            "euro_usd": 1.15,
            "euro_mxn": 21.5
        }

    def saludar(self):
        return f"\n💥💣 ¡Bienvenid@s al {self.nombre}! 💥💣\n✨ Tu compa digital que convierte TODO con estilo ✨"

    def agregar_conversion(self, descripcion):
        self.historial.append(descripcion)

    def buscar_conversion(self, termino):
        """Filtra el historial de conversiones usando búsqueda parcial."""
        return [c for c in self.historial if termino.lower() in c.lower()]


# -------------------------------------------------------------
# FUNCIONES AUXILIARES
# -------------------------------------------------------------
def convertir_a_minusculas(texto):
    """Convierte texto a minúsculas sin espacios."""
    return texto.lower().strip()

def validar_si_no(respuesta):
    """Usa expresiones regulares para validar respuestas de 'si' o 'no'."""
    return re.match(r'^(si|no)$', respuesta.strip().lower()) is not None


# -------------------------------------------------------------
# PROGRAMA PRINCIPAL
# -------------------------------------------------------------
app = Conversor("Multiconversor BAM")
print(app.saludar())
print("-" * 50)

seguir = 'si'

while seguir == 'si':
    try:
        print("\n--- MENÚ PRINCIPAL --- 🌡️⚖️💰")
        print("1️⃣ Temperatura 🌡️")
        print("2️⃣ Peso ⚖️")
        print("3️⃣ Moneda 💰")
        print("4️⃣ Ver historial 📜")
        print("5️⃣ Buscar conversión 🔍")
        print("6️⃣ Salir 🚪")

        opcion = int(input("👉 ¿Qué quieres convertir hoy? "))

        # -------------------------------------------------------------
        # 1️⃣ CONVERSIONES DE TEMPERATURA
        # -------------------------------------------------------------
        if opcion == 1:
            print("\n🌞🔥 ¡Hora de calentar o enfriar! 🔥🌞")
            print("1️⃣ Fahrenheit ➡️ Celsius")
            print("2️⃣ Celsius ➡️ Fahrenheit")
            
            subopcion = int(input("Ingresa tu elección: "))
            valor = float(input("Ingresa el valor que quieras convertir 🌡️: "))

            if subopcion == 1:
                resultado = (valor - 32) * 5 / 9
                mensaje = f"{valor:.2f} °F = {resultado:.2f} °C"
                print(f"❄️ Resultado: {mensaje} — ¡Fresco como una lechuga! 🥬")
            elif subopcion == 2:
                resultado = (valor * 9 / 5) + 32
                mensaje = f"{valor:.2f} °C = {resultado:.2f} °F"
                print(f"🔥 Resultado: {mensaje} — ¡Esto está que arde! 🔥")
            else:
                print("😅 Ups... esa opción no existe.")
                continue

            app.agregar_conversion(f"Temperatura: {mensaje}")

        # -------------------------------------------------------------
        # 2️⃣ CONVERSIONES DE PESO
        # -------------------------------------------------------------
        elif opcion == 2:
            print("\n🏋️ ¡Hora de mover el cuerpo! 💪")
            print("1️⃣ Libras ➡️ Kilogramos")
            print("2️⃣ Kilogramos ➡️ Libras")

            subopcion = int(input("Ingresa tu elección: "))
            valor = float(input("Ingresa el peso que quieras convertir ⚖️: "))

            if subopcion == 1:
                resultado = valor / 2.20462
                mensaje = f"{valor:.2f} lb = {resultado:.2f} kg"
                print(f"💫 Resultado: {mensaje} — ¡Más livian@ de lo que pensabas! 😜")
            elif subopcion == 2:
                resultado = valor * 2.20462
                mensaje = f"{valor:.2f} kg = {resultado:.2f} lb"
                print(f"💥 Resultado: {mensaje} — ¡Puro músculo! 💪")
            else:
                print("😅 Esa opción no está en el gimnasio.")
                continue

            app.agregar_conversion(f"Peso: {mensaje}")

        # -------------------------------------------------------------
        # 3️⃣ CONVERSIONES DE MONEDA
        # -------------------------------------------------------------
        elif opcion == 3:
            print("\n💸 ¡Hora de hablar de dinero! 💵💶💴")
            print("1️⃣ Dólares 🇺🇸 ➡️ Pesos MXN 🇲🇽")
            print("2️⃣ Pesos MXN 🇲🇽 ➡️ Dólares 🇺🇸")
            print("3️⃣ Dólares 🇺🇸 ➡️ Euros 🇪🇺 (Tasa fija: USD * 0.87)")
            print("4️⃣ Euros 🇪🇺 ➡️ Dólares 🇺🇸 (Tasa fija: 1.15)")
            print("5️⃣ Euros 🇪🇺 ➡️ Pesos MXN 🇲🇽 (Tasa fija: 21.5)")
            print("6️⃣ Pesos MXN 🇲🇽 ➡️ Euros 🇪🇺 (Tasa fija: 21.5)")
            
            subopcion = int(input("Ingresa tu elección: "))
            valor = float(input("Ingresa el monto a convertir 💰: "))

            if subopcion == 1:
                resultado = valor * app.tasas["dolar_mxn"]
                mensaje = f"${valor:.2f} USD = ${resultado:.2f} MXN"
            elif subopcion == 2:
                resultado = valor / app.tasas["dolar_mxn"]
                mensaje = f"${valor:.2f} MXN = ${resultado:.2f} USD"
            elif subopcion == 3:
                resultado = valor * 0.87
                mensaje = f"${valor:.2f} USD = €{resultado:.2f} EUR"
            elif subopcion == 4:
                resultado = valor * app.tasas["euro_usd"]
                mensaje = f"€{valor:.2f} EUR = ${resultado:.2f} USD"
            elif subopcion == 5:
                resultado = valor * app.tasas["euro_mxn"]
                mensaje = f"€{valor:.2f} EUR = ${resultado:.2f} MXN"
            elif subopcion == 6:
                resultado = valor / app.tasas["euro_mxn"]
                mensaje = f"${valor:.2f} MXN = €{resultado:.2f} EUR"
            else:
                print("😅 Opción inexistente...")
                continue

            print(f"✅ Resultado: {mensaje}")
            app.agregar_conversion(f"Moneda: {mensaje}")

        # -------------------------------------------------------------
        # 4️⃣ MOSTRAR HISTORIAL
        # -------------------------------------------------------------
        elif opcion == 4:
            if app.historial:
                print("\n📜 HISTORIAL DE CONVERSIONES:")
                for h in app.historial:
                    print("•", h)
            else:
                print("🕳️ Todavía no hay conversiones registradas.")

        # -------------------------------------------------------------
        # 5️⃣ BÚSQUEDA DE CONVERSIÓN
        # -------------------------------------------------------------
        elif opcion == 5:
            termino = input("🔍 Ingresa un texto para buscar en el historial: ")
            resultados = app.buscar_conversion(termino)
            if resultados:
                print("\n🎯 Coincidencias encontradas:")
                for r in resultados:
                    print("•", r)
            else:
                print("😅 No se encontraron coincidencias.")

        # -------------------------------------------------------------
        # 6️⃣ SALIR
        # -------------------------------------------------------------
        elif opcion == 6:
            seguir = 'no'
            print("\n👋 Gracias por usar el Multiconversor BAM 💥💣 ¡Vuelve pronto! 😄")

        else:
            print("😅 Esa opción no existe, prueba otra vez 💫")

        # -------------------------------------------------------------
        # PREGUNTAR SI DESEA CONTINUAR
        # -------------------------------------------------------------
        if seguir != 'no':
            print("-" * 50)
            respuesta = input("¿Quieres seguir jugando a convertir cosas? (si/no): ")
            respuesta = convertir_a_minusculas(respuesta)

            if not validar_si_no(respuesta):
                print("🙃 No entendí eso, supongo que ya te vas 🫠")
                seguir = 'no'
            else:
                seguir = respuesta

    except ValueError:
        print("❌ Error: ¡Debes ingresar un número válido o una opción numérica!")
        print("Volviendo al menú principal...")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        seguir = 'no'

# -------------------------------------------------------------
# FIN DEL PROGRAMA
# -------------------------------------------------------------
print("\n🎉 Programa terminado. ¡Eres oficialmente un/a maestr@ de las conversiones! 🏆")