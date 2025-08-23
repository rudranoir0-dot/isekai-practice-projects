# io_practice.py
# Simple I/O practice for Sekai Week 1 (no API calls)

def main():
    print("=== AI Vibe: I/O Practice ===")

    # Collect user input
    anime = input("Enter your favorite anime: ").strip()
    character = input("Enter your favorite character from that anime: ").strip()

    # Basic validation (keeps it friendly if left blank)
    if not anime:
        anime = "Unknown Anime"
    if not character:
        character = "Unknown Character"

    # Formatted summary line
    summary = f"Got it. Favorite anime: {anime} | Character: {character}"
    print(summary)

    # Tiny stub 'prompt' string we’ll use later for an LLM (no API today)
    # A 'prompt' is the instruction we would send to a model.
    vibe_prompt = (
        "Write a 3–4 sentence scene in a light, anime-inspired style featuring "
        f"{character} from {anime}. Keep it PG, energetic, and vivid. "
        "Avoid spoilers. No real-world brands."
    )

    print("\n--- Prompt Stub (for later use) ---")
    print(vibe_prompt)

    # End marker
    print("\n=== Done ===")

if __name__ == "__main__":
    main()

