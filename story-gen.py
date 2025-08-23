from gradio_client import Client

# Connect to your Hugging Face Space
client = Client("rudranoir0/isekai-model")

# Ask the user for input
prompt = input("Enter a short anime/fanfiction prompt: ")

# Send the prompt to your model
result = client.predict(
    prompt="Write a short isekai anime-style story.\nSetting: world with dragons and demons, enemies of humanity.\nStyle: light novel, dramatic, adventurous, no religion quotes.",
    api_name="/predict"
)

# Some Spaces return a list, some return a string
if isinstance(result, list):
    story = result[0]
else:
    story = result

print("=== Story ===\n")
print(story.strip())
