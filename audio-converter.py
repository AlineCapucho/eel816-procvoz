import os
import PySimpleGUI as sg
from algorithms import convert_to_mp3, convert_to_flac, convert_to_aac
from pydub import AudioSegment
from pydub.playback import play

def play_audio(file_path):
    audio = AudioSegment.from_file(file_path)
    audio = audio[:10 * 1000]
    play(audio)

file_formats = {'MP3': 'mp3', 'AAC': 'aac', 'FLAC': 'flac'}

sg.theme('DarkTeal12')

layout = [
    [sg.Text("Selecione um arquivo:")],
    [sg.InputText(key="input_path", enable_events=True, visible=False), sg.FileBrowse(button_text="Buscar Arquivo", file_types=(("Audio Files", "*.wav;*.mp3;*.aac;*.flac"),))],
    [sg.Text("Arquivo:", key="selected_file_text")],
    [sg.Text("Formato novo:"), sg.Combo(values=list(file_formats.keys()), key="output_format", default_value="MP3")],
    [sg.Button("Converter"), sg.Button("Amostra do Áudio Convertido"), sg.Button("Fechar")],
]

window = sg.Window("Conversor de áudio", layout)

converted_file_path = None 

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Fechar":
        break

    if event == "Converter":
        input_path = values["input_path"]
        output_format = values["output_format"]

        if not input_path or not os.path.isfile(input_path):
            sg.popup_error("Por favor selecione um arquivo válido.")
            continue

        output_directory = os.path.dirname(input_path)

        output_path = sg.popup_get_file("Salvar Como", save_as=True, initial_folder=output_directory)

        if output_path:
            if output_format == 'MP3':
                convert_to_mp3(input_path, output_path)
            elif output_format == 'AAC':
                convert_to_aac(input_path, output_path)
            elif output_format == 'FLAC':
                convert_to_flac(input_path, output_path)
            sg.popup_ok(f"Conversão completa. Arquivo salvo:\n{output_path}", keep_on_top=True)
            converted_file_path = output_path

    elif event == "Amostra do Áudio Convertido":
        if converted_file_path:
            play_audio(converted_file_path)
        else:
            sg.popup_error("Nenhum arquivo convertido disponível. Por favor, converta um arquivo primeiro.")

    window["selected_file_text"].update(f"Arquivo: {os.path.basename(values['input_path'])}")

window.close()
