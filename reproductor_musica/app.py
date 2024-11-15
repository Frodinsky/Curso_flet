import flet as ft
import os
import pygame
import asyncio
from mutagen.mp3 import MP3

class Song:
    def __init__(self, filename):
        self.filename = filename
        self.title = os.path.splitext(filename)[0]
        self.duration = self.get_duration()

    def get_duration(self):
        audio = MP3(os.path.join("canciones", self.filename))
        return audio.info.length



async def main(page: ft.Page):
    page.Title = "Reproductor de musica"
    page.bgcolor = ft.colors.BLUE_GREY_800
    page.padding = 20
    titulo = ft.Text("Reproductor de musica", size=30, color=ft.colors.WHITE)
    pygame.mixer.init()
    playlist = [Song(f) for f in os.listdir("canciones") if f.endswith(".mp3")]

    def load_song():
        pygame.mixer.music.load(os.path.join("canciones",playlist[current_song_index].filename))
        return

    def play_pause(e):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            play_button.icon = ft.icons.PLAY_ARROW
        else:
            if pygame.mixer.music.get_pos() == -1:
                load_song()
                pygame.mixer.music.play()
            else:
                pygame.mixer.music.unpause()
            play_button.icon = ft.icons.PAUSE
        page.update()

    def change_song(delta):
        nonlocal current_song_index
        current_song_index = (current_song_index + delta) % len(playlist)
        load_song()
        pygame.mixer.music.play()
        update_song_info()
        play_button.icon = ft.icons.PAUSE
        page.update()


    def update_song_info():
        song = playlist[current_song_index]
        song_info.value = f"{song.title}"
        duration.value = format_time(song.duration)
        progress_bars.value = 0.0
        current_time_text.value = "01:00"
        page.update()

    def format_time(seconds):
        minutes, seconds = divmod(int(seconds), 60)
        return f"{minutes:02d}:{seconds:02d}"

    async def update_progress():
        while True:
            if pygame.mixer.music.get_busy():
                current_time = pygame.mixer.music.get_pos() / 1000
                progress_bars.value = current_time / playlist[current_song_index].duration
                current_time_text.value = format_time(current_time)
                page.update()
            await asyncio.sleep(1)



    current_song_index = 0
    song_info = ft.Text("",size=20 , color=ft.colors.WHITE60)
    current_time_text = ft.Text("01:00", color=ft.colors.WHITE60)
    duration = ft.Text("00:00", color=ft.colors.WHITE60)
    progress_bars = ft.ProgressBar(value=0.0, width=333, color="white", bgcolor="263238")
    play_button = ft.IconButton(icon=ft.icons.PLAY_ARROW, on_click=play_pause , icon_color=ft.colors.WHITE)
    preview_button = ft.IconButton(icon=ft.icons.SKIP_PREVIOUS, on_click=lambda e: change_song(-1) , icon_color=ft.colors.WHITE)
    next_button = ft.IconButton(icon=ft.icons.SKIP_NEXT, on_click=lambda e: change_song(1), icon_color=ft.colors.WHITE)

    controls = ft.Row([preview_button,play_button,next_button],
                      alignment=ft.MainAxisAlignment.CENTER
                      )
    fila_reproductor = ft.Row ([current_time_text, progress_bars, duration],
                               alignment=ft.MainAxisAlignment.CENTER)

    columna = ft.Column([song_info, fila_reproductor, controls],
                        alignment=ft.MainAxisAlignment.CENTER, spacing= 20
                        )


    page.add(columna)
    if playlist:
        load_song()
        update_song_info()
        page.update()
        await update_progress()
    else:
        song_info.value = "No se encontraron canciones en la carpeta canciones"
        page.update()

ft.app(target=main)

