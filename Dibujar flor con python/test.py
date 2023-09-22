import turtle

# Configuración inicial de Turtle
turtle.speed(2)  # Aumenta la velocidad de Turtle
turtle.bgcolor("sky blue")  # Fondo azul cielo
turtle.title("Flor Amarilla")

# Función para dibujar un pétalo
def dibujar_petalo():
    turtle.color("yellow")
    turtle.begin_fill()
    turtle.circle(100, 60)
    turtle.left(120)
    turtle.circle(100, 60)
    turtle.end_fill()

# Función para dibujar la flor completa
def dibujar_flor():
    for _ in range(6):
        dibujar_petalo()
        turtle.left(60)

# Función para dibujar el tallo
def dibujar_tallo():
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()
    turtle.color("green")  # Tallo verde
    turtle.pensize(10)
    turtle.setheading(90)
    turtle.forward(200)

# Función para dibujar el pasto
def dibujar_pasto():
    turtle.penup()
    turtle.goto(-400, -200)
    turtle.pendown()
    turtle.color("green")
    turtle.begin_fill()
    turtle.goto(400, -200)
    turtle.goto(400, -220)  # Bajar un poco para cubrir el tallo
    turtle.goto(-400, -220)
    turtle.goto(-400, -200)
    turtle.end_fill()

# Función para dibujar el polen en la parte superior del tallo (un poco abajo a la derecha)
# Función para dibujar el polen en la parte superior del tallo (un poco arriba a la izquierda)
def dibujar_polen():
    turtle.penup()
    turtle.goto(16, -5)  # Ajusta la posición arriba y a la izquierda
    turtle.pendown()
    turtle.color("orange")  # Color del polen
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()

# Dibuja el pasto, el tallo y la flor
dibujar_pasto()
dibujar_tallo()
dibujar_flor()
dibujar_polen()






# Mueve Turtle al lugar para el mensaje
turtle.penup()
turtle.goto(0, 200)
turtle.pendown()

# Escribe el mensaje
turtle.color("black")
turtle.write("de un rarito para ti mivida :3", align="center", font=("Arial", 12, "normal"))

# Cierra la ventana al hacer clic
turtle.exitonclick()
