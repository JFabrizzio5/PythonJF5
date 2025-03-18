from flask import Flask, render_template, request, redirect, url_for
import subprocess
import webbrowser
import speech_recognition as sr
import threading

app = Flask(__name__)

PROGRAMS = {
    "chrome": "C:/Program Files/Google/Chrome/Application/chrome.exe",
    "vscode": "C:/Users/TuUsuario/AppData/Local/Programs/Microsoft VS Code/Code.exe",
    "spotify": "C:/Users/TuUsuario/AppData/Roaming/Spotify/Spotify.exe",
    "bloc de notas": "notepad",
    "explorador de archivos": "explorer",
}

@app.route("/")
def index():
    return render_template("index.html", programs=PROGRAMS)

@app.route("/open/<program>")
def open_program(program):
    if program in PROGRAMS:
        subprocess.Popen(PROGRAMS[program], shell=True)
    return redirect(url_for("index"))

def process_command(command):
    """Procesa el comando de voz y ejecuta la acción correspondiente."""
    command = command.lower().strip()

    if command in PROGRAMS:
        print(f"🔹 Abriendo {command}...")
        subprocess.Popen(PROGRAMS[command], shell=True)
    elif command == "menú":
        print("🔹 Abriendo menú en el navegador...")
        webbrowser.open("http://127.0.0.1:5000/")
    else:
        print("⚠️ Comando no reconocido")

def background_listener(recognizer, source):
    """Función de reconocimiento en segundo plano."""
    def callback(recognizer, audio):
        try:
            text = recognizer.recognize_google(audio, language="es-ES").lower()
            print(f"🎙️ Has dicho: {text}")
            
            if "alexa" in text:
                command = text.replace("alexa", "").strip()
                process_command(command)

        except sr.UnknownValueError:
            print("⚠️ No se entendió el audio")
        except sr.RequestError:
            print("❌ Error en la conexión con el servicio de reconocimiento")

    recognizer.adjust_for_ambient_noise(source)  # Ajuste de ruido inicial
    print("🎤 Escuchando en segundo plano...")

    stop_listening = recognizer.listen_in_background(source, callback)
    return stop_listening  # Devuelve el método para detener el reconocimiento si es necesario

if __name__ == "__main__":
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    
    stop_listening = background_listener(recognizer, mic)  # Iniciar reconocimiento en segundo plano
    
    flask_thread = threading.Thread(target=app.run, kwargs={"debug": True, "use_reloader": False}, daemon=True)
    flask_thread.start()

    try:
        while True:
            pass  # Mantener el programa corriendo sin ciclos bloqueantes
    except KeyboardInterrupt:
        print("🛑 Cerrando aplicación...")
        stop_listening()  # Detener el reconocimiento antes de salir
