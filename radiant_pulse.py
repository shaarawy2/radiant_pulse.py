import flet as ft

def main(page: ft.Page):
    page.title = "Radiant Pulse"
    page.theme_mode = "dark"
    page.scroll = "adaptive"

    # Header
    page.add(ft.Text("⚡ RADIANT PULSE", size=30, weight="bold"))
    page.add(ft.ProgressBar(value=0.05, color="red")) # Day 1 Progress

    # Input Fields
    vandal_score = ft.TextField(label="Hard Bots (Vandal)", keyboard_type="number")
    body_practice = ft.Checkbox(label="Body Practicing Done")
    
    def save_clicked(e):
        page.add(ft.Text(f"Saved! Vandal: {vandal_score.value}", color="green"))
        page.update()

    page.add(
        vandal_score,
        body_practice,
        ft.ElevatedButton("Save Daily Grind", on_click=save_clicked)
    )

ft.app(target=main)
