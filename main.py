from nicegui import ui

energia = 50
felicidad = 50
bateria = 50

audio_robot = ui.audio('robot.mp3').style('display: none;')

def actualizar():
    barra_energia.value = energia / 100
    barra_felicidad.value = felicidad / 100
    barra_bateria.value = bateria / 100

    texto_energia.text = f'Energía: {energia}%'
    texto_felicidad.text = f'Felicidad: {felicidad}%'
    texto_bateria.text = f'Batería: {bateria}%'

def iniciar():
    inicio.visible = False
    juego.visible = True
    audio_robot.play()
    video.play()

def jugar():
    global energia, felicidad, bateria

    felicidad = min(felicidad + 20, 100)
    energia = max(energia - 10, 0)
    bateria = max(bateria - 15, 0)

    estado.text = '🎮 El robot está jugando'
    video.set_source('play.MP4')
    audio_robot.play()
    actualizar()

def alimentar():
    global energia, felicidad, bateria

    energia = min(energia + 20, 100)
    felicidad = min(felicidad + 5, 100)

    estado.text = '🍎 El robot está recibiendo energía'
    video.set_source('eat.MP4')
    audio_robot.play()
    actualizar()

def dormir():
    global energia, felicidad, bateria

    bateria = min(bateria + 25, 100)
    energia = min(energia + 10, 100)
    felicidad = max(felicidad - 5, 0)

    estado.text = '😴 El robot está descansando'
    video.set_source('sleep.MP4')
    audio_robot.play()
    actualizar()

def esperar():
    estado.text = '🤖 El robot está esperando instrucciones'
    video.set_source('idle.MP4')
    audio_robot.play()


with ui.column().classes('w-full h-screen items-center justify-center') as inicio:
    ui.label('🤖 Mi Robot Virtual').style('font-size: 36px; font-weight: bold')
    ui.label('Cuida a tu robot para mantenerlo feliz y con energía')
    ui.button('▶️ Iniciar Robot', on_click=iniciar)


with ui.column().classes('w-full items-center').style(
    'background-color: #eaf6ff; min-height: 100vh; padding: 20px'
) as juego:

    ui.label('🤖 Mi Robot Virtual').style(
        'font-size: 34px; font-weight: bold'
    )

    estado = ui.label('🤖 El robot está esperando instrucciones').style(
        'font-size: 22px'
    )

    video = ui.video('idle.MP4').props('autoplay loop muted').style(
        'width: 520px; border-radius: 20px'
    )

    with ui.card().style('width: 520px; padding: 15px'):
        texto_energia = ui.label('Energía: 50%')
        barra_energia = ui.linear_progress(value=0.5)

        texto_felicidad = ui.label('Felicidad: 50%')
        barra_felicidad = ui.linear_progress(value=0.5)

        texto_bateria = ui.label('Batería: 50%')
        barra_bateria = ui.linear_progress(value=0.5)

    with ui.row():
        ui.button('🎮 Jugar', on_click=jugar)
        ui.button('🍎 Alimentar', on_click=alimentar)
        ui.button('😴 Dormir', on_click=dormir)
        ui.button('🤖 Esperar', on_click=esperar)

juego.visible = False

ui.run()